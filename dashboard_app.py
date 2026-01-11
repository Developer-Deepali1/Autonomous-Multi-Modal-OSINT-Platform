# dashboard/dashboard_app.py

import dash
from dash import html, dcc
import plotly.express as px
from core.orchestrator import run_osint_scan

# Sample input for demonstration
sample_input = {
    "username": "deepali",
    "text": "This is a sample text for OSINT scan",
    "image": "data/sample.jpg",
    "video": "data/sample.mp4"
}

# Run scan
scan_result = run_osint_scan(sample_input)["scan_result"]

# Extract results
text_intel = scan_result.get("text_intel", {})
image_intel = scan_result.get("image_intel", {})
video_intel = scan_result.get("video_intel", {})

# Create Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1(f"OSINT Dashboard for {scan_result['username']}"),

    html.H2("Text Intelligence"),
    html.Pre(str(text_intel)),

    html.H2("Image Intelligence"),
    html.Pre(str(image_intel)),

    html.H2("Video Intelligence"),
    html.Pre(str(video_intel)),

    html.H3("Video Landmarks Table"),
    html.Table([
        html.Tr([html.Th("Landmark"), html.Th("Coordinates")])] +
        [html.Tr([html.Td(lm["landmark"]), html.Td(str(lm["coordinates"]))])
         for lm in video_intel.get("landmarks", [])]
    )
])

# Run app
if __name__ == "__main__":
    app.run(debug=True, port=8050)
