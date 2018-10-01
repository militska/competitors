from CompetitionSgltn import CompetitionsSgltn

competitions = CompetitionsSgltn()

round1 = competitions.get_instance()
print(round1.start(12))

round2 = competitions.get_instance()
print(round2.start(16))

round3 = competitions.get_instance()
print(round3.start(30))
