import logging
import torch
from openai import OpenAI
from tqdm.auto import tqdm
from transformers import AutoTokenizer, pipeline, set_seed
from transformers import logging as transformers_logging
from typing import List

logger = logging.getLogger(__name__)
transformers_logging.set_verbosity_info()
transformers_logging.enable_default_handler()
transformers_logging.enable_explicit_format()

class LLMManager:
    def __init__(
            self,
            model_name: str,
            do_sample: bool,
            temperature: float,
            top_p: float,
            seed: int,
            llama_repetition_penalty: float = 1.2,
            batch_size: int = 32,
            max_new_tokens: int = 20,
            gpt_stop_seq: List[str] = [",", ".", "\n"]
            ):
        self.checkpoint = model_name.value
        if self.checkpoint == LLM.FLAN_T5_XL.value:
            self.task = Task.TEXT2TEXT_GENERATION
        elif self.checkpoint in [LLM.LLAMA_2_CHAT_7B.value, LLM.OPT_IML_1P3B.value]:
            self.task = Task.TEXT_GENERATION
            self.llama_repetition_penalty = llama_repetition_penalty
        elif self.checkpoint == LLM.GPT_35.value:
            self.task = Task.CHAT
            self.client = OpenAI(api_key="api_key")
            self.gpt_stop_seq = gpt_stop_seq
        else:
            raise NotImplementedError("The specified LLM is not supported.")
        
        self.batch_size = batch_size
        self.do_sample = do_sample
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.seed = seed

    def predict(self, dataset):
        if self.task == Task.CHAT:
            return self._chat_completion(dataset)
        elif self.task == Task.TEXT2TEXT_GENERATION:
            return self._text2text_generation(dataset)
        elif self.task == Task.TEXT_GENERATION:
            return self._text_generation(dataset)
    
    def _text_generation(self, dataset):
        set_seed(self.seed)
        pipe = pipeline(
            task=self.task.value,
            model=self.checkpoint,
            torch_dtype=torch.bfloat16,
            device_map="auto"
        )
        tokenizer = AutoTokenizer.from_pretrained(self.checkpoint)
        pipe.tokenizer.pad_token_id = pipe.model.config.eos_token_id
        pipe.tokenizer.padding_side = "left"
        predictions = []
        for pred in tqdm(
                pipe(
                    dataset,
                    batch_size=self.batch_size,
                    temperature=self.temperature,
                    top_p=self.top_p,
                    repetition_penalty=self.llama_repetition_penalty,
                    do_sample=self.do_sample,
                    eos_token_id=tokenizer.eos_token_id,
                    max_new_tokens=self.max_new_tokens,
                    return_full_text=False,
                    ), 
                total=len(dataset)
                ):
            predictions.append(pred[0]["generated_text"])
        return predictions
    
    def _text2text_generation(self, dataset):
        set_seed(self.seed)
        pipe = pipeline(
            task=self.task.value,
            truncation=True, 
            model=self.checkpoint, 
            device="cpu"
        )
        predictions = []
        for pred in tqdm(
                pipe(
                    dataset,
                    batch_size=self.batch_size,
                    temperature=self.temperature,
                    top_p=self.top_p,
                    do_sample=self.do_sample,
                    ), 
                total=len(dataset)
                ):
            predictions.append(pred[0]["generated_text"])
        return predictions
    
    def _chat_completion(self, dataset):
        predictions = [self._chat_one_turn(input_text) for input_text in tqdm(dataset)]
        return predictions

    def _chat_one_turn(self, input_text) -> str:
        completion = self.client.chat.completions.create(
            model=self.checkpoint,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
            ],
            temperature=self.temperature,
            max_tokens=self.max_new_tokens,
            top_p=self.top_p,
            stop=self.gpt_stop_seq,
            seed=self.seed
        )
        pred = completion.choices[0].message.content
        return pred
    
    def get_llm_params(self):
        return f'-temp{self.temperature}-top_p={self.top_p}-seed{self.seed}'

from enum import Enum

class LLM(Enum):
    FLAN_T5_XL = "google/flan-t5-xl"
    OPT_IML_1P3B = "facebook/opt-iml-1.3b"
    LLAMA_2_CHAT_7B = "meta-llama/Llama-2-7b-chat-hf"
    GPT_35 = "gpt-3.5-turbo-0125"

class Task(Enum):
    TEXT_GENERATION = "text-generation"
    TEXT2TEXT_GENERATION = "text2text-generation"
    CHAT = "chat-completion"
