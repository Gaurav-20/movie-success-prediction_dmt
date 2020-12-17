# How to use this project

You need to have Python3 for trying out this project.

`
python3 models.py
`

Following are pip dependencies:
- sklearn
- matplotlib
- pandas
- seaborn
- numpy
- tmdbsimple



# Conclusion

|    Algorithms               |    Mean   Test Score    |    Mean   Training Score    |    Hyper-parameters                                          |
|-----------------------------|-------------------------|-----------------------------|--------------------------------------------------------------|
|    Logistic   Regression    |    0.7047               |    0.7055                   |    solver:   newton-cg   C:   1000                           |
|    KNN                      |    0.6557               |    0.7251                   |    n-neighbors: 11                                           |
|    Decision   Tree          |    0.6581               |    0.7441                   |    criterion:   entropy,   max_depth:   6                    |
|    Random   Forest          |    0.6735               |    0.7558                   |    criterion:   gini   n_estimators:   9   max_depth:   8    |

The logistic regression algorithm yielded the best accuracy with a mean test score of 0.7047. It also has the lowest difference between mean test score and mean training score (0.0008), which means that it is fit neither overfitted nor underfitted.
