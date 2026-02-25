from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connection.cursor().db_conn
        users = db.users
        teams = db.teams
        activities = db.activities
        leaderboard = db.leaderboard
        workouts = db.workouts

        # Clear collections
        users.delete_many({})
        teams.delete_many({})
        activities.delete_many({})
        leaderboard.delete_many({})
        workouts.delete_many({})

        # Insert teams
        marvel = {'name': 'Marvel', 'members': []}
        dc = {'name': 'DC', 'members': []}
        teams.insert_many([marvel, dc])

        # Insert users
        user_data = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
        ]
        users.insert_many(user_data)

        # Insert activities
        activity_data = [
            {'user': 'Spider-Man', 'activity': 'Running', 'duration': 30},
            {'user': 'Iron Man', 'activity': 'Cycling', 'duration': 45},
            {'user': 'Wonder Woman', 'activity': 'Swimming', 'duration': 60},
            {'user': 'Batman', 'activity': 'Walking', 'duration': 20},
        ]
        activities.insert_many(activity_data)

        # Insert workouts
        workout_data = [
            {'user': 'Spider-Man', 'workout': 'Pushups', 'reps': 50},
            {'user': 'Iron Man', 'workout': 'Squats', 'reps': 40},
            {'user': 'Wonder Woman', 'workout': 'Situps', 'reps': 60},
            {'user': 'Batman', 'workout': 'Pullups', 'reps': 30},
        ]
        workouts.insert_many(workout_data)

        # Insert leaderboard
        leaderboard_data = [
            {'user': 'Spider-Man', 'points': 100},
            {'user': 'Iron Man', 'points': 90},
            {'user': 'Wonder Woman', 'points': 110},
            {'user': 'Batman', 'points': 95},
        ]
        leaderboard.insert_many(leaderboard_data)

        # Ensure unique index on email
        users.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
