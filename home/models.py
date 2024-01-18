from django.db import models

class Newsletter(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    subscribed = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Newsletter subscribers'
        ordering = ['created']

    def __str__(self):
        return self.name
        
