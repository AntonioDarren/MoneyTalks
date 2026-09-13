from fastapi import APIRouter, File, UploadFile, HTTPException
from backend.app.schemas.prediction import PredictionResponse
from backend.app.services.prediction_service import prediction_service

router = APIRouter(
    prefix="/prediction",
    tags=["predictions"]
)

@router.post("", response_model=PredictionResponse)
async def create_prediction(file: UploadFile = File(...)) -> PredictionResponse:
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload an image file!"
        )

    image_bytes = await file.read()

    if not image_bytes:
        raise HTTPException(
            status_code=400,
            detail="The uploaded image is empty!"
        )

    try:
        result = prediction_service.predict(image_bytes)
        return result
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        ) from exc
    except Exception as exc:
        print(f"Prediction Error: {exc}")
        raise HTTPException(
            status_code=400,
            detail="Prediction Failed!"
        ) from exc