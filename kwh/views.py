from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FemsTrans
from .serializers import kwhFemsTrans_serializer
import json

class addFemsTransData(APIView):
    def post(self, request):
        kwhFemsTrans = kwhFemsTrans_serializer(data=request.data)
        json_data = request.data
        print(json_data)

        if kwhFemsTrans.is_valid():
            kwhFemsTrans.save()
            return Response(kwhFemsTrans.data, status=status.HTTP_201_CREATED)
        else:
            return Response(kwhFemsTrans.errors, status=status.HTTP_400_BAD_REQUEST)

