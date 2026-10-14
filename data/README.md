# Telemetry demo data

These three independently authored fictional records demonstrate the exercise's two input schemas and common output schema. They are not the original Forage dataset or live factory telemetry.

- `data-1.json`: flat device fields, epoch milliseconds, slash-separated location, `operationStatus` and `temp`.
- `data-2.json`: nested device fields, a timezone-aware ISO timestamp, individual location fields and a `data` object.
- `data-result.json`: expected common output for either input.

Both inputs describe `demo-laser-001` at `2024-01-01T00:00:00.123Z`, corresponding to `1704067200123` milliseconds since the Unix epoch. The values are deliberately identical across representations so the tests can compare complete output dictionaries.

The examples are fixtures, not a complete validation specification. Format 1 expects five location components. Format 2 requires a timestamp with `Z` or an explicit UTC offset; finer-than-millisecond precision is floored.
