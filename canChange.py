# 2337. Move Pieces to Obtain a String
# Runtime O(n)
# Memory O(n)

# Given two strings that can contain "L", "R", or "_", returns true if target
# can be reached from start by moving L's to the left and R's to the right through _'s

def canChange(self, start: str, target: str) -> bool:
    squeue = []
    tqueue = []

    for i in range(len(start)):
        if start[i] != "_":
            squeue.append((start[i], i))
        if target[i] != "_":
            tqueue.append((target[i], i))

    if len(squeue) != len(tqueue):
        return False
    
    while len(squeue) > 0:
        schar, sindex = squeue.pop(0)
        tchar, tindex = tqueue.pop(0)

        if schar != tchar or (schar == "L" and sindex < tindex) or (schar == "R" and sindex > tindex):
            return False

    return True
