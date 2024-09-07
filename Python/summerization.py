from modal import App, web_endpoint, Image
from typing import Dict
from transformers import pipeline, GPT2Tokenizer

# Define the image with necessary packages
image = Image.debian_slim().pip_install(
    "transformers",
    "torch",
    "sentencepiece"
)

# Initialize the App
app = App(name="summarization", image=image)

# Function to summarize text
@app.function()
@web_endpoint(label="summarize", method="POST")
def summarize_text(requestData: Dict):
    # Extract data from request
    text = requestData.get("text", "")
    model_name = 'distilgpt2'  # Use the DistilGPT-2 model
    max_input_tokens = 512  # Adjust this value based on the model's token limit
    summary_max_length = 150
    summary_min_length = 50

    # Initialize summarization pipeline and tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    summarizer = pipeline("text-generation", model=model_name, tokenizer=tokenizer)

    # Function to truncate text to fit within max_input_tokens
    def truncate_text(text, max_tokens):
        tokens = tokenizer.encode(text, truncation=False)
        truncated_tokens = tokens[:max_tokens]
        return tokenizer.decode(truncated_tokens, skip_special_tokens=True)

    # Truncate text if it exceeds the token limit
    truncated_text = truncate_text(text, max_input_tokens)

    # Perform summarization
    try:
        summary = summarizer(truncated_text, max_length=summary_max_length, min_length=summary_min_length, do_sample=True)
        return {"summary": summary[0]['generated_text']}
    except Exception as e:
        return {"error": str(e)}
