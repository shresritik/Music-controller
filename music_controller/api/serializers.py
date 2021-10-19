from rest_framework import serializers
from .models import Rooms

# Creating json of the Room model for backend api

# get request


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')

# post request


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('guest_can_pause', 'votes_to_skip')


class UpdateRoomSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])

    class Meta:
        model = Rooms
        fields = ('guest_can_pause', 'votes_to_skip', 'code')
