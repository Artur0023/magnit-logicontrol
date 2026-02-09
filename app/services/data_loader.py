from app.services.kpi import build_kpi_dataset

_df_cache = None


def get_data():
    """
    Загружает и кэширует KPI-датасет для веб-приложения и Telegram-бота
    """
    global _df_cache
    if _df_cache is None:
        _df_cache = build_kpi_dataset()
    return _df_cache
