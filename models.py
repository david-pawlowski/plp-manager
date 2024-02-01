from uuid import uuid4 as uuid
from datetime import datetime
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine


class DateTimeMixins:
    created_at: Optional[datetime] = Field(default=datetime.now)
    updated_at: Optional[datetime] = Field(None)


class Team(SQLModel, DateTimeMixins, table=True):
    id: Optional[uuid] = Field(default=None, primary_key=True)
    name: str
    city: str


class Player(SQLModel, DateTimeMixins, table=True):
    id: Optional[uuid] = Field(default=None, primary_key=True)
    name: str
    team_id: Optional[int] = Field(foreign_key="team.id")


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
