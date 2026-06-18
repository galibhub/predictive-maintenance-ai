def calculate_health_score(
    probability
):

    score = int(
        100 - probability
    )

    return max(
        0,
        min(score, 100)
    )