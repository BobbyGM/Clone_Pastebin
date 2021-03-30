from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.db.models import Q
from .models import Paste
from .forms import PasteForm


class CreatePasteView(LoginRequiredMixin, CreateView):
    model = Paste
    form_class = PasteForm
    template_name = 'pastes/create_paste.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DisplayPasteView(DetailView):
    model = Paste
    template_name = 'pastes/display_paste.html'


class UpdatePasteView(UpdateView):
    model = Paste
    form_class = PasteForm
    template_name = 'pastes/update_paste.html'
    success_url = '/'


class DeletePasteView(DeleteView):
    model = Paste
    template_name = 'pastes/delete_paste.html'
    success_url = '/'


class SearchResultsView(ListView):
    model = Paste
    template_name = 'pastes/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Paste.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-date')
        return object_list
