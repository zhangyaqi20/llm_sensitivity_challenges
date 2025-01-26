import json
import logging
import os
from collections import Counter
from pathlib import Path
from utils import *
from ListDataset import ListDataset
from LLMManager import LLMManager, LLM
from prompts import *

log_file = "run.log"
logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
logger = logging.getLogger(__name__)

def run(data_name, data_split, label2index, 
        model_name, do_sample, temperature, top_p, seed, 
        prompt_type, prompt_template, 
        label_order=None, 
        ):

    config = {
        "data": {}, 
        "prompt": {},
        "llm": {}, 
        "outputs": {}, 
        "metrics": {}
    }

    # Configure LLM.
    config["llm"]["model_name"] = str(model_name)
    config["llm"]["do_sample"] = do_sample
    config["llm"]["temperature"] = temperature
    config["llm"]["top_p"] = top_p
    config["llm"]["seed"] = seed
    llm_manager = LLMManager(
        model_name=model_name,
        do_sample=config["llm"]["do_sample"],
        temperature=config["llm"]["temperature"],
        top_p=config["llm"]["top_p"],
        seed=config["llm"]["seed"]
    )

    # Configure prompt.
    config["prompt"]["prompt_type"] = prompt_type + llm_manager.get_llm_params()
    config["prompt"]["prompt_template"] = prompt_template
    config["prompt"]["text_placeholder"] = "{text}"

    # Load data.
    config["data"]["data_name"] = data_name
    config["data"]["data_split"] = data_split
    config["data"]["label2index"] = label2index
    if len(config["data"]["label2index"]) > 2:
        config["data"]["label_col"] = "label_multi"
        config["data"]["data_type"] = "multi"
    else:
        config["data"]["label_col"] = "label"
        config["data"]["data_type"] = "bin"
    
    data = read_from_csv(f'data/{config["data"]["data_name"]}/{config["data"]["data_split"]}_clean.csv')
    config["data"]["data_size"] = len(data)
    labels = data[config["data"]["label_col"]].tolist()
    cnt_labels = Counter(labels)
    config["data"]["label_size"] = {label: cnt_labels[index] for label, index in label2index.items()}
    texts = data['text'].tolist()
    dataset = ListDataset(
        texts=texts, 
        prompt_template=config["prompt"]["prompt_template"], 
        text_placeholder=config["prompt"]["text_placeholder"]
    )
    
    # Configure output files.
    output_dir = Path(f'outputs/{config["data"]["data_name"]}/{config["data"]["data_split"]}')
    output_dir.mkdir(parents=True, exist_ok=True)
    data_prefix = (config["data"]["data_name"] + "_" +
                   config["data"]["data_split"] + "_" +
                   config["data"]["data_type"])
    llm_prefix = model_name.value.split('/')[-1].lower().rsplit('-', 1)[0] if model_name == LLM.GPT_35 else model_name.value.split('/')[-1].lower()
    outputs_prefix = f'{data_prefix}_{llm_prefix}_{config["prompt"]["prompt_type"]}'

    config["outputs"]["predictions_filename"] = str(output_dir / f"{outputs_prefix}_predictions.json")
    # Predict labels and save raw responses.
    logger.info(config)
    if os.path.exists(config["outputs"]["predictions_filename"]):
        with open(config["outputs"]["predictions_filename"], "r") as f:
            responses = json.load(f)
    else:
        responses = llm_manager.predict(dataset)
        with open(config["outputs"]["predictions_filename"], 'w') as f:
            json.dump(responses, f)
    
    # Precess raw response to compute metrics.
    predictions = process_predictions(responses, model_name, label_order)

    # Convert label string to indices
    y_preds = [config["data"]["label2index"][pred_label] if pred_label in config["data"]["label2index"].keys() else -1 for pred_label in predictions]
    # remove invalid predictions(and corresponding truth labels)
    y_truth = [truth for i, truth in enumerate(labels) if y_preds[i] != -1]
    y_preds = [pred for pred in y_preds if pred != -1]
    config = evaluation(y_preds=y_preds, y_truth=y_truth, config=config, output_dir=output_dir, outputs_prefix=outputs_prefix)

    with open(output_dir / f'{outputs_prefix}_config.json', 'w') as f:
        json.dump(config, f, indent=4)
    
if __name__ == "__main__":

    seeds = [0, 21, 42]

    # Example to run the script
    model_name = LLM.FLAN_T5_XL
    data_split = "test"
    
    prompt_type = "vanilla-toxic-nh"
    prompt_template = prompt_vanilla_bin_toxic_nh
    
    run(data_name="civil-comments", data_split=data_split, label2index={"non-toxic": 0, "toxic": 1},
        model_name=model_name, do_sample=True, temperature=0.7, top_p=0.7, seed=seeds[0],
        prompt_type=prompt_type, prompt_template=prompt_template,)