# helper functions for weather insights

def convert_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def format_timestamp(ts: str) -> str:
    """Make timestamp easier to read (YYYY-MM-DD HH:MM)."""
    return ts.replace("T", " ")[:16]
