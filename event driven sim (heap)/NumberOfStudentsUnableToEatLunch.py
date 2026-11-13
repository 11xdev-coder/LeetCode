from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        q1 = deque(students)
        q2 = deque(sandwiches)

        den = 0
        while q1 and den < len(q1):
            stud = q1.popleft()
            if stud == q2[0]:
                q2.popleft()
                den = 0
                continue

            q1.append(stud)
            den += 1

        return len(q1)
