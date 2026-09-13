from ml.inference.predictor import predict_currency

class ModelService:
    def predict(self, image_bytes:bytes) -> dict:
        return predict_currency(image_bytes)

model_service = ModelService()