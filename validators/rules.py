"""Validation rules placeholder."""


def validate_packet(data, rules, interval):
    errors = []

    for f in rules["required_fields"]:
        if f not in data:
            errors.append(f"Missing field: {f}")

    if "temperature" in data:
        if not (rules["min_temp"] <= data["temperature"] <= rules["max_temp"]):
            errors.append("Temperature out of range")

    if interval and interval > rules["max_interval_sec"]:
        errors.append("Publish interval too long")

    return errors


