import joblib
import numpy as np

class CustomerSegmenter:
    def __init__(self, model_path, scaler_path, encoder_path):
        self.kmeans = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.le = joblib.load(encoder_path)

        # Define cluster descriptions
        self.cluster_info = {
            0: "Group1: Young with high spending score – Target with premium offers and loyalty programs.",
            1: "Group2: Older with low spending score – Possibly budget-conscious, target with discounts.",
            2: "Group3: Average income and spending – Potential growth group, use personalized engagement.",
            3: "Group4: High income but low spending – Encourage spending with luxury incentives.",
            4: "Group5: Low income but high spending – Monitor for churn, offer value-based deals."
        }

    def predict_group(self, gender, age, income, spending_score):
        # Encode gender
        gender_encoded = self.le.transform([gender.strip().capitalize()])[0]

        # Prepare and scale input
        user_data = np.array([[gender_encoded, age, income, spending_score]])
        user_data_scaled = self.scaler.transform(user_data)

        # Predict cluster
        cluster = self.kmeans.predict(user_data_scaled)[0]

        # Map to group
        group_description = self.cluster_info.get(cluster, "Group description not available.")
        return f"The user belongs to Group{cluster+1}\n{group_description}"
