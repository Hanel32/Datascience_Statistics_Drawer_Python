
"""
@author: Carson Hanel
Note: These code snippets are derived from Data Science from Scratch First Principles by Joel Grus.
      For right now, I'll be transferring the code from the book, explaining the functions, and creating
      an API that can be utilized in further analysis. While some of these functions may be part of 
      the Python standard library or a package already created, I thought it would be useful to begin
      creating my own data science toolbelt for the future, with self written commentary.
"""
class Statistics_Analysis:
  """
   Mean:
     Essentially the average value of the elements of x.
  """
  def mean(x):
    return sum(x) / len(x)
  
  """
  Median:
    When sorted, the central value of the elements of x.
  """
  def median(v):
    n        = len(v)
    sorted_v = sorted(v)
    midpoint = n / 2
    
    if n % 2 == 1:
      return sorted_v[midpoint]
    else:
      lo = midpoint - 1
      hi = midpoint
      return (sorted_v[lo] + sorted_v[hi]) / 2
  
  """
  Quantile:
    The percentile index; i.e. .01'th quantile to .99'th quantile.
    To put it in other words, the quantile is the count of data points within that percentile range
    of the data set; If there are 100 data points, there are 18 data points in the .18 quantile.
  """
  def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]
  
  """
  Mode:
    The most commonly occurring value in x
  """
  def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]
  
  """
  Data Range:
    Dispersion between the highest and lowest values of dataset x.
  """
  def data_range(x):
    return max(x) - min(x)
  
  """
  De-Mean:
    Essentially, subtract the mean from all values from x, making the mean 0.
    This is an intermediary step in finding the variance.
  """
  def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
  
  """
  Variance:
    The expectation of the squared deviation of a random variable from its mean.
    Colloquially, it is how far spread the set of random numbers is from their
    average value.
  """
  def variance(x):
    n          = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
  
  """
  Standard Deviation:
    The quantification of the amount of dispersion in a set of data; the square-root of the variance.
  """
  def standard_deviation(x):
    return math.sqrt(variance(x))
  
  """
  Inter-Quartile Range:
    The number of data points between the 25'th and 75'th quantiles of x.
  """
  def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)

  """
  Covariance:
    The paired analogue of variance. Whereas variance measures how a single variable
    deviates from its mean, covariance measures how two variables vary in tandem from
    their means.

    Interpreting Covariance:
      Large, positive covariance: The tendency is when X is large, Y is large, and when X is small, Y is small
      Large, negative covariance: The tendency is when X is large, Y is small, amd when X is small, Y is large
      Small, positive covariance: The correlation between the X and Y is less strong, but dominantly positive.
      Small, negative covariance: The correlation between the X and Y is less strong, but dominantly negative.
      Near-zero covariance: There is little to no correlation in the variance of X and Y.
  """
  def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

  """
  Correlation:
    Lies between -1 and 1, either a perfect ant-correlation (an X, giving -1), or a perfect correlation (Essentially, a vector)
    The correlation metric can give you insight on how close your data is taking into account covariance and dividing out the
    the standard deviation for the two variables X and Y.
  """
  def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0. and stdex_y > 0.:
      return covariance(x, y) / stdev_x / stdev_y
    else:
      return 0
