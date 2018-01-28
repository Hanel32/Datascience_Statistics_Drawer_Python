
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

  """
  Furthermore:
    We can also do the reverse, finding the intervals at which likelihood cutoffs exist.
    For example, "if we want to find an interval centered at the mean and containing 60%
    probability, then we find the cutoffs of the upper and lower 20%"
    
    These are the methods we can utilize:
  """
  def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability """
    return inverse_normal_cdf(probability, mu, sigma)

  def normal_lower_bound(probability, mu=0, sigma=1):
    """retuns the z for which P(Z >= z) = probability """
    return inverse_normal_cdf(1 - probability, mu, sigma)

  def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
       that contain the specified probability         """
    tail_probability = (1 - probability) / 2
    upper_bound      = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound      = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound
 
  """
  Example:
      In order to run the experiment of flipping an unbiased coin 1000 times:
  """
  mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
      
  """
  Next:
    We need to make a decision about significance.
    How willing are we to accept an error?  
    In this, let's choose 2.5% of the time.
  """
  normal_two_sided_bounds(0.975, mu_0, sigma_0)
  
  """
  Continuing:
    Assuming the hypothesis is true, there's at most a 2.5% chance we observe a set of 1000
    trials outside of the tested confidence interval.
    
    Further, we're concerned with the probability that we've made a type 2 error, or rather,
    we've accepted the hypothesis although it is generally false in nature. To find this, we
    calculate the "power" of a test, which is the probability of _not_ making a type 2 error.
    
    Let's check out what happens if p is actually .55 rather than .5
  """
  #95% bounds based on assumption p is 0.5
  lo, hi = normal_two_sided_bounds(0.975, mu_0, sigma_0)
      
  #actual mu and sigma based on p = .55
  mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
      
  #a type 2 error means we fail to reject the null hypothesis
  #which will happen when x is still in our original interval
  type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
  power = 1 - type_2_probability # 0.887
      
  """
  Also:
    Imagine that the null hypothesis was instead the the coin was not biased
    towards heads, or rather p <= .5. "In that case we want a one-sided test that rejects the
    null hypothesis when X is much larger than 50 but not when X is smaller than 50. So a 5%
    significance test involves normal_probability_below to find the cutoff below which 95% of
    the probability lies"
  """
  hi = normal_upper_bound(0.95, mu_0, sigma_0)
  #is 526 (< 531, since we need more probability in the upper tail)
  
  type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
  power = 1 - type_2_probability # 0.936
      
  """
  Two-sided bias test:
    To test if the probability is actually .5
  """
  def two_sided_p_value(x, mu=0, sigma=1):
    if x>= mu:
      #if x is greater than the mean, the tail is what's greater than x
      return 2 * normal_probability_above(x, mu, sigma)
    else:
      #if x is less than the mean, the tail is what's less than x
      return 2 * normal_probability_below(x, mu, sigma)

  #If we were to see 530 heads in 1000, we would compute:
  two_sided_p_value(529.5, mu_0, sigma_0) # 0.062

  """
  Tradeskill Note:
    Utilizing 529.5 instead of 530.
    This is called a "continuity correction" which reflects the fact that
    normal_probability_between(529.5, 530.5, mu_0, sigma_0) is a better probability
    of seeing 530 heads than normal_probability between(530, 531, mu_0, sigma_0) is.
    
    Nice.
  """
  #One way to convince yourself that this is a sensible estimate is with a simulation:
  extreme_value_count = 0
  for _ in range(1000000):
    num_heads = sum(1 if random.random() < 0.5 else 0
                    for _ in range(1000)
    if num_heads >= 530 or num_heads <= 470:
      extreme_value_count += 1
  print extreme_value_count / 1000000 # 0.062

  """
  Since the p-value is greater than our 5% significance, we don't reject the null. If we'
  instead saw 532 heads, the p-value would be:
  """
  two_sided_p_value(531.5, mu_0, sigma_0) # 0.0463
                    
  """
  Which is smaller than the 5% significance, which means we reject the null.
  Similarly:
  """
  upper_p_value = normal_probability_above
  lower_p_value = normal_probability_below
  
  #For a one-sided test, if we saw 525 heads, we would compute:
  upper_p_value(524.5, mu_0, sigma_0) # 0.061
                    
                    


   



  #It's outside if it's not between
  def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)
  
  
