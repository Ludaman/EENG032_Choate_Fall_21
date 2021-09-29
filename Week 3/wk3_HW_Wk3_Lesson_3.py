# ## Week 3 Lesson 3: Solving Equations


# ### Problem 1

# Based on  General Linear Least Squares from chapter 15 of Numerical_recipes_chap15.pdf
# [Numerical Recipes in C](http://s3.amazonaws.com/nrbook.com/book_C210.html)
#  with focus on Solution by Use of Singular Value Decomposition
 
# HW: 
# For the svd fit example, re-write the the function to allow for any n degree polynomial fit.

# e.g. 
# ```python 
# def svg_fit(x,y,n):
#    Your Code here
#    return a_fit
# ```

# SVD Fit Example:

# ```python
# def svd_fit_quad(x, y):
#     """
#      perform a linear regression using svd
#     y = a_0 + a_1 * x + a_2 * x**2
#     decompose the design matrix (A) from 15.4.4 of Numerical Recipes in C

#     Inputs:
#         x: Numpy array or pandas series
#         y: Numpy array or pandas series

#     Returns:
#         a_0, a_1 and a_2
#     """
#     design_matrix = np.array([np.ones_like(x), x, x ** 2]).T  # len(x) x 3
#     a_fit = np.zeros(3)  # We know we want a length 3
#     u, s, vh = np.linalg.svd(design_matrix, full_matrices=False)
#     for i in range(3):
#         a_fit += u[:, i].dot(y) / s[i] * vh[i, :]  # 15.4.17
#     print(a_fit)
#     y_fit = design_matrix @ a_fit
#     plt.figure()
#     plt.plot(x, y, label="real")
#     plt.plot(x, y_fit, label="fit")
#     plt.legend()
#     plt.grid()
#     plt.show()
#     return a_fit



# if __name__ == '__main__':
#     df = pd.read_csv('../data/co2_weekly_mlo.txt', skiprows=49,
#                      names=['yr', 'mon', 'day', 'decimal', 'ppm', ' #days', '1 yr ago', '10 yr ago', 'since 1800'],
#                      delim_whitespace=True)
#     clean_df = df[df.ppm != -999.99]
#     # clean_df.plot('decimal', 'ppm')
#     afit = svd_fit_quad(clean_df['decimal'], clean_df['ppm'])
# ```  