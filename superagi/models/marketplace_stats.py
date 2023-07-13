from __future__ import annotations

from sqlalchemy import Column, Integer, String
import requests

# from superagi.models import AgentConfiguration
from superagi.models.base_model import DBBaseModel

#marketplace_url = "https://app.superagi.com/api"
marketplace_url = "http://localhost:8001"

class MarketPlaceStats(DBBaseModel):
    """
    Represents an knowledge entity.

    Attributes:
        id (int): The unique identifier of the marketplace stats.
        reference_id (int): The unique identifier of the reference.
        reference_name (str): The name of the reference used.
        key (str): The key for the statistical value.
        value (int): The value for the specified key.
    """

    __tablename__ = 'marketplace_stats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    reference_id = Column(Integer)
    reference_name = Column(String)
    key = Column(String)
    value = Column(Integer)

    def __repr__(self):
        """
        Returns a string representation of the MarketplaceStats object.

        Returns:
            str: String representation of the MarketplaceStats.

        """
        return f"Knowledge(id={self.id}, reference_id='{self.reference_id}', reference_name='{self.reference_name}', " \
               f"key='{self.key}', value='{self.value}'"
    
    @classmethod
    def get_knowledge_installation_number(cls, session, knowledge_id: int):
        installation_number = session.query(MarketPlaceStats).filter(MarketPlaceStats.reference_id == knowledge_id, MarketPlaceStats.reference_name == "KNOWLEDGE", MarketPlaceStats.key == "download_count").first()
        if installation_number is None:
            value = 0
        else:
            value = installation_number.value
        return value