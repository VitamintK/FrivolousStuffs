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

def run_trial(families) -> ('girls', 'boys'):
    all_children = []
    for family in range(families):
        children = []
        while True:
            child = birth()
            children.append(child)
            if child:
                break
        all_children.extend(children)
    return all_children.count(True), all_children.count(False)

def run_trials(trials, families) -> [('girls', 'boys')]:
    results = []
    for trial in range(trials):
        trial_result = run_trial(families)
        results.append(trial_result)
    return results

def get_percent_girl(trials, families):
    results = run_trials(trials, families)
    avg_pct_girl = statistics.mean(map(lambda x: x[0]/(x[0] + x[1]), results))
    print("""Out of {} trials of {} families each, the average percentage of girls
that makes up each population is {}""".format(trials, families, avg_pct_girl))
    return avg_pct_girl

get_percent_girl(TRIALS,FAMILIES)
get_percent_girl(1, 500)
get_percent_girl(500,1)
