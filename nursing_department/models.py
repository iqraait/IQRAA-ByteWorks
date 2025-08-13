from django.db import models
from users.models import BaseModel,Employee
from django.db.models import JSONField  # Django ≥ 3.1
from django.core.validators import MinValueValidator, MaxValueValidator
# from .constants_data import RatingScale


class Staff(BaseModel):
    staff_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    employee_id = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100)
    date_of_join = models.DateField(null=True, blank=True)  # Allows null values

    def __str__(self):
        return self.staff_name


class Form1_assement(BaseModel):

    EVALUATION_PERIODS = [
        ('INITIAL', '<1 Month (Initial)'),
        ('THREE_MONTH', '3rd Month'),
        ('SIX_MONTH', '6th Month'),
        ('TWELVE_MONTH', '12th Month'),
    ]

    evaluation_period = models.CharField(
        max_length=12,
        choices=EVALUATION_PERIODS,
    )
        
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    evaluator_name = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True,blank=True)
    total_score = models.IntegerField(null=True,blank=True)
    percentage = models.FloatField(null=True,blank=True,validators=[MinValueValidator(0), MaxValueValidator(100)])
    data = JSONField(default=dict)
    evaluation_date = models.DateField(auto_now_add=True)




    class Meta:
        ordering = ['-evaluation_date']






