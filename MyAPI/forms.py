from django import forms
from .models import approvals

"""
class ApprovalForm(forms.ModelForm):
    class Meta:
        model =approvals
        fields = '__all__'
"""

class ApprovalForm(forms.Form):
    Firstname=forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder':'Enter Firstname'}))
    Lastname=forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder':'Enter Lastname'}))
    Dependents=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter deps'}))
    ApplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter income'}))
    CoApplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter coincome'}))
    LoanAmount=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter loan amount'}))
    Loan_Amount_Term=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter loan term'}))
    Credit_History=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter credit history'}))
    Gender=forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')])
    Married=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
    Education=forms.ChoiceField(choices=[('Graduate', 'Graduate'),('Not_Graduate', 'Not_Graduate')])
    Self_Employed=forms.ChoiceField(choices=[('Yes', 'Yes'),('No', 'No')])
    Property_Area=forms.ChoiceField(choices=[('Rural', 'Rural'),('SemiUrban', 'SemiUrban'), ('Urban', 'Urban')])
    