from django.views.generic import ListView
from pastes.models import Paste


class AllPastesView(ListView):
    model = Paste
    template_name = 'homepage.html'
    ordering = ['-date']
