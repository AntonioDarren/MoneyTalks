from typing import Optional
from pydantic import BaseModel, Field

class PredictionResponse (BaseModel):
    denomination: Optional[int] = Field(default=None, description="Detected denomination in Rupiah")
    confidence: float = Field(ge=0.0, le=1.0, description="Model confidence 0.0 - 1.0")
    box: Optional[list[float]] = Field(default=None, description="Normalized bounding box [x, y, width, height]")