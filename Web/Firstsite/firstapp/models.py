from django.db import models
from django.contrib.auth.models import User

class ProjectList(models.Model):
    objects = models.Manager()
    # Fieleds
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=20, help_text="Enter profect name")
    man_hour = models.FloatField(default=0)

    # pre_work = models.ManyToManyField('self', symmetrical=False)
    pre_work = models.CharField(max_length=20, null=True, blank=True)
    belong_to = models.ForeignKey(to=User, related_name="owner", on_delete=models.CASCADE, null=True, blank=True)

    # Metadata
    class Meta:
        ordering = ["id"]
    
    
    def __str__(self):
        """
        String for representing the ObjectList object (in Admin site etc.)
        """
        return self.project_name

class ProjectDetails(models.Model):
    # Fieleds
    project_list = models.ForeignKey(to=ProjectList, related_name="details", on_delete=models.CASCADE)
    ES = models.FloatField(default=0)
    TF = models.FloatField(default=0)
    LF = models.FloatField(default=0)
    FF = models.FloatField(default=0)
    critical = models.BooleanField(default=False)

    