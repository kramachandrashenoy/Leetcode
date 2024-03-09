https://www.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1
There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is the start time of meeting i and F[i] is the finish time of meeting i.
The task is to find the maximum number of meetings that can be accommodated in the meeting room. You can accommodate a meeting if the start time of the meeting is 
strictly greater than the finish time of the previous meeting. Print all meeting numbers.

Example 1:

Input:
N = 6
S = {1,3,0,5,8,5}
F = {2,4,6,7,9,9} 
Output:
{1,2,4,5}
Explanation:
We can attend the 1st meeting from (1 to 2), then the 2nd meeting from (3 to 4), then the 4th meeting from (5 to 7),
and the last meeting we can attend is the 5th from (8 to 9). It can be shown that this is the maximum number of meetings we can attend

Solution:
class Solution:
    def maxMeetings(self, N: int, S: List[int], F: List[int]) -> List[int]:
        # Combine the start and finish times and also store the meeting numbers
        meetings = list(zip(range(1, N + 1), S, F))
        
        # Sort meetings based on finish time
        meetings.sort(key=lambda x: x[2])
        
        # List to store the selected meetings
        selected_meetings = []
        
        # Initialize end time with the finish time of the first meeting
        end_time = meetings[0][2]
        
        # Select the first meeting
        selected_meetings.append(meetings[0][0])
        
        # Iterate through the rest of the meetings
        for i in range(1, N):
            if meetings[i][1] > end_time:
                # If the start time of the current meeting is greater than the end time of the previous meeting
                selected_meetings.append(meetings[i][0])
                end_time = meetings[i][2]

        return sorted(selected_meetings)
