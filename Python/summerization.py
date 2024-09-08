from modal import App, web_endpoint, Image
from typing import Dict
from transformers import pipeline, T5TokenizerFast

# Define the image with necessary packages
image = Image.debian_slim().pip_install(
    "transformers",
    "torch",
    "sentencepiece"
)

# Initialize the App
app = App(name="summarization", image=image)

@app.function()
@web_endpoint(label="summarize", method="POST")
def summarize_text(requestData: Dict):
    from transformers import pipeline, T5TokenizerFast
    import re

    # Extract data from request
    text = requestData.get("text", "")
    model_name = 't5-small'
    max_input_tokens = 256 
    summary_max_length = 100
    summary_min_length = 30

    # Initialize summarization pipeline and tokenizer
    tokenizer = T5TokenizerFast.from_pretrained(model_name, legacy=False)
    summarizer = pipeline("summarization", model=model_name, tokenizer=tokenizer)

    # Function to remove both instances of consecutive duplicate words and capitalize the first letter
    def process_summary(text):
        # Remove both instances of consecutive duplicate words
        text = re.sub(r'\b(\w+)( \1\b)', '', text).strip()
        # Capitalize the first letter
        if text:
            text = text[0].upper() + text[1:]
        return text

    # Tokenize and truncate the input text to fit within max_input_tokens
    tokens = tokenizer.encode(text, truncation=False)
    truncated_tokens = tokens[:max_input_tokens]
    truncated_text = tokenizer.decode(truncated_tokens, skip_special_tokens=True)

    # Perform summarization
    try:
        summary = summarizer(
            truncated_text,
            max_length=summary_max_length,
            min_length=summary_min_length,
            do_sample=False,
            num_beams=4  
        )
        
        # Process the summary to remove duplicates and capitalize the first letter
        processed_summary = process_summary(summary[0]['summary_text'])

        return {"summary": processed_summary}
    except Exception as e:
        return {"error": str(e)}
