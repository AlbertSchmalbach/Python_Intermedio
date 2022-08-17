import numpy
from sklearn import linear_model

X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X,y)

def logit2prob(logr, X):
  log_odds = logr.coef_ * X + logr.intercept_
  odds = numpy.exp(log_odds)
  probability = odds / (1 + odds)
  return(probability)

print(logit2prob(logr, X))

# Resultado

#   [[0.60749955]
#    [0.19268876]
#    [0.12775886]
#    [0.00955221]
#    [0.08038616]
#    [0.07345637]
#    [0.88362743]
#    [0.77901378]
#    [0.88924409]
#    [0.81293497]
#    [0.57719129]
#    [0.96664243]]