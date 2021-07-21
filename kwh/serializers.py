from rest_framework import serializers
from .models import FemsTrans,FemsPayload


class kwhFemsPayload(serializers.ModelSerializer):
    # dev = serializers.CharField(required=True)
    # dev_time = serializers.CharField(required=True)
    class Meta:
        model = FemsPayload
        fields = ('dev_id','dev_time','payload_data')

class kwhFemsTrans(serializers.ModelSerializer):

    # payload = kwhFemsPayload(many=True)
    # payload = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = FemsTrans
        fields = ('transaction_id', 'site_id', 'eng_type', 'version')