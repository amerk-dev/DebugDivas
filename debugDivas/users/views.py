from rest_framework import viewsets, generics, permissions, response, status
from .models import CustomUser, SportType, Location
from .serializers import UserSerializer, SportTypeSerializer, LocationSerializer, RegisterSerializer

class SportTypeViewSet(viewsets.ModelViewSet):
    queryset = SportType.objects.all()
    serializer_class = SportTypeSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Вывести далее необходимую информацию или токен
        headers = self.get_success_headers(serializer.data)
        return response.Response({
            "user": serializer.data,
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED, headers=headers)
