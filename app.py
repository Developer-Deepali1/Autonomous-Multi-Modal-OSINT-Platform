from flask import Flask, request, jsonify, render_template
import os
from core.orchestrator import run_osint_scan

app = Flask(__name__)
UPLOAD_FOLDER = "data"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan-ui", methods=["POST"])
def scan_ui():
    username = request.form.get("username")

    image = request.files.get("image")
    video = request.files.get("video")

    image_path = None
    video_path = None

    if image and image.filename:
        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)

    if video and video.filename:
        video_path = os.path.join(UPLOAD_FOLDER, video.filename)
        video.save(video_path)

    result = run_osint_scan({
        "username": username,
        "image": image_path,
        "video": video_path
    })

    return render_template(
        "result.html",
        risk=result.get("risk_assessment", {
            "level": "LOW",
            "score": 0,
            "summary": "No risk assessment generated yet"
        }),
        trackers=result.get("reverse_osint", {}).get("trackers_found", [])
    )

if __name__ == "__main__":
    app.run(debug=True)



