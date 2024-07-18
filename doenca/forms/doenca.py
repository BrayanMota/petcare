from core.forms import BaseForm
from doenca.models import Doenca


class DoencaForm(BaseForm):
    """ Form padrão para o model Doenca """
    class Meta:
        exclude = ["deleted", "enabled"]
        model = Doenca

class DoencaModalForm(DoencaForm):...

