# Shared Household Chores Tool Plan

## Requirements

- Support one shared household with a small group of members.
- Use one shared interface without separate user accounts or authentication.
- Support one-time chores only.
- Require every chore to have a title, assignee, and due date.
- Allow any household member to mark any chore complete.
- Keep completed chores visible in a separate completed section.
- Do not provide an audit trail.

## Core Features

1. **Household member list** — Add and view members who can be assigned chores.
2. **Chore creation and assignment** — Create a one-time chore with a title, assignee, and due date.
3. **Active chore list** — Display outstanding chores with their assigned member and due date.
4. **Completion history** — Mark a chore complete and display it in a completed section.

## Acceptance Criteria

1. A user can add a household member, and that member becomes available as a chore assignee.
2. A user can create a chore only when its title, assignee, and due date are provided.
3. A newly created chore appears in the active-chore section with its title, assignee, and due date.
4. Any person using the shared interface can mark an active chore complete.
5. Completing a chore removes it from active chores and shows it in the completed section.
6. The tool does not require sign-in or distinguish users.
7. The tool provides no recurrence scheduling and no audit/activity log.

## Exclusions

- Multiple households.
- User accounts, sign-in, and authentication.
- Recurring chores.
- Completion or activity audit history.

## Assumptions

- None.

## Open Questions

- No product questions remain for the approved scope.
