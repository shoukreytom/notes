from django.test import TestCase
from home.models import Note
from django.contrib.auth.models import User


class NoteTests(TestCase):
    def test_add_note(self):
        pre_count = Note.objects.all()
        author = User(username="testuser", password="demouserpassword123")
        author.save()
        note = Note(title="A demo note", body="demo note for testing", author=author)
        note.save()
        post_count = Note.objects.all()
        self.assertEqual(pre_count+1, post_count)
