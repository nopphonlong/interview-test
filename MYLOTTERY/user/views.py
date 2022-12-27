from django.contrib.auth import authenticate, login
from rest_framework import status,generics, permissions,viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.models import AuthToken
from .serializers import UserSerializer, RefreshTokenSerializer,LoginSerializer
from .models import User
from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from knox.auth import TokenAuthentication
from knox.models import AuthToken

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
        print('error')
    return render(request, 'register.html', {'form': form})

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1],
            # "refresh": AuthToken.objects.create(user, context=self.get_serializer_context(), expires_in=604800)
        })


class RefreshTokenView(GenericAPIView):
    serializer_class = RefreshTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data['refresh_token']
        device_id = serializer.validated_data.get('device_id')
        user = request.user
        token = AuthToken.objects.filter(token=refresh_token).first()

        if token and token.user == user:
            new_token = AuthToken.objects.create(user, device_id)
            return Response({'token': new_token})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

def home_view(request):
    return render(request, 'home.html')



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]