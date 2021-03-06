"""The application's model objects"""
from mymusic.model.meta import Session, Base

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base

from mymusic.model import meta

def init_model(engine):
    Session.configure(bind=engine)
    sm = orm.sessionmaker(autoflush=True, autocommit=False, bind=engine)

    meta.engine = engine
    meta.Session = orm.scoped_session(sm)


