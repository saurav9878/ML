# Machine Learning

Arthur Samuel: The field of study that gives computers the ability to learn without
	           being explicitly programmed.
Tom Michael: A computer program is said to learn from experience E with respect to 
	         some class of tasks T and performance measure P, if its performance at
			 tasks in T, as measured by P, improves with experience E.
Example:- playing checkers

E = the "experience' (need not to be winning experience only) of playing many games 
	of checkers
T = the "task" of playing checkers.
P = the probability that the program will win the next game.(performance)

## Types:-

1. Supervised Learning
2. Unsupervised Learning

## Supervised Learning

We are given a data set and already know what our correct output should look like,
having the idea that there is an relationship between input and output.

1. Regression Problem
2. Classification Problem

### Regression Problem

Regression analysis is a statistical process for estimating the relationships among
variable and predict real valued output. Typically, there is an output or dependent 
variable(price of house) and one or more predictors or features (area of house, no. 
of bedrooms). Specifically regression models estimate how the "typical" value of the
output variable changes when one of the features is changed(while keeping others as 
fixed constant).

Eg. Linear regression where the dependent variable is modeled as a function of
	the features.
	
### Classification Problem

It is a problem of identifying which category(out of a set of categories) an example
belongs to.
e.g. Classify tumors as affected/unaffected. Another example could be classifying
	handwritten digits into 0,1,2,3,4,5,6,7,8,9.


### When the target variable that we’re trying to predict is continuous, such as in our housing example, we call the learning problem a regression problem.

###  When y can take on only a small number of discrete values (such as if, given the living area, we wanted to predict if a dwelling is a house or an apartment, say), we call it a classification problem.


## Unsupervised Learning

1. It allows us to approach problems with little or no idea about what our results 
   should look like. We can derive structure from data where we don't necessarily 
   know the effect of the variables.
2. We can derive this structure by clustering the data based on relationships among 
   the variables in the data.
3. With unsupervised learning there is no feedback based on the prediction results.

Example:

### Clustering Problem

Take a collection of 1000000 different genes and find a way to automatically group
these genes into groups that are somehow similar or related by different variables
in the data.

### Non-Clustering Problem

The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment
(i,e, identifying individual voices and music from a mesh of sounds at party)

## Notations:

m = Number of Training Examples
x's = "input" variable/features
y's = "output" variable/"target" variable
(x, y) = single training example
(x<sub>i</sub>, y<sub>i</sub>) = ith training example i=1,2,3...

## Linear Regression Models

Given a training set, to learn a function h : X → Y so that h(x) is a “good” 
predictor for the corresponding value of y. and this 'h' is called Hypothesis.

h<sub>θ</sub>(x) = θ<sub>0</sub> + θ<sub>1</sub>x

Shorthand: h(x)

θ - parameter

### Cost Function

We can measure the accuracy of our hypothesis function by using a cost function.
J (θ<sub>0</sub>, θ<sub>1</sub>) = ![](http://www.HostMath.com/Show.aspx?Code=%5Cfrac%7B1%7D%7B2m%7D%5Csum_%7Bi%3D1%7D%5Em(h(x_i)%20-%20y_i)%5E2)
