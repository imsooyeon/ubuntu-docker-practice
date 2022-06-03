from django.shortcuts import render
from django.http      import JsonResponse
from django.views     import View
from logs.models      import Log

class LogView(View):
    def get(self, request):
        ip_address = request.META['REMOTE_ADDR']

        Log.objects.create(
            ip_address = ip_address
        )

        logs = Log.objects.all()

        infos = [{
            "ip_adress"   : log.ip_address,
            "access_time" : log.access_time
        }for log in logs]
        
        return JsonResponse({'result' : infos}, status=200)