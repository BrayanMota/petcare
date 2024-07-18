from core.forms import BaseForm
from configuracao_core.models import LogoSistema


class LogoSistemaForm(BaseForm):
    """ Form padrão para o model LogoSistema """
    class Meta:
        exclude = ["deleted", "enabled"]
        model = LogoSistema


