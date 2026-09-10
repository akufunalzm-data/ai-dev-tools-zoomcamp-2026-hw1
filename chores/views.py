from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import ChoreForm, HouseholdMemberForm
from .models import Chore, HouseholdMember


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


def chore_create(request: HttpRequest) -> HttpResponse:
    """Create a one-time chore and redirect to the active chore list."""
    if request.method == "POST":
        form = ChoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("active_chore_list")
    else:
        form = ChoreForm()

    return render(request, "chores/chore_form.html", {"form": form})


def active_chore_list(request: HttpRequest) -> HttpResponse:
    """Display incomplete chores with their assignees and due dates."""
    chores = (
        Chore.objects.filter(is_complete=False)
        .select_related("assignee")
        .order_by("due_date", "pk")
    )
    return render(request, "chores/active_chore_list.html", {"chores": chores})
