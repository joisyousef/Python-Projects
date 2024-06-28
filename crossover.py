#crossover
def crossover(parent1,parent2,pc):
    r=np.random.random()
    if r < pc:
        m=np.random.radint(1,8)#1-7
        child1=np.concatenate([parent1[:m],parent2[m:]])
        child2=np.concatenate([parent2[:m],parent1[m:]])
    else:
         child1=parent1.copy()
         child2=parent2.copy()
    return child1,child2 