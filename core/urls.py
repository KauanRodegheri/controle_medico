from django.contrib import admin
from django.urls import path, include
from drug.views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home_view'),

    # DRUG
    path('remedios/', include('drug.urls')),
]
