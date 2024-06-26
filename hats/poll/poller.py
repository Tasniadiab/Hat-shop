import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hats_project.settings")
django.setup()


from hats_rest.models import LocationVO


def get_locations():
    print("HI")
    response = requests.get("http://wardrobe-api:8000/api/locations/")
    content = json.loads(response.content)
    for location in content["locations"]:
        LocationVO.objects.update_or_create(
            import_href=location["href"],
            defaults={
                "closet_name": location["closet_name"],
            }
        )


def poll():
    while True:
        print('1Hats poller polling for data')
        try:
            get_locations()
            pass
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(5)


if __name__ == "__main__":
    poll()
