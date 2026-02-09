from pathlib import Path

from data_platform.db.engine import engine, Base
from data_platform.db import models 


def init_db():
    """
    Создает все таблицы в БД
    """
    Path(engine.url.database).parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=engine)
    print('Database initialized')


if __name__ == '__main__':
    init_db()