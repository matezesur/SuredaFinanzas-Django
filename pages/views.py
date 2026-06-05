from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PageForm, PageSearchForm
from .models import Page


class PageListView(ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = PageSearchForm(self.request.GET)
        if self.form.is_valid():
            q = self.form.cleaned_data.get('q')
            if q:
                queryset = queryset.filter(
                    Q(titulo__icontains=q) |
                    Q(subtitulo__icontains=q) |
                    Q(categoria__icontains=q)
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = getattr(self, 'form', PageSearchForm())
        context['busqueda'] = self.request.GET.get('q', '')
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'La página fue creada correctamente.')
        return super().form_valid(form)


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/page_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'La página fue actualizada correctamente.')
        return super().form_valid(form)


class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        messages.success(self.request, 'La página fue eliminada correctamente.')
        return super().form_valid(form)
