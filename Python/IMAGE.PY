import numpy as np
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess image
def preprocess_image(image_path):
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    img = img.resize((128, 128))  # Resize for uniformity (optional)
    pixel_values = np.array(img).flatten()  # Flatten to 1D array
    normalized_pixels = pixel_values / 255.0  # Normalize to [0, 1]
    return normalized_pixels

# Calculate cosine similarity
def calculate_cosine_similarity(image1_path, image2_path):
    # Extract image vectors
    img1_vector = preprocess_image(image1_path)
    img2_vector = preprocess_image(image2_path)
    
    # Compute cosine similarity
    similarity = cosine_similarity([img1_vector], [img2_vector])
    return img1_vector, img2_vector, similarity[0][0]

# Example usage
image1_path = 'cricket1.jpg'
image2_path = 'cricket2.jpg'

# Get vectors and similarity
img1_vector, img2_vector, similarity = calculate_cosine_similarity(image1_path, image2_path)

# Output results
print("Image 1 Vector:", img1_vector)
print("Image 2 Vector:", img2_vector)
print(f"Image 1 context is {similarity * 100:.2f}% similar to Image 2")
