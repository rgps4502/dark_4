from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import CommoDityModel
from serializers.serializers import CommoDitySerializer
# Create your views here.


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    def commdity_list(self):
        commdity_list = CommoDityModel.objects.all()
        commdity_serializer = CommoDitySerializer(instance=commdity_list,many=True)
        return JSONResponse({'result':commdity_serializer.data})
