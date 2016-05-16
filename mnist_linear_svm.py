print(__doc__)
# Author: Krzysztof Sopyla <krzysztofsopyla@gmail.com>
# https://machinethoughts.me
# License: BSD 3 clause


# Standard scientific Python imports
import matplotlib.pyplot as plt
import numpy as np
from time import time

from mnist_helpers import *

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
#fetch original mnist dataset
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original', data_home='./')

#minist object contains: data, COL_NAMES, DESCR, target fields
#you can check it by running
mnist.keys()

#data field is 70k x 784 array, each row represents pixels from 28x28=784 image
images = mnist.data
targets = mnist.target

# Let's have a look at the random 16 images, 
# We have to reshape each data row, from flat array of 784 int to 28x28 2D array
#pick  random indexes from 0 to size of our dataset
show_some_digits(images,targets)


#full dataset classification
X_data =images/255.0
Y = targets

#split data to train and test 
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_data, Y, test_size=0.15, random_state=42)


# Create a classifier: a support vector classifier
classifier = svm.LinearSVC(C=1)

import datetime as dt
# We learn the digits on train part
start_time = dt.datetime.now()
print 'Start learning at {}'.format(str(start_time))
classifier.fit(X_train, y_train)
end_time = dt.datetime.now() 
print 'Stop learning {}'.format(str(end_time))
elapsed_time= end_time - start_time
print 'Elapsed learning {}'.format(str(elapsed_time))


# Now predict the value of the test
expected = y_test
predicted = classifier.predict(X_test)

show_some_digits(X_test,predicted,title_text="Predicted {}")

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
      
cm = metrics.confusion_matrix(expected, predicted)
print("Confusion matrix:\n%s" % cm)


plt.figure()

plot_confusion_matrix(cm)

###
psvm = lsvm.PrimalSVM(l2reg=0.1)

start_time = dt.datetime.now()
print 'Start learning at {}'.format(str(start_time))
psvm.fit(X_train, y_train)
end_time = dt.datetime.now() 
print 'Stop learning {}'.format(str(end_time))
elapsed_time= end_time - start_time
print 'Elapsed learning {}'.format(str(elapsed_time))



pred, pred_val = psvm.predict(X_test)

acc = np.sum(pred==Y)/len(Y)

print(psvm.w)
print(pred_val)
print('accuracy={}'.format(acc))


print("Classification report for psvm classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, pred)))
      
cm = metrics.confusion_matrix(expected, predicted)
print("Confusion matrix for psvm:\n%s" % cm)


plt.figure()

plot_confusion_matrix(cm)

