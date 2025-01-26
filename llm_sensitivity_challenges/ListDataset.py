import ast
from torch.utils.data import Dataset
class ListDataset(Dataset):
    
    def __init__(self, texts, prompt_template, text_placeholder):
        self.texts = texts
        self.prompt_template = prompt_template
        self.text_placeholder = text_placeholder

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, i):
        prompted_text = self._build_prompt(self.prompt_template, self.text_placeholder, self.texts[i])
        return prompted_text
    
    def _build_prompt(self, prompt_template: str, text_placeholder: str, input_text: str):
        if prompt_template:
            prompt = prompt_template.replace(text_placeholder, input_text)
        else:
            raise NotImplementedError("Insert a template")
        return prompt