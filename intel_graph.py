import networkx as nx

def build_graph(text_data, image_data=None, video_data=None, trackers_data=None):
    """
    Build a unified intelligence graph from multiple OSINT sources:
    - text (platforms, entities)
    - image (EXIF, landmarks)
    - video (frames, landmarks)
    - trackers (reverse OSINT)
    """
    G = nx.Graph()

    # Add User Node
    user_node = "User"
    G.add_node(user_node, type="user")

    # Text OSINT
    if text_data:
        for platform in text_data.get("platforms_found", []):
            G.add_node(platform, type="platform")
            G.add_edge(user_node, platform, relation="posted_on")

        for ent in text_data.get("entities", []):
            entity_node = ent.get("text")
            if entity_node:
                G.add_node(entity_node, type="entity", label=ent.get("label"))
                G.add_edge(user_node, entity_node, relation="entity")

    # Image OSINT
    if image_data:
        image_node = "Image"
        G.add_node(image_node, type="image")
        G.add_edge(user_node, image_node, relation="uploaded_image")
        if "exif_gps" in image_data:
            gps_node = "Image_GPS"
            G.add_node(gps_node, type="gps", data=image_data["exif_gps"])
            G.add_edge(image_node, gps_node, relation="gps_metadata")

    # Video OSINT
    if video_data:
        video_node = "Video"
        G.add_node(video_node, type="video")
        G.add_edge(user_node, video_node, relation="uploaded_video")
        for i, landmark in enumerate(video_data.get("landmarks", [])):
            lm_node = f"Video_Landmark_{i}"
            G.add_node(lm_node, type="landmark", data=landmark)
            G.add_edge(video_node, lm_node, relation="landmark")

    # Reverse OSINT Trackers
    if trackers_data and "trackers_found" in trackers_data:
        for tracker in trackers_data["trackers_found"]:
            tracker_node = tracker["entity"]
            G.add_node(tracker_node, type="tracker", risk=tracker["risk_score"])
            G.add_edge(user_node, tracker_node, relation=tracker["method"])

    return G

