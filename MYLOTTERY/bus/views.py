from django.shortcuts import render
from bus.models import *
from bus.serializer import *
from knox.auth import TokenAuthentication
from rest_framework import mixins,viewsets
from rest_framework.permissions import IsAuthenticated
# from bus.reserv import reset_boolean_field
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class CartypeViewSet(viewsets.ModelViewSet):
    queryset = Cartype.objects.all()
    serializer_class = CartypeSerializer
    authentication_classes = [TokenAuthentication]

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    authentication_classes = [TokenAuthentication]

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [TokenAuthentication]

class SeatView(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    authentication_classes = [TokenAuthentication]


    
class SeatReserve(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    authentication_classes = [TokenAuthentication]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        bus_id = Bus.objects.get(pk=data.get("bus_id", instance.bus_id))
        instance.on_reserve = data.get("on_reserve", instance.on_reserve)
        instance.saled = False
        serializer = SeatSerializer(instance)
        instance.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class SeateBuy(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    authentication_classes = [TokenAuthentication]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        bus_id = Bus.objects.get(pk=data.get("bus_id", instance.bus_id))
        if instance.on_reserve is False:
            return Response(status=400,data=
                {
                "error": {
                    "message": "Sorry This seat haven't reserve yet",
                }
                }) 
        else:
            instance.saled = True
            serializer = SeatSerializer(instance)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
