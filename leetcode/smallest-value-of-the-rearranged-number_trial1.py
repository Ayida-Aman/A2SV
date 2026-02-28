class Solution:
    def smallestNumber(self, num: int) -> int:
        counter = [0] * 10
        is_negative = num < 0

        for n in str(num):
            if n.isdigit():
                counter[int(n)] +=1
        answer = []

        for i in range(1, 10):
            for count in range(counter[i]):
                answer.append(i)
        zeros = [0] * counter[0]

        if is_negative:
            answer = answer[::-1] + zeros
        else:
            answer = answer[:1] + zeros + answer[1:]
        answer = int("".join(map(str, answer)))
        if is_negative:
            answer *= -1
        return answer