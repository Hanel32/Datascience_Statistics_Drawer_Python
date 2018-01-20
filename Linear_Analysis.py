
"""
@author: Carson Hanel

Note: These code snippets are derived from Data Science from Scratch First Principles by Joel Grus.
      For right now, I'll be transferring the code from the book, explaining the functions, and creating
      an API that can be utilized in further analysis. While some of these functions may be part of 
      the Python standard library or a package already created, I thought it would be useful to begin
      creating my own data science toolbelt for the future, with self written commentary.
"""

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
      """
      def vector_sum (vectors):
            result = vectors[0]
            for vector in vectors[1:]:
                  result = vector_add(result, vector)
            return result
                  
