
import random

############################################################################
# CLASSES
############################################################################

class Player:
    def __init__(self, name: str, email: str, race: str):
        self.name = name
        self.email = email
        self.race = race
        self.status = "Active"
        self.match_counter = 0
        self.point_counter = 0


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.name = f"{player1.name} VS {player2.name}"
        self.winner = None

    def play(self):
        # Randomly determine the winner
        if random.randint(0, 1) == 0:
            self.winner = self.player1
        else:
            self.winner = self.player2

        self.winner.match_counter += 1
        self.winner.point_counter += 3          # 3 points for winning match

        # Select winner and loser
        loser = self.player1 if self.winner == self.player2 else self.player2
        loser.match_counter += 1
        loser.point_counter += 1                # 1 point for loss match
        loser.status = "Inactive"


class Tournament:
    def __init__(self):
        self.players = []
        self.matches = []

    def add_player(self, name, email, race):
        self.players.append(Player(name, email, race))

    def get_active_players(self):
        return [p for p in self.players if p.status == "Active"]

    def get_inactive_players(self):
        return [p for p in self.players if p.status == "Inactive"]

    def create_match(self, player1, player2):
        # Create a match between the two specified players
        match = Match(player1, player2)
        match.play()
        self.matches.append(match)
        return match

    def play_tournament(self):
        # Randomize the player index in order to create the matches
        active_players = self.get_active_players()
        random.shuffle(active_players)
        num_players = len(active_players)
        print("\n TOURNAMENT BEGINS ")
        print("*" * 40)

        for i in range(0, num_players, 2):
            player1 = active_players[i]
            player2 = active_players[i + 1]
            match = self.create_match(player1, player2)
            print(f"{match.name}: {match.winner.name} wins!")

        # Determine the winner of the tournament
        final_match = Match(self.matches[-1].winner, self.matches[-2].winner)
        final_match.play()
        print("\n FINAL MATCH ")
        print("*" * 40)
        print(f"{final_match.name}: {final_match.winner.name} wins!")

    def display_results(self):
        # Displaying tournament results
        print("\n - TOURNAMENT RESULTS:")
        for i, player in enumerate(self.players):
            print(
                f"{i + 1}. {player.name}: {player.point_counter} points, {player.match_counter} matches played, status: {player.status}")
        print("\n")
        print("*" * 40)
        print("1. Export file")
        print("2. Only display the results")
        export_decision = input("\nDo you want to export a file with results? ")

        if export_decision == "1":
            t.export_results()
        elif export_decision == "2":
            pass

# CREATE TEXT FILE
    def export_results(self):
        with open("tournament_results.txt", "w") as file:
            file.write("- TOURNAMENT RESULTS:")
            for i, player in enumerate(self.players):
                file.write(f"""
    {i + 1}. {player.name}: 
        Email: {player.email}
        Race: {player.race}
        Total points: {player.point_counter}
        Matches Played: {player.match_counter} 
        Status: {player.status}\n""")

        print("\n")
        print("*" * 40)
        print(" TEXT FILE HAS BEEN EXPORTED ")
        print("*" * 40)



############################################################################
# MAIN
############################################################################

t = Tournament()

while True:
    print("1. Add player")
    print("2. Start tournament")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        race = input("Enter race: ")
        t.add_player(name, email, race)
        print(f"\nThe player '{name}' has been added.")

    elif choice == "2":
        active_players = t.get_active_players()
        num_players = len(active_players)
        if num_players < 4:
            print("\n Not enought players to start.")
        else:
            t.play_tournament()
            t.display_results()
            break

    elif choice == "3":
        break