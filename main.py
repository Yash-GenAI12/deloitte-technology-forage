"""Run the telemetry conversion checks from the repository root."""

from pathlib import Path
import unittest


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parent
    suite = unittest.defaultTestLoader.discover(
        start_dir=str(project_dir / "tests"),
        top_level_dir=str(project_dir),
    )
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
