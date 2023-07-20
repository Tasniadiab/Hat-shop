from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import LocationVO, Hats
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods

class LocationVoEncoder(ModelEncoder):
    model = LocationVO
    properties = ["closet_name" , "import_href",]

class HatsListEncoder(ModelEncoder):
    model =  Hats
    properties = [
        "style_name",

    ]
class HatsDetailEncoder(ModelEncoder):
    model = Hats
    properties = [
        "style_name",
        "fabric",
        "color",
        "picture_url",
        "location"
    ]
    encoders = {
        "location": LocationVoEncoder(),
    }

@require_http_methods(["GET", "POST"])
def api_list_hats(request, location_vo_id= None):
    if request.method == "GET":
        if location_vo_id is not None:
            hats = Hats.objects.filter(location = location_vo_id)
        else:
            hats = Hats.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder= HatsListEncoder,
        )
    else:
        content = json.loads(request.body)
        try:
            location_href = content["location"]
            location = LocationVO.objects.get(id=location_href)
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status = 400,
            )
        hat = Hats.objects.create(**content)
        return JsonResponse(
            hat,
            encoder= HatsDetailEncoder,
            safe = False,
        )
@require_http_methods(["GET", "PUT", "DELETE"])
def api_show_hat(request,id):
    if request.method == "GET":
        hat = Hats.objects.get(id=id)
        return JsonResponse(
            hat,
            encoder=HatsDetailEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        count, _ = Hats.objects.filter(id=id).delete()
        return JsonResponse({"deleted":count >0})
    else:
        content =  json.loads(request.body)
        try:
            location = LocationVO.objects.get(id=content["location"])
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location"},
                status = 400,
            )
        Hats.objects.filter( id = id).update(**content)
        hat = Hats.objects.get(id =id)
        return JsonResponse(
            hat,
            encoder= HatsDetailEncoder,
            safe=False,
        )
