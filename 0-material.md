
Hello PREP students! I'm a graduate student studying optimization/machine learning, and I'm going to give you a lesson on optimization. My learning objectives are to answer these questions:

* Why should you care about optimization?
* What are the basics of optimization? How do you get a better solution?
* Where does optimization fail?

"Optimization" is producing a *model* that accurately represents *data*, aka "fitting" a model to data. Importantly, the choice of "model" and "data" are perhaps more important than the specific method of fitting the model to the data. In short, optimization is what happens with this code:

``` python
from sklearn.linear_model import LinearRegression

estimator = LinearRegression()

# X and y are stand-ins for other data; they could easily from a CSV
X = [[1, 2], [3, 4]]
y = [3, 5]

est.fit(X, y)
```

In this lesson, I'll try to open up the black box that happens when you call `fit`. I've selected about an hour's worth of video for you to watch, and will try to highlight some relevant issues in person.

*Note: optimization is heavy in mathematics. I will try to illustrate optimization without relying on mathematics.*

# Background

### What's optimization?

Optimization is a process to *"fit"* a *"model"* to *"data."*

* **Data**, typically some features and a label for each example.
* **A model** which will try to predict the label from a feature fector.
* **A loss function** that chacterizes how poorly the model is performing for a specific example.

"Fitting" means "can the model accurately predict an unseen example?" Here are some good background videos on the components above:

* **What's optimization?** https://www.youtube.com/watch?v=x6f5JOPhci0 (10:08) provides a general overview of optimization methods (and tradeoffs of those methods) and and some common issues in optimization in a real-world example.

* **How are machine learning (ML) and optimization related?** https://www.youtube.com/watch?v=NzwMV2b7jbQ (10:31) introduces ML models, and introduces how to find it. In addition the primary goal given noisy/non-standard examples?

### How are models found?
The videos above provide a general overview of machine learning/optimization and a general idea of what happens inside `fit`. Now, let's get into some specifics on how to find the best model for the models mentioned in "Mixed Linear Models":

* **How is linear regression performed?** https://www.youtube.com/watch?v=PaFPbb66DxQ (9:21).

* **How is the minimum "loss" or "error" found in machine learning?** https://www.youtube.com/watch?v=IHZwWFHWa-w (only the first 11:18 is relevant from this 21:00 video).

* **Which loss function should I use?** https://www.youtube.com/watch?v=fr7dfyfB7mI (6:14) steps through different use cases where different loss functions would apply. This is the most important part of ML.

This is enough background to get understand my examples. In the example, I'll highlight some issues with optimization, included data size, noise and loss functions.

# Demo

The videos above are all the material you need for the demo. To follow along for me demos, visit https://github.com/stsievert/PREP21/blob/main/README.md. If you have difficulty, email me at stsievert@wisc.edu.

# Want to learn more?

This material is not required for the example.

Here are some other useful videos:

* **How do I score a model?** https://www.youtube.com/watch?v=rY5pdNW7jKM (4:40) steps through the data you should use, **a critical choice.** (I can talk all day about this).

* **How does classification work? And how can it be modified to support more complex data?** https://www.youtube.com/watch?v=-Z4aojJ-pdg&t=5m40s (12:23)

* **Which model class should I use?** How to choose a model class: https://www.youtube.com/watch?v=7jjzMZOdPZw (18:37)

* **What's a neural network?**  https://www.youtube.com/watch?v=aircAruvnKk (19:13)

Also, I would skim Chapter 7 of "Shape" by Jordan Ellenburg (23 pages). It's light reading, and tells stiches a good story of optimization. The author, Jordan Ellenburg, is a mathematics professor at UW--Madison and experienced with optimization.

In addition, I've written a blog series on optimization that try to introduce the math behind optimization:

1. "Least squares and regularization," which steps through the basics of linear regression https://stsievert.com/blog/2015/11/19/inverse-part-1/
2. "Finding sparse solutions to linear systems," which examines a particular type of regularization (and has some fancy interactive widgets to understand what the minimization is doing) https://stsievert.com/blog/2015/12/09/inverse-part-2/
3. "Gradient descent and physical intuition for heavy-ball acceleration with visualization", which looks at a method to modify optimization methods. https://stsievert.com/blog/2016/01/30/inverse-3/
