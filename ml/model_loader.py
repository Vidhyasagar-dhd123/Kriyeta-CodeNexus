import pickle
import numpy as np

with open("C:\CodeNexusProject\ml\logistic_model_diabetes.pkl","rb") as file:
    model = pickle.load(file)


def get_pred_diabetes(
    f1: float, f2: float, f3: float, f4: float, f5: float, f6: float, f7: float,
    f8: float, f9: float, f10: float, f11: float, f12: float, f13: float, f14: float,
    f15: float, f16: float, f17: float
) -> float:
    """
    Predicts an output using a machine learning model given 17 float input features.

    Parameters:
        f1 to f17 (float): The 17 input features required by the model.

    Returns:
        float: The model's predicted value or class label.
    """

    # Step 1: Combine inputs into a numpy array and reshape it to (1, 17)
    input_features = np.array([
        f1, f2, f3, f4, f5, f6, f7,
        f8, f9, f10, f11, f12, f13, f14,
        f15, f16, f17
    ]).reshape(1, -1)

    # Step 2: Predict using the preloaded model
    prediction = model.predict(input_features)

    # Step 3: Return the first prediction (since it's a single input)
    return prediction[0]

