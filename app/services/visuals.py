import pandas as pd
import matplotlib.pyplot as plt

# KPI главного дашборда
def get_dashboard_kpi(df: pd.DataFrame) -> dict:
    '''
    Агрегированные KPI для главного дашборда
    '''
    return {
        'avg_doh': round(df['doh'].mean(), 2),
        'high_oos_share': round((df['oos_risk'] == 'HIGH').mean() * 100, 1),
        'sla_rate': round(df['sla_ok'].mean() * 100, 1),
        'avg_delay': round(df['delay_days'].dropna().mean(), 2)
    }


# Топ SKU с риском OOS
def get_top_oos_sku(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    '''
    SKU с наибольшим риском out-of-stock
    '''
    result = (
        df[df['oos_risk'] == 'HIGH']
        .groupby(['dc_id', 'sku_id'])
        .agg(avg_doh=('doh', 'mean'), days_high_oos=('oos_risk', 'count'))
        .sort_values('avg_doh')
        .head(top_n)
        .reset_index()
    )

    return result


# SLA поставщиков
def get_supplier_sla(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Аналитика SLA по поставщикам
    '''
    result = (
        df[df['shipment_actual'].notna()]
        .groupby('supplier')
        .agg(
            sla_rate=('sla_ok', 'mean'),
            avg_delay=('delay_days', 'mean'),
            shipments=('shipment_qty', 'count')
        )
        .sort_values('sla_rate')
        .reset_index()
    )

    return result


# График: остатки / продажи (SKU + РЦ) 
def get_plot_stock_vs_sales(df: pd.DataFrame, sku_id: str, dc_id: str) -> None:
    '''
    График остатков и продаж для одного SKU на одном РЦ
    '''
    data = df[(df['sku_id'] == sku_id) & (df['dc_id'] == dc_id)]

    if data.empty:
        print('Нет данных для выбранного SKU / РЦ')
        return

    plt.figure()
    plt.plot(data['date'], data['stock_qty'], label='Остаток')
    plt.plot(data['date'], data['sales_qty'], label='Продажи')
    plt.legend()
    plt.title(f"{sku_id} | {dc_id}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# График: распределение задержек поставок
def get_plot_shipment_delays(df: pd.DataFrame) -> None:
    '''
    Распределение задержек поставок в днях
    '''
    delays = df['delay_days'].dropna()

    if delays.empty:
        print('Нет данных по задержкам поставок')
        return

    plt.figure()
    delays.value_counts().sort_index().plot(kind='bar')
    plt.title('Задержки поставок (дни)')
    plt.xlabel('Дни задержки')
    plt.ylabel('Количество')
    plt.tight_layout()
    plt.show()