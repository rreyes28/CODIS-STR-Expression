##STR MEM VALUES##
#Note: Each section is separated by the dashed line comments
    
#--------------------#
#ACCESSING TOOLKITS
#Import matplotlib, pandas, and ImageGrid in order to run code
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
from mpl_toolkits.axes_grid1 import ImageGrid 
import pandas as pd

#--------------------#
#list of STRs
## SF1PO, D1S1656, D2S441, D2S1338, D3S1358, D5S818, D7S820, 
## D8S1179, D10S1248, D12S391, D13S317, D18S51, D19S433,
## D22S1045, FGA, TH01, TPOX, vWA

#--------------------#
#PLOT CREATION#
#For each STR: import CSV file, create plot with labeled title and axes, and save the figure as a PNG file
#Note: the x-axis label may show a box as the name, but it will show up as the Mem Value sign in the plot

#CSF1PO
CSF1PO = pd.read_csv('CSF1PO_Mem_Genotypes.txt', sep='\t')

CSF1PO.plot(kind='hist', bins=15, color='#A13647', rwidth=0.9, legend=False)
plt.title('CSF1PO', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('CSF1PO.png')


#D1S1656
D1S1656 = pd.read_csv('D1S1656_Mem_Genotypes.txt', sep='\t')

D1S1656.plot(kind='hist', bins=15, color='#763DB8', rwidth=0.9, legend=False)
plt.title('D1S1656', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D1S1656.png')


#D2S441
D2S441 = pd.read_csv('D2S441_Mem_Genotypes.txt', sep='\t')

D2S441.plot(kind='hist', bins=15, color='#8EC44F', rwidth=0.9, legend=False)
plt.title('D2S441', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D2S441.png')

#D2S1338
D2S1338 = pd.read_csv('D2S1338_Mem_Genotypes.txt', sep='\t')

D2S1338.plot(kind='hist', bins=15, color='#246020', rwidth=0.9, legend=False)
plt.title('D2S1338', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D2S1338.png')

#D3S1358
D3S1358 = pd.read_csv('D3S1358_Mem_Genotypes.txt', sep='\t')

D3S1358.plot(kind='hist', bins=15, color='#283E77', rwidth=0.9, legend=False)
plt.title('D3S1358', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D3S1358.png')

#D5S818
D5S818 = pd.read_csv('D5S818_Mem_Genotypes.txt', sep='\t')

D5S818.plot(kind='hist', bins=15, color='#8A602E', rwidth=0.9, legend=False)
plt.title('D5S818', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D5S818.png')

#D7S820
D7S820 = pd.read_csv('D7S820_Mem_Genotypes.txt', sep='\t')

D7S820.plot(kind='hist', bins=15, color='#322311', rwidth=0.9, legend=False)
plt.title('D7S820', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D7S820.png')

#D8S1179
D8S1179 = pd.read_csv('D8S1179_Mem_Genotypes.txt', sep='\t')

D8S1179.plot(kind='hist', bins=15, color='#191339', rwidth=0.9, legend=False)
plt.title('D8S1179', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D8S1179.png')

#D10S1248
D10S1248 = pd.read_csv('D10S1248_Mem_Genotypes.txt', sep='\t')

D10S1248.plot(kind='hist', bins=15, color='#D2797C', rwidth=0.9, legend=False)
plt.title('D10S1248', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D10S1248.png')

#D12S391
D12S391 = pd.read_csv('D12S391_Mem_Genotypes.txt', sep='\t')

D12S391.plot(kind='hist', bins=15, color='#9AC6DB', rwidth=0.9, legend=False)
plt.title('D12S391', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D12S391.png')

#D13S317
D13S317 = pd.read_csv('D13S317_Mem_Genotypes.txt', sep='\t')

D13S317.plot(kind='hist', bins=15, color='#494618', rwidth=0.9, legend=False)
plt.title('D13S317', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D13S317.png')

#D18S51
D18S51 = pd.read_csv('D18S51_Mem_Genotypes.txt', sep='\t')

D18S51.plot(kind='hist', bins=15, color='#49181A', rwidth=0.9, legend=False)
plt.title('D18S51', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D18S51.png')

#D19S433
D19S433 = pd.read_csv('D19S433_Mem_Genotypes.txt', sep='\t')

D19S433.plot(kind='hist', bins=15, color='#A45A37', rwidth=0.9, legend=False)
plt.title('D19S433', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D19S433.png')

#D22S1045
D22S1045 = pd.read_csv('D22S1045_Mem_Genotypes.txt', sep='\t')

D22S1045.plot(kind='hist', bins=15, color='#D071D0', rwidth=0.9, legend=False)
plt.title('D22S1045', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('D22S1045.png')

#FGA
FGA = pd.read_csv('FGA_Mem_Genotypes.txt', sep='\t')

FGA.plot(kind='hist', bins=15, color='#2E688A', rwidth=0.9, legend=False)
plt.title('FGA', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('FGA.png')

#TH01
TH01 = pd.read_csv('TH01_Mem_Genotypes.txt', sep='\t')

TH01.plot(kind='hist', bins=15, color='#62246B', rwidth=0.9, legend=False)
plt.title('TH01', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('TH01.png')

#TPOX
TPOX = pd.read_csv('TPOX_Mem_Genotypes.txt', sep='\t')

TPOX.plot(kind='hist', bins=15, color='#000080', rwidth=0.9, legend=False)
plt.title('TPOX', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('TPOX.png')

#vWA
vWA = pd.read_csv('vWA_Mem_Genotypes.txt', sep='\t')

vWA.plot(kind='hist', bins=15, color='#BFAC40', rwidth=0.9, legend=False)
plt.title('vWA', size=18)
plt.xlabel("𐡌", size=15, name='Noto Sans Imperial Aramaic',
              fontweight='bold')
plt.ylabel('Number of Individuals', size = 15)
plt.savefig('vWA.png')

#--------------------#
#PLOTTING PNGs IN GRID#
#Read in each png as an image
im1 = mpimg.imread('CSF1PO.png') 
im2 = mpimg.imread('D1S1656.png')
im3 = mpimg.imread('D2S441.png')
im4 = mpimg.imread('D2S1338.png')
im5 = mpimg.imread('D3S1358.png')
im6 = mpimg.imread('D5S818.png')
im7 = mpimg.imread('D7S820.png')
im8 = mpimg.imread('D8S1179.png')
im9 = mpimg.imread('D10S1248.png')
im10 = mpimg.imread('D12S391.png')
im11 = mpimg.imread('D13S317.png')
im12 = mpimg.imread('D18S51.png')
im13 = mpimg.imread('D19S433.png')
im14 = mpimg.imread('D22S1045.png')
im15 = mpimg.imread('FGA.png')
im16 = mpimg.imread('TH01.png')
im17 = mpimg.imread('TPOX.png')
im18 = mpimg.imread('vWA.png')

#Create grid space to put images in
fig = plt.figure(figsize=(50., 50.))
grid = ImageGrid(fig, 121,
                 nrows_ncols=(6, 3), 
                 axes_pad=0.1,
                 share_all=True)

grid[0].get_yaxis().set_ticks([])
grid[3].get_xaxis().set_ticks([])

#Add each image into the grid
for ax, im in zip(grid, [im1, im2, im3, im4, im5, im6, im7, 
                         im8, im9, im10, im11, im12, im13, im14, 
                         im15, im16, im17, im18]):
    ax.imshow(im)

#View full grid of STR mem values
plt.show()

