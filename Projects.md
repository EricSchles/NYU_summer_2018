# Project One

## Deadline

The first project will be due June 21st

## Description 

In this project you will be building a tiny computer.  By understanding how your computer works, you'll better be able to understand how computation works more generally speaking.  For this project you'll be implementing the basics of a computer system.

Specifically, we will be making an arithmetic logic unit (ALU) for this project.  You will need to implement a series of logic gates in order to build this ALU.  These gates will be written as functions.

## Steps

1. In order to get background on computer systems you'll need to watch this excellent [youtube series](https://www.youtube.com/watch?v=O5nskjZ_GoI&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=2).  For a diagram of the actual ALU you'll need to look at [this diagram found on wikipedia.](https://en.wikipedia.org/wiki/Arithmetic_logic_unit#/media/File:74181aluschematic.png)

2. Next you'll need to follow the blueprint, implementing the functions outlined in template_project_one.py - also found in the repo.   Make sure you change the name of the file from template_project_one.py to `project_one_[group_name].py` where group_name is filled in with the name of your group.

3. Turn in the project along with a write up of what you did.  You should explain each function and the choices you made when building your system.  You should also include three examples programs that use your ALU to perform some simple computation.

 
# Project Two

## Description

In this project you'll be implementing and using linear regression in a few ways.  First you'll implement it without libraries, this will teach you how the algorithm works.  Then you'll implement it in numpy.  This will give you a sense of how to make use of the numpy interface in detail.  Finally you'll implement distributed linear regression using dask.  This will give you a sense of how to write a production machine learning algorithm. 

## Deadline

July 19th

## Steps

1. In order to get background on linear regression read the following materials explaining how the algorithm works:

* [Introduction to linear regression](https://www.youtube.com/watch?v=zPG4NjIkCjc)
* [Linear regression OLS algorithm](https://www.youtube.com/watch?v=JvS2triCgOY)
* [Linear Regression Reference](https://economictheoryblog.com/contents-ordinary-least-squares/) - In this reference there is R code and Julia code but no Python, so no need to read through anything on that.  But there are no implementation helpers here.

* [statsmodels linear regression docs](http://www.statsmodels.org/dev/regression.html)
* [sci-kit learn linear regression docs](http://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares)

Once you have a good sense of this you'll write your "from scratch" implementation.  You'll use your implementation to analyze this data set.  Compare how your version of linear regression does against statsmodels version and scikit-learn's version.  Did your algorithm come up with the same results?  Why or why not?  What did other implementations do differently.  Is the running time of your algorithm faster or slower?  Why?



2. Next you'll write a Cythonized version of the linear regression algorithm.  Read through the Cython documentation found [here](https://cython.readthedocs.io/en/latest/).  Compare and contrast the running time and accuracy of the cythonized version with the vanilla version.  What were the contributing factors for any differences?

3. Next you'll read through the numpy specification found [here](https://docs.scipy.org/doc/numpy-1.13.0/reference/) and this this tutorial found [here](https://docs.scipy.org/doc/numpy/user/quickstart.html). Now you'll reimplement linear regression using numpy.  What are the differences between the cythonized version and the numpy version, in terms of performance and accuracy?  How much faster is the numpy version than the vanilla version?  

4.  Finally you'll read through the dask documentation found [here](https://dask.pydata.org/en/latest/docs.html) and this watch this tutorial on dask found [here](https://www.youtube.com/watch?v=yI_yZoUaz60).  Then you'll implement a distributed version of linear regression using dask.  Compare and contrast the performance and accuracy of the dask implementation against the vanilla, cythonized, and numpy versions.  Which does the best in terms of speed?  Why might this be the case?  Which does the best in accuracy?  Why might this be the case?

