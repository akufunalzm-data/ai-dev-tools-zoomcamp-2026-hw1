from django import forms

from .models import Chore, HouseholdMember


class HouseholdMemberForm(forms.ModelForm):
    class Meta:
        model = HouseholdMember
        fields = ["name"]


class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = ["title", "assignee", "due_date"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
