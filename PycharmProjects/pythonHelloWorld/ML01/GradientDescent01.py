import numpy as np

X_train=np.array([[2104,5,1,45],[1416,3,2,40],[852,2,1,35]])
Y_train=np.array([460,232,178])

b_init=785.1811367994083
w_init=np.array([0.39133535,18.75376741,-53.36032453,-26.42131618])


# def predict_single_loop(x,w,b):
#     return np.dot(x,w)+b
#
# print(predict_single_loop(X_train[0,:],w_init,b_init))

def predict_cost(x,y,w,b):
    m=x.shape[0]
    cost=0.0
    for i in range(m):
        f_wb_i=np.dot(x[i],w)+b
        cost=cost+ (f_wb_i-y[i])**2
    cost=cost/(2*m)
    return cost


print(predict_cost(X_train,Y_train,w_init,b_init))

# compute gradient descent----------------------------------

def gradient_descent(x,y,w,b):

    m,n = x.shape
    print(x.shape)
    dj_dw=np.zeros((n,))
    dj_db=0

    for i in range(m):
        err=(np.dot(x[i],w)+b) - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err * x[i,j]
        dj_db = err + dj_db

    dj_db=dj_db/m
    dj_dw=dj_dw/m
    return  dj_dw, dj_db

tmp_dj_dw, tmp_dj_db=gradient_descent(X_train, Y_train, w_init, b_init)

print(f"{tmp_dj_db}....{tmp_dj_dw}")