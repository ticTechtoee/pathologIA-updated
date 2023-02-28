from django.urls import path
from . import views

app_name = 'ImagesApp'

urlpatterns = [
    path('CreateImage/', views.ViewCreateImage, name='CreateImageView'),
    path('ImagesGrid/<str:pk>', views.ViewImagesGrid, name='GridImages'),
]
