import os
import sys
import requests

from rich.console import Console
console = Console()

TOKEN = os.environ.get('OPEN_AI')
ASSISTANT_INSTRUCTION = "You are a assistant for the Linux terminal of few words. Answer questions about how to do something in the Linux terminal with a command matching the request only. Only answer with the suggested command."
PROMPT = " ".join(sys.argv[1:])


def check_token() -> None:
    if not TOKEN:
        console.print("[blue underline]Please put export OPEN_AI=APIKEY in your ~/.bash_profile or such.")
        exit(0)


def drop_first_and_last_code_quote(s: str) -> str:
    if s[0:3] == "```":
        s = s[3:]
    if s[-3:] == "```":
        s = s[:-3]
    if s[0] == "`":
        s = s[1:]
    if s[-1] == "`":
        s = s[:-1]
    return s.strip()


def ask_gpt():
    check_token()

    url = "https://api.openai.com/v1/chat/completions"
    response = requests.post(
        url, 
            json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": ASSISTANT_INSTRUCTION},
                {"role": "user", "content": PROMPT},
            ],
        }, 
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
        }
    )

    choises = response.json()["choices"]
    for choise in choises:
        console.print(drop_first_and_last_code_quote(choise["message"]["content"]))