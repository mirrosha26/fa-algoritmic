class Permutations:
    def __init__(self, list):
        self.value = [[i+1 for i in range(len(list))], list]
        self.len = len(list)

    def reverse(self):
        rande_list = []
        count = 0
        for i in self.value[1]:
            count += 1
            rande_list.append([i, count])
        res = sorted(rande_list, key=lambda x: x[1])
        self.value = [rande_list]

        



d = Permutations([1,2,3,7,6,5])
print(d.value)
d.reverse()
print(d.value)