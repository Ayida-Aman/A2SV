class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        r = len(people)-1
        l = count = 0

        while l <= r:
            if l == r:
                count+=1
                break
            if people[l] + people[r] > limit:
                r-=1
            elif people[l] + people[r] <= limit:
                r-=1
                l+=1
            count+=1
        return count


        