import pandas

class Vote:
    def __init__(self, file_name, sheet_name, vote_name):
        self.read(file_name, sheet_name, vote_name)
        self.result = self.range_all()

    def read(self, file_name, sheet_name, vote_name):
            excel_data = pandas.read_excel(file_name, sheet_name=sheet_name)
            self.data_vote = excel_data[vote_name].tolist()
            return  self.data_vote

    def range_all(self):
        pass

    def winner_all(self):
        pass

    def winner_n(self, n):
        pass

    def winner(self):
        pass

class FirstPastPost(Vote):

    def range_all(self):
        winner_dict = {}
        for i in self.data_vote:
            if winner_dict.get(i) == None:
                 winner_dict[i] = 1
            winner_dict[i] += 1
            self.result = dict(sorted(winner_dict.items(), key=lambda item: item[1], reverse = True))
        return self.result

    def winner_all(self):
        return list(self.result.keys())

    def winner_n(self, n):
        return list(self.result.keys())[:n]

    def winner(self):
        return list(self.result.keys())[0]

class AbsoluteMajority(FirstPastPost):
    def winner(self):
        if 2*list(self.result.values())[0] > sum(list(self.result.values())):
            return list(self.result.keys())[0]
        return 'Абсолютного большенства нет!'


if __name__ == '__main__':
    # file, VoteType, VoteName
    vote_set = FirstPastPost('test.xlsx', 'OneVote', 'Vote1')
    print(vote_set.winner_all())
    print(vote_set.winner_n(3))
    print(vote_set.winner())

    # file, VoteType, VoteName
    vote_set = AbsoluteMajority('test.xlsx', 'OneVote', 'Vote1')
    print(vote_set.winner_all())
    print(vote_set.winner_n(3))
    print(vote_set.winner())

    # file, VoteType, VoteName
    vote_set = AbsoluteMajority('test.xlsx', 'OneVote', 'Vore2')
    print(vote_set.winner_all())
    print(vote_set.winner_n(3))
    print(vote_set.winner())
