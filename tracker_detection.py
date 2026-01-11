import random

def detect_trackers(username):
    """
    Simulated Reverse OSINT detection
    Input: username
    Output: potential tracking entities
    """

    if not username:
        return {"trackers_found": []}

    # Simulated known tracker sources
    trackers = [
        "SocialScraper Inc.",
        "ProfileIndexer.com",
        "OpenData Aggregator",
        "AnalyticsTracker.net",
        "DarkWebMonitor AI"
    ]

    # Randomly select 0-3 trackers for demo
    found = random.sample(trackers, random.randint(0, 3))

    tracker_info = []
    for t in found:
        tracker_info.append({
            "entity": t,
            "risk_score": random.randint(30, 90),
            "method": random.choice([
                "Web crawling",
                "Profile indexing",
                "API aggregation",
                "Social media scraping"
            ])
        })

    return {"trackers_found": tracker_info}
