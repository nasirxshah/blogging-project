from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class HomeView(APIView):
    def get(self, request):
        return Response({
            'register':reverse('register',request=request),
            'jwt-create':reverse('jwt-create',request=request),
            'jwt-refresh':reverse('jwt-refresh',request=request),
            'blogs':reverse('blogs-list',request=request),
        })