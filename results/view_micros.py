from pymks.tools import draw_concentrations
from scipy.io import loadmat

micros = loadmat('data_more_step_4000.mat')['data']

for m in micros:
    draw_concentrations(m[None])

