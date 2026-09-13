from backend.app.ml.model_service import model_service
from backend.app.schemas.prediction import PredictionResponse

class PredictionService:
    DENOMINATION = {
        "idr_100000": 100000,
        "idr_50000": 50000,
        "idr_20000": 20000,
        "idr_10000": 10000,
        "idr_5000": 5000,
        "idr_2000": 2000,
        "idr_1000": 1000,
        "none": None
    }

    def predict(self, image_bytes:bytes) -> PredictionResponse:
        result = model_service.predict(image_bytes)
        if "error" in result:
            raise ValueError(result["error"])

        label = str(result.get("label", "none"))
        confidence = float(result.get("confidence", 0.0))

        denomination = self.DENOMINATION.get(label)

        response = PredictionResponse(
            denomination=denomination,
            confidence=confidence
        )

        if "box" in result:
            response.box = result["box"]

        return response


prediction_service = PredictionService()
