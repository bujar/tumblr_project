from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status

from api.models import TumblrCache
from api.serializers import TumblrCacheSerializer
from rest_framework.decorators import api_view

import requests, json

# Create your views here.
@api_view(['GET'])
def tumblr_lookup(request, name):
    # find tumblr by pk (tumblr_name)
    if name == "null":
        return JsonResponse({'error':'Enter Valid Tumblr Name','json_response':""},status=200)
    try:
        # Search our cache to see if we found it
        # TODO add check to see how old the cached item is
        # if older than N seconds, invalidate and make API call to Tumblr

        json_response = TumblrCache.objects.get(tumblr_name=name)
        tumblr_serializer = TumblrCacheSerializer(json_response)

        return JsonResponse(tumblr_serializer.data)
    except TumblrCache.DoesNotExist:
        # Not in cache so we need to make an api call
        request_url = 'http://%s.tumblr.com/api/read/json' % (name)

        request = requests.get(request_url)
        json_response = ""
        print("API")
        if str(request.status_code)[0] != "4" and str(request.status_code)[0] == "5":
            response = request.text.replace('var tumblr_api_read = ', '')[:-2]
            json_response = json.loads(response)

        #Store this json response in our cache so we can serve it quickly
        tumblr_data = {"tumblr_name": name, "json_response": json_response}


        tumblr_serializer = TumblrCacheSerializer(data=tumblr_data)
        if tumblr_serializer.is_valid():
            tumblr_serializer.save()
            return JsonResponse(tumblr_serializer.data, status=status.HTTP_201_CREATED)

        # invalid request, return 400
        return JsonResponse(tumblr_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
