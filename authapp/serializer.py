from django.core.serializers.json import Serializer as JSONSerializer


class UserSerializer(JSONSerializer):
    def get_dump_object(self, obj):
        return {
            'id': obj.id,
            'username': obj.username,
            'email': obj.email,
        }
