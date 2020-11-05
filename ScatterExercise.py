import matplotlib.pyplot as plt
from scipy import stats
temp = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
soup_sale = [220.00, 330.00, 190.00, 340.00, 410.00, 445.00, 415.00]

slope, intercept, r, p, std_err = stats.linregress(temp, soup_sale)

def myfunction(x):
    return slope * x + intercept
mod = list(map(myfunction, temp))

plt.scatter(temp, soup_sale)
plt.xlabel("Temperature")
plt.ylabel("Price in (R)")
plt.title("Soup sales in relation to temperature")
plt.plot(temp, mod)

plt.show()
