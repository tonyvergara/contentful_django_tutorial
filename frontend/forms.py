from django import forms


class Search_Form(forms.Form):
    search_term = forms.CharField(label='Search Term ',label_suffix="",required=True)
    