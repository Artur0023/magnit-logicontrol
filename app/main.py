from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.services.kpi import build_kpi_dataset
from app.services.data_loader import get_data
from app.services.visuals import (
    get_dashboard_kpi,
    get_top_oos_sku,
    get_supplier_sla
)


app = FastAPI(title='Magnit LogiControl')

# Подключение статистики и шаблонов
app.mount('/static', StaticFiles(directory='app/static'), name='static')
templates = Jinja2Templates(directory='app/templates')

# Загрузка данных один раз при старте
df = get_data()


# Главный дашборд
@app.get('/')
def dashboard(request: Request):
    """
    Главная страница с ключевыми логистическими показателями
    """
    kpi = get_dashboard_kpi(df)
    return templates.TemplateResponse(
        'dashboard.html',
        {
            'request': request,
            'kpi': kpi
        }
    )


# Остакти и OOS
@app.get('/stock')
def stock_page(request: Request):
    """
    Страница анализа SKU с высоким риском Out-of-Stock
    """
    oos = get_top_oos_sku(df).to_dict(orient='records')
    return templates.TemplateResponse(
        'stock.html',
        {
            'request': request,
            'oos': oos
        }
    )


# Поставки и SLA
@app.get('/shipments')
def shipments_page(request: Request):
    """
    Страница анализа SLA и задержек поставщиков
    """
    suppliers = get_supplier_sla(df).to_dict(orient='records')
    return templates.TemplateResponse(
        'shipments.html',
        {
            'request': request,
            'suppliers': suppliers
        }
    )