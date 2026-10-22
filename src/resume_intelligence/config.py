from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    project_root: Path = Path(__file__).resolve().parents[2]
    data_dir: Path = project_root / "data"
    synthetic_dir: Path = data_dir / "synthetic"
    resumes_dir: Path = synthetic_dir / "resumes"
    ground_truth_dir: Path = synthetic_dir / "ground_truth"
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    vector_db_path: str = os.getenv("VECTOR_DB_PATH", str(project_root / "data" / "processed" / "vector_store"))


settings = Settings()
