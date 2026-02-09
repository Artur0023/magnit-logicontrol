from app.services.kpi import build_kpi_dataset
from app.services.visuals import (
    dashboard_kpi,
    top_oos_sku,
    supplier_sla,
    plot_stock_vs_sales,
    plot_shipment_delays
)


df = build_kpi_dataset()


print('---- DASHBOARD KPI ----')
print(dashboard_kpi(df))


print('---- TOP OOS SKU ----')
print(top_oos_sku(df))


print('---- SUPPLIER SLA ----')
print(supplier_sla(df))


plot_stock_vs_sales(df, 'SKU_001', 'DC_01')
plot_shipment_delays(df)