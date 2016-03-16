from math import log

x = [1,2,3,4, 5, 6, 7]
p_x=[.1, .2, .3, .1, 0 , .1, .2]

# Expected Value = SUM(Mean of Outcomes)
# Outcome = x * probability[x]
def expectedValue( x_arr, y_arr ):
    total = 0;
    for i,n in enumerate(x_arr):
        total += n*(y_arr[i])
    return total
# Entropy = -SUM( p[x]*log(p[x]) )
def entropy( x_arr, y_arr ):
    entropy = 0
    for i,n in enumerate(x_arr):
        if y_arr[i] == 0:
            continue
        entropy += y_arr[i]*log(y_arr[i])
    entropy *= -1;
    return entropy

print ("Expected Value: ", expectedValue(x, p_x))
print ("Entropy: ", entropy(x, p_x))
