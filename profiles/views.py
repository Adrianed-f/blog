from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import logging


logger = logging.getLogger(__name__)

logger.info("Informational message")

if int(settings.SOME_NUMBER) % 2 == 0:
    logger.info(f"RESULT:   {settings.FIRST_RESULT}")
else:
    logger.info(f"RESULT:   {settings.SECOND_RESULT}")


def profiles(request):
    logger.info(settings.ENV)
    if request.GET.get("key") == "test":
        return HttpResponse("Posts with test key")
    elif request.GET.get("djan") == "go":
        return HttpResponse("Posts Django")
    return HttpResponse("Posts index view")


def profiles_post(request):
    logger.info(settings.ENV)
    logger.info("function starting")
    for key, value in request.POST.items():
        logger.info(f"Posts with {key} {value}")
        return HttpResponse(f"Posts with {key} {value}")

# Create your views here.
# Create your views here.
