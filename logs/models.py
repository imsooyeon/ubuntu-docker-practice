from django.db import models

class Log(models.Model):
    ip_address  = models.CharField(max_length=50, blank=True)
    access_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "logs"