import random
from data_platform.db.engine import SessionLocal
from data_platform.db.models import Supplier

def generate_suppliers():
    session = SessionLocal()

    regions = ["Central", "North", "South", "Ural", "Siberia"]

    for i in range(1, 11):
        supplier_id = f"SUP_{i:02d}"

        supplier = Supplier(
            supplier_id=supplier_id,
            name=f"Supplier {i}",
            region=random.choice(regions),
            base_sla=random.randint(1, 7)
        )

        session.merge(supplier)

    session.commit()
    session.close()

    print("Suppliers generated")
