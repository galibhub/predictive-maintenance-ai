from pydantic import BaseModel
from typing import Optional


class PredictionRequest(BaseModel):

    company_name: Optional[str] = None

    machine_id: Optional[str] = None

    machine_type: str

    air_temperature: float

    process_temperature: float

    rotational_speed: int

    torque: float

    tool_wear: int