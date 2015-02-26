from django.forms import widgets
from rest_framework import serializers
from temp.models import TempInput

class TempInputSerializer(serializers.Serializer):
    snsr_create_date = serializers.DateTimeField()
    snsr_name = serializers.CharField(required=False, allow_blank=False, max_length=50)
 #   cur_temp = serializers.IntegerField(read_only=True)
    cur_temp = serializers.DecimalField(max_digits=5, decimal_places=2)
    temp_units = serializers.CharField(required=False, allow_blank=False, max_length=1)
    temp_updated_date = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `TempInput` instance, given the validated data. What??
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data. What??
        """
        instance.snsr_create_date = validated_data.get('snsr_create_date', instance.snsr_create_date)
        instance.snsr_name = validated_data.get('snsr_name', instance.snsr_name)
        instance.cur_temp = validated_data.get('cur_temp', instance.cur_temp)
        instance.temp_units = validated_data.get('temp_units', instance.temp_units)
        instance.temp_updated_date = validated_data.get('temp_updated_date', instance.temp_updated_date)
        instance.save()
        return instance
