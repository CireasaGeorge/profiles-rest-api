from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,formt=None):
        """returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        'Is similar to a traditional django view',
        'Gives you the most control over your application logic',
        'Is mapped manyally to URLs'
        ]

        return Response({'message':"Hello",
        'an_apiview':an_apiview}
        )
