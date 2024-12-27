from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drug.views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home_view'),

    # DRUG
    path('remedios/', include('drug.urls')),

    # ACCOUNTS
    path('', include('accounts.urls')),

    # EXAMS
    path('', include('exams.urls')),

    # SCHEDULES
    path('', include('schedules.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
