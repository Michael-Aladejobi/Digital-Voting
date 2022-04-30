print("""2020/2021 FUNAAB CSC Election

Welcome to Computer Science\n""")

from collections import Counter

class votes:

    

    def vote_for(self, names):

        self.candidates = [ ]

        self.candidates += names

        return self.candidates

    def get_winner(self):

        self.result = Counter(self.candidates)

        return self.result

        

print('Candidates are: "Segun", "Seye", "Mayor", "Michael", "Femi"\n Please enter the names carefully! \n \nNB: There is only ten(10) votes available!')

        

names = [ ]

vote = votes()

for lifeline in range(10):

    name = input("Enter your Candidate's name: ").capitalize()

    names.append(name)

vote.vote_for(names)

print(vote.get_winner())
