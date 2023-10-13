from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
     Maps to the 'states' table.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.

    Args:
        Base (DeclarativeMeta): The base class.
        """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)