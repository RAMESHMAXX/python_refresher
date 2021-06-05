from typing import List
def avg_cal(sequence:List) -> float:      #float is return type and List is object type
    return sum(sequence)/len(sequence)



print(avg_cal([1,2,3]))