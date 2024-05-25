from django.db import models

class Users(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Products(models.Model):
  name = models.CharField(max_length=50)
  value = models.DecimalField(max_digits=10, decimal_places=2)
  created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name

class Orders(models.Model):
  order_value = models.DecimalField(max_digits=10, decimal_places=2)
  product = models.ForeignKey(Products, on_delete=models.CASCADE)
  created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.order_value