from __future__ import annotations

import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

SYSTEM_PROMPT = """You are Luyava AI Text Assistant. Answer in the user's language, be accurate and concise.
Never invent sources or claim to have performed actions you did not perform. Do not reveal secrets.
For cybersecurity content, provide defensive, authorized, educational guidance only."""


def ask(text: str, mode: str, model: str, max_tokens: int) -> str:
    load_dotenv()
    client = OpenAI(api_key=os.getenv("AI_API_KEY") or os.getenv("OPENAI_API_KEY"), base_url=os.getenv("AI_API_BASE") or os.getenv("OPENAI_API_BASE"))
    task = {
        "summarize": "Summarize the following text into clear bullet points and a one-sentence takeaway:",
        "extract": "Extract the key facts, decisions, action items, and unanswered questions from:",
        "rewrite": "Rewrite the following text in clear, professional Persian while preserving meaning:",
        "answer": "Answer the user's question using only the provided context when context is present:",
    }[mode]
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"{task}\n\n{text}"},
        ],
        max_completion_tokens=max_tokens,
    )
    return response.choices[0].message.content or ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Luyava AI Text Assistant")
    parser.add_argument("text", nargs="?", help="Text to process")
    parser.add_argument("--file", type=Path, help="Read input text from UTF-8 file")
    parser.add_argument("--mode", choices=["summarize", "extract", "rewrite", "answer"], default="summarize")
    parser.add_argument("--model", default=os.getenv("AI_MODEL", "gpt-5-mini"))
    parser.add_argument("--max-tokens", type=int, default=1200)
    args = parser.parse_args()
    if bool(args.text) == bool(args.file):
        parser.error("Provide exactly one of TEXT or --file")
    text = args.file.read_text(encoding="utf-8") if args.file else args.text
    print(ask(text, args.mode, args.model, args.max_tokens))


if __name__ == "__main__":
    main()
