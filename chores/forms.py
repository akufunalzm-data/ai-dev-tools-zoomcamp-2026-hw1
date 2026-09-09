from django import forms

from .models import HouseholdMember


class HouseholdMemberForm(forms.ModelForm):
    class Meta:
        model = HouseholdMember
        fields = ["name"]
