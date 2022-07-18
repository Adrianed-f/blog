from django.shortcuts import render
from django.http import HttpResponse
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Informational message")


def profiles(request):
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    elif request.GET.get("djan") == "go":
        return HttpResponse("Posts Django")
    return HttpResponse("Posts index view")


def profiles_post(request):
    logger.info("function starting")
    for key, value in request.POST.items():
        logger.info(f"Posts with {key} {value}")
        return HttpResponse(f"Posts with {key} {value}")

# Create your views here.
# Create your views here.
