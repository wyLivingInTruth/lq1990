#encode=utf-8

from django.db import models
from django.contrib import admin 

class Item(models.Model):
	title = models.CharField(max_length=50)
	url = models.URLField()  #URLField is a class ,so "()" is essential
	summary = models.CharField(max_length=300)


class ItemAdmin(admin.ModelAdmin):
	pass

admin.site.register(Item, ItemAdmin)
