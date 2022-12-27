from rest_framework import serializers
from bus.models import *
from django.contrib.auth import authenticate
from rest_framework import serializers

class CartypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartype
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class BusScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('schedule')

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):

    schedule = serializers.Serializer(read_only=True)

    def get_schedule(self,obj):
        query = Bus.objects.get(pk=obj.Bus.id)
        serializer = BusScheduleSerializer(query)
        return serializer.data

    class Meta:
        model = Ticket
        fields = ('id','bus_id','seat_id','schedule')