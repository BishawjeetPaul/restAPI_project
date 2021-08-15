from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_api.serializers import EmoloyeeInfoSerializer
from django.views.generic import View
from rest_framework.renderers import JSONRenderer
from rest_api.models import EmoloyeeInfo
import io


# class EmployeeOperation(View):
# 	def post(self, request):
# 		byte_data = request.body
# 		stm = io.BytesIO(byte_data)
# 		dict_data = JSONParser().parse(stm)
# 		ps = EmoloyeeInfoSerializer(data=dict_data)
# 		if ps.is_valid():
# 			ps.save()
# 			message = {"Success": "Product is Saved"}
# 		else:
# 			message = {"Errors": ps.errors}
# 		json_data = JSONRenderer().render(message)
# 		return HttpResponse(json_data, content_type="application/json")


# 	def get(self, request):
# 		byte_data = request.body
# 		stm = io.BytesIO(byte_data)
# 		dict_data = JSONParser().parse(stm)
# 		employee_id = dict_data.get('emp_id', None)
# 		if employee_id:
# 			try:
# 				qs = EmoloyeeInfo.objects.get(emp_id=employee_id)
# 				ps = EmoloyeeInfoSerializer(qs)
# 				json_data = JSONRenderer().render(ps.data)
# 			except EmoloyeeInfo.DoesNotExist:
# 				message = {"Errors": "Invalid Product Number"}
# 				json_data = JSONRenderer().render(message)
# 		else:
# 			qs = EmoloyeeInfo.objects.all()
# 			ps = EmoloyeeInfoSerializer(qs, many=True)
# 			json_data = JSONRenderer().render(ps.data)
# 		return HttpResponse(json_data, content_type="application/json")



# 	def put(self, request):
# 		byte_data = request.body
# 		stm = io.BytesIO(byte_data)
# 		dict_data = JSONParser().parse(stm)
# 		employee_id = dict_data.get("emp_id", None)
# 		if employee_id:
# 			try:
# 				res = EmoloyeeInfo.objects.get(emp_id=employee_id)
# 				ps = EmoloyeeInfoSerializer(res, dict_data, partial=True)
# 				if ps.is_valid():
# 					ps.save()
# 					message = {"message":"Employee is Updated"}
# 				else:
# 					message = {"error": ps.errors}
# 			except EmoloyeeInfo.DoesNotExist:
# 				message = {"Error": "Invalid Employee ID"}
# 		else:
# 			message = {"error": "Please provide Employee ID"}
# 		json_data = JSONRenderer().render(message)
# 		return HttpResponse(json_data, content_type="application/json")


# 	def delete(self, request):
# 		byte_data = request.body
# 		stm = io.BytesIO(byte_data)
# 		dict_data = JSONParser().parse(stm)
# 		employee_id = dict_data.get("emp_id", None)
# 		try:
# 			EmoloyeeInfo.objects.get(emp_id=employee_id).delete()
# 			message = {"message": "Employee is Deleted"}
# 		except EmoloyeeInfo.DoesNotExist:
# 			message = {"message:": "Incalid Employee ID"}
# 		json_data = JSONRenderer().render(message)
# 		return HttpResponse(json_data, content_type="application/json")


class ReadAllEmployee(View):
	def get(self, request):
		qs = EmoloyeeInfo.objects.all()
		ps = EmoloyeeInfoSerializer(qs, many=True)
		json_data = JSONRenderer().render(ps.data)
		return HttpResponse(json_data, content_type="application/json")


class ReadOneEmployee(View):
	def get(self, request, employee):
		try:
			qs = EmoloyeeInfo.objects.get(emp_id=employee)
			ps = EmoloyeeInfoSerializer(qs)
			json_data = JSONRenderer().render(ps.data)
		except EmoloyeeInfo.DoesNotExist:
			message = {"Errors": "Invalid Product Number"}
			json_data = JSONRenderer().render(message)
		return HttpResponse(json_data, content_type="application/json")


class UpdateEmployee(View):
	def put(self, request, employee):
		byte_data = request.body
		stm = io.BytesIO(byte_data)
		dict_data = JSONParser().parse(stm)
		try:
			res = EmoloyeeInfo.objects.get(emp_id=employee)
			ps = EmoloyeeInfoSerializer(res, dict_data, partial=True)
			if ps.is_valid():
				ps.save()
				message = {"message":"Employee is Updated"}
			else:
				message = {"error": ps.errors}
		except EmoloyeeInfo.DoesNotExist:
			message = {"Error": "Invalid Employee ID"}
		json_data = JSONRenderer().render(message)
		return HttpResponse(json_data, content_type="application/json")


class DeleteEmployee(View):
	def delete(self, request, employee):
		try:
			qs = EmoloyeeInfo.objects.get(emp_id=employee).delete()
			message = {"message": "Employee is Deleted"}
		except EmoloyeeInfo.DoesNotExist:
			message = {"message": "Invalid Employee ID"}
		json_data = JSONRenderer().render(message)
		return HttpResponse(json_data, content_type="application/json")