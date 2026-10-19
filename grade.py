"""Convert a score (0-100) to a letter grade A-F."""


def grade(score):
    """Return the letter grade for a score between 0 and 100.

    Raises:
        ValueError: if score is not a number or outside 0-100.
    """
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise ValueError("score must be a number")
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 80:
        return "A"
    if score >= 70:
        return "B"
    if score >= 60:
        return "C"
    if score >= 50:
        return "D"
    return "F"
