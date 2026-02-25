

def extract_features(raw_input):
    """
    raw_input should be dictionary like:
    {
        "avg_key_hold": float,
        "typing_speed": float,
        "mouse_speed": float,
        "click_rate": float,
        "session_duration": float
    }
    """

    features = [
        raw_input["avg_key_hold"],
        raw_input["typing_speed"],
        raw_input["mouse_speed"],
        raw_input["click_rate"],
        raw_input["session_duration"]
    ]

    return features