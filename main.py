import random
import names
from prettytable import PrettyTable as table
from classification import Classification as freelancer

exp_weight = 8
rating_weight = 5
cap_weight = 9
pricing_weight = 4

task_exp_coff = 4
task_r_coff = 8
task_c_coff = 6
task_p_coff = 2
task_rel_coff = 8

freelancers = []

for i in range(0, 10):
    freelancers.append(
        freelancer(
            names.get_first_name(),
            random.randrange(0, exp_weight),
            random.randrange(0, rating_weight),
            random.randrange(0, cap_weight),
            random.randrange(0, pricing_weight),
            random.randrange(0, task_exp_coff),
            random.randrange(0, task_r_coff),
            random.randrange(0, task_c_coff),
            random.randrange(0, task_p_coff),
            random.randrange(0, task_rel_coff)
        )
    )

for person in freelancers:
    score = 0
    score += person.experience * person.experience_modififer
    score += person.rating * person.rating_mod
    score += person.confidence * person.confidence_mod
    score += person.pricing * person.pricing_mod
    person.score = score

sortedlist = sorted(freelancers, key=lambda x: x.score, reverse=True)

t = table(['Name', 'Score'])

for i in sortedlist:
    t.add_row([i.name, i.score])

print(t)

