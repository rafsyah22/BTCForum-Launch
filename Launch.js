// launch.js

function parseMessage(message) {
  const regex = /@LaunchOnBTC\s+\$(\w+)\s+([\w\s]+)/i;
  const match = message.match(regex);
  if (match) {
    return {
      ticker: match[1].toUpperCase(),
      name: match[2].trim(),
    };
  }
  return null;
}

function postAnnouncement(ticker, name) {
  const slug = ticker.toLowerCase();
  const forumURL = `https://bitcointalk.org/index.php?topic=${slug}_launch`;
  console.log(`✅ $${ticker} (${name}) has been launched on BitcoinForum.org!`);
  console.log(`👉 ${forumURL}`);
}

const messages = [
  "@LaunchOnBTC $APE ApeCoin",
  "Some other text",
  "@LaunchOnBTC $MOON MoonToken"
];

messages.forEach(message => {
  const result = parseMessage(message);
  if (result) {
    postAnnouncement(result.ticker, result.name);
  } else {
    console.log("❌ No valid launch command found.\n");
  }
});


// launch.json
{
  "exampleMessages": [
    "@LaunchOnBTC $APE ApeCoin",
    "@LaunchOnBTC $MOON MoonToken"
  ],
  "simulatedLaunches": [
    {
      "ticker": "APE",
      "name": "ApeCoin",
      "forumLink": "https://bitcointalk.org/index.php?topic=ape_launch"
    },
    {
      "ticker": "MOON",
      "name": "MoonToken",
      "forumLink": "https://bitcointalk.org/index.php?topic=moon_launch"
    }
  ],
  "disclaimer": "This is a simulation and does not create real forum threads."
}
