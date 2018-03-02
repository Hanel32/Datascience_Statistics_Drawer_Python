###############################################################################
#                   A Study of Support Vector Machines                        #
#                                                                             #
#                     Data Mining in Social Networks                          #
#                         Author: Carson Hanel                                #
#                      Professor: Eduardo Nakamura                            #
###############################################################################
# Note: I had intended this to be a Jupyter notebook, but having technical    #
#       difficulties w/ the program.                                          #
###############################################################################
# a)                                                                          #
# Create a training data set with 200 random samples. Plot the training obser-#
# vations, colored according to their class labels. Your plot should display  #
# X1 on the x-axis, and X2 on the y-axis.                                     #
###############################################################################
set.seed(1)
x1=runif(200)-0.5
x2=runif(200)-0.5
y=1*(x1^2-x2^2>0)
plot(x1, x2, col=(y+1), pch=(y+19), cex=2)

# Prepare the data for the SVM
# Import the SVM library
install.packages("e1071")
install.packages("caret")
library(e1071)
library(caret)

# Bind x1, x2 into a column matrix, print it out (optionally)
x = cbind(x1, x2)
x

# Create a dataframe, print it out (optionally)
dat = data.frame(x=x, y=as.factor(y))
dat

# Designate the sample for train
train=sample(200,100)

###############################################################################
# b)                                                                          #
# Fit a support vector classifier (tuned) to the data with X1 and X2 as predi-#
# ctors. Obtain a class prediction for each test observation. Plot the traini-#
# ng and test observations, colored according to the predicted class labels   #
#                                                                             #
# A note here:                                                                #
#    These data have a polynomial of order 2 relationship. A simpler linear   #
#    kernal is not going to be sufficient to correctly classify.              #
###############################################################################

# Tune the SVM, output the results
tl.out=tune(svm, y~., data=dat[train,], kernel="linear", ranges=list(cost=10^(-4:4)))
summary(tl.out)
bestl = tl.out$best.model
plot(bestl, dat)

# Get predictions for training set
lin_train_ypred = predict(bestl, newdata=dat[train,])
table(predict=lin_train_ypred, truth=dat[train, "y"])

# Get predictions for test set
lin_test_ypred  = predict(bestl, newdata=dat[-train,])
actual          = table(predict=lin_test_ypred, truth=dat[-train, "y"])

# Plot training set
plot(bestl, dat[train,])

# Plot testing set
plot(bestl, dat[-train,])

# F1 recall
TP        = actual[1][1]
FP        = actual[3][1]
FN        = actual[2][1]
TN        = actual[4][1]
precision = TP / (TP + FP)
recall    = TP / (TP + FN)
f1_recall = 2 * ((precision * recall)/(precision + recall))
f1_recall # .5319149

###############################################################################
# Discussion of findings:                                                     #
#                                                                             # 
# Alright! So, as you can see the initial linear kernel fit is pretty garbage,#
# but, why? Well, this is because the dataset has a degree 2 polynomial relat-#
# ionship. We know this because that's how we've generated our dataset. Howev-#
# er, we don't always know this. So, in those situations when our data aren't #
# as obvious, we look at the performance metrics of the SVM. When predicting  #
# the training data's classification, class 0 had 22 correct classifications, #
# and 30 incorrect classifications, and class 1 had 34 correct classifications#
# and only 14 incorrect classifications.                                      #
#                                                                             #
# F1 recall = .5319149 which is only slightly better than random chance!      #
# In other words, without knowing the polynomial relationship, F1 recall just #
# told us our fit is junk.                                                    #
#                                                                             #
# Let's move on to the polynomial kernel.                                     #
###############################################################################

###############################################################################
# c)                                                                          #
# Fit a support vector classifier (tuned) using a polynomial kernel. Obtain a #
# class prediction for each training and test observation. Plot the training  #
# and test observations, colored according to predicted class labels.         #
###############################################################################

# Tune the SVM, output the results
tp.out=tune(svm, y~., data=dat[train,], kernel="polynomial", ranges=list(cost=10^(-1:2), degree=(1:4)))
summary(tp.out)
bestp = tp.out$best.model
plot(bestp, dat)

# Get predictions for training set
poly_train_ypred = predict(bestp, newdata=dat[train,])
table(predict=poly_train_ypred, truth=dat[train, "y"])

# Get predictions for test set
poly_test_ypred  = predict(bestp, newdata=dat[-train,])
actual = table(predict=poly_test_ypred, truth=dat[-train, "y"])

# Plot training set
plot(bestp, dat[train,])

# Plot testing set
plot(bestp, dat[-train,])

# F1 recall
TP        = actual[1][1]
FP        = actual[3][1]
FN        = actual[2][1]
TN        = actual[4][1]
precision = TP / (TP + FP)
recall    = TP / (TP + FN)
f1_recall = 2 * ((precision * recall)/(precision + recall))
f1_recall # .8695652

###############################################################################
# Discussion of findings:                                                     #
#                                                                             #
# Intuitively, it would make sense that a degree 2 polynomial would be fit ap-#
# propriately by a degree 2 polynomial kernel. From the plotting, you can see #
# a great improvement in classification from the simple linear kernel. The cl-#
# assification boundaries detailed by the support vectors is much more repres-#
# entative of the actual function than the linear kernel, as instead of a line#
# you can actually see the "X" shape.                                         #
#                                                                             #
# F1 score = .8695652 which is a substatial improvement over the slightly-gre-#
# eater-than-random-chance linear classifier.                                 #
#                                                                             #
# Before going on, I'd like to assert that I know factually that this model is#
# the appropriate fit for the data. Thus, moving on to the radial kernel will #
# greatly overfit the data, but seem like a better option w/ higher f1.       #
###############################################################################

###############################################################################
# d)                                                                          #
# Fit a support vector classifier (tuned) using a radial kernel. Obtain a     #
# class prediction for each training and test observation. Plot the training  #
# and test observations, colored according to predicted class labels.         #
###############################################################################

# Tune the SVM, output the results
tr.out=tune(svm, y~., data=dat[train,], kernel="radial", ranges=list(cost=10^(-1:2), gamma=c(0.5, 1:4)))
summary(tr.out)
bestr = tr.out$best.model

# Get predictions for training set
radial_train_ypred = predict(bestr, newdata=dat[train,])
table(predict=radial_train_ypred, truth=dat[train, "y"])

# Get predictions for test set
radial_test_ypred  = predict(bestr, newdata=dat[-train,])
actual = table(predict=radial_test_ypred, truth=dat[-train, "y"])

# Plot training set
plot(bestr, dat[train,])

# Plot testing set
plot(bestr, dat[-train,])

# F1 recall
TP        = actual[1][1]
FP        = actual[3][1]
FN        = actual[2][1]
TN        = actual[4][1]
precision = TP / (TP + FP)
recall    = TP / (TP + FN)
f1_recall = 2 * ((precision * recall)/(precision + recall))
f1_recall # .9052632

###############################################################################
# Discussion of findings:                                                     #
#                                                                             #
# Now that we're looking at the plot of the test set data, you can see that   #
# this model is GREATLY overfitting our randomized dataset. The reason for    #
# this is that there are a finitely number of randomly generated points with  #
# a low resolution, in other words, there's not enough data, and we've really #
# overfit. To show that, I'll use that same fit to predict on a dataset that  #
# was created the same way, but with 1,000,000 observations.                  #
###############################################################################
# Generate the data
set.seed(1)
x1=runif(1000000)-0.5
x2=runif(1000000)-0.5
y=1*(x1^2-x2^2>0)

# Check out the resolution of the data.
plot(x1, x2, col=(y+1), pch=(y+19), cex=2)

# Create the dataset
x = cbind(x1, x2)
dat = data.frame(x=x, y=as.factor(y))

# Score w/ radial and polynomial
radial_highres  = predict(bestr, dat)
poly_highres    = predict(bestp, dat)
actual_radial   = table(predict=radial_highres, truth=dat[, "y"])
actual_poly     = table(predict=poly_highres, truth=dat[, "y"])

# F1 for radial
TP        = actual_radial[1][1]
FP        = actual_radial[3][1]
FN        = actual_radial[2][1]
TN        = actual_radial[4][1]
precision = TP / (TP + FP)
recall    = TP / (TP + FN)
f1_recall = 2 * ((precision * recall)/(precision + recall))
f1_recall # .8735287

# Plot radial w/ 1,000,000 data pts
# Warning, code takes a second.
plot(bestr, dat)

# F1 for polynomial
TP        = actual_poly[1][1]
FP        = actual_poly[3][1]
FN        = actual_poly[2][1]
TN        = actual_poly[4][1]
precision = TP / (TP + FP)
recall    = TP / (TP + FN)
f1_recall = 2 * ((precision * recall)/(precision + recall))
f1_recall # .8856425

# Plot polynomial w/ 1,000,000 data pts
# Warning, code takes a second.
plot(bestp, dat)

###############################################################################
# Conclusion of findings:                                                     #
#                                                                             #
# What I saw was that essentially, you can have a great f1 with a not-so-great#
# fit on the data. The radial kernel was grossly overfit to the small amount  #
# of data that it was originally fit to, though it was similar in f1 recall to#
# the much closer to the truth polynomial fit. Essentially, this is caused by #
# the original polynomial fit being good, but lacking resolution in the areas #
# closest to the "X" section where the classes meet. If the polynomial kernel #
# was fed with more data, it would be possible to reach ~99% F1, as would the #
# radial kernel, but the polynomial kernel would take much less data to make  #
# that transition.                                                            #
#                                                                             #
# Super fun lab! I hope my insight was enough, and I apologize if the extra   #
# analysis was unnecessary/too much                                           #
###############################################################################



