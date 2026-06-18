def generate_recommendations(
    root_causes
):

    recommendations = []

    if "High Power Load" in root_causes:
        recommendations.append(
            "Reduce machine workload."
        )

    if "High Stress Index" in root_causes:
        recommendations.append(
            "Schedule preventive maintenance."
        )

    if "Low Rotational Speed" in root_causes:
        recommendations.append(
            "Inspect drive system and motor."
        )

    if "High Torque" in root_causes:
        recommendations.append(
            "Reduce mechanical load."
        )

    if "High Thermal Stress" in root_causes:
        recommendations.append(
            "Inspect cooling system."
        )

    if "Excessive Tool Wear" in root_causes:
        recommendations.append(
            "Replace worn tool."
        )

    return recommendations