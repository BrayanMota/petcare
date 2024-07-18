from core.forms import BaseForm
from configuracao_core.models import ImagemGenerica


class ImagemGenericaForm(BaseForm):
    """ Form padrão para o model ImagemGenerica """
    class Meta:
        exclude = ["deleted", "enabled"]
        model = ImagemGenerica

class ImagemGenericaModalForm(ImagemGenericaForm):...

