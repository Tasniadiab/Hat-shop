from django.shortcuts import render
from common.json import ModelEncoder
from .models import BinVO, Shoe
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json


class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = [
        'closet_name',
        'bin_number',
        'bin_size',
        'import_href',
    ]


class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "Manufacturer",
        "model_name",
        "color",
        "picture_url",
        "bin",
    ]
    encoders = {
        "bin": BinVOEncoder()
    }


class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "Manufacturer",
        "model_name",
        "color",
        "picture_url",
        "bin",
        "id",
    ]

    encoders = {
        'bin': BinVOEncoder()
    }


@require_http_methods({"GET", "POST"})
def api_list_shoes(requests, bin_vo_id=None):
    if requests.method == "GET":
        if bin_vo_id is not None:
            shoe = Shoe.objects.filter(bin=bin_vo_id)
        else:
            shoe = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoe},
            encoder=ShoeListEncoder,
        )
    else:
        content = json.loads(requests.body)
        try:
            import_href = f'/api/bins/{content["bin"]}/'
            bin = BinVO.objects.get(import_href=import_href)
            content["bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400,
            )
        shoes = Shoe.objects.create(**content)
        return JsonResponse(
            shoes,
            encoder=ShoeDetailEncoder,
            safe=False,
        )


@require_http_methods(["GET", "DELETE", "PUT"])
def api_shoe_detail(request, id):
    if request.method == "GET":
        try:
            shoe = Shoe.objects.get(id=id)
            return JsonResponse(
                shoe,
                encoder=ShoeDetailEncoder,
                safe=False,
            )
        except Shoe.DoesNotExist:
            return JsonResponse(
                {"message": "no id exists"},
                status=400,
            )

    elif request.method == "DELETE":
        count, _ = Shoe.objects.filter(id=id).delete()
        return JsonResponse({"Shoe Deleted": count > 0})
    else:
        content = json.loads(request.body)
        Shoe.objects.filter(id=id).update(**content)
        shoe = Shoe.objects.get(id=id)
        return JsonResponse(
            shoe,
            encoder=ShoeDetailEncoder,
            safe=False,
        )
