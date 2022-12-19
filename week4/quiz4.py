from numpy import log2

# Suppose that we have a neuron which, in a given time period, will fire with probability 0.1, yielding a Bernoulli distribution for the neuron's firing (denoted by the random variable F = 0 or 1) with P(F = 1) = 0.1.

# Which of these is closest to the entropy H(F) of this distribution (calculated in bits, i.e., using the base 2 logarithm)?
# 2 points

# 0.4690

 # -0.1954

# 1.999

# 0.1954

print (-0.1 *log2(0.1) - 0.9*log2(0.9))

# Question 2

# Continued from Question 1:

# Now lets add a stimulus to the picture. Suppose that we think this neuron's activity is related to a light flashing in the eye. Let us say that the light is flashing in a given time period with probability 0.10. Call this stimulus random variable SS.

# If there is a flash, the neuron will fire with probability 1/2. If there is not a flash, the neuron will fire with probability 1/18. Call this random variable FF (whether the neuron fires or not).

# Which of these is closest, in bits (log base 2 units), to the mutual information MI(S,F)?
# 4 points

# 0.0904

# 0.8476

# 0.3786

# -0.3786
