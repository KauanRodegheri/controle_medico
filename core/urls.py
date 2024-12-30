from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drug.views import home_view, DrugListAPIView

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

    # API
    path('api/v1/medicamentos/', DrugListAPIView.as_view(), name='drug_listapiview'),
    path('api/v1/', include('authentication.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
