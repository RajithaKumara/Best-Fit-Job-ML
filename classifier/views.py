from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseBadRequest

from .estimator import predictor


def index(request):
    return HttpResponse('<h1>Best Fit Job ML</h1><p>Welcome to Best Fit Job ML</p>')


@csrf_exempt
def classification(request):
    if request.method != "POST":
        return HttpResponseForbidden()

    try:
        string = (request.body).decode("utf-8")
        result = predictor.contentClassification(string)
    except Exception:
        return HttpResponseBadRequest()

    return HttpResponse(str(result))
