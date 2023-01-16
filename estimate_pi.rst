How to estimate the value of π...
=================================

... using Monte Carlo simulation

Many moons ago...
-----------------

I was interviewing for internships while in grad school and I am
and have always been a terrible interviewer. Period.
This interview, turned out to be the atypical technical interview
which called for an out of the box interview.
The interviewer was a, I later learned, a PhD in particle physics
and his interest was in gauging my skills in designing and
implementing Monte Carlo simulations. The question was

*Given a (pseudo) random number generator, how can you estimate the
value of π*

At this point, you would do well to **NOT** read on and think about
designing the experiment by yourself and then you can can read on
to see three possible solutions below.
*Hint: eschew premature optimization*

The dead simple solution
^^^^^^^^^^^^^^^^^^^^^^^^

Without loss of generality, consider a unit circle (i.e. of radius 1 and centered at the origin in the Cartesian plane).  The equation of this circle will be :math:`x^2 + y^2 = 1`

Circumscribe
a square box around the circle, such that its sides are parallel to the :math:`x` and :math:`y` axes. Now, we know that for any pair of numbers :math:`(x, y)`, if :math:`x` and :math:`y` are on the circle,

Assume the random number generator generates numbers between -1.0
to 1.0. I can use this to generate a pair of numbers
:math:`(x_i, y_i)` designating a point on the :math:`xy` plane. We
know that this point must lie on or inside the circumscribed
square, the area of which is 4.
The area of the circle is :math:`\pi`, so the probability that
:math:`(x_i, y_i)` will lie inside the circle should be
:math:`\pi/4`.

The code
^^^^^^^^

Or how to be shown the door early.

The following code works but as I will discuss, it is a cardinal sin
to give someone the following solution.

.. code-block:: python
    :linenos:

    import numpy as np


    def inside_circle(x: float, y: float) -> bool:
        return 1 if x ** 2 + y ** 2 - 1 < 0 else 0


    def estimate_pi(n=1000000):
        nums = 2 * np.random.random_sample((n, 2)) - 1.0

        insides = np.array([1 if inside_circle(x, y) else 0 for x, y in nums])
        mean = np.mean(insides)
        return 4 * mean


    if __name__ == "__main__":
        estimate_pi()


Technically, the above code is correct but grossly insufficient.
Let us first dwell on why it is technically correct.
Then we can point out the insufficiency of it all.

Lines 4-5 defines a function that determines if a point
:math:`(x,y)` lies inside or outside the circle.

The function ``estimate_pi()`` runs the simulations ``n`` times.

Line 9 is where we draw a pair of numbers :math:`(x_i,y_i)`
``n`` times. Since the numbers themselves are actually in the range
:math:`[0,1]`, they have to be scaled up by a factor of 2 and then
subtract by 1 to produce numbers in the range :math:`[-1,1]`.

In line 11, we determine if each pair of :math:`(x_i,y_i)`
is inside the unit circle (1) or outside (0), and we create an
array of size ``n`` so that for every pair that is inside the
unit circle is produces 1 while every one outside the unit
circle produces 0.

Then, it is a simple matter of averaging to
arrive at an estimate of π which is line 12 - 13. Line 12 estimates
:math:`\frac{\hat{\pi}}{4}` and line 13 then multiplies this by 4 to
provide the estimate :math:`{\hat{\pi}}`

Of course, I teased the idea that this solution would have led to me
being shown the door. That's because I am providing a way to estimate
π but nowhere have I provided an error estimate and it is a cardinal
sin in this field to provide a Monte Carlo simulation that does not
provide an error estimate. In fact, I Googled
`estimate pi using monte carlo` and in the first page of results,
only one site bothered to deal with errors. I plan to revisit this
at a later point. For now, this fatally flawed solution will have
to do.