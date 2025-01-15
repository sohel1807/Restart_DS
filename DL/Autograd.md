### Training Neural Network Stpes requires:-

1. **Forward Pass**:  
   Input data is passed through the network, layer by layer, to compute the predictions (output). This step involves matrix multiplications and applying activation functions to the intermediate layers.

2. **Loss Calculation**:  
   The predicted output from the forward pass is compared to the true labels using a loss function (e.g., Mean Squared Error for regression or Cross-Entropy Loss for classification). This computes how far the predicted output is from the actual target.

3. **Backpropagation**:  
   Using the chain rule of calculus, the loss is propagated backward through the network to compute gradients of the loss function with respect to each model parameter (weights and biases).

4. **Update Gradients**:  
   The gradients calculated during backpropagation are used to update the network parameters using an optimization algorithm (e.g., Gradient Descent, Adam). The update is typically performed as:
   #### Parameter = Parameter - Learning Rate * Gradient
   
## What is Autograd ? and Why it is used ?
We use autograd because it simplifies and automates the process of computing gradients for neural network training. Here's why it's important and useful:
   - Autograd calculates derivatives (gradients) automatically using the chain rule.
   - It eliminates the need to manually derive and implement gradient computations, which can be tedious and error-prone, especially for complex models.
