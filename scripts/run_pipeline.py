from pathlib import Path

from src.io_utils import load_config
from src.pipeline import run_pipeline


def main():
    PROJECT_DIR = Path(__file__).resolve().parents[1]
    config_path = PROJECT_DIR / "configs" / "default.yaml"

    config = load_config(config_path)
    config["input"]["path"] = PROJECT_DIR / config["input"]["path"]

    result = run_pipeline(config)


if __name__ == "__main__":
    main()