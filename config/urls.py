
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path('movi/<int:id>', views.detail,name = 'view'),
    path('movie/create',views.create, name='create'),
    path("delete/<int:id>", views.delete, name="delete"),
    path("update/<int:id>", views.update,name="update")
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

