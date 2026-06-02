class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        min_finish_time = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        
        # Check every pair of land ride (i) and water ride (j)
        for i in range(n):
            for j in range(m):
                
                # Case 1: Land Ride first, then Water Ride
                land_finish = landStartTime[i] + landDuration[i]
                water_start = max(land_finish, waterStartTime[j])
                total_time_1 = water_start + waterDuration[j]
                
                # Case 2: Water Ride first, then Land Ride
                water_finish = waterStartTime[j] + waterDuration[j]
                land_start = max(water_finish, landStartTime[i])
                total_time_2 = land_start + landDuration[i]
                
                # Update the absolute minimum finish time
                min_finish_time = min(min_finish_time, total_time_1, total_time_2)
                
        return min_finish_time 