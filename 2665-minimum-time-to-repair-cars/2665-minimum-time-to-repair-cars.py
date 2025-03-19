class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        mint=min(ranks)*cars*cars
        def isvalid(time):
            carsrep=0
            for i in ranks:
                carsrep+=int((time//i)**0.5)
            return carsrep>=cars
        
        l,r=1,mint
        while l<r:
            time=(l+r)//2
            if isvalid(time):
                r=time
            else:
                l=time+1
        return l