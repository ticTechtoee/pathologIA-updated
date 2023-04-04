from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('HomeApp.urls')),
    path('admin/', admin.site.urls),
    path('Accounts/', include('AccountsApp.urls')),
    path('Images/', include('ImagesApp.urls')),
    path('Questions/', include('QuestionsApp.urls')),
    path('Students/', include('StudentsApp.urls')),
    path('Demarcate/', include('DemarcateApp.urls')),
    path('Prediction/', include('PredictionApp.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.MODEL_URL, document_root = settings.MODEL_ROOT)