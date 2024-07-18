from django.urls import include, path
from rest_framework import routers
from doenca.api.views.doenca import DoencaReadOnlyAPI, DoencaViewAPI

router = routers.DefaultRouter()

# URL para a API Doenca
router.register(r"doenca", DoencaViewAPI, "doenca-api")
router.register(r"doenca_readonly", DoencaReadOnlyAPI, "doenca-readonly-api")


from django.urls import include, path
from rest_framework import routers
from doenca.api.views.diagnostico import DiagnosticoReadOnlyAPI, DiagnosticoViewAPI



# URL para a API Diagnostico
router.register(r"diagnostico", DiagnosticoViewAPI, "diagnostico-api")
router.register(r"diagnostico_readonly", DiagnosticoReadOnlyAPI, "diagnostico-readonly-api")


urlpatterns = router.urls