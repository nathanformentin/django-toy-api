from django.contrib import admin
from django.urls import path, include
from escola.views import alunos_view_set
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos',alunos_view_set)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
