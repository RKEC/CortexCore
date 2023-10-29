from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Idea
from .forms import AddIdea
from django.db.models import Q

def index(request):
    return render(request, "index.html")


def delete(request, pk):
    return render(request, "idea_confirm_delete.html", {"id": pk})


class IdeaCreateView(CreateView):
    model = Idea
    form_class = AddIdea
    template_name = 'add-idea.html'
    success_url = reverse_lazy('idea')

    def form_valid(self, form):
        messages.success(self.request, "Idea has been added successfully")
        return super(IdeaCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('idea')

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with your submission.')
        return super().form_invalid(form)


class IdeaDetailView(DetailView):
    model = Idea
    template_name = "idea.html"


class IdeaListView(ListView):
    model = Idea
    template_name = "idea.html"
    context_object_name = 'ideas'
    queryset = Idea.objects.all().order_by("-dateAdded")


class IdeaSearchView(ListView):
    model = Idea
    template_name = "idea.html"
    context_object_name = 'ideas'

    def get_queryset(self):
        search_idea = self.request.GET.get('search', '')
        if search_idea:
            return Idea.objects.filter(Q(title__icontains=search_idea))
        return Idea.objects.all().order_by("-dateAdded")


class IdeaUpdateView(UpdateView):
    model = Idea
    form_class = AddIdea  # Using the form class you've defined
    template_name = 'update-idea.html'  # Specify your update template
    success_url = reverse_lazy('idea')

    def form_valid(self, form):
        messages.success(self.request, "The idea was updated successfully.")
        return super(IdeaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(IdeaUpdateView, self).get_context_data(**kwargs)
        # You can add additional context here if needed
        return context


class IdeaDeleteView(DeleteView):
    model = Idea
    template_name = "idea_confirm_delete.html"
    success_url = reverse_lazy('idea')

    def get_queryset(self):
        return Idea.objects.all()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "The idea was deleted successfully.")
        return super(IdeaDeleteView, self).delete(request, *args, **kwargs)
