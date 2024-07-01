https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2024-07-01

            count = 0
            for num in arr:
                if num % 2 != 0:
                    count += 1
                    if count == 3:
                        return True
                else:
                    count = 0
            return False
