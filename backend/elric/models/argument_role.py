from db.base import Base
from db.version import Version
from sqlalchemy import Column, Integer, String, ForeignKey


class ArgumentRole(Base):
    __tablename__ = 'events'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    role = Column(String(20))
    version = Column(Integer, ForeignKey(Version.id))

    def __repr__(self):
        return "<Argument Role(role='%s', start='%s', end='%s', text='%s')>" % self.role