from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Field, HTML
from django.urls import reverse



class Item:
  def __init__(self, name, price):
    self.price = price  
    self.name = name 
  def getName(self):
        return self.name
  def getPrice(self):
        return self.price
   
class DiscountCode:
  def __init__(self, code, discount_percent):
    self.code = code
    self.discount_percent = discount_percent

class ShoppingCart:
  def __init__(self):
    self.list = []
  def addItem(self, item):
    self.list.append(item)
  def getList(self):
        return self.list
  def printItems(self):
    for item in self.list:
      print(item.getName(), item.getPrice())
  def getTotalPrice(self):
    total = 0
    for item in self.list:
      total += item.getPrice()
    return total
  def removeItem(self, item):
    self.list.remove(item)
        
def applyDiscount(cart, discounts):
  authorized_codes = {
    "FREE2023": 70
  }
  for discount in discounts:
    if discount.code in authorized_codes:
      discount_percent = authorized_codes[discount.code]
      for item in cart.getList():
        item.price = item.price * (1 - discount_percent/100)


