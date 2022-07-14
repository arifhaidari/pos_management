# from django.db import models
# from django.contrib.auth import authenticate, login, get_user_model
# import random
# import os

# User = get_user_model()


# class PosBackup(models.Model):
#     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
#     version_name = models.CharField(max_length=255, null=True, blank=True)
#     backup_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    
#     def __str__(self):
#         return self.version_name
    
    # def delete(self, *args, **kwargs):
    #     self.db_backup.delete()
    #### db_backup is one column in table or the file column which is picture or docuement
    #     super().delete(*args, **kwargs)

#     class Meta:
#         db_table = "employee"

########################
# the version name  would be the (versin+time.time()) object
#  every table table in rest api should has PosBackup foreign key
# and through that key we can recognize that which back up should be insert in pos database



