from django.contrib import admin
from .models import *
# Register your models here.

model_list=[Cpu,Gpu,Laptop,Game,Program]

for model in model_list:
    admin.site.register(model)