from django.db import models



class NursingModelListing(models.Model):

    APPROVED_FORM_CHOICES =  [('pending','Pending'),('completed','Completed')]


    iqraa_id = models.IntegerField(max_length=6,unique=True,blank=False,null=False,
                                   help_text="6-digit unique identification number")
    
    staff_name = models.CharField(max_length=100)
    nursing_station = models.CharField(max_length=100)
    statues = models.CharField(max_length=15,choices=APPROVED_FORM_CHOICES,default='pending')
    form_pdf = models.FileField(upload_to='pdfs')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.iqraa_id)