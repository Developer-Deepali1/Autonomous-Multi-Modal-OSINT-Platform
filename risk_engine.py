def assess_risk(text_data, image_data):
    score = 0

    if text_data.get("platforms_found"):
        score += 30

    if image_data.get("exif_gps") not in [None, "No GPS Data"]:
        score += 50

    level = "LOW"
    if score >= 60:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"

    return {
        "score": score,
        "level": level,
        "explanation": "Based on public exposure and metadata."
    }
