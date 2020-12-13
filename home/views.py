from django.shortcuts import render
from django.views.generic import (ListView, DetailView, 
                                    View, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from home.models import Note
from home.forms import AddNoteForm


def home(request):
    return render(request, "home.html")


class NoteList(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/note_list.html'
    ordering = ['-updated', ]
    context_object_name = 'notes'


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes/note_detail.html'
    context_object_name = 'note'


class CreateNote(LoginRequiredMixin, View):
    init_form = AddNoteForm()

    def get(self, request):
        ctx = {'form': self.init_form}
        return render(request, 'notes/add_note.html', ctx)
    
    def post(self, request):
        form = AddNoteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return render(request, 'notes/note_list.html')
        else:
            ctx = {'form': self.init_form}
            return render(request, 'notes/add_note.html', ctx)


class UpdateNote(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'notes/update_note.html'
    fields = ('title', 'body', )


class DeleteNote(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes')
