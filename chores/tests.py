from datetime import date

from django.urls import reverse
from django.test import TestCase
from django.utils.formats import date_format

from .forms import ChoreForm, HouseholdMemberForm
from .models import Chore, HouseholdMember


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


class ChoreCreationAndActiveListTests(TestCase):
    def setUp(self):
        self.member = HouseholdMember.objects.create(name="Alex")

    def test_chore_form_offers_existing_members(self):
        form = ChoreForm()

        self.assertIn(self.member, form.fields["assignee"].queryset)

    def test_valid_chore_post_persists_as_incomplete_and_redirects(self):
        response = self.client.post(
            reverse("chore_create"),
            {
                "title": "Wash dishes",
                "assignee": self.member.pk,
                "due_date": "2026-01-01",
            },
        )

        self.assertRedirects(response, reverse("active_chore_list"))
        chore = Chore.objects.get()
        self.assertEqual(chore.title, "Wash dishes")
        self.assertEqual(chore.assignee, self.member)
        self.assertEqual(str(chore.due_date), "2026-01-01")
        self.assertFalse(chore.is_complete)

    def test_missing_required_chore_fields_show_feedback(self):
        response = self.client.post(reverse("chore_create"), {})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertEqual(Chore.objects.count(), 0)

    def test_past_due_date_is_allowed(self):
        form = ChoreForm(
            data={
                "title": "Past due chore",
                "assignee": self.member.pk,
                "due_date": "2020-01-01",
            }
        )

        self.assertTrue(form.is_valid(), form.errors)

    def test_active_list_shows_only_incomplete_chores(self):
        active = Chore.objects.create(
            title="Active chore",
            assignee=self.member,
            due_date=date(2026, 1, 1),
        )
        Chore.objects.create(
            title="Completed chore",
            assignee=self.member,
            due_date=date(2026, 1, 2),
            is_complete=True,
        )

        response = self.client.get(reverse("active_chore_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, active.title)
        self.assertContains(response, active.assignee.name)
        self.assertContains(response, date_format(active.due_date, "DATE_FORMAT"))
        self.assertNotContains(response, "Completed chore")
        self.assertNotContains(response, "Mark complete")
