""" In a country in which people only want girls
every family continues to have children until they have a girl.
If they have a boy, they have another child.
If they have a girl, they stop.
What is the proportion of boys to girls in the country?"""
import random
import statistics

TRIALS = 500 #amount of trials
FAMILIES = 500 #amount of families per trial.

def birth():
    """True = girl.  False = boy"""
    return random.random() > 0.5

def run_trial(families):
    all_children = []
    for family in range(FAMILIES):
        children = []
        while True:
            child = birth()
            children.append(child)
            if child:
                break
        all_children.extend(children)
    #print("girls: {}, boys: {}, percentage of girls of all children: {}".format(
    #    all_children.count(True), all_children.count(False), all_children.count(True)/len(all_children)))
    return all_children.count(True), all_children.count(False)

def run_trials(trials, families):
    results = []
    for trial in range(trials):
        trial_result = run_trial(families)
        results.append(trial_result)
    return results

results = run_trials(TRIALS, FAMILIES)
avg_pct_girl = statistics.mean(map(lambda x: x[0]/(x[0] + x[1]), results))

print("""Out of {} trials of {} families each, the average percentage of girls
that makes up each population is {}""".format(TRIALS, FAMILIES, avg_pct_girl))
