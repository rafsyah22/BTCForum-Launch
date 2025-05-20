# launch.py
from parser import parse_message
from forum_api import post_announcement


def main():
    print("Listening for launch commands...")

    # Simulated messages input (replace with Twitter API, Discord bot, etc.)
    messages = [
        "@LaunchOnBTC $FISH Fish Coin",
        "@LaunchOnBTC $MOON MoonShiba",
        "random message",
    ]

    for message in messages:
        ticker, name = parse_message(message)
        if ticker and name:
            url = post_announcement(ticker, name)
            print(f"✅ ${ticker} ({name}) launched!")
            print(f"👉 {url}\n")
        else:
            print("❌ No valid launch command found.\n")


if __name__ == "__main__":
    main()


# parser.py
import re

def parse_message(message):
    pattern = r"@LaunchOnBTC\s+\$(\w+)\s+([\w\s]+)"
    match = re.search(pattern, message)
    if match:
        ticker = match.group(1).upper()
        name = match.group(2).strip()
        return ticker, name
    return None, None


# forum_api.py
from config import BITCOINFORUM_BASE_URL

def post_announcement(ticker, name):
    # Simulated announcement post
    # Replace this with actual forum posting logic (Selenium or API-based)
    slug = ticker.lower()
    announcement_url = f"{BITCOINFORUM_BASE_URL}/index.php?topic={slug}_launch"
    print(f"Posting to BitcoinForum.org: ${ticker} - {name}")
    return announcement_url


# config.py
BITCOINFORUM_BASE_URL = "https://bitcointalk.org"


# README.md
# LaunchOnBTC

**LaunchOnBTC** is an automated tool that simulates launching your coin on [BitcoinForum.org](https://bitcointalk.org).

## 🚀 Usage

Post this format anywhere LaunchOnBTC listens:

```
@LaunchOnBTC $TICKER CoinName
```

Example:
```
@LaunchOnBTC $FISH Fish Coin
```

## 📁 Files

- `launch.py`: Main entry point
- `parser.py`: Parses trigger messages
- `forum_api.py`: Simulates forum posting
- `config.py`: Configuration settings
