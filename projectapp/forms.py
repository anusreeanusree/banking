from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    dob = forms.DateField(label='DOB')
    age = forms.IntegerField(label='Age')
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    district = forms.ChoiceField(label='District', choices=[('district1', 'Thiruvananthapuram'), ('district2', 'Kollam'),('district3', 'Pathanamtitta'),('district4', 'Alapuzha'),('district5', 'Kottayam')]) # Choices will be dynamically populated
    # branch = forms.ChoiceField(label='Branch', choices=[])  # Choices will be dynamically populated
    account_type = forms.ChoiceField(label='Account Type', choices=[('savings', 'Savings Account'), ('current', 'Current Account')])
    materials_provide = forms.MultipleChoiceField(label='Materials Provide', choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')])

#     def __init__(self, *args, **kwargs):
#         super(MyForm, self).__init__(*args, **kwargs)
#         self.fields['district'].choices = [('thiruvananthapuram', 'Thiruvananthapuram'), ('kolam', 'Kollam'),('pathanamtitta', 'Pathanamtitta'),('alapuzha', 'Alapuzha'),('kottayam', 'Kottayam')]  # Populate initial choices
#
# class DistrictForm(forms.Form):
#     district = forms.ChoiceField(label='District', choices=[('thiruvananthapuram', 'Thiruvananthapuram'), ('kolam', 'Kollam'),('pathanamtitta', 'Pathanamtitta'),('alapuzha', 'Alapuzha'),('kottayam', 'Kottayam')])


