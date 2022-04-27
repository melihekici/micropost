from django.urls import reverse
from .models import Micropost, User
from rest_framework import serializers

class MicropostHyperlink(serializers.HyperlinkedRelatedField):
    view_name = "micropost-detail"

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            "pk": obj.pk,
            "username": obj.user.username,
        }
        result = reverse(view_name, kwargs=url_kwargs, request=request, format=format)

        return result


class MicropostSerializer(serializers.ModelSerializer):
    href = MicropostHyperlink(source="*", read_only=True)
    text = serializers.CharField(max_length=255)
    referenced = serializers.SlugRelatedField(queryset=User.objects.all(), 
                                              slug_field="username",
                                              allow_null=True)
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Micropost
        fields = ["href", "id", "text", "referenced", "timestamp", "user"]


