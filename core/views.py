from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
