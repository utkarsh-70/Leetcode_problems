class Solution:
    def numTeams(self, ratings) -> int:
        if len(ratings) < 3:
            return 0
        
        team = [None]*3
        res = 0
        cache = dict()
        res += self.helper(ratings, 0, team, 0, True, cache)
        res += self.helper(ratings, 0, team, 0, False, cache)
        return res
    
    def helper(self, ratings, start, team, curr, flag, cache):
        key = (start, curr, flag)
        if key in cache:
            return cache[key]
        if curr == 3:            
            return 1
        if start == len(ratings):
            return 0
        
        res = 0         
        for idx in range(start, len(ratings)):
            curr_rating = ratings[idx]
            if curr == 0:
                team[curr] = curr_rating
                res += self.helper(ratings,idx+1,team,curr+1, flag, cache)
                team[curr] = None
            elif flag and curr_rating > team[curr-1]:
                team[curr] = curr_rating
                res += self.helper(ratings,idx+1,team,curr+1, flag, cache)
                team[curr] = None
            elif not flag and curr_rating < team[curr-1]:
                team[curr] = curr_rating
                res += self.helper(ratings,idx+1,team,curr+1, flag, cache)
                team[curr] = None
        
        res = res
        cache[key] = res
        return res