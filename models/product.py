# #!/usr/bin/python3
# """ holds class Product"""

# import models
# from models.base_model import BaseModel, Base
# from os import getenv
# import sqlalchemy
# from sqlalchemy import Column, String, Boolean, Text, ForeignKey, Integer
# from sqlalchemy.orm import relationship
# from hashlib import md5
# from models.category import product_category, Category


# class Product(BaseModel, Base):
#     """Representation of a product data and methods """
#     __tablename__ = 'products'
#     name = Column(String(128), nullable=False)
#     description = Column(Text, nullable=False)
#     price  = Column(Integer, nullable=False)
#     quantity = Column(Integer, default=False)
#     location = Column(String(100), nullable=True)
#     category_id = Column(String(60), ForeignKey('categories.id'),
#                          nullable=True)
#     user_id = Column(String(60), ForeignKey('users.id'),
#                      nullable=True)

#     # Relationship to Category model
#     categories = relationship('Category', secondary=product_category,
#                               back_populates='users')
#     user = relationship('User', back_populates='products')

#     def __init__(self, *args, **kwargs):
#         """initializes product"""
#         super().__init__(*args, **kwargs)

#     def set_price(self, price):
#         """ sets the price of the product """
#         self.price = price

#     def set_quantity(self, quantity):
#         """ sets the quantity of the product """
#         self.quantity = quantity
#     def set_location(self, location):
#         """ sets the location of the product """
#         self.location = location
#     def set_category(self, category):
#         """ sets the category of the product """
#         self.category_id = category.id
#     def set_user(self, user):
#         """ sets the user of the product """
#         self.user_id = user.id