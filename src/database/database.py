from peewee import *


db = SqliteDatabase(
    "src/database/database.db", check_same_thread=False
)


class BaseModel(Model):
    class Meta:
        database = db


class Settings(BaseModel):
    is_installed = BooleanField(default=0)
    token = TextField()


class Chats(BaseModel):
    local_id = IntegerField()
    peer_id = IntegerField()


def load_db():
    db.create_tables([Settings, Chats])
