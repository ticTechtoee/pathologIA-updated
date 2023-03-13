from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from StudentsApp.views import ViewSubmitAnswers

urlpatterns = [
    path('', include('HomeApp.urls')),
    path('admin/', admin.site.urls),
    path('Images/', include('ImagesApp.urls')),
    path('Questions/', include('QuestionsApp.urls')),
    path('Students/', include('StudentsApp.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)