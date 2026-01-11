# osint/text_osint.py

def text_scan(username: str) -> dict:
    """Dummy text OSINT scan."""
    if not username:
        return None

    return {
        "mentions_count": 2,
        "mentions": [
            {"source": "Twitter", "content": f"{username} tweeted about OSINT"},
            {"source": "Reddit", "content": f"{username} mentioned in r/OSINT"}
        ]
    }

