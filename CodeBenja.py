from numpy import *
from datetime import datetime
import matplotlib.pyplot as plt


def removeOutliers(a, b, dates, outlierConstant):
    upper_quartile_a = percentile(a, 75)
    lower_quartile_a = percentile(a, 25)
    IQR_a = (upper_quartile_a - lower_quartile_a) * outlierConstant
    quartileSet_a = (lower_quartile_a - IQR_a, upper_quartile_a + IQR_a)

    upper_quartile_b = percentile(b, 75)
    lower_quartile_b = percentile(b, 25)
    IQR_b = (upper_quartile_b - lower_quartile_b) * outlierConstant
    quartileSet_b = (lower_quartile_b - IQR_b, upper_quartile_b + IQR_b)

    return a[where((a >= quartileSet_a[0]) & (a <= quartileSet_a[1]) & (b >= quartileSet_b[0]) & (b <= quartileSet_b[1]))], b[where((a >= quartileSet_a[0]) & (a <= quartileSet_a[1]) & (b >= quartileSet_b[0]) & (b <= quartileSet_b[1]))], dates[where((a >= quartileSet_a[0]) & (a <= quartileSet_a[1]) & (b >= quartileSet_b[0]) & (b <= quartileSet_b[1]))]

filename = "Radiation.csv"
with open(filename, 'r') as f:
    header = f.readline().strip().split(",")[1:]
    f.close()
# print (header)
arr = genfromtxt(filename,dtype=int, delimiter=",", skip_header=1)[:,1:]
dates = empty(size(arr[:,0]),dtype='datetime64[D]')
for i in range(len(dates)): dates[i] = str(arr[:,0][i])[:4] + "-" + str(arr[:,0][i])[4:6] + "-" + str(arr[:,0][i])[6:8]

#dates = ['1974-01-01' '1974-01-02' '1974-01-03' ... '2023-03-29' '2023-03-30' '2023-03-31']

E_sol_Caen = arr[:,1]   #[W/m²]
E_sol_Tours = arr[:,2]  #[W/m²]
# print(dates, E_sol_Caen, E_sol_Tours)

P_cr = 0.18     #peak power coefficient (monocristal silicium)
f_pref = 0.75

C_Caen = E_sol_Caen*24*P_cr*f_pref      #[WH/m²] ou [WH] pour 1m²
C_Tours = E_sol_Tours*24*P_cr*f_pref    #[WH/m²] ou [WH] pour 1m²

C_Caen_fix, C_Tours_fix, dates_fix = removeOutliers(C_Caen, C_Tours, dates, 1.5) #[WH/m²]

list_mean_Caen = [list(range(1977, 2020)),list(range(1977, 2020))]
list_mean_Caen = [list(range(1977, 2020)),list(range(1977, 2020))]
print(list_mean_Caen)
# for i in range(len(C_Caen_fix)):
    
#     if(dates[i][0:4]<1977 or dates[i][0:4]>2019): #check if we are in the good year
#         continue
    
#     if(dates[i][5:7]==4):
#         if(dates[i][0:4])

       
    
    
    



