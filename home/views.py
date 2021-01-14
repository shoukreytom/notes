from django.shortcuts import render
from django.views.generic import (ListView, DetailView, 
                                    View, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from home.models import Note
from home.forms import AddNoteForm


def home(request):
    return render(request, "home/index.html")


class NoteList(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'home/notes/note_list.html'
    ordering = ['-updated', ]
    context_object_name = 'notes'


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'home/notes/note_detail.html'
    context_object_name = 'note'


class CreateNote(LoginRequiredMixin, View):
    init_form = AddNoteForm()

    def get(self, request):
        ctx = {'form': self.init_form}
        return render(request, 'home/notes/add_note.html', ctx)
    
    def post(self, request):
        form = AddNoteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            notes = Note.objects.all()
            return render(request, 'home/notes/note_list.html', {'notes': notes})
        else:
            ctx = {'form': self.init_form}
            return render(request, 'home/notes/add_note.html', ctx)


class UpdateNote(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'home/notes/update_note.html'
    fields = ('title', 'body', )
    
    def get_success_url(self):
        return reverse('note-detail', kwargs={
            'slug': self.object.slug,
        })


class DeleteNote(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'home/notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes')
