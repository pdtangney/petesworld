from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic a user is discussing."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) < 50:
            return self.text
        else:
            return f'{self.text[:50]}...'

class Entry(models.Model):
    """A specific entry related to a specified topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) < 50:
            return self.text
        else:
            return f'{self.text[:50]}...'
