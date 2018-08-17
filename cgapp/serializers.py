from rest_framework import serializers


class DateSerializer(serializers.Serializer):

	date_type = serializers.CharField(max_length=2)
	date = serializers.CharField(max_length=10)
	year = serializers.IntegerField()
	month = serializers.IntegerField()
	day = serializers.IntegerField()

class CGSuccessSerializer(serializers.Serializer):

	message = serializers.CharField()