import json

def output():
    allowed = [
        "magictcg",
        "baseball",
        "nba",
        "sfgiants",
    ]

    block = [
        {
            "action": {"type": "block"},
            "trigger": {"url-filter": "https?://www.reddit.com"}
        },
        {
            "action": {"type": "ignore-previous-rules"},
            "trigger": {"url-filter": "https?://www.reddit.com/.+"}
        },
        {
            "action": {"type": "block"},
            "trigger": {"url-filter": "https?://www.reddit.com/default.json"}
        },
        {
            "action": {"type": "block"},
            "trigger": {"url-filter": "https?://www.reddit.com/hot.json"}
        },
        {
            "action": {"type": "block"},
            "trigger": {"url-filter": "https?://www.reddit.com/r/.*"}
        },
        {
            "action": {"type": "block"},
            "trigger": {"url-filter": "https?://i.reddit.com/*"}
        },
    ]

    for subreddit in allowed:
        block.append({
            "action": {
                "type": "ignore-previous-rules",
            },
            "trigger": {
                "url-filter": "https?://www.reddit.com/r/{}".format(subreddit),
            }
        })

    print(json.dumps(block, indent=4))


if __name__ == "__main__":
    output()
