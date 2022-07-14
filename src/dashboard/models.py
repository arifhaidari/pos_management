from django.db import models
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()


class Payment(models.Model):
     client              = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
     paid_amount         = models.DecimalField(decimal_places=2, max_digits=10)
     amount              = models.DecimalField(decimal_places=2, max_digits=10)
     status              = models.BooleanField(default=False)
     start_contract_date = models.DateField()
     end_contract_date   = models.DateField()
     paid_date           = models.DateField(auto_now=True) # it will be changed everytime we update
     
     def __str__(self):
          return str(self.paid_amount)
     
     def get_remaining(self):
          if self.amount is not None and self.paid_amount is not None:
               return self.amount - self.paid_amount



