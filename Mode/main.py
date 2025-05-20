from segment import CustomerSegmenter

# Initialize the segmenter
segmenter = CustomerSegmenter(
    model_path='kmeans_model.pkl',
    scaler_path='scaler.pkl',
    encoder_path='label_encoder.pkl'
)

result = segmenter.predict_group(gender="Female", age=36, income=53, spending_score=86)
print(result)
