import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

import matplotlib
matplotlib.use('Tkagg')


import matplotlib as mpl
mpl.rc('font',**{'family':'sans-serif', 'serif':['Computer Modern Serif'],'sans-serif':['Helvetica'], 'size':15,'weight':'bold'})
mpl.rc('axes',**{'labelweight':'bold', 'linewidth':2.0})
mpl.rc('ytick',**{'major.pad':22, 'color':'k'})
mpl.rc('xtick',**{'major.pad':10,})
mpl.rc('mathtext',**{'default':'regular','fontset':'cm','bf':'monospace:bold'})
mpl.rc('text', **{'usetex':True})
mpl.rc('text.latex',preamble=r'\usepackage{cmbright},\usepackage{relsize},'+r'\usepackage{upgreek}, \usepackage{amsmath}')
mpl.rc('contour', **{'negative_linestyle':'solid'})

def FormatLabel(LabelsX):
    LabelsX = np.array(LabelsX)
    Diff=np.mean(np.diff(LabelsX))
    if min(abs(LabelsX))<10.0 and min(abs(LabelsX))>0.001:
        LabelStr = ["%.2f" %(Value) for Value in LabelsX]
    elif min(abs(LabelsX))<1000 and min(abs(LabelsX))>1:
        LabelStr = ["%.0d" %(Value) for Value in LabelsX]
    else:
        LabelStr = ["%.2e" %(Value) for Value in LabelsX]
    return LabelStr


def CustomCornerPlot(Data, Parameters):

    NDim = len(Data)
    FigDim = NDim*2.5

    if len(Parameters)>0:
        try:
          assert len(Parameters) == NDim
        except:
          raise("The number of should match the dimension of the data provided.")


    fig, ax = plt.subplots(NDim, NDim, figsize=(FigDim, FigDim), dpi=80)


    for i in range(NDim):
        for j in range(NDim):
            if j<i:

                NBins = 20
                counts,xbins,ybins=np.histogram2d(Data[i,:], Data[j,:],bins=NBins)
                Levels = np.percentile(counts,[68,96,99])

                labels = np.round(np.linspace(min(xbins), max(xbins),6),2)

                #good options for colormap are gist_earth_r, gray_r
                ax[i,j].hist2d(Data[i,:], Data[j,:], cmap='gist_earth_r', bins = 2*NBins)#, norm=PowerNorm(gamma=0.5))
                ax[i,j].contour(counts.transpose(),Levels,extent=[xbins.min(),xbins.max(),
                    ybins.min(),ybins.max()],linewidths=2,cmap="gray",
                    linestyles='-')


                #Format the labels
                NumLabels = 5
                StepSizeX = (max(xbins) - min(xbins))/NumLabels
                StepSizeY = (max(ybins) - min(ybins))/NumLabels

                LabelsX = np.linspace(min(xbins)+StepSizeX, max(xbins)-StepSizeX, NumLabels)
                LabelsXStr = FormatLabel(LabelsX)

                LabelsY = np.linspace(min(ybins)+StepSizeY, max(ybins)-StepSizeY, NumLabels)
                LabelsYStr = FormatLabel(LabelsX)

                ax[i,j].set_xticks(LabelsX)
                ax[i,j].set_xticklabels(LabelsXStr, rotation=45)
                ax[i,j].set_xlim(min(xbins), max(xbins))

                ax[i,j].set_yticks(LabelsY)
                ax[i,j].set_yticklabels(LabelsYStr, rotation=45)
                ax[i,j].set_ylim(min(ybins), max(ybins))

                ax[i,j].tick_params(which="both", pad=5)


            elif i==j:
                ax[i,j].hist(Data[i,:], fill=False, histtype='step', linewidth=2, color="navy", normed=True)
                PercentileValues = np.percentile(Data[i,:],[15.8, 50.0, 84.2])
                for counter_pc, Value in enumerate(PercentileValues):
                    if counter_pc == 1:
                            ax[i,j].axvline(x=Value, color="red",  lw=1.5)
                    else:
                            ax[i,j].axvline(x=Value, color="cyan",  linestyle="--", lw=2.5)

                #assign the title
                Median = PercentileValues[1]

                if Median<100 and Median>0.001:
                    MedianStr = "%0.2f" %Median
                else:
                    MedianStr = "%0.2e" %Median

                UpperError = PercentileValues[2] - PercentileValues[1]
                if UpperError<100 and UpperError>0.001:
                    UpperErrorStr = "%0.2f" %UpperError
                else:
                    UpperErrorStr = "%0.2e" %UpperError

                LowerError = PercentileValues[1] - PercentileValues[0]
                if LowerError<100 and LowerError>0.001:
                    LowerErrorStr = "%0.2f" %LowerError
                else:
                    LowerErrorStr = "%0.2e" %LowerError

                Title = Parameters[i]+ " = %s$^{+%s}_{-%s}$" %(MedianStr, UpperErrorStr, LowerErrorStr)
                print(Title)
                ax[i,j].set_title(Title)

            else:
                ax[i,j].set_visible(False)


            #Now for the ylabels
            if j!=0 or i==j:
                ax[i,j].set_yticklabels([])


            #Now for the xlabels
            if i!=NDim-1 or i==j:
                ax[i,j].set_xticklabels([])


            #assign the title

            #

    plt.subplots_adjust(wspace=0.025, hspace=0.025, left = 0.05,
    right = 0.95, bottom = 0.05, top = 0.95)
    plt.savefig("Trial.png")
    plt.savefig("Trial.pdf", format='pdf')
    plt.show()


def MultipleCustomCornerPlot(Data1, Data2, Parameters):

    NDim = len(Data1)
    assert len(Data2) == NDim
    FigDim = NDim*2.5

    if len(Parameters)>0:
        try:
          assert len(Parameters) == NDim
        except:
          raise("The number of should match the dimension of the data provided.")


    fig, ax = plt.subplots(NDim, NDim, figsize=(FigDim, FigDim), dpi=80)


    for i in range(NDim):
        for j in range(NDim):
            if j<i:

                NBins = 20
                counts,xbins,ybins=np.histogram2d(Data[i,:], Data[j,:],bins=NBins)
                Levels = np.percentile(counts,[68,96,99])

                labels = np.round(np.linspace(min(xbins), max(xbins),6),2)

                #good options for colormap are gist_earth_r, gray_r
                ax[i,j].hist2d(Data1[i,:], Data1[j,:], cmap='gist_earth_r', bins = 2*NBins)#, norm=PowerNorm(gamma=0.5))
                ax[i,j].hist2d(Data2[i,:], Data2[j,:], cmap='gray_r', bins = 2*NBins)#, norm=PowerNorm(gamma=0.5))

                ax[i,j].contour(counts.transpose(),Levels,extent=[xbins.min(),xbins.max(),
                    ybins.min(),ybins.max()],linewidths=2,cmap="gray",
                    linestyles='-')


                #Format the labels
                NumLabels = 5
                StepSizeX = (max(xbins) - min(xbins))/NumLabels
                StepSizeY = (max(ybins) - min(ybins))/NumLabels

                LabelsX = np.linspace(min(xbins)+StepSizeX, max(xbins)-StepSizeX, NumLabels)
                LabelsXStr = FormatLabel(LabelsX)

                LabelsY = np.linspace(min(ybins)+StepSizeY, max(ybins)-StepSizeY, NumLabels)
                LabelsYStr = FormatLabel(LabelsX)

                ax[i,j].set_xticks(LabelsX)
                ax[i,j].set_xticklabels(LabelsXStr, rotation=45)
                ax[i,j].set_xlim(min(xbins), max(xbins))

                ax[i,j].set_yticks(LabelsY)
                ax[i,j].set_yticklabels(LabelsYStr, rotation=45)
                ax[i,j].set_ylim(min(ybins), max(ybins))

                ax[i,j].tick_params(which="both", pad=5)


            elif i==j:
                ax[i,j].hist(Data1[i,:], fill=False, histtype='step', linewidth=2, color="navy", normed=True)
                ax[i,j].hist(Data2[i,:], fill=False, histtype='step', linewidth=2, color="maroon", normed=True)
                PercentileValues = np.percentile(Data[i,:],[15.8, 50.0, 84.2])
                for counter_pc, Value in enumerate(PercentileValues):
                    if counter_pc == 1:
                            ax[i,j].axvline(x=Value, color="red",  lw=1.5)
                    else:
                            ax[i,j].axvline(x=Value, color="cyan",  linestyle="--", lw=2.5)

                #assign the title
                Median = PercentileValues[1]

                if Median<100 and Median>0.001:
                    MedianStr = "%0.2f" %Median
                else:
                    MedianStr = "%0.2e" %Median

                UpperError = PercentileValues[2] - PercentileValues[1]
                if UpperError<100 and UpperError>0.001:
                    UpperErrorStr = "%0.2f" %UpperError
                else:
                    UpperErrorStr = "%0.2e" %UpperError

                LowerError = PercentileValues[1] - PercentileValues[0]
                if LowerError<100 and LowerError>0.001:
                    LowerErrorStr = "%0.2f" %LowerError
                else:
                    LowerErrorStr = "%0.2e" %LowerError

                Title = Parameters[i]+ " = %s$^{+%s}_{-%s}$" %(MedianStr, UpperErrorStr, LowerErrorStr)
                print(Title)
                ax[i,j].set_title(Title)

            else:
                ax[i,j].set_visible(False)


            #Now for the ylabels
            if j!=0 or i==j:
                ax[i,j].set_yticklabels([])


            #Now for the xlabels
            if i!=NDim-1 or i==j:
                ax[i,j].set_xticklabels([])


            #assign the title

            #

    plt.subplots_adjust(wspace=0.025, hspace=0.025, left = 0.05,
    right = 0.95, bottom = 0.05, top = 0.95)
    plt.savefig("Trial.png")
    plt.savefig("Trial.pdf", format='pdf')
    plt.show()
