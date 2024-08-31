class Solution:
	def minJumps(self, arr):
		# store current index we are at
		curr_index = 0
		
        # length of array
		length = len(arr)
		
        # number of steps 
		steps = 0
		
        # keep moving until we haven't reached the end
		while curr_index < length - 1:
			
            # check the max possible increment
			increment = arr[curr_index]
			
            # if increment is zero and we haven't reached the end, we cannot reach the end
			if increment == 0 and curr_index < length - 1:
				return -1
			
            # if increment is 1, no calculations needed, just move to next index
			elif increment == 1:
				curr_index += 1
				steps += 1
				
            # if increment is enough to reach the final index, return current steps plus 1
			elif curr_index + increment >= length - 1:
				return steps + 1
			
            # else check all possible jumps to calculate the max jump
			else:
				
                # max jump possible and index from which it is possible
				max_jump = 0
				max_jump_index = 0
				
                # for all numbers reachable through increment
				for i in range(1, increment+1):
					
                    # if index we are checking is out of bound, skip it
					check_index = curr_index + i
					if check_index >= length:
						continue
					
                    # if reach from the check index is greater than max jump calculated so far
					# set it as the max jump
					jump = i + arr[check_index]
					if jump > max_jump:
						max_jump = jump
						max_jump_index = check_index
						
                # move to the index providing the maximum jump
				curr_index = max_jump_index
				steps += 1
				
        # return calculated steps
		return steps