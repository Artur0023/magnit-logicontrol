import random
from data_platform.db.engine import SessionLocal
from data_platform.db.models import Sales, SKU, DistributionCenter
from data_platform.generators.calendar import generate_dates


def generate_sales():
    '''
    Генерация ежедневных продаж
    '''
    session = SessionLocal()
    dates = generate_dates()

    skus = session.query(SKU).all()
    dcs = session.query(DistributionCenter).all()

    for d in dates:
        for dc in dcs:
            for sku in skus:
                units = max(0, int(random.gauss(20, 7)))

                session.add(
                    Sales(
                        date=d,
                        sku_id=sku.sku_id,
                        dc_id=dc.dc_id,
                        units_sold=units
                    )
                )

    session.commit()
    session.close()