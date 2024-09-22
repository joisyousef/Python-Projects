def muatation(individual,pm):
    r=np.random.random()
    if r < pm:
        m=np.random.randint(8)#1-7
        individual[m
]=np.random.randint(8)
    return individual