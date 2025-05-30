"""A puller for yahoo finance data."""

# pylint: disable=global-statement
import logging

import pandas as pd
import yfinance as yf  # type: ignore


def pull(series: str) -> list[pd.Series]:
    """Pull the yfinance data."""
    logging.info("Pulling yfinance series %s", series)
    series_name = "yfinance_" + series
    df = yf.Ticker(series).history(start="2000-01-01")
    df.index = df.index.date  # type: ignore
    df = df.sort_index()
    return [
        df["Close"].rename(series_name + "_close"),
        df["Volume"].rename(series_name + "_volume"),
    ]
