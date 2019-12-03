from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    # 软删除
    status = Column(SmallInteger, default=1)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def set_attrs(self,attrs_dict):

        for key, value in attrs_dict.items():
            # 判断当前key在模型中 是否有同名属性  hasattr（判断对象，是否包含某个属性）
            if hasattr(self, key) and key != 'id':
                # 赋值
                setattr(self, key, value)