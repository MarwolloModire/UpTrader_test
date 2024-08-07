from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['content'] = 'Вы на главной странице!'
        return context


class PageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['content'] = f'Именной URL__{kwargs["url"]}'
        return context
