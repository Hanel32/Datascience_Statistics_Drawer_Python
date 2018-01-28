
"""
@author: Carson Hanel
Note: These code snippets are derived from Data Science from Scratch First Principles by Joel Grus.
      For right now, I'll be transferring the code from the book, explaining the functions, and creating
      an API that can be utilized in further analysis. While some of these functions may be part of 
      the Python standard library or a package already created, I thought it would be useful to begin
      creating my own data science toolbelt for the future, with self written commentary.
"""
class Hypothesis_Analysis():
  """
  Normal approximation to binomial:
    Coin flipping trial.
    p = 0.5
    Each coin flip is a Bernoulli trial;
    X is a Binomial(n, p) random variable
    You can approximate it utilizing:
  """
  def normal_approximation_to_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma
  
  """
  Explanation:
    Whenever a random variable follows a normal distribution, we can use
    normal_cdf to figure out the probability that its realized value lies
    either within or outside a certain interval.
  """
  # The normal CDF _is_ the probability the variable is below a threshold
  normal_probability_below = normal_cdf
  
  #It's above the threshold if it's not below the threshold
  def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)
  
  #It's between the threshold if it's less than hi, but not less than lo
  def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)
  
  #It's outside if it's not between
  def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)
  
  
