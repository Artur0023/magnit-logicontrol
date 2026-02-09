import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "logistics.db"


def load_table(table_name: str) -> pd.DataFrame:
    """
    Загружает таблицу из SQLite в pandas DataFrame
    """
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df
