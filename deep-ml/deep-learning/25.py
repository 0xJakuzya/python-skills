import numpy as np

def loss(output, labels):
    s =(np.square(output-labels))
    s = np.sum(s)/len(labels)
    return s

def train_neuron(
    features: np.ndarray, 
    labels: np.ndarray, 
    initial_weights: np.ndarray, 
    initial_bias: float, 
    learning_rate: float, 
    epochs: int
) -> (np.ndarray, float, list[float]):
    features = np.array(features)
    labels = np.array(labels)
    weights = np.array(initial_weights)
    bias = float(initial_bias)
    mse_values = []
    for epoch in range(epochs):
        z = features.dot(weights) + bias
        output = 1 / (1 + np.exp(-z))
        mse = loss(output, labels)
        mse_values.append(mse)
        error = output - labels
        sigmoid_derivative = output * (1 - output)
        delta = 2 * error * sigmoid_derivative
        weight_gradient = features.T.dot(delta) / len(labels)
        bias_gradient = np.sum(delta) / len(labels)
        weights = weights - learning_rate * weight_gradient
        bias = bias - learning_rate * bias_gradient
    return np.round(weights, 4).tolist(), round(bias, 4), mse_values