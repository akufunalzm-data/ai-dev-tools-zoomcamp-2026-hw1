# Django Backlog: Shared Household Chores Tool

## Task 1: Initialize the Django application

**Purpose:** Establish a Django project and a dedicated chores application with a root route for the shared household interface. Do not add accounts or authentication.

**Acceptance criteria:**

- The Django project starts successfully in a local development environment.
- The chores application is registered and has a reachable root route.
- No user account, sign-in, or authentication functionality is present.

**Dependencies:** None.

## Task 2: Create household-member and chore data models

**Purpose:** Represent assignable household members and one-time chores, including title, assignee, due date, and completion state.

**Acceptance criteria:**

- A household member can be stored and retrieved for chore assignment.
- A chore requires a title, assignee, and due date.
- A chore records whether it is active or complete.
- The model does not include recurrence or audit-history data.

**Dependencies:** Task 1.

## Task 3: Add household-member management

**Purpose:** Let the shared household add and view members who can receive chore assignments.

**Acceptance criteria:**

- A household member can be added through the shared interface.
- Added members appear in the household member list.
- Added members are available when assigning a new chore.

**Dependencies:** Task 2.

## Task 4: Create and display active chores

**Purpose:** Let the shared household create one-time chores and see outstanding work.

**Acceptance criteria:**

- A chore can be created only with a title, assignee, and due date.
- A newly created chore appears in the active-chore list.
- Each active chore displays its title, assigned member, and due date.

**Dependencies:** Tasks 2 and 3.

## Task 5: Complete chores and show completion history

**Purpose:** Allow anyone using the shared interface to complete a chore and retain it in a separate completed section.

**Acceptance criteria:**

- Any person using the interface can mark an active chore complete.
- A completed chore no longer appears in the active-chore list.
- A completed chore appears in the completed section.
- No completion or activity audit log is displayed or recorded.

**Dependencies:** Task 4.

## Task 6: Add feature-level automated tests

**Purpose:** Verify the approved behavior for member management, chores, and completion.

**Acceptance criteria:**

- Tests cover adding a household member and using that member as a chore assignee.
- Tests cover required chore title, assignee, and due date.
- Tests cover active and completed chore separation after completion.

**Dependencies:** Tasks 3, 4, and 5.
