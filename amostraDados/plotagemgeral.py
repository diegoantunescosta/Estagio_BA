import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('checkout_business_information_limpo.csv')

plt.plot(x["country_id"])

plt.show()