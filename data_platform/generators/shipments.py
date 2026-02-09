import random
from data_platform.db.engine import SessionLocal
from data_platform.db.models import Shipment, Supplier, SKU, DistributionCenter
from data_platform.generators.calendar import generate_dates

def generate_shipments():
    """
    Генерация поставок с задержками
    """
    session = SessionLocal()
    dates = generate_dates()

    suppliers = session.query(Supplier).all()
    skus = session.query(SKU).all()
    dcs = session.query(DistributionCenter).all()

    for d in dates:
        for dc in dcs:
            supplier = random.choice(suppliers)
            sku = random.choice(skus)

            session.add(
                Shipment(
                    date=d,
                    sku_id=sku.sku_id,
                    supplier_id=supplier.supplier_id,
                    dc_id=dc.dc_id,
                    qty=random.randint(50, 200),
                    delay_days=max(0, int(random.gauss(1, 2)))
                )
            )

    session.commit()
    session.close()
