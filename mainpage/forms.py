from django import forms

class newVote(forms.Form):
	email = forms.EmailField(required=False)
	name = forms.CharField(required=False)
	comment = forms.CharField(required=False)
	choice =forms.CharField(required=True)
	
