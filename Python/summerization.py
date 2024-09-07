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
app = App(name="t5-base-summarization", image=image)

# Function to summarize text
@app.function()
@web_endpoint(label="summarize", method="POST")
def summarize_text(requestData: Dict):
    # Extract data from request
    text = requestData.get("text", "")
    model_name = 't5-base'  # Use the T5-base model
    max_input_tokens = 1024 # Use only the first 800 tokens for summarization
    summary_max_length = 150
    summary_min_length = 50

    # Initialize summarization pipeline and tokenizer
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    summarizer = pipeline("summarization", model=model_name, tokenizer=tokenizer)

    # Function to truncate text to fit within max_input_tokens
    def truncate_text(text, max_tokens):
        tokens = tokenizer.encode(text, truncation=False)
        truncated_tokens = tokens[:max_tokens]
        return tokenizer.decode(truncated_tokens, skip_special_tokens=True)

    # Truncate text to use only the first 800 tokens
    truncated_text = truncate_text(text, max_input_tokens)

    # Prepare input for T5 model
    input_text = f"summarize: {truncated_text}"  # Prefix for T5

    # Perform summarization
    try:
        summary = summarizer(
            input_text,
            max_length=summary_max_length,
            min_length=summary_min_length,
            do_sample=False  # Set to False for deterministic output
        )
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        return {"error": str(e)}

