from core.forms import BaseForm
from configuracao_core.models import ImagemLogin


class ImagemLoginForm(BaseForm):
    """ Form padrão para o model ImagemLogin """
    class Meta:
        exclude = ["deleted", "enabled"]
        model = ImagemLogin


