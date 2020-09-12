import json
from django.http import HttpResponse
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from accountaboddiesapi.models import Group

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        url = serializers.HyperlinkedIdentityField(
            view_name='group',
            lookup_field='id'
        )
        fields = ('title', 'created_at', 'created_by', 'size', 'population')
        depth = 1

class Groups(ViewSet):

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized User instance
        """

        user = User.objects.create_user(
            title=request.data["title"],
            created_at=request.data["created_at"],
            created_by=request.data["created_by"],
            size=request.data["size"],
            population=request.data["population"]
        )

        account = Account.objects.create(
            user=user
        )

        token = Token.objects.create(user=user)

        data = json.dumps({"token": token.key})
        return HttpResponse(data, content_type='application/json')

    def retrieve(self, request, pk=None):
        """Handle GET requests

        Returns:
            Response -- JSON serialized park area instance
        """
        try:
            account = Account.objects.get(pk=pk)
            serializer = AccountSerializer(
                account, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests

        Returns:
            Response -- Empty body with 204 status code
        """

        account = Account.objects.get(pk=pk)

        user = User.objects.get(pk=account.user.id)
        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            user = User.objects.get(pk=pk)
            user.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Account.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):

        if request.user.id:
            account = Account.objects.filter(user=request.user.id)
        else:
            account = Account.objects.all()
        serializer = AccountSerializer(account, many=True, context={'request': request})
        return Response(serializer.data)