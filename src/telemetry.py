"""Unify the two telemetry formats used in the Forage coding task."""

import datetime


def convertFromFormat1(jsonObject):
    """Split the location path and rename the telemetry fields."""
    country, city, area, factory, section = jsonObject["location"].split("/")
    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": country,
            "city": city,
            "area": area,
            "factory": factory,
            "section": section,
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"],
        },
    }


def convertFromFormat2(jsonObject):
    """Flatten device details and convert an ISO timestamp to epoch milliseconds."""
    # Z means UTC; replacing it also supports Python versions before 3.11.
    timestamp = datetime.datetime.fromisoformat(
        jsonObject["timestamp"].replace("Z", "+00:00")
    )
    if timestamp.tzinfo is None:
        raise ValueError("The ISO timestamp must include a timezone (Z or an offset).")

    epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
    # Integer timedelta division avoids floating-point rounding errors.
    # Inputs have millisecond precision; any finer precision is floored.
    milliseconds = (timestamp - epoch) // datetime.timedelta(milliseconds=1)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": milliseconds,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"],
        },
        "data": dict(jsonObject["data"]),
    }


def main(jsonObject):
    """Select the converter for a record's input format."""
    if jsonObject.get("device") is None:
        return convertFromFormat1(jsonObject)
    return convertFromFormat2(jsonObject)
