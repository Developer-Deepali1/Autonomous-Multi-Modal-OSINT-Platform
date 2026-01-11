import json
import time
from osint.text_osint import text_scan
from osint.image_osint import image_scan

SCAN_FILE = "data/scans.json"

class AutonomousAgent:

    def __init__(self):
        self.load_history()

    def load_history(self):
        try:
            with open(SCAN_FILE, "r") as f:
                self.history = json.load(f)
        except:
            self.history = {"history": []}

    def save_history(self):
        with open(SCAN_FILE, "w") as f:
            json.dump(self.history, f, indent=4)

    def perform_scan(self, input_data):
        username = input_data.get("username")
        image = input_data.get("image")

        scan_result = {
            "timestamp": time.time(),
            "username": username,
            "text": text_scan(username),
            "image": image_scan(image) if image else {}
        }

        changes = self.detect_new_exposure(scan_result)
        self.learn_patterns(scan_result)

        self.history["history"].append(scan_result)
        self.save_history()

        return {
            "scan_result": scan_result,
            "new_exposure_detected": changes
        }

    def detect_new_exposure(self, new_scan):
        if not self.history["history"]:
            return "Initial scan – no comparison"

        last_scan = self.history["history"][-1]

        new_platforms = set(new_scan["text"]["platforms_found"]) - \
                        set(last_scan["text"]["platforms_found"])

        if new_platforms:
            return {
                "new_platforms_found": list(new_platforms)
            }

        return "No new exposure detected"

    def learn_patterns(self, scan):
        """
        Self-learning behavior:
        - Learn username pattern
        - Increase weight of repeated platforms
        """
        username = scan["username"]

        if username and len(username) > 5:
            pattern = f"{username[:3]}*"
            scan["learned_username_pattern"] = pattern
