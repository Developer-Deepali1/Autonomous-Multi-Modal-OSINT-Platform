# core/orchestrator.py

from osint.text_osint import text_scan
from osint.image_osint import image_scan  # Make sure image_scan exists in image_osint.py
from osint.video_osint import video_scan

def run_osint_scan(input_data):
    """
    Runs the OSINT scan on text, image, and video data.
    input_data: dict with keys 'username', 'text', 'image', 'video' (optional)
    """
    # Text OSINT
    text_intel = text_scan(input_data.get("text", ""))

    # Image OSINT
    image_intel = image_scan(input_data.get("image", ""))

    # Video OSINT
    video_intel = {}
    video_path = input_data.get("video")
    if video_path:
        video_intel = video_scan(video_path)

    username = input_data.get("username", "")

    # Combine results
    return {
        "scan_result": {
            "username": username,
            "text_intel": text_intel,
            "image_intel": image_intel,
            "video_intel": video_intel
        }
    }

