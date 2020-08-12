# Event Planner Client Application

  The event planner app is a client facing app that allows clients to create events.

# Links
### Deployed Client Site
  <https://dajana8127.github.io/event_planner_client/>
### Back-End Repository
  <https://github.com/Dajana8127/project_event_planner>
### Deployed API
  <https://project-event-planner.herokuapp.com/>

# Planning
  My planning started with user stories, wireframes and ERDs. I had planned to finish backend repository in the first day, next 2 days I worked on connecting the frontend to the backend. By the 3rd day I had an app where user is able to sign up, sign in, change their password, sign out, get all events, create new events and then update and delete those events.

# User stories
  1. User is able signup/create an account, sign in, change password and sign out.
  2. User is able to see all created events after they sign in.
  3. User is able to see all of their events on page "My Events".
  4. User is able to see each individual event that they created.
  5. User is able to create new events.
  6. User is able to update and delete events.


# Technologies Used:
  - JavaScript
  - React.js
  - Python
  - Django
  - Node.js
  - React Bootstrap
  - Axios
  - eventgreSQL

# Wireframes
![Wireframe](https://i.imgur.com/4oUl6xO.jpg?1)

# ERD
![ERD](https://i.imgur.com/FxWqBor.jpg)

# API End Points

| Verb   | URI Pattern               | Controller#Action |
|--------|---------------------------|-------------------|
| POST   | `/sign-up/`               | `users#signup`    |
| POST   | `/sign-in/`               | `users#signin`    |
| DELETE | `/sign-out`               | `users#signout`   |
| PATCH  | `/change-password/`       | `users#changepw`  |
| GET    | `/events`                 | `events#index`    |
| POST   | `/events/`                | `events#create`   |
| GET    | `/events/:id`             | `events#show`     |
| PATCH  | `/events/:id`             | `events#update`   |
| DELETE | `/events/:id`             | `events#destroy`  |
| POST   | `/rsvps/`                 | `rsvps#create`    |
| DELETE | `/rsvps/:id`              | `rsvps#destroy`   |


# Future Development Plans
I would like to add rsvp option so user can rsvp to events and make the code more clean.

# Setup Steps

1. Fork and clone this repository.
2. Run `pipenv shell` to enter the virtual environment
3. Create a database named `project_event_planner` in PostgreSQL by running `psql` to enter the shell, and then `CREATE DATABASE project_event_planner`
3. In your terminal, run `python manage.py makemigrations` and `python manage.py migrate` to ensure your database is up to date
4. Run `python manage.py runserver` to spin up your local server
