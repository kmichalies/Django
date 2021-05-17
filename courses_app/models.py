from django.db import models


class CourseManager(models.Manager):
    def course_validation(self, postData):
        errors= {}
        if len(postData['name']) < 6:
            errors['name'] = "* Sorry - Title needs to be at least 6 characters *"
        
        if len(postData['description']) < 16:
            errors['desc'] = "* Sorry - The description needs to be at least 16 characters *"

        return errors

class Course(models.Model):
    name = models.CharField(max_length=15, default='name')
    desc = models.TextField(default = '')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    # describe = desc from Description

#class DescriptionManager(models.Manager):
    #def description_validation(self, postData):
        #errors= {}
        #if len(postData['description']) < 16:
           # errors['desc'] = "* Sorry - The descirption needs to be at least 16 characters *"
        #return errors

#class Description(models.Model):
    #desc = models.TextField()
    #description = models.OneToOneField(Course, related_name='describe', #on_delete=models.CASCADE)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    ##objects = DescriptionManager()
