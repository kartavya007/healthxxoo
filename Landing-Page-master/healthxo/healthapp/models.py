from django.db import models

# Create your models here.
class track(models.Model):
    i_d = models.CharField(max_length=255 , primary_key=True)
    pro = models.IntegerField(null=False)
    carbs = models.IntegerField(null=False)
    water = models.IntegerField(null=False)
    fats = models.IntegerField(null=False)
    def __str__(self) -> str:
        return str(self.i_d)
class login(models.Model):
    i_d = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255 , unique=True)
    password = models.CharField(max_length=255)
    def __str__(self) -> str:
        return str(self.i_d) + " " + str(self.user_name)
class plan(models.Model):
     i_d = models.CharField(max_length=255 , primary_key=True)
     plan_no = models.IntegerField(null=False)
     current_w = models.IntegerField(null=False)
     target_w = models.IntegerField(null=False)
     height = models.IntegerField(null=False)
     start = models.DateField(auto_now_add=True)
     end = models.DateField(null=True)
     def __str__(self) -> str:
         return str(self.i_d)
class diet(models.Model):
     i_d = models.CharField(max_length=255 , primary_key=True)
     pro = models.IntegerField(null=False)
     carbs = models.IntegerField(null=False)
     fat = models.IntegerField(null=False)
     water = models.IntegerField(null=False)
     def __str__(self) -> str:
         return str(self.i_d)