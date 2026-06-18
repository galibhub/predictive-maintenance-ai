def get_root_causes(features):

    causes = []

    power = features["power"].iloc[0]
    stress_index = features["stress_index"].iloc[0]
    rpm = features["Rotational speed [rpm]"].iloc[0]
    torque = features["Torque [Nm]"].iloc[0]
    heat_stress = features["heat_stress"].iloc[0]
    tool_wear = features["Tool wear [min]"].iloc[0]

    if power > 66873:
        causes.append(
            "High Power Load"
        )

    if stress_index > 6279:
        causes.append(
            "High Stress Index"
        )

    if rpm < 1423:
        causes.append(
            "Low Rotational Speed"
        )

    if torque > 46.8:
        causes.append(
            "High Torque"
        )

    if heat_stress > 470:
        causes.append(
            "High Thermal Stress"
        )

    if tool_wear > 162:
        causes.append(
            "Excessive Tool Wear"
        )

    return causes