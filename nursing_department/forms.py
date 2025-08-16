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

    # evaluation_period = forms.ChoiceField(label="Select Evaluation Period",choices=Form1_assement.EVALUATION_PERIODS,required=True)



    class Meta:
        model = Form1_assement
        fields = ['evaluation_period']  # dynamic fields only


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for section, items in FORM1_FULL_STRUCTURE.items():
            heading = section
            self.fields[heading] = forms.CharField(
                label=heading,
                widget=forms.HiddenInput(),  # hides the input box
                required=False
            

            )    
            for i in items:
                field_name = i
                self.fields[field_name] = forms.ChoiceField(
                    label=i,
                    choices=self.RATING_CHOICES,
                    widget=forms.RadioSelect,
                    required=True,
                )



    def save(self, commit=True, staff=None, evaluator=None):
        """Store all field values in JSON grouped by section and set staff/evaluator."""
        instance = super().save(commit=False)

        # Save JSON data
        data_dict = {}
        total_score = 0
        total_items = 0

        for section, items in FORM1_FULL_STRUCTURE.items():
            section_data = {}
            for item in items:
                score_str = self.cleaned_data.get(item)
                score = int(score_str) if score_str else 0
                section_data[item] = score

                # accumulate totals
                total_score += score
                total_items += 1
                data_dict_item = self.cleaned_data.get(item)

                section_data[item] = data_dict_item
            data_dict[section] = section_data

        instance.data = data_dict  # JSONField in model
        instance.total_score = total_score
        instance.percentage = round((total_score / (total_items * 4)) * 100, 2) if total_items else 0
        instance.staff = staff
        instance.evaluator_name = evaluator

        if commit:
            instance.save()
        return instance