from core.forms import BaseForm
from doenca.models import Diagnostico


class DiagnosticoForm(BaseForm):
    """ Form padrão para o model Diagnostico """
    class Meta:
        exclude = ["deleted", "enabled"]
        model = Diagnostico


