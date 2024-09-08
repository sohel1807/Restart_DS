from modal import App, web_endpoint, Image
from typing import Dict
from transformers import pipeline, T5TokenizerFast


image = Image.debian_slim().pip_install(
    "transformers",
    "torch",
    "sentencepiece"
)


app = App(name="summarization", image=image)


@app.function()
@web_endpoint(label="summarize", method="POST")
def summarize_text(requestData: Dict):
    from transformers import pipeline, T5TokenizerFast
    import re
    text = requestData.get("text", "")
    model_name = 't5-small'
    max_input_tokens = 256 
    summary_max_length = 100
    summary_min_length = 30

    def preprocess_text(text):
        text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
        return text.strip()

    processed_text = preprocess_text(text)

    tokenizer = T5TokenizerFast.from_pretrained(model_name, legacy=False)
    summarizer = pipeline("summarization", model=model_name, tokenizer=tokenizer)

    tokens = tokenizer.encode(processed_text, truncation=False)

    # Take only the first 256 tokens for summarization
    truncated_tokens = tokens[:max_input_tokens]
    truncated_text = tokenizer.decode(truncated_tokens, skip_special_tokens=True)

    try:
        summary = summarizer(
            truncated_text,
            max_length=summary_max_length,
            min_length=summary_min_length,
            do_sample=False,
            num_beams=4  
        )
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        return {"error": str(e)}
