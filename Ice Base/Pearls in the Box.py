def checkio(marbles: str, step: int) -> float:
    
    probs = []
    count = len(marbles)

    w = marbles.count('w')

    prob_w = w / count if w else 0
    prob_b = 1 - prob_w

    print(prob_b)





           






checkio('bbw', 3)   