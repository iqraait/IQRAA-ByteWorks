from django import forms
from .models import Form1_assement,Staff
from .constants_data import FORM1_FULL_STRUCTURE, RatingScale

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
    class Meta:
        model = Form1_assement
        fields = []  # dynamic fields only

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for section_key, section_data in FORM1_FULL_STRUCTURE.items():
            for item_key, item_value in section_data['items'].items():
                field_name = f"section_{section_key}_item_{item_key}"

                if section_data['type'] == 'frequency':
                    self.fields[field_name] = forms.ChoiceField(
                        label=item_value,
                        choices=[(str(i), str(i)) for i in range(1, 5)],
                        widget=forms.RadioSelect
                    )

                elif section_data['type'] == 'rating':
                    self.fields[field_name] = forms.ChoiceField(
                        label=item_value[0],  # descriptive label
                        choices=[(str(i+1), option) for i, option in enumerate(item_value)],
                        widget=forms.RadioSelect
                    )

                elif section_data['type'] == 'procedural':
                    self.fields[field_name] = forms.ChoiceField(
                        label=item_value['name'],
                        choices=[(str(i+1), option) for i, option in enumerate(item_value['options'])],
                        widget=forms.RadioSelect
                    )







