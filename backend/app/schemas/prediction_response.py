from pydantic import BaseModel


class PredictionResponse(BaseModel):

    prediction: str

    probability: float

    risk_level: str

    health_score: int

    root_causes: list[str]

    recommendations: list[str]