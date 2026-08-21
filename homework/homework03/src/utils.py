"""Utility functions for the Stage 3 Python fundamentals homework."""

import pandas as pd


def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for the numeric columns in ``df``.

    Args:
        df: Dataset to summarize.

    Returns:
        A DataFrame containing count, mean, standard deviation, quartiles,
        minimum, and maximum for each numeric column.

    Raises:
        TypeError: If ``df`` is not a pandas DataFrame.
        ValueError: If ``df`` does not contain any numeric columns.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    numeric_df = df.select_dtypes(include="number")
    if numeric_df.empty:
        raise ValueError("df must contain at least one numeric column")

    return numeric_df.describe()
