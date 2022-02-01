
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('gallery', gallery, name='gallery'),
    path('full-width', full_width, name='full'),
    path('sidebar', side_bar, name='side-bar'),
    path('side-right', sidebar_right, name='sidebar-right'),
    path('basic-grid', basic_grid, name='basic-grid'),
]