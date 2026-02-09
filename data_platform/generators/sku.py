import random
from data_platform.db.engine import SessionLocal
from data_platform.db.models import SKU

def generate_sku():
    session = SessionLocal()

    categories = ["FMCG", "Fresh", "NonFood"]

    for i in range(1, 51):
        sku_id = f"SKU_{i:04d}"
        category = random.choice(categories)

        # логика цены по категории (реалистично для Магнита)
        if category == "Fresh":
            price = random.randint(50, 300)
            shelf_life = random.randint(3, 14)
        elif category == "FMCG":
            price = random.randint(30, 200)
            shelf_life = random.randint(90, 365)
        else:
            price = random.randint(100, 1000)
            shelf_life = random.randint(365, 2000)

        session.merge(
            SKU(
                sku_id=sku_id,
                category=category,
                price=price,
                shelf_life=shelf_life
            )
        )

    session.commit()
    session.close()
    print("SKU generated")
