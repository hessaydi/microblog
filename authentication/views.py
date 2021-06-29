from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer, LoginSerializer, UserListSerializer
from .models import User
from api.tasks import send_email_task 

class RegistrationAPIView(APIView):
    
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "email": request.data.get('email'),
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        # Sending email to the user
        send_email_task.delay(request.data.get('username'),request.data.get('email') )
        
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        if not user:
            user = {
                "username": request.data.get('username'),
                "password": request.data.get('password')
            }
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserListViewSet(ReadOnlyModelViewSet):

    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = UserListSerializer
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter
        )
    filter_fields = ('username',)
    search_fields = ('username',)
    ordering_fields = ('username', 'email')
    ordering = ('username')
