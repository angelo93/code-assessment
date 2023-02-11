from sqlalchemy import Boolean, Column, Integer, String

# Local imports
from .database import Base


class Save(Base):
    '''Save table model'''

    __tablename__ = "saves"

    # Autoincrement should be set by default
    id = Column(Integer, primary_key=True, index=True)

    plr_one_active = Column(Boolean)
    plr_one_name = Column(String)
    plr_two_name = Column(String)
    plr_one_score = Column(Integer)
    plr_two_score = Column(Integer)
# end Save()
