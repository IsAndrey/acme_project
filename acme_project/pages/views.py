from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from birthday.models import Birthday


class HomePage(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['total_count'] = Birthday.objects.count()
        return context
    

def homepage(request):
    return render(request, 'pages/index.html')
