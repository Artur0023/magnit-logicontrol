import sqlite3
import pandas as pd

DB_PATH = "data/logistics.db"
OUT_PATH = "data/ab_dataset.csv"

def main():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT
        sh.id AS shipment_id,
        sh.supplier_id,
        sh.dc_id,
        sh.delay_days
    FROM shipments sh
    WHERE sh.delay_days IS NOT NULL
    """

    df = pd.read_sql(query, conn)
    conn.close()

    df.to_csv(OUT_PATH, index=False)
    print(f"Dataset saved to {OUT_PATH}, rows: {len(df)}")

if __name__ == "__main__":
    main()
