from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self , request ,format=None):

        """Returns a List of API view Features"""
        an_apiview = [
            'Uses HTTP methods as Function (get, post, patch, put, delete)',
            'Is similar to Traditional Django View',
            'Gives you the most control over your application Logic',
            'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
