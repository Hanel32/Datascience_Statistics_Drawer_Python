
"""
@author: Carson Hanel

Note: These code snippets are derived from Data Science from Scratch First Principles by Joel Grus.
      For right now, I'll be transferring the code from the book, explaining the functions, and creating
      an API that can be utilized in further analysis. While some of these functions may be part of 
      the Python standard library or a package already created, I thought it would be useful to begin
      creating my own data science toolbelt for the future, with self written commentary.
"""
import math

class Linear_Analysis():
      """
      Vector addition:
            Vector addition is simply pointwise addition of two lines, or vectors.
            The function creates a tuple (v,w) of all pointwise pairs between the
            two vectors, and iteratively adds them together in a pointwise fashion,
            finally returning a list of generated points.

            Noteworthy: You're only supposed to be able to add two vectors of equal length,
                        however, zip adapts to the dimensions of the shortest vector given
                        as per the library definitions. Perhaps this could be improved by
                        introducing error handling.
      """
      def vector_add (v, w):
            return [v_i + w_i for v_i, w_i in zip(v,w)]
      
      """
      Vector subtraction:
            Please refer to the notes written on vector addition.
      """
      def vector_sub (v, w):
            return [v_i - w_i for v_i, w_i in zip(v,w)]
      
      """
      Vector summation:
            Takes a list of vectors as an argument.
            The 0'th vector is set as the accumulation point, rather, in order to effectively
            create a sum across all vectors, all vectors must be added to some vector; namely 
            the 0'th. From then, the function iterates from the 1'st vector onward, adding all
            subsequent vectors to 0'th, and finally returning the accumulated sum.

            Some useful application from the book:
            
                  def vector_sum(vectors):
                        return reduce(vector_add, vectors)
                        
            Which is a higher order function that reduces the vector space to a singular vector
            by utilizing the given function, "vector_add". It's not necessary, but is a good usage
            of space if that's the type of best practice you're after.
      """
      def vector_sum (vectors):
            result = vectors[0]
            for vector in vectors[1:]:
                  result = vector_add(result, vector)
            return result

      """
      Scalar multiplication:
            Used for multiplying a vector by a scalar. Essentially vector_add with multiplication,
            and rather than a second vector being zipped and summed, all points are simply multiplied
            by a constant.
      """
      def scalar_multiply(c, v):
            return [c * v_i for v_i in v]

      """
      Dot product:
            Used for multiplying the pointwise information of two vectors into pointwise products.
            Simply works like vector_sum, but rather than the sum, you're deriving the product of
            the two vectors; a simple algorithm.
      """
      def dot(v, w):
            return sum(v_i * w_i for v_i, w_i in zip(v,w))

      ""
      Sum of squares:
            The multiplication of a vector by itself. Utilized for determining the dispersion of a 
            vector which is representative of a set of data. Also utilized in determining the line
            of best fit for a dataset.
      """
      def sum_of_squares(v):
            return dot(v, v)
                  
