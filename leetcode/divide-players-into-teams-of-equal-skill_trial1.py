class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) -1
        initial_sum = skill[l] + skill[r]
        sum = 0
        while l < r:
            if skill[l] + skill[r] == initial_sum:
                sum += skill[l] * skill[r]
                l+=1
                r-=1
            else:
                return -1
        return sum