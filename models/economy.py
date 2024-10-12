from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class EconomyPlayer(Base):
    __tablename__ = 'economy_player'

    id = Column(Integer, primary_key=True)
    discord_id = Column(String, nullable=False, unique=True)
    discord_name = Column(String, nullable=False)
    balance = Column(Integer, default=0)
    inventory = relationship('Inventory', back_populates='player', cascade='all, delete-orphan')

class Inventory(Base):
    __tablename__ = 'economy_inventory'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('economy_player.id'))
    item_name = Column(String, nullable=False)
    item_type = Column(String, nullable=False)
    quantity = Column(Integer, default=1)
    player = relationship('EconomyPlayer', back_populates='inventory')

    