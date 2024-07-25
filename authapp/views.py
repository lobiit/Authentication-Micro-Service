from django.http import JsonResponse
from django.views import View
from django.utils.decorators import classonlymethod
from asgiref.sync import sync_to_async
from .models import CustomUser
from .serializer import UserSerializer


class UserListCreateView(View):
    @classonlymethod
    async def get(cls, request):
        users = await sync_to_async(CustomUser.objects.all)()
        serialized_data = UserSerializer().serialize(users)
        return JsonResponse(serialized_data, safe=False)

    @classonlymethod
    async def post(cls, request):
        data = request.POST
        user = await sync_to_async(CustomUser.objects.create)(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        serialized_data = UserSerializer().serialize([user])
        return JsonResponse(serialized_data, safe=False)
