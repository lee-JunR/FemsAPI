from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import kwhFemsPayload, kwhFemsTrans



class addFemsTransData(APIView):
    def post(self, request):
        # post로 들어오는 json의 형식 맞추기
        for i in range(len(request.data['payload'])):
            json_data1 = request.data['payload'][i]
            c = dict({key: value for key, value in json_data1.items() if key == 'dev_id' or key == 'dev_time'})
            d = str({key: value for key, value in json_data1.items() if key != 'dev_id' and key != 'dev_time'})
            c['payload_data'] = d
            request.data['payload'][i] = c
        json_data1 = dict({key: value for key, value in request.data.items() if key == 'transaction_id' or key == 'site_id' or key == 'eng_type'or key == 'version'})
        json_data2 = dict({key: value for key, value in request.data['payload'][0].items() if key == 'dev_id' or key == 'dev_time' or key == 'payload_data'})
        print(json_data2)
        kwhFemsTrans_serializer = kwhFemsTrans(data=json_data1)
        kwhFemsPayload_serializer = kwhFemsPayload(data=json_data2)
        if kwhFemsTrans_serializer.is_valid() and kwhFemsPayload_serializer.is_valid():
            kwhFemsTrans_serializer.save()
            kwhFemsPayload_serializer.save()
            return Response(kwhFemsTrans_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(kwhFemsTrans_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

