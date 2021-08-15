from rest_framework import serializers
from rest_api.models import EmoloyeeInfo


class EmoloyeeInfoSerializer(serializers.Serializer):
	emp_id = serializers.IntegerField()
	emp_firstname = serializers.CharField(max_length=255)
	emp_lastname = serializers.CharField(max_length=255)
	emp_salary = serializers.FloatField()

	def create(self, validated_data):
		return EmoloyeeInfo.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.emp_id = validated_data.get("emp_id", instance.emp_id)
		instance.emp_firstname = validated_data.get("emp_firstname", instance.emp_firstname)
		instance.emp_lastname = validated_data.get("emp_lastname", instance.emp_lastname)
		instance.emp_salary = validated_data.get("emp_salary", instance.emp_salary)
		instance.save()
		return instance