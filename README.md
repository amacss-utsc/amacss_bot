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

Clone the repository:
```
git clone git@github.com:amacss-utsc/amacss_bot.git
cd amacss_bot
```

Note: Cloning with either SSH or HTTPS is fine

Create a virtual environment:

```
python -m venv venv
```

Note 1: If "python" doesn't work for the command above, try "python3"

Note 2: Please name your virtual environment "venv" (as done above) - if you decide to use a different name, add it to .gitignore

Activate your venv:
```
source venv/bin/activate
```

Note: To deactivate your venv, use the command:
```
deactivate
```

Install necessary packages:
```
pip install -r deps.txt
```

Note: If "pip" doesn't work for the command above, try "pip3"