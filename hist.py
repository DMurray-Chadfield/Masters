import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import numpy
from matplotlib.colors import LogNorm
from velociraptor.tools.lines import binned_median_line as bml
import unyt

def plot_hist(x, y, xlabel, ylabel, filepath):
    pyplot.rcParams.update({'font.size':40})

    fig, ax = pyplot.subplots(figsize = (20,20))

    x_bins = numpy.logspace(numpy.log10(numpy.amin(x)), numpy.log10(numpy.amax(x)), num = 50)
    bins = unyt.unyt_array(numpy.logspace(numpy.log10(numpy.amin(x)), numpy.log10(numpy.amax(x)), num = 20), units = x.units)
    y_bins = numpy.logspace(numpy.log10(numpy.amin(y)), numpy.log10(numpy.amax(y)), num = 50)
    h = ax.hist2d(x, y, bins = [x_bins, y_bins], norm = LogNorm())
    pyplot.colorbar(h[3], ax=ax)

    ax.loglog()
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

    ax.tick_params(which = 'both', direction = 'in')
    ax.tick_params(length = 10, width = 2)

    centers, med, err = bml(x, y, x_bins = bins)
    ax.plot(centers, med, linestyle = '--', linewidth = 7, color = 'red')

    fig.savefig(filepath)

def lin_hist(x, y, xlabel, ylabel, filepath, num):
    pyplot.rcParams.update({'font.size':40})

    fig, ax = pyplot.subplots(figsize = (20,20))

    x_bins = numpy.linspace(numpy.amin(x), numpy.amax(x), num = num)
    #bins = unyt.unyt_array(numpy.amin(x), numpy.amax(x), num = 20), units = x.units)
    y_bins = numpy.linspace(numpy.amin(y), numpy.amax(y), num = num)
    h = ax.hist2d(x, y, bins = [x_bins, y_bins], norm = LogNorm())
    pyplot.colorbar(h[3], ax=ax)

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)

    ax.tick_params(which = 'both', direction = 'in')
    ax.tick_params(length = 10, width = 2)

    #centers, med, err = bml(x, y, x_bins = bins)
    #ax.plot(centers, med, linestyle = '--', linewidth = 7, color = 'red')

    fig.savefig(filepath)