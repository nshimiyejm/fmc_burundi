from django.db import models

# Create your models here.
class Profile_Role(models.Model): 
    # Holds the image of the user 
    image = models.ImageField(upload_to='images/') # uploads the this image to a folder named images 

    # Hold the first name of the individual 
    first_name = models.CharField(max_length=250)

    # Hold the last name of the individual 
    last_name = models.CharField(max_length=250)  

    # Holds the title of the individual 
    title = models.CharField(max_length=50)

    # Holds the description of the individual 
    description = models.TextField()

    def __str__(self): 
        return self.first_name + ' ' + self.last_name  