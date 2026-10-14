"""Demo fixture checks and timestamp boundary regression tests."""

from copy import deepcopy
import json
from pathlib import Path
import unittest

from src.telemetry import main


DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_fixture(filename):
    """Read a UTF-8 fixture independently of the current working directory."""
    with (DATA_DIR / filename).open(encoding="utf-8") as fixture:
        return json.load(fixture)


class TestSolution(unittest.TestCase):
    """Retain the exercise's three check patterns using public demo fixtures."""

    @classmethod
    def setUpClass(cls):
        cls.jsonData1 = load_fixture("data-1.json")
        cls.jsonData2 = load_fixture("data-2.json")
        cls.jsonExpectedResult = load_fixture("data-result.json")

    def test_sanity(self):
        result = json.loads(json.dumps(self.jsonExpectedResult))
        self.assertEqual(result, self.jsonExpectedResult)

    def test_dataType1(self):
        self.assertEqual(
            main(self.jsonData1),
            self.jsonExpectedResult,
            "Converting from Type 1 failed",
        )

    def test_dataType2(self):
        self.assertEqual(
            main(self.jsonData2),
            self.jsonExpectedResult,
            "Converting from Type 2 failed",
        )

    def test_inputs_are_not_mutated(self):
        for fixture in (self.jsonData1, self.jsonData2):
            with self.subTest(format="nested" if "device" in fixture else "flat"):
                record = deepcopy(fixture)
                main(record)
                self.assertEqual(record, fixture)


class TestTimestamps(unittest.TestCase):
    """Check timezone handling and millisecond precision around the Unix epoch."""

    def setUp(self):
        self.record = load_fixture("data-2.json")

    def assert_timestamp(self, iso_timestamp, expected_milliseconds):
        self.record["timestamp"] = iso_timestamp
        actual = main(self.record)["timestamp"]
        self.assertIsInstance(actual, int)
        self.assertEqual(actual, expected_milliseconds)

    def test_epoch_and_adjacent_milliseconds(self):
        cases = (
            ("1969-12-31T23:59:59.999Z", -1),
            ("1970-01-01T00:00:00.000Z", 0),
            ("1970-01-01T00:00:00.001Z", 1),
        )
        for timestamp, expected in cases:
            with self.subTest(timestamp=timestamp):
                self.assert_timestamp(timestamp, expected)

    def test_utc_offsets_represent_the_same_instant(self):
        cases = (
            "1970-01-01T00:00:00.001+00:00",
            "1970-01-01T05:30:00.001+05:30",
            "1969-12-31T19:00:00.001-05:00",
        )
        for timestamp in cases:
            with self.subTest(timestamp=timestamp):
                self.assert_timestamp(timestamp, 1)

    def test_timezone_is_required(self):
        self.record["timestamp"] = "1970-01-01T00:00:00.001"
        with self.assertRaisesRegex(ValueError, "must include a timezone"):
            main(self.record)


if __name__ == "__main__":
    unittest.main()
