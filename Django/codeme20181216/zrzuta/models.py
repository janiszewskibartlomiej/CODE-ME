from django.db import models

class Zrzuta(models.Model):
    user = models.CharField(max_length=200)
    sum = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '{user}({sum}zł)'.format(user=self.user, sum=self.sum)
        # return f'{self.user} ({self.sum}zł)'
