from rest_framework import serializers
from home.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'body', )
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['created'] = instance.created
        data['updated'] = instance.updated
        return data