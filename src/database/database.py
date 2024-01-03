from peewee import *


db = SqliteDatabase(
    "src/database/database.db",
    check_same_thread=False
)


class BaseModel(Model):
    class Meta:
        database = db


class Settings(BaseModel):
    ...


class Chats(BaseModel):
    ...


def load_db():
    db.create_tables([Settings, Chats])
