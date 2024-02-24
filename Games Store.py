class AppStore:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.rented_games = {}

    def register(self):
        email = input("Enter your email: ")
        if email in self.users:
            print("Email already registered. Please log in.")
            return

        password = input("Enter your password: ")
        self.users[email] = {'password': password}
        print("Registration successful!")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        if email in self.users and self.users[email]['password'] == password:
            self.current_user = email
            print(f"Welcome, {email}!")
        else:
            print("Invalid email or password. Please try again.")

    def rent_game(self):
        if not self.current_user:
            print("You need to log in first.")
            return

        game_title = input("Enter the title of the game you want to rent: ")
        if game_title not in self.rented_games:
            self.rented_games[game_title] = self.current_user
            print(f"You have successfully rented '{game_title}'.")
        else:
            print(f"'{game_title}' is already rented by another user.")

    def check_rented_games(self):
        if not self.current_user:
            print("You need to log in first.")
            return

        rented_games = [game for game, user in self.rented_games.items() if user == self.current_user]
        if rented_games:
            print("You have rented the following games:")
            for game in rented_games:
                print(f"- {game}")
        else:
            print("You have not rented any games.")

    def return_game(self):
        if not self.current_user:
            print("You need to log in first.")
            return

        game_title = input("Enter the title of the game you want to return: ")
        if game_title in self.rented_games and self.rented_games[game_title] == self.current_user:
            del self.rented_games[game_title]
            print(f"You have successfully returned '{game_title}'.")
        else:
            print(f"You have not rented '{game_title}' or it is rented by another user.")

    def logout(self):
        if self.current_user:
            print(f"Goodbye, {self.current_user}!")
            self.current_user = None
        else:
            print("You are not logged in.")

if __name__ == "__main__":
    app_store = AppStore()

    while True:
        print("\nApp Store Menu:\n"
              "1. Register\n"
              "2. Log In\n"
              "3. Rent Game\n"
              "4. Check Rented Games\n"
              "5. Return Game\n"
              "6. Log Out\n"
              "7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            app_store.register()
        elif choice == '2':
            app_store.login()
        elif choice == '3':
            app_store.rent_game()
        elif choice == '4':
            app_store.check_rented_games()
        elif choice == '5':
            app_store.return_game()
        elif choice == '6':
            app_store.logout()
        elif choice == '7':
            print("Exiting the App Store. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
