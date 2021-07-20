from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FemsTrans
from .serializers import kwhFemsTrans_serializer
import json

class addFemsTransData(APIView):
    def post(self, request):
        # kwhFemsTrans = kwhFemsTrans_serializer(data=request.data)
        json_data = str(request.data)
        d_time = '\'dev_time\': \'' + str(request.data['payload'][0]['dev_time'] + '\',')
        b_time = d_time.replace(',','') + ', \'payload_data\': \"'
        json_data = json_data.replace(d_time,b_time)
        json_data = json_data.replace('\'}','\' \"}')
        json_data = eval(json_data)
        print(type(json_data))
        kwhFemsTrans = kwhFemsTrans_serializer(data=json_data)
        if kwhFemsTrans.is_valid():
            kwhFemsTrans.save()
            return Response(kwhFemsTrans.data, status=status.HTTP_201_CREATED)
        else:
            return Response(kwhFemsTrans.errors, status=status.HTTP_400_BAD_REQUEST)

