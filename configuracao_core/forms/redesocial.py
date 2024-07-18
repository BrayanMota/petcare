from core.forms import BaseForm
from configuracao_core.models import RedeSocial


class RedeSocialForm(BaseForm):
    """ Form padrão para o model RedeSocial """
    class Meta:
        exclude = ["deleted", "enabled"]
        model = RedeSocial

