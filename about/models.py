from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Renders the most recent info on the website author 
    and allows user collaboration requests
    Displays an individual instance of :model:`about.About`.
    **Context**
    ``about``
    The most recent instance of :model:`about.About`.
    ``collaboration_form``
    The instance of :form:`about.collaborationForm`.
    **Template:**
    template:`about/about.html`
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"