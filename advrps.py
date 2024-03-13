import random

class RPS_AI:
    def __init__(self):
        self.moves = ['r', 'p', 's']
        self.transition_probs = {move: {next_move: 1 for next_move in self.moves} for move in self.moves}
        self.user_moves = []

    def predict_next_move(self):
        if not self.user_moves:
            return random.choice(self.moves)

        last_user_move = self.user_moves[-1]
        next_move_probs = self.transition_probs[last_user_move]
        most_likely_user_move = max(next_move_probs, key=next_move_probs.get)
        return {'r': 'p', 'p': 's', 's': 'r'}[most_likely_user_move]

    def update_transition_probs(self):
        if len(self.user_moves) < 2:
            return
        for i in range(len(self.user_moves) - 1):
            current_move = self.user_moves[i]
            next_move = self.user_moves[i + 1]
            self.transition_probs[current_move][next_move] += 1

    def update_moves(self, user_move):
        self.user_moves.append(user_move)

def get_winner(user_move, ai_move):
    if (user_move == 'r' and ai_move == 's') or \
       (user_move == 'p' and ai_move == 'r') or \
       (user_move == 's' and ai_move == 'p'):
        return "You win"
    elif user_move == ai_move:
        return "Tie"
    else:
        return "AI wins"

def main():
    ai = RPS_AI()
    user_score = 0
    ai_score = 0
    while user_score < 15 and ai_score < 15:
        user_move = input("Enter a move (r, p, or s): ").lower()
        if user_move not in ['r', 'p', 's']:
            print("Only enter 'r', 'p', or 's'.")
            continue
        ai_move = ai.predict_next_move()
        print(f"The AI responds with: {ai_move.upper()}")
        
        winner = get_winner(user_move, ai_move)
        print(winner)
        if "AI" in winner:
            ai_score += 1
        elif "You" in winner:
            user_score += 1
        
        print("Scores:")
        print(f"You: {user_score}\tAI: {ai_score}")
        print("-" * 20)

        ai.update_moves(user_move)
        ai.update_transition_probs()

    if user_score == 15:
        print("Just lucky")
    else:
        print("IMAGINE YOU LOST TO A BOT")

if __name__ == "__main__":
    main()
