# BTCForum-Launch
# LaunchOnBTC

**LaunchOnBTC** is an automated tool that enables seamless coin launches on [BitcoinForum.org](https://bitcointalk.org). Simply post:
"@LaunchonBTC $ticker + name"


… and LaunchOnBTC will generate and publish an official launch thread for your project on BitcoinForum.org.

---

## 🚀 Features

- ✅ Automatically detects launch commands from social media or community platforms
- 🧠 Parses ticker and project name from a simple trigger message
- 🌐 Posts a formatted announcement thread to BitcoinForum.org
- 📎 Generates a shareable launch thread URL
- 📈 Helps kickstart community traction and exposure

---

## 📥 Command Format

To initiate a launch, use the following syntax anywhere LaunchOnBTC is active:


LaunchOnBTC will handle the rest.

---

## 📝 Announcement Format

Each launch creates a standardized thread that includes:

- Project name and ticker
- Description template (can be customized)
- Placeholder links for website, tokenomics, whitepaper, etc.
- Optional embedded images or banners

Example output:


---

## 🔧 Setup & Deployment

> Requirements: Python 3.8+, access credentials to a BitcoinForum.org account with posting rights

1. Clone the repo  
2. Configure your `config.py` with forum credentials and thread template
3. Run the listener:
```bash
python launch.py




