import numpy as np
import linearSVM as lsvm

X = np.array([[0.5, 0.3], [1, 0.8], [1, 1.4], [0.6, 0.9]])
Y = np.array([-1, -1, 1, 1])
svm = lsvm.PrimalSVM(l2reg=0.1)

svm.fit(X,Y,0)

pred, pred_val = svm.predict(X)

acc = np.sum(pred==Y)/len(Y)

print("w={}".format(svm.w))
print("pred vals={}".format(pred_val))
print('accuracy={}'.format(acc))


print('minres method \n')
svm.fit(X,Y,1)

pred, pred_val = svm.predict(X)

acc = np.sum(pred==Y)/len(Y)

print("w={}".format(svm.w))
print("pred vals={}".format(pred_val))

print('accuracy={}'.format(acc))

