from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import HouseholdMemberForm
from .models import HouseholdMember


def member_list(request: HttpRequest) -> HttpResponse:
    """Display household members and handle adding a new member."""
    if request.method == "POST":
        form = HouseholdMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("member_list")
    else:
        form = HouseholdMemberForm()

    members = HouseholdMember.objects.order_by("name", "pk")
    return render(
        request,
        "chores/member_list.html",
        {"form": form, "members": members},
    )
