from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    """Display the shared household chores landing page."""
    return HttpResponse("Shared Household Chores")
