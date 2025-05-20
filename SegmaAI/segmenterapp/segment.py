from segmenter import CustomerSegmenter

class SegmenterWrapper:
    def __init__(self):
        self.segmenter = CustomerSegmenter(
            model_path='kmeans_model.pkl',
            scaler_path='scaler.pkl',
            encoder_path='label_encoder.pkl'
        )

    def predict(self, gender, age, income, spending_score):
        return self.segmenter.predict_group(
            gender=gender,
            age=age,
            income=income,
            spending_score=spending_score
        )
