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
        for i in range(len(request.data['payload'])):
            json_data1 = request.data['payload'][i]
            c = dict({key: value for key, value in json_data1.items() if key == 'dev' or key == 'dev_time'})
            d = str({key: value for key, value in json_data1.items() if key != 'dev' and key != 'dev_time'})
            c['payload_data'] = d
            request.data['payload'][i] = c
        # json_data1 = request.data['payload'][1]
        # print(json_data1)
        # print()
        # c = dict({key: value for key, value in json_data1.items() if key == 'dev' or key == 'dev_time'})
        # d = str({key: value for key, value in json_data1.items() if key != 'dev' and key != 'dev_time'})
        # c['payload_data'] = d
        # request.data['payload'][1]=c
        print(request.data)
        # print(json_data)
        # d_time = '\'dev_time\': \'' + str(request.data['payload'][0]['dev_time'] + '\',')
        # b_time = d_time.replace(',','') + ', \'payload_data\': \"'
        # json_data = json_data.replace(d_time,b_time)
        # json_data = json_data.replace('\'}','\' \"}')
        # json_data = eval(json_data)
        # print(json_data)
        kwhFemsTrans = kwhFemsTrans_serializer(data=request.data)
        if kwhFemsTrans.is_valid():
            kwhFemsTrans.save()
            return Response(kwhFemsTrans.data, status=status.HTTP_201_CREATED)
        else:
            return Response(kwhFemsTrans.errors, status=status.HTTP_400_BAD_REQUEST)

