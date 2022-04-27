from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Micropost, User
from .serializers import MicropostSerializer

# Create your views here.
class MicropostListView(ListCreateAPIView):
    serializer_class = MicropostSerializer

    def get_queryset(self):
        result = Micropost.objects.filter(
            user__username=self.kwargs["username"]
        )

        return result
    
    def perform_create(self, serializer):
        user = User.objects.get(username=self.kwargs["username"])
        serializer.save(user=user)

class MicropostView(RetrieveUpdateDestroyAPIView):
    serializer_class = MicropostSerializer

    def get_queryset(self):
        result = Micropost.objects.filter(
            user__username=self.kwargs["username"]
        )
        
        return result