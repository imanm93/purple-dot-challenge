import os
import time
from typing import Iterator

from app.config import settings
from sqlalchemy import create_engine, engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
GenDB = Iterator[orm.Session]


def postgres_url():
    return engine.url.URL(
        "postgresql",
        username=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        database=os.getenv("POSTGRES_DATABASE", "postgres"),
    )


def wait_for_db(db_uri):
    """checks if database connection is established"""

    _local_engine = create_engine(db_uri)
    _LocalSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=_local_engine
    )

    up = False
    while not up:
        try:
            db_session = _LocalSessionLocal()
            db_session.execute("SELECT 1")
            db_session.commit()
        except Exception as err:
            print(f"Connection error: {err}")
            up = False
        else:
            up = True

        time.sleep(2)


url = settings.POSTGRES.URL if settings.POSTGRES.URL else postgres_url()
wait_for_db(url)

db_engine = create_engine(url, pool_size=5, max_overflow=20, pool_pre_ping=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


def get_db() -> GenDB:
    db = None
    try:
        db = Session()
        yield db
    finally:
        if db:
            db.close()
