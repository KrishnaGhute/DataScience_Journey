# utils/helpers.py
def format_large_number(num):
    """Formatting utility helper function for large numeric indicators."""
    if num is None:
        return "0"
    return f"{num:,.2f}"