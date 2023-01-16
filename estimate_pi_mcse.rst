How to estimate the value of π...(part 2)
=========================================

In my last blog entry, I had ended by introducing the idea why a Monte-Carlo simulation that estimates a :math:`\pi`
without estimating the error involved in the simulation gives an incomplete picture of the simulation. The Monte Carlo
Standard Error (MCSE) is a measure of the accuracy of the simulation. The lower the MCSE, the more accurate the
simulation.

Let :math:`\widehat{\pi}` be the Monte Carlo-estimated value of :math:`pi`
and let :math:`\widehat{\sigma}` be the corresponding standard deviation of the simulation.
The MCSE of the simulation would be :math:`\frac{\widehat{\sigma_M}}{n}` where :math:`n` would be the size of the generated
scenarios (I belabor this point but we generated :math:`2n` numbers so we could get :math:`n`-*pairs* of numbers
and thus we have :math:`n` scenarios)

So, let us tweak the previous program to change the function `estimate_pi()`

.. code-block:: python
    :linenos:

    def estimate_pi(n=1000000):
        nums = 2 * np.random.random_sample((n, 2)) - 1.0

        insides = np.array([1 if inside_circle(x, y) else 0 for x, y in nums])
        mean = np.mean(insides)
        sd = np.std(insides)
        return 4 * mean, 4 * sd/sqrt(n)


This generates both the estimate of :math:`\pi` and the MCSE.
For example, I ran the program with :math:`n=1000000`, and :math:`n=4000000`, which gave the estimates and MCSE
values of :math:`\widehat{\pi}=3.139252` and :math:`\widehat{\sigma_M}=0.0016438080424721131` for :math:`n=1000000`
and :math:`\widehat{\pi}=3.141344` and :math:`\widehat{\sigma_M}=0.0008211780978667174` for :math:`n=4000000`
