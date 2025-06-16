from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class Translator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.model_name = "facebook/nllb-200-distilled-600M"
            cls._instance.tokenizer = AutoTokenizer.from_pretrained(cls._instance.model_name)
            cls._instance.model = AutoModelForSeq2SeqLM.from_pretrained(cls._instance.model_name)
            cls._instance.device = "cuda" if torch.cuda.is_available() else "cpu"
            cls._instance.model.to(cls._instance.device)
        return cls._instance

    def translate_to_somali(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True).to(self.device)
        translated_tokens = self.model.generate(
            **inputs, forced_bos_token_id=self.tokenizer.lang_code_to_id["som_Latn"]
        )
        return self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]