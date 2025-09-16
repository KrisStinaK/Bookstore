from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    #user management
    path('accounts/', include('allauth.urls')),
    #local apps
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path("books/", include("books.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





