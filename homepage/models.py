from django.db import models
from django.conf import settings

# Create your models here.


class Article(models.Model):
    """An news article post."""
    headline = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.headline) > 30:
            headline_str = f'{self.headline[:30]}...'
        else:
            headline_str = f'{self.headline}'
        if len(self.content) > 50:
            content_str = f'\n{self.content[:50]}...'
        else:
            content_str = f'\n{self.content}'

        return headline_str + content_str
