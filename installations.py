import subprocess
import sys

PACKAGES = [
    "streamlit",
    "groq",
    "python-dotenv",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "scipy",
]

for package in PACKAGES:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
