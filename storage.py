"""Load and save wellness data as JSON in the project root."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DATA_FILE = Path(__file__).resolve().parent / "wellness_data.json"


def default_data() -> dict[str, Any]:
    return {
        "profile": {
            "age": 30,
            "sleep_hours": 7.0,
            "habits": {
                "water_glasses": 5,
                "exercise_minutes": 15,
                "steps_per_day": 6000,
            },
        },
        "chat_history": [],
    }


def load_data() -> dict[str, Any]:
    if not DATA_FILE.exists():
        return default_data()
    with DATA_FILE.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        return default_data()
    data.setdefault("profile", default_data()["profile"])
    data.setdefault("chat_history", [])
    return data


def save_data(data: dict[str, Any]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)