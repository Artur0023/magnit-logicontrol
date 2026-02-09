import pandas as pd
import numpy as np

from app.config import OOS_HIGH_DOH, OOS_MEDIUM_DOH


def load_data(path=r"C:\Users\artur\Desktop\портфолио\magnit-logicontrol\data\magnit_mock.csv"):
    df = pd.read_csv(path, sep=';')
    df['date'] = pd.to_datetime(df['date'])
    df['shipment_planned'] = pd.to_datetime(df['shipment_planned'], errors='coerce')
    df['shipment_actual'] = pd.to_datetime(df['shipment_actual'], errors='coerce')
    return df


def calc_avg_daily_sales(df, window=7):
    df = df.sort_values('date')
    df['avg_daily_sales'] = (
        df.groupby(['dc_id', 'sku_id'])['sales_qty'].transform(lambda x: x.rolling(window, min_periods=1).mean())
    )
    return df


def calc_doh(df):
    """
    Рассчитывает Days of Hand (DOH) по SKU и РЦ
    """
    df['doh'] = np.where(
        df['avg_daily_sales'] > 0,
        df['stock_qty'] / df['avg_daily_sales'],
        np.nan
    )
    return df


def calc_oos_risk(df):
    """
    Классифицирует риск Out-of-Stock на основе DOH
    """

    df['oos_risk'] = np.select(
        [
            df['doh'] < OOS_HIGH_DOH,
            (df['doh'] >= OOS_HIGH_DOH) & (df['doh'] < OOS_MEDIUM_DOH),
            df['doh'] >= OOS_MEDIUM_DOH
        ],
        ['HIGH', 'MEDIUM', 'LOW'],
        default='UNKNOWN'
    )

    return df


def calc_sla(df):
    df['sla_ok'] = np.where(
        df['shipment_actual'].notna(),
        df['shipment_actual'] <= df['shipment_planned'],
        np.nan
    )
    return df


def calc_shipment_delay(df):
    """
    Рассчитывает задержку поставок относительно плановой даты
    """
    df['delay_days'] = (
        df['shipment_actual'] - df['shipment_planned']
    ).dt.days
    return df


def build_kpi_dataset(path=r"C:\Users\artur\Desktop\портфолио\magnit-logicontrol\data\magnit_mock.csv"):
    """
    Формирует единый датасет с KPI для логистической аналитики
    """    
    df = load_data(path)
    df = calc_avg_daily_sales(df)
    df = calc_doh(df)
    df = calc_oos_risk(df)
    df = calc_sla(df)
    df = calc_shipment_delay(df)
    return df