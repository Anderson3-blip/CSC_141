class User:
    """Represent a simple user profile."""


    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()


    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"   Username: {self.username}")
        print(f"   Email: {self.email}")
        print(f"   location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")


ande = User('ande', 'matthes', 'e_matt_9', 'e_matthes@example.com', 'alaska')
ande.describe_user()
ande.greet_user()

james= User('bond', 'bbondy', 'bondyburger', 'jb@example.com', 'alaska')
james.describe_user()
james.greet_user()