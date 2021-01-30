# Lottery honesty

## What is it?

This is a statistics study about lottery honesty using a test for association (independence).
It does NOT prove that a lottery system is not biased, but it points against or in his favor.

## Motivation

Sometimes I heard people say that lottery is not fair, things like: they pick the winners, the result is biased some way, etc. 
But non of those argued pointing to a scientific study, and as I couldn't find one, I'm doing this by my own.

## How does a test for association works?

We establish two hypothesis, one that tells the system is not biased, the other tells the opposite (biased system).
We compare the expected values to be seen and the actual seen values using the chi-square statistic, finally this is going to give a probability for our conclusion between the two hypothesis.

## The chosen system

It was chosen the *Lotofácil* system which is brazilian lottery system consisting of 25 numbers, ordered from 1 to 25, 
where 15 numbers are randomly riffled, the maximum prize is achieved by guessing all the 15 numbers correctly.
This was the chosen system just because it belongs to the government, this means all data used in this study is opensource.

## The test

### Step 1:

Assume the null hypothesis as the probabilities of all numbers be observed is the same, 
which means the game is not biased, and the alternative hypothesis as the probabilities being biased among the 25 numbers, 
i.e. 

![Null hypothesis](https://latex.codecogs.com/svg.latex?{\color{blue}H_0:p_1=p_2=p_3=\ldots=p_{25}=\frac{15}{25}})

![Alternative hypothesis](https://latex.codecogs.com/svg.latex?{\color{blue}H_1:p_j{\neq}{\frac{15}{25}}})

### Step 1.1:

Every contest 15 numbers are riffled out of 25, it means every number has a 15/25 probability of being observed, 
so the expected value of a number being observed out of 2125 contest (number of contest used at this study) is 
![Expected value](https://latex.codecogs.com/svg.latex?{\color{blue}2125\frac{15}{25}=1275})

### Step 2:

The test statistic is ![Statistic](https://latex.codecogs.com/svg.latex?{\color{blue}\chi^{2}(v)}), 
where ![V](https://latex.codecogs.com/svg.latex?{\color{blue}v}) are degrees of freedom given by ![Degree](https://latex.codecogs.com/svg.latex?{\color{blue}{(r-1)}})
where ![r](https://latex.codecogs.com/svg.latex?{\color{blue}r}) is the dimensions of the table `Lotofac_hist.xlsx` (only the Obs_value column), 
i.e. ![Real_r](https://latex.codecogs.com/svg.latex?{\color{blue}r=25{\Rightarrow}v=24})

### Step 3:

Assuming ![Epsilon](https://latex.codecogs.com/svg.latex?{\color{blue}\alpha=0.05}) (probabiility of guessing the system is fair when it actually isn't)
we got ![Statistic](https://latex.codecogs.com/svg.latex?{\color{blue}\chi^{2}(24)=36.41503})

### Step 4:

The observed value for the statistic is 

![Statistic](https://latex.codecogs.com/svg.latex?{\color{blue}\chi^{2}=13.55765}) 

### Step 5:

As the observed value for ![Statistic](https://latex.codecogs.com/svg.latex?{\color{blue}\chi^2}) 
was lower than the critical value, obtained at **Step 3**, we should accept (not reject) the null hypothesis.
The p-value of the test is ![Statistic](https://latex.codecogs.com/svg.latex?{\color{blue}p.value=0.9560187}) which tells us the same thing. 