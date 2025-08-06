from django import forms
from .models import Form1_assement
from .constants_data import FORM1_FULL_STRUCTURE


class FormAssement1_form(forms.ModelForm):
    class Meta:
        model = Form1_assement
        fields = ['staff', 'evaluator_name', 'evaluation_period']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    
    for section_id,section_data in FORM1_FULL_STRUCTURE.items():
        for item_id,item_data in section_data['items'].items():
            field_name = f"section {section_data} __item__{item_id6}"

    