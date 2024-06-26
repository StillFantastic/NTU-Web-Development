from django.db import models
from django.utils import timezone

# Create your models here.
'''
<form id="registrationForm">
      <label for="fname">Last Name:</label><br>
      <input type="text" id="fname" name="fname" required><br>
      <label for="email">Email:</label><br>
      <input type="email" id="email" name="email"><br>
      <p id="invalidEmail" class="hidden">Please enter a valid email</p>
      <label for="bday">Birthday:</label><br>
      <input type="date" id="bday" name="bday"><br>
      <input type="submit" value="Submit">
    </form>
'''
class Registration(models.Model):
    fname = models.CharField(max_length=100)
    email = models.EmailField()
    bday = models.DateField()
    
    def __str__(self):
        return self.fname

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-pub_date',)
    
    def __str__(self):
        return self.title