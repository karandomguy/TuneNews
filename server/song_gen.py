from peft import PeftModel, PeftConfig
import re
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    pipeline
)
from typing import List

class TuneNewsModel:
    def __init__(self):
        self.config = PeftConfig.from_pretrained("karandomguy/TuneNews")
        if torch.cuda.is_available():
            self.device = torch.device("cuda:0")
        else:
            self.device = torch.device("cpu:0")

        self.model_name = "meta-llama/Llama-2-7b-hf"
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name,use_auth_token="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")
        self.model = PeftModel.from_pretrained(self.model, "karandomguy/TuneNews")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True, use_auth_token="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")
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "right"

    def tnm_pipeline(self, user_input: str) -> List[dict]:
        pipe = pipeline(task="text-generation", model=self.model, tokenizer=self.tokenizer, max_length=1000)
        system_prompt = "Convert this to casual Hinglish Bollywood Lyrics"
        formatted_string = f"[INST]<>{system_prompt}<>{user_input}[/INST]"
        result = pipe([formatted_string])  # Pass a list of strings
        lyrics = re.sub(r'\[INST\].*?\[/INST\]', '', result[0]['generated_text'], flags=re.DOTALL)
        return lyrics
