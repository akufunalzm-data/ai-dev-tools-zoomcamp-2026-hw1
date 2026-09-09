from django.urls import reverse
from django.test import TestCase

from .forms import HouseholdMemberForm
from .models import HouseholdMember


class HouseholdMemberManagementTests(TestCase):
    def test_member_list_is_public_and_shows_members(self):
        member = HouseholdMember.objects.create(name="Alex")

        response = self.client.get(reverse("member_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, member.name)
        self.assertNotContains(response, "login")

    def test_valid_member_post_persists_and_redirects(self):
        response = self.client.post(
            reverse("member_list"),
            {"name": "  Alex  "},
        )

        self.assertRedirects(response, reverse("member_list"))
        self.assertTrue(HouseholdMember.objects.filter(name="Alex").exists())

    def test_blank_member_name_shows_validation_feedback(self):
        response = self.client.post(reverse("member_list"), {"name": "   "})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertEqual(HouseholdMember.objects.count(), 0)

    def test_member_form_requires_name(self):
        form = HouseholdMemberForm(data={})

        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_members_are_available_for_future_assignment_queries(self):
        first = HouseholdMember.objects.create(name="Alex")
        second = HouseholdMember.objects.create(name="Sam")

        members = list(HouseholdMember.objects.order_by("name", "pk"))

        self.assertEqual(members, [first, second])
