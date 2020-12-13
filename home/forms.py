from django import forms
from home.models import Note


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body')