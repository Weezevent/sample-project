from rest_framework import serializers

from sample_project.events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'name',
            'organization',
            'type'
        ]
