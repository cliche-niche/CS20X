This directory contains my assignment submissions in the course CS203B (2021-22 II Sem.). The course covered topics relevant to Probability Theory. As an extra topic, we were taught Markov Chains (and were given a sneak-peek into MCMC methods).

+ [<u>Assignment 1</u>](./Assignment1/)- The assignment had questions based mainly on Conditional Probability and Bayes' Theorem. One question was based on the [CLT](https://en.wikipedia.org/wiki/Central_limit_theorem).<br>
The directory contains a [PDF](./Assignment1/Assignment.pdf) file containing my solutions, a [python file](./Assignment1/main.py) which contains the program for the 4<sup>th</sup> question and a README file. The `PDF` also contains some plots which were made by the [program](./Assignment1/main.py).<br>
Marks Distribution <i>(2 marks were cut in Q2b because continuity of g(u) not checked at u=0 and u=1/2)</i>:
<div align="center">

| Question |  Marks   |
|:---------:|:--------:|
|Q1 |15+15|
|Q2 |10+10+10|
|Q3 |10+5+5+10|
|Q4 |20+10|
</div>

+ [<u>Assignment 2</u>](./Assignment2/)- The assignment had questions based mainly on Estimation/Approximation and Markov Chains. It had an optional question which was a mix of CS202 and CS203 (I attempted it).<br>
The directory contains a [PDF](./Assignment2/Assignment.pdf) file containing my solutions, two python files which contain the programs for the [3<sup>rd</sup>](./Assignment2/Q3.py) and the [4<sup>th</sup>](./Assignment2/Q4.py) question and a README file.<br>
<u>Note:</u> In Question 2, part (c) of the assignment, exp[-k(1+2&delta;<sup>2</sup>)/2(3-2&delta;)] was corrected to exp[-(1+k&delta;)<sup>2</sup>/2(2k+1-k&delta;)].<br>
To show this bound, consider a Bernoulli R.V. that takes the value 1 if the draw is less than (N-&delta;N)/2. Then use the one-sided Chernoff bound. Compute similarly for the case of greater than and then club the inequalities to obtain the result.<br>
Marks Distribution <i>(8 marks were cut in Q2c because bound was not shown)</i>:
<div align="center">

| Question |  Marks  |
|:---------:|:--------:|
|Q1 |15+15|15+15|
|Q2 |5+10+10+15|
|Q3 |15+15|10+5+5+10|
|Q4 |<i>(Optional)</i>|
</div>

<i>Interesting Fact: In A2Q1b, we were free to come up with any kind of algorithm. Some derandomized an algorithm discussed in class [intended solution]. Others came up with deterministic algorithms.<br>
I later got to know that the problem is famously known as Max-Cut problem (NP-Hard and APX-Hard), and what I had rediscovered was (a slight variation of) the 1/2 approximation <b>Greedy algorithm</b>. Pretty poetic if you ask me :)</i>