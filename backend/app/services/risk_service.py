def get_risk_level(
    probability
):

    if probability >= 80:
        return "Critical"

    if probability >= 60:
        return "High"

    if probability >= 30:
        return "Medium"

    return "Low"