class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        mins=0
        for i in range(len(seats)):
            mins+=abs(seats[i]-students[i])
        return mins