from core.forms import BaseForm
from doenca.models import Apresentacao


class ApresentacaoForm(BaseForm):
    """ Form padrão para o model Apresentacao """
    class Meta:
        exclude = ["deleted", "enabled"]
        model = Apresentacao


