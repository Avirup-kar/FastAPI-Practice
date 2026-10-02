from sqlalchemy import Column, Integer, String, Text
from database import Base

class Blog (Base):
    _tablename_ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)