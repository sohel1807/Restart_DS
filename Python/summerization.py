from modal import App, web_endpoint, Image
from typing import Dict
from transformers import pipeline, T5Tokenizer

# Define the image with necessary packages
image = Image.debian_slim().pip_install(
    "transformers",
    "torch",
    "sentencepiece"
)

# Initialize the App
app = App(name="summarization", image=image)

# Function to summarize text
@app.function(timeout=1000)
@web_endpoint(label="summarize", method="POST")
def summarize_text(requestData: Dict):
    from transformers import pipeline, T5Tokenizer

    # Extract data from request
    text = requestData.get("text", "")
    model_name = 't5-small'
    max_input_tokens = 500
    summary_max_length = 150
    summary_min_length = 40

    # Initialize summarization pipeline and tokenizer
    tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=False)
    summarizer = pipeline("summarization", model=model_name, tokenizer=tokenizer)

    # Function to truncate text to fit within max_input_tokens
    def truncate_text(text, max_tokens):
        tokens = tokenizer.encode(text, truncation=False)
        truncated_tokens = tokens[:max_tokens]
        return tokenizer.decode(truncated_tokens, skip_special_tokens=True)

    # Truncate text if it exceeds the token limit
    truncated_text = truncate_text(text, max_input_tokens)

    # Dynamically adjust max_length based on input length
    input_length = len(tokenizer.encode(truncated_text, truncation=False))
    adjusted_max_length = min(summary_max_length, max(int(input_length * 0.5), summary_min_length))

    # Perform summarization
    try:
        summary = summarizer(truncated_text, max_length=adjusted_max_length, min_length=summary_min_length, do_sample=False)
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        return {"error": str(e)}
