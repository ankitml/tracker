from django.db import models


class FoodItem(models.Model):
    name = models.TextField(help_text="Primary foods name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FoodItemNames(models.Model):
    food = models.ForeignKey(FoodItem)
    name = models.TextField(help_text="A synonym of foods item")
    locale = models.TextField(help_text="Which language / region uses this name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Eating(models.Model):
    food = models.ForeignKey(FoodItem)
    time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

