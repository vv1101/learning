def lineareq(eq1, eq2, eq3, ra=0, rb=0, rc=0):
    import numpy as np
    a = np.array([eq1, eq2, eq3])
    b = np.array([ra, rb, rc])
    x = np.linalg.solve(a, b)
    print(f"x = {x[0]} y = {x[1]} z = {x[2]}")


lineareq([20, -3, 10], [10, -5, 20], [10, -5, 20], 100, 200, 200)
