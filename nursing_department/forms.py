from django import forms
from .models import Form1_assement,Staff
from .constants_data import FORM1_FULL_STRUCTURE

class NicuForm(forms.ModelForm):
    class  Meta:
        model = Staff
        fields = ['staff_name','designation','employee_id','location','date_of_join']
        widgets = {
            'date_of_join': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['staff_name'].label = "Name of the Staff"
        self.fields['date_of_join'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']






class NicuFormAssementData(forms.ModelForm):

    RATING_CHOICES = [
        ('1', '1 '),
        ('2', '2 '),
        ('3', '3 '),
        ('4', '4 '),
    ]


    class Meta:
        model = Form1_assement
        fields = []  # dynamic fields only

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for section, items in FORM1_FULL_STRUCTURE.items():
            heading = section
            self.fields[heading] = forms.CharField(
                label=heading,
            )    
            for i in items:
                field_name = i
                self.fields[field_name] = forms.ChoiceField(
                    label=i,
                    choices=self.RATING_CHOICES,
                    widget=forms.RadioSelect,
                    required=True,
                )
                
    def save(self, commit=True):
            """Store all field values in JSON grouped by section."""
            instance = super().save(commit=False)

            data_dict = {}

            for section, items in FORM1_FULL_STRUCTURE.items():
                section_data = {}
                for item in items:
                    section_data[item] = self.cleaned_data.get(item)  # choice/radio value
                data_dict[section] = section_data

            instance.data = data_dict  # JSONField in model("data is model attribute name")

            if commit:
                instance.save()
            return instance