"""Load and save wellness data as JSON in the project root."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DATA_FILE = Path(__file__).resolve().parent / "wellness_data.json"