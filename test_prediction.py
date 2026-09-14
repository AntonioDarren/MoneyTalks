from pathlib import Path

from ml.inference.predictor import predict_currency


image_path = Path("data/idr_1000/1000_0010.jpg")

with open(image_path, "rb") as f:
    image_bytes = f.read()

result = predict_currency(image_bytes)

print(result)