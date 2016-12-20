from pymks.tools import draw_coeff
from os import listdir
from scipy.io import loadmat

print 'initial coeff'
coeff_files = sorted([f for f in listdir('.') if f[:5] == 'coef_'])
for f in coeff_files:
    coeff = loadmat(f)['coef_'][..., 1::2]
    draw_coeff(coeff)

print 'middle coeff'
middle_coeff = sorted([f for f in listdir('.') if f[:5] == 'middl'])
for f in middle_coeff:
    coeff = loadmat(f)['coef_'][..., 1::2]
    draw_coeff(coeff)


print 'diff in coeff'
for fi, fm in zip(coeff_files, middle_coeff):
    coeff = loadmat(fi)['coef_'][..., 1::2]
    m_coeff = loadmat(fm)['coef_'][..., 1::2]
    draw_coeff(coeff - m_coeff)
