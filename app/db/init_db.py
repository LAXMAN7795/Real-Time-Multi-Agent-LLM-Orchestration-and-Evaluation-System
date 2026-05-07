from app.db.session import engine, Base

from app.db.base import *


def init_db():

    Base.metadata.create_all(bind=engine)