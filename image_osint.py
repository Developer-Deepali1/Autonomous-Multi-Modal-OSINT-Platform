# osint/image_osint.py

def image_scan(username: str) -> dict:
    """Dummy image OSINT scan."""
    if not username:
        return None

    return {
        "images_found": 2,
        "images": [
            {"image_id": "img_001", "description": f"Profile picture of {username}"},
            {"image_id": "img_002", "description": f"{username} at an event"}
        ]
    }


