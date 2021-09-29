# # Python 101: Homework
# ## By Evelyn J. Boettcher
# ## Week 3 Lesson 1: Linear Regression
# Major Jeff Choate Responses

# ### Problem 1
# #* Explain what np.polynomial does in this script. 
# #** And what are my options besides Polynomial


##The np.polynomial item calls the polynomial fucntion from the np library and passes in a cleaned up and fitted data set with the ppm and decimal columns.  
# All this function really does is instantiate a polynomial object to be used later
# Another option could be to simply represent the polynomials as arrays


# #```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../../data/co2_weekly_mlo.txt', skiprows=49,
                    names=['yr', 'mon', 'day', 'decimal', 'ppm', ' #days', '1 yr ago', '10 yr ago', 'since 1800'],
                    delim_whitespace=True)
clean_df = df[df.ppm != -999.99]
pp = np.polynomial.Polynomial(np.polyfit(clean_df.decimal, clean_df.ppm, 1))
plt.scatter(clean_df.decimal, clean_df.ppm)
plt.plot(clean_df.decimal, pp(clean_df), color='red')
plt.show()
# ```

# ### Problem 2
print(pp)




# ### Problem 3

#  - [ ] What happens if you try to run this
 
# ```python
#import scipy as sp
#sp.stats.linregress(clean_df.decimal, clean_df.ppm)
#print(sp)

# i tried SCIPI and SCIPY and neither worked, SCIPY ahs no moduel STATS and SCIPI didnt seem to exist


### Problem 4

#- [ ] For the Seaborn example 
#   - [ ] Change the order to: 2 or 3
   
import seaborn as sns; sns.set_theme(color_codes=True)
import pandas as pd
import matplotlib.pyplot as plt

# Get Data
df = pd.read_csv('../../data/co2_weekly_mlo.txt', skiprows=49, 
                 names=['yr', 'mon', 'day', 'decimal','ppm', '#days', '1 yr ago', '10 yr ago', 'since 1800'], 
                 delim_whitespace=True)
clean_df = df[df.ppm != -999.99]
# Set the plots
# ax = sns.regplot(x='decimal', y='ppm', data=clean_df, ci=95, order=2,  
#                  line_kws={'label': 'Linear regression line: $Y(X)=-3827 + 1.8 X$', 'color': 'm'}, 
#                  label="CO2 Weekly average"
#                  ,x_bins=100)
ax = sns.regplot(x='decimal', y='ppm', data=clean_df, ci=95, order=2,  
                 line_kws={'label': 'Linear regression line: $Y(X)=-3827 + 1.8 X$', 'color': 'm'}, 
                 label="CO2 Weekly average"
                 ,x_bins=50)
ax.set_ylabel("CO2 (ppm)")
ax.set_xlabel("Year")
ax.legend(loc="upper left")
plt.show()
# ```

# changed the order, but not 100% sure why

# ### Problem 5 (a,b)
#    - [ ] Add x_bins = 100
#    - [ ] Add x_bins = 50