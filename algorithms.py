#minimax 
def minimax(state):
    if game.terminal(state):
        return game.score(state)
    #draw tree
    state_values=[]
    for action in game.aviable_actions(state):
        next_state=game.next_state(state)
        val=minimax(next_state)
        state_values.append(val)
    #RETURN SCORE
    if game.current_player(state)=="X":
        return max(state_values)
    else:
        return min(state_values)
#########################################################
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
#muatation
def muatation(individual,pm):
    r=np.random.random()
    if r < pm:
        m=np.random.randint(8)#1-7
        individual[m]=np.random.randint(8)
    return individual
##########################################################
#machine learning (training and testing)
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
model =KNeighborsClassifier(n_neighbors=3)# "3" can be change in exam
model.fit(X_train,y_train)

#calculate accuracy
import sklearn.metrics import accuracy_score

#accuracy of train
y_pred_train=model.predict(X_train)
accuracy_score(y_train,y_pred_train)

#accuracy of test
y_pred_test=model.predict(X_test)
accuracy_score(y_test,y_pred_test)