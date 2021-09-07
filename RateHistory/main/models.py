from django.db import models

# Creating a database model
class Base(models.Model):
    date = models.DateField('Date')
    rate = models.DecimalField('Rate', max_digits=5, decimal_places=2)

    # The name of the base vtable on admin page
    class Meta:
        verbose_name = 'Base'
        verbose_name_plural = 'Base'

    def __str__(self):
        return f'{self.date}-{self.rate}'
