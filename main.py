"""Six-word story: an AI agent's first payday."""
import os

LINE = "Earned first dollar, bought creator coffee."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as handle:
    handle.write(LINE)
