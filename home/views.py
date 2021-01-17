from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'home/notes/note_detail.html'
    context_object_name = 'note'


class CreateNote(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'home/notes/add_note.html')
    
    def post(self, request):
        title = request.POST.get('title', None)
        body = request.POST.get('body', None)
        if not (title is None or body is None):
            note = Note(title=title, body=body)
            note.author = request.user
            note.save()
            return redirect('notes')
        else:
            return render(request, 'home/notes/add_note.html')


class UpdateNote(LoginRequiredMixin, UpdateView):
    model = Note
    template_name = 'home/notes/update_note.html'
    fields = ['title', 'body', ]
    
    def get_success_url(self):
        return reverse('note-detail', kwargs={
            'slug': self.object.slug,
        })


class DeleteNote(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'home/notes/note_confirm_delete.html'
    context_object_name = 'note'
    success_url = reverse_lazy('notes')


def download_note(request, slug):
    note = get_object_or_404(Note, slug=slug)
    file_name = note.slug + ".txt"
    note_file = open(file_name, "w+")
    note_file.write(note.body)
    note_file.close()
    note_file = open(file_name)
    response = HttpResponse(note_file.read(), content_type="application/text")
    response['Content-Disposition'] = 'inline; filename=' + file_name
    return response
