from rest_framework import generics
from users.serializers import UserRegisterSerializer, UserProfileSerializer
from users.models import User
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateAPIView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
