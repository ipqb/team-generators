#!/usr/bin/python

## How to run: Script takes one argument (number of teams to create)
## More balance parameters can be added

import sys
import random

starting_error_margin = 0.01 # Percent deviation allowed from ideal gender/program/etc ratio

class FirstYears:
    def __init__(self):
        self.people = []
        self.parameters = set()
        self.parameter_solution_found = {}

    def add(self, first_name, gender, program, **kwargs):
        assert( (program == 'iPQB') or (program == 'CCB') )
        new_person = FirstYear(first_name, gender, program, kwargs)
        for parameter in new_person.parameters:
            self.parameters.add(parameter)
            if parameter not in self.parameter_solution_found:
                self.parameter_solution_found[parameter] = False

        self.people.append(new_person)

    def check_team_balance(self, teams, error_margins, ideal_parameters):
        team_balances = [ {} for team in teams]
        for parameter in self.parameters:
            for i, team in enumerate(teams):
                true_count = 0
                false_count = 0
                for person in team:
                    if parameter in person.parameters and person.parameters[parameter]:
                        true_count += 1
                    else:
                        false_count += 1
                balance = float(true_count) / float(true_count+false_count)
                team_balances[i][parameter] = balance

                if abs(ideal_parameters[parameter]-balance) > error_margins[parameter]:
                    # print 'Team has parameter ratio %.2f for parameter %s; exceeds allowed margin of %.2f' % (abs(ideal_parameters[parameter]-balance), parameter, error_margins[parameter])
                    if self.parameter_solution_found[parameter]:
                        error_margins[parameter] += 0.0000000001 # Controls convergence pace
                    else:
                        error_margins[parameter] += 0.001 # Controls convergence pace
                    return (None, False, error_margins)
            # Once we've found that our error margin can work, we set this variable
            # to no longer increase it as quickly
            self.parameter_solution_found[parameter] = True

        return (team_balances, True, error_margins)

    def make_teams(self, num_teams, starting_error_margin=0.01):
        ideal_parameters = {}
        error_margins = {}
        for parameter in self.parameters:
            error_margins[parameter] = starting_error_margin
            true_count = 0
            false_count = 0
            for person in self.people:
                if parameter in person.parameters and person.parameters[parameter]:
                    true_count += 1
                else:
                    false_count += 1
            ideal_parameters[parameter] = float(true_count) / float(true_count+false_count)

        solution_found = False
        combinations_tried = 0
        while(not solution_found):
            people = random.sample(self.people, len(self.people))
            teams = [ [] for x in xrange(num_teams) ]
            for i, person in enumerate(people):
                teams[ i % len(teams) ].append(person)
            team_balances, solution_found, error_margins = self.check_team_balance(teams, error_margins, ideal_parameters)
            combinations_tried += 1

        print 'Tried %d team combinations' % combinations_tried

        for i, team in enumerate(teams):
            print 'Team %d:' % (i+1)
            print '\t%s' % str(team)
            for parameter in team_balances[i]:
                print '\t%s: %.0f%%/%.0f%%' % (
                    parameter, team_balances[i][parameter]*100.0,
                    (1.0-team_balances[i][parameter])*100.0
                )

    def __len__(self):
        return len(self.people)

class FirstYear:
    def __init__(self, first_name, gender, program, kwargs):
        self.first_name = first_name
        self.parameters = {}

        for key, value in kwargs.iteritems():
            self.parameters[key] = value

        # All parameters must be binary so we convert to true/false (no judgement!)
        # Apologies for implying gender is binary
        if gender == 'M':
            self.parameters['gender'] = False
        elif gender == 'F':
            self.parameters['gender'] = True
        else:
            raise Exception('Invalid person input')

        if program == 'iPQB':
            self.parameters['program'] = True
        elif program == 'CCB':
            self.parameters['program'] = False
        else:
            raise Exception('Invalid person input')

    def __repr__(self):
        return str(self.first_name)

def make_first_year_class():
    first_years = FirstYears()
    first_years.add('Tyler', 'M', 'iPQB')
    first_years.add('Stefan', 'M', 'iPQB')
    first_years.add('Evan', 'M', 'iPQB')
    first_years.add('Seth', 'M', 'iPQB', bioinformatics=True)
    first_years.add('Marco', 'M', 'iPQB')
    first_years.add('Eugene', 'M', 'iPQB')

    first_years.add('Ina', 'F', 'iPQB', bioinformatics=True)
    first_years.add('Elena', 'F', 'iPQB', bioinformatics=True)
    first_years.add('Leanna', 'F', 'iPQB')
    first_years.add('Meena', 'F', 'iPQB', bioinformatics=True)
    first_years.add('Weiyue', 'F', 'iPQB')
    first_years.add('Rachel', 'F', 'iPQB')
    first_years.add('Lillian', 'F', 'iPQB')

    first_years.add('Kaitlin', 'F', 'CCB')
    first_years.add('Chimno', 'F', 'CCB')
    first_years.add('Erin', 'F', 'CCB')
    first_years.add('Eugenia', 'F', 'CCB')
    first_years.add('Stephanie', 'F', 'CCB')
    first_years.add('Allison', 'F', 'CCB')

    first_years.add('Adolfo', 'M', 'CCB')
    first_years.add('Bruk', 'M', 'CCB')
    first_years.add('Steven', 'M', 'CCB')
    first_years.add('Ryan', 'M', 'CCB') 

    return first_years

def main():
    first_years = make_first_year_class()
    first_years.make_teams(int(sys.argv[1]))

if __name__ == "__main__":
    main()
