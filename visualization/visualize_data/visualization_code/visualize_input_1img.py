
'''
overlaps 10.000 input pictures and draws one picture for every rotation type
'''

# imports
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.gridspec as gridspec



def do_plot(mylist, path, labels):
	# plots the overlapping input pictures

	# set norm for histogram
	norm = cm.colors.Normalize(vmax=0, vmin=1) 
	cmap = plt.cm.Purples

	# set size of canvas
	f = plt.figure(figsize=(8., 6.)) 

	grid = gridspec.GridSpec(100, 3, wspace=.3, width_ratios=[15,15,1])
	
	# first channel
	ax=f.add_subplot(grid[:,0])
	ax.set_xlabel('$\\eta$', size=8)
	ax.set_ylabel('$\\phi$', size=8, rotation=0)
	ax.set_title('Jet_Pt')
	ax.imshow(mylist[0], cmap=cmap, vmin=0, vmax=1, extent=[-2.2, 2.2, -np.pi, np.pi])
	'''
	# second channel
	ax=f.add_subplot(grid[:,1])
	ax.set_xlabel('$\\eta$', size=8)
	ax.set_ylabel('$\\phi$', size=8, rotation=0)
	ax.set_title('TaggedJet_Pt')
	ax.imshow(mylist[1], cmap=cmap, vmin=0, vmax=1, extent=[-2.2, 2.2, -np.pi, np.pi])
	'''
	# third channel
	ax=f.add_subplot(grid[:,1])
	ax.set_xlabel('$\\eta$', size=8)
	ax.set_ylabel('$\\phi$', size=8, rotation=0)
	ax.set_title('Jet_CSV')
	ax.imshow(mylist[2], cmap=cmap, vmin=0, vmax=1, extent=[-2.2, 2.2, -np.pi, np.pi])
	
	# create colorbar
	cbar_ax = f.add_subplot(grid[11:89,2])
	mpl.colorbar.ColorbarBase(cbar_ax, cmap=cmap, norm=norm)

	# save figure
	#plt.suptitle('Overlapping Input Images ttH', size= 12)
	plt.savefig(path+'image_CSV_'+ sample +'.png')
	plt.show()


# set paths
path = '../input_images/'
sample = 'ttH'


rawInputImages = eval(open(path + '3ch_img_' + sample + '.txt', 'r').read())
inputImage = rawInputImages[0]
maxVal = np.asarray(inputImage[0]).max()
for i in range(3):
	inputImage[i] = np.flip(np.swapaxes(np.asarray(inputImage[i]), 0, 1), axis=0)
	print inputImage[i]
	if i != 2:
		for row in inputImage[i]:
			for j in range(11):
				row[j] = row[j]/maxVal
	print inputImage[i]
	print '\n'




do_plot(inputImage, path, sample)







