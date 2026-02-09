from data_platform.db.engine import SessionLocal
from data_platform.db.models import DistributionCenter
from data_platform.config import DC_LIST


def generate_distribution_centers():
    """
    Создаёт распределительные центры
    """
    session = SessionLocal()

    for dc_id, region, capacity in DC_LIST:
        session.merge(
            DistributionCenter(
                dc_id=dc_id,
                region=region,
                capacity=capacity
            )
        )

    session.commit()
    session.close()
    print("Distribution Centers generated")
