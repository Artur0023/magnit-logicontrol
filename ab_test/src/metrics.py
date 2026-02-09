def calc_metrics(df):
    """
    Считает ключевые метрики по группам
    """
    return (
        df.groupby("ab_group")
        .agg(
            avg_delay=("delay_days", "mean"),
            p95_delay=("delay_days", lambda x: x.quantile(0.95)),
            late_share=("delay_days", lambda x: (x > 2).mean())
        ).reset_index()
    )
