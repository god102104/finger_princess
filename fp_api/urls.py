from django.urls import path, include
from fp_api import views
from rest_framework import routers
from . import services

router = routers.DefaultRouter()
router.register('cpus',views.CpuViewSet)
router.register('gpus',views.GpuViewSet)
router.register('laptops',views.LaptopViewSet)
router.register('games',views.GameViewSet)
router.register('programs',views.ProgramViewSet)
router.register('laptop_performances',views.LaptopPerformanceViewSet)
router.register('game_requirements',views.GameRequirementsViewSet)
router.register('program_requirements',views.ProgramRequirementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('services/recommend/',services.recommend)
    # path('asdfasdf/', views.asdfasdf, exampleparameter='wfeefsdf')
]
