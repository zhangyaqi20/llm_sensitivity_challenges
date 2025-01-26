import ast
import logging
import pandas as pd
import re
from sklearn.metrics import ConfusionMatrixDisplay, f1_score, accuracy_score
from LLMManager import LLM

logger = logging.getLogger(__name__)

def read_from_csv(data_name, header=0, names=None):
    if "tsv" in data_name:
        data = pd.read_csv(data_name,
                            sep='\t',
                            encoding = "utf-8",
                            engine = "python",
                            header = header,
                            names = names)
    elif "csv" in data_name:
        data = pd.read_csv(data_name,
                        encoding = "utf-8",
                        engine = "python",
                        header = header,
                        names = names)
    else:
        raise NotImplementedError("Given data file type is not supported yet.")
    return data

def print_dataset_info(df, split, label_col):
    label_counts = df[label_col].value_counts().to_dict()
    output = f"{split}\t{len(df)}"
    for label in sorted(label_counts.keys()):
        output += f"\t{label}: {label_counts[label]}, "
        output += "{:.1%}".format(label_counts[label]/len(df))
    logger.info(output)

def process_predictions(predictions, model_name, label_order=None):
    return [_process_pred(pred, model_name, label_order) for pred in predictions]

def _process_pred(pred, model_name, label_order=None):
    if model_name == LLM.GPT_35:
        pred = pred.strip().lower()
    elif model_name == LLM.FLAN_T5_XL:
        pred = pred.split()[0].strip().lower()
    elif model_name == LLM.LLAMA_2_CHAT_7B:
        pred = re.compile('[^0-9]').sub(' ', pred).strip()[:1]
        if pred.isnumeric() and int(pred) < len(label_order):
            pred = ast.literal_eval(pred)
            pred = label_order[pred].lower()
    elif model_name == LLM.OPT_IML_1P3B:
        pred = ''.join(re.findall(r'[a-z]', pred.lower()))
        if pred in ['hateful', 'hatepeach', 'hatespeach']: # !!! Special case
            pred = 'hatespeech'
        if pred in ['nope', 'na']:
            pred = 'no'
    else:
        raise NotImplementedError("Invalid LLM name for processing texts.")
    return pred

def evaluation(y_preds, y_truth, config, output_dir, outputs_prefix):
    config["metrics"]["success_rate"] = len(y_preds) / config["data"]["data_size"]

    # Compute F1 score.
    f1score = f1_score(y_truth, y_preds, average='macro')
    config["metrics"]["f1score"] = f1score

    f1score_per_label = f1_score(y_truth, y_preds, average=None)
    config["metrics"]["f1score_label"] = dict()
    for label, index in config["data"]["label2index"].items():
        config["metrics"]["f1score_label"][label] = f1score_per_label[index]

    # Compute accuracy.
    acc_score = accuracy_score(y_truth, y_preds)
    config["metrics"]["acc_score"] = acc_score

    # Compute confusion matrix and normalize it based on true labels numbers.
    confusion_matrix_display = ConfusionMatrixDisplay.from_predictions(y_truth, y_preds)
    config["outputs"]["confusion_matrix_filename"] = str(output_dir / f"{outputs_prefix}_confusionmatrix.png")
    confusion_matrix_display.figure_.savefig(config["outputs"]["confusion_matrix_filename"], dpi=300)

    # Compute imbalance ratio = ((tp+fp) - (tp+fn))/(tp+fn) = positive - truth / truth
    labels = list(config["data"]["label2index"].keys())
    bias = dict.fromkeys(labels, None)
    bias_agg = 0
    for label_i in labels:
        pos_i = y_preds.count(config["data"]["label2index"][label_i])
        truth_i = y_truth.count(config["data"]["label2index"][label_i])
        imb_rate = (pos_i - truth_i) / truth_i
        bias[label_i] = imb_rate
        bias_agg += abs(imb_rate)
    config["metrics"]["bias"] = bias
    config["metrics"]["bias_agg"] = bias_agg / len(labels)
    logger.info("Macro F1\tSuccess Rate\tBias\tAggregated Bias")
    logger.info("{:.2f}".format(config['metrics']['f1score']) + f"\t{config['metrics']['success_rate']}\t{config['metrics']['bias']}\t{config['metrics']['bias_agg']}")

    return config