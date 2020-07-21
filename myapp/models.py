from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=True)

    # function to return what was searched in the field instead of the memory location where it was stored
    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'