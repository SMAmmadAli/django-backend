from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

# Single Student Details
def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serializer =  StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
    # return JsonResponse(serializer.data, safe=True)


# Query set All Student Data

def all_student_detail(request):
    stu = Student.objects.all()
    serializer =  StudentSerializer(stu, many=True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe=False)