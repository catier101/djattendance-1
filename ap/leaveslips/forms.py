from django import forms

from .models import IndividualSlip, GroupSlip
from accounts.models import Trainee

#TODO support events

class IndividualSlipForm(forms.ModelForm):
    class Meta:
        model = IndividualSlip
        fields = ['type', 'description', 'comments', 'texted', 'informed', 'rolls']


class GroupSlipForm(forms.ModelForm):

    trainees = forms.ModelMultipleChoiceField(queryset=Trainee.objects.select_related().filter(is_active=True))

    class Meta:
        model = GroupSlip
        fields = ['type', 'trainees', 'description', 'comments', 'texted', 'informed', 'start', 'end']