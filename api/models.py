from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    item_id = models.CharField(max_length=60)
    name = models.TextField(null=True, blank=True)
    url = models.URLField(blank=True)
    complete = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.item_id, self.name)

    def get_absolute_url(self):
        return reverse('delete', kwargs={'pk': self.pk})
   

