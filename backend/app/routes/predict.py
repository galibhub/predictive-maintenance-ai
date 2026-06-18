from fastapi import APIRouter

from app.schemas.prediction_request import (
    PredictionRequest
)

from app.schemas.prediction_response import (
    PredictionResponse
)

from app.services.prediction_service import (
    predict_machine_failure
)

router = APIRouter()


@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(
    payload: PredictionRequest
):

    result = predict_machine_failure(
        payload
    )

    return result