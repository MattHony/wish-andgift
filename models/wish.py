# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/6 20:50
# @Author : '红文'
# @File : wish.py
# @Software: PyCharm
from sqlalchemy.orm import relationship
from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)