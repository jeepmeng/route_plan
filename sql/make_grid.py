from dis_calculate import *
import json
import numpy as np

x_side_length = 0.004
y_side_length = 0.003
central = '125.325504,43.928104'
grid = []
grid_dict = dict()
for i in range(20):
    # x0_y0 = central
    x0 = np.round(float(central.split(',')[0])+x_side_length*i,6)
    x1 = np.round(float(central.split(',')[0])+x_side_length*(i+1),6)
    for k in range(20):
       y0 =  np.round(float(central.split(',')[-1])+y_side_length*k,6)
       y1 = np.round(float(central.split(',')[-1]) + y_side_length*(k+1),6)

       # grid.append({'1_'+str(i)+'_'+str(k):[x0,y0,x1,y1]})
       grid_dict['1_'+str(i)+'_'+str(k)] = [x0,y0,x1,y1]


for i in range(20):
    # x0_y0 = central
    x0 = np.round(float(central.split(',')[0]) - x_side_length * (i + 1), 6)
    x1 = np.round(float(central.split(',')[0])-x_side_length*i,6)
    for k in range(20):
       y0 =  np.round(float(central.split(',')[-1])+y_side_length*k,6)
       y1 = np.round(float(central.split(',')[-1]) + y_side_length*(k+1),6)

       # grid.append({'1_'+str(i)+'_'+str(k):[x0,y0,x1,y1]})
       grid_dict['2_'+str(i)+'_'+str(k)] = [x0,y0,x1,y1]


for i in range(20):
    # x0_y0 = central
    x1 = np.round(float(central.split(',')[0])-x_side_length*i,6)
    x0 = np.round(float(central.split(',')[0])-x_side_length*(i+1),6)
    for k in range(20):
       y1 =  np.round(float(central.split(',')[-1])-y_side_length*k,6)
       y0 = np.round(float(central.split(',')[-1])-y_side_length*(k+1),6)

       # grid.append({'1_'+str(i)+'_'+str(k):[x0,y0,x1,y1]})
       grid_dict['3_'+str(i)+'_'+str(k)] = [x0,y0,x1,y1]

for i in range(20):
    # x0_y0 = central
    x0 = np.round(float(central.split(',')[0])+x_side_length*i,6)
    x1 = np.round(float(central.split(',')[0])+x_side_length*(i+1),6)
    for k in range(20):
       y1 =  np.round(float(central.split(',')[-1])-y_side_length*k,6)
       y0 = np.round(float(central.split(',')[-1]) - y_side_length*(k+1),6)

       # grid.append({'1_'+str(i)+'_'+str(k):[x0,y0,x1,y1]})
       grid_dict['4_'+str(i)+'_'+str(k)] = [x0,y0,x1,y1]
# print(grid)
# print(grid_dict)
grid_json = json.dumps(grid_dict, indent=3, ensure_ascii=False)
with open('grid_json.json', 'w') as f:
    f.write(grid_json)