from .models import Capsfood
from rest_framework import viewsets, permissions
from .serializers import capsfoodSerializer

class CapsfoodViewSet(viewsets.ModelViewSet):
    ## queryset is a list of all Todo objects
    queryset = Capsfood.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing and deserializing queryset and model instances.
    serializer_class = capsfoodSerializer
    # Set permission_classes to allow unrestricted access to the API.
    permission_classes = [permissions.AllowAny]