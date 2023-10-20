from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    category.disabled = True

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        """Return a string representation of the model."""
        return self.category


class ClassifiedAd(models.Model):
    """A classified ad in a specified category."""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.headline) > 75:
            return f'{self.headline[:75]}...'
        else: 
            return self.headline

