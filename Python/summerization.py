from modal import App, build, enter, method, web_endpoint, Image
from typing import Dict
import modal
import re

image = Image.debian_slim().pip_install(
    "transformers",
    "torch",
    "sentencepiece"
)

app = App(name="summarization", image=image)

@app.function()
@web_endpoint(label="summarize", method="POST")
def summarize_text(requestData: Dict):
    
    text = requestData.get("text", "")
    
    try:
        result = SummarizerModel().summarize.remote(text)  
        return result
    except Exception as e:
        return {"error": str(e)}

@app.cls()  
class SummarizerModel:
    @build()
    @enter()
    def initialize(self):
        # Initialize model 
        from transformers import pipeline, T5TokenizerFast
        self.model_name = 't5-small'
        self.tokenizer = T5TokenizerFast.from_pretrained(self.model_name, legacy=False)
        self.summarizer = pipeline("summarization", model=self.model_name, tokenizer=self.tokenizer)

    @method()
    def summarize(self, text: str):
        max_input_tokens = 256
        summary_max_length = 100
        summary_min_length = 30

        def process_summary(text):
        # Remove duplicate and make first letter capital
            text = re.sub(r'\b(\w+)( \1\b)', '', text).strip()
            if text:
                text = text[0].upper() + text[1:]
            return text
        
        # Tokenize 
        tokens = self.tokenizer.encode(text, truncation=False)
        truncated_tokens = tokens[:max_input_tokens]
        truncated_text = self.tokenizer.decode(truncated_tokens, skip_special_tokens=True)
        
        
        summary = self.summarizer(
            truncated_text,
            max_length=summary_max_length,
            min_length=summary_min_length,
            do_sample=False,
            num_beams=4
        )
        

        processed_summary = process_summary(summary[0]['summary_text'])
        
        return {"summary": processed_summary}


