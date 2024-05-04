<div align="center">
  <a href="https://discord.com" target="_blank">
      <img width="70" src="images/discord.svg">
  </a>
  <a href="https://amacss.org/" target="_blank">
      <img width="70" src="images/amacss.svg">
  </a>

  <h1>AMACSS Discord Bot</h1>

  <p>
    This is the repository for the AMACSS open source Discord bot. By contributing to this bot, you can learn about open-source contribution while developing your Python skills.
  </p>
</div>

## Prerequisites

- Git
- Python 3.6-3.10
- Pip
- A Discord account

## Getting Started

<b>(1) Clone the repository:</b>
```
git clone git@github.com:amacss-utsc/amacss_bot.git
cd amacss_bot
```

Note: Cloning with either SSH or HTTPS is fine

<b> (2) Create a virtual environment: </b>

```
python -m venv venv
```

Note 1: If "python" doesn't work for the command above, try "python3"

Note 2: Please name your virtual environment "venv" (as done above) - if you decide to use a different name, add it to .gitignore

<b>(3) Activate your venv:</b>
```
source venv/bin/activate
```

Note: To deactivate your venv, use the command:
```
deactivate
```

<b>(4) Install necessary packages:</b>
```
pip install -r deps.txt
```

Note: If "pip" doesn't work for the command above, try "pip3"

## Discord Developer Portal

(1) Navigate to the <a href="https://discord.com/developers/applications">Discord Developer Portal</a> and authenticate using your Discord credentials.

(2) On the Applications dashboard page, click "New Application" and give a name of your choice:

![alt text](/images/instructions1.png)

(3) Navigate to the "Bot" tab, and in the token section, click "Reset Token". You should see a new token:

![alt text](/images/instructions2.png)

(4) Copy the token and store it for future use.