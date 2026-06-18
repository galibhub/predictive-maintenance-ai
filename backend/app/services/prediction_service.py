import joblib
from pathlib import Path

from app.utils.feature_engineering import (
    create_features
)

from app.utils.health_score import (
    calculate_health_score
)

from app.services.risk_service import (
    get_risk_level
)

from app.services.explanation_service import (
    get_root_causes
)

from app.services.recommendation_service import (
    generate_recommendations
)

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "random_forest.pkl"
)

model = joblib.load(MODEL_PATH)


def predict_machine_failure(data):

    features = create_features(
        data
    )

    prediction = model.predict(
        features
    )[0]

    probability = (
        model.predict_proba(
            features
        )[0][1]
        * 100
    )

    probability = round(
        probability,
        2
    )

    risk_level = get_risk_level(
        probability
    )

    health_score = calculate_health_score(
        probability
    )

    root_causes = get_root_causes(
        features
    )

    recommendations = generate_recommendations(
        root_causes
    )

    result = {
        "prediction":
            "Failure"
            if prediction == 1
            else "No Failure",

        "probability":
            probability,

        "risk_level":
            risk_level,

        "health_score":
            health_score,

        "root_causes":
            root_causes,

        "recommendations":
            recommendations
    }

    return result