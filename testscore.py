import scores

score = scores.Scores()

# score.guess_hit()
# score.guess_hit()
# score.guess_hit()
# score.guess_hit()

print(score.get_total())

score.guess_error()
score.guess_error()
score.guess_error()
score.guess_error()
score.guess_error()

print(score.get_total())


score.guess_hit()
score.guess_hit()

print(score.get_total())

score.guess_error()
score.guess_error()

print(score.get_total())

# score.guess_hit()
# score.guess_hit()
# score.guess_hit()

print(score.get_total())

score.guess_error()
score.guess_error()
# score.guess_hit()
# score.guess_hit()

print(score.get_total())

# score.winner()
score.loser()

print(score.get_total())
