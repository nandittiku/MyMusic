import datetime
from sqlalchemy import schema, types, orm
from sqlalchemy.ext.declarative import declarative_base


metadata = schema.MetaData()
Base = declarative_base(metadata=metadata)

class Music(Base):
    __tablename__ = 'music'
    id = schema.Column(types.Integer, schema.Sequence('music_seq_id'), primary_key=True)
    title = schema.Column(types.Text(), default="")
    artist = schema.Column(types.Text(), default="")
    albumart = schema.Column(types.Text(), default="/albumart.jpg")
    name = schema.Column(types.Text())
    path = schema.Column(types.Text())
    summary = schema.Column(types.Text(), default="No info found")
    content = schema.Column(types.Text(), default="No info found")

music_table = Music.__tablename__

