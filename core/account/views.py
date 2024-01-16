from rest_framework.generics import GenericAPIView
from .serializers import CreateUserSerializer
from rest_framework.response import Response
from rest_framework import status
class RegisterUserView(GenericAPIView):
    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'username' : serializer.validated_data['username'],
            }
            return Response(data,status.HTTP_201_CREATED)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)