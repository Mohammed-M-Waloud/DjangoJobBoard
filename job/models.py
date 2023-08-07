from django.db import models

JOB_TYPE_CHOICES = [
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
]

def upload_img(instance, filename):
    image_name, extintion = filename.split(".")
    return f"jobs/{instance.id}.{extintion}"



class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE_CHOICES)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("category",on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_img)
    # location

    
    def __str__ (self):
        return self.title
    

class category(models.Model):
    name = models.CharField(max_length=25)

    def __str__ (self):
        return self.name