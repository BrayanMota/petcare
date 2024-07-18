from core.views.base import BaseTemplateView


# Views Inicial Doenca
class DoencaIndexTemplateView(BaseTemplateView):
    # Views para renderizar a tela inicial Doenca
    template_name = "doenca/index.html"
    context_object_name = "doenca"

    def get_context_data(self, **kwargs):
        context = super(DoencaIndexTemplateView, self).get_context_data(**kwargs)
        return context
