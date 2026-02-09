import pandas as pd
import numpy as np

def assign_ab_groups(df, seed=42):
    """
    Случайно распределяет поставщиков на A/B группы
    """
    np.random.seed(seed)

    suppliers = df["supplier_id"].unique()
    group_map = {
        s: "B" if np.random.rand() < 0.5 else "A"
        for s in suppliers
    }

    df["ab_group"] = df["supplier_id"].map(group_map)
    return df
