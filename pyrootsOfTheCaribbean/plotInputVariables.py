import os
import sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import optparse
# local imports
filedir = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.dirname(filedir)
sys.path.append(basedir)

import utils.generateJTcut as JTcut

from evaluationScripts.plotVariables import variablePlotter

usage="usage=%prog [options] \n"
usage+="USE: python plotInputVariables.py -i DIR -o DIR -v FILE  --ksscore --scalesignal=OPTION --lumiscale=FLOAT --ratio --ratiotitel=STR --privatework --log"

parser = optparse.OptionParser(usage=usage)

parser.add_option("-o", "--outputdirectory", dest="outputDir",default="plots_InputFeatures",
        help="DIR for output", metavar="outputDir")

parser.add_option("-i", "--inputdirectory", dest="inputDir",default="InputFeatures",
        help="DIR for input", metavar="inputDir")

parser.add_option("-n", "--naming", dest="naming",default="_dnn.h5",
        help="file ending for the samples in preprocessing", metavar="naming")

parser.add_option("-v", "--variableselection", dest="variableSelection",default="example_variables",
        help="FILE for variables used to train DNNs", metavar="variableSelection")

parser.add_option("-l", "--log", dest="log", action = "store_true", default=False,
        help="activate for logarithmic plots", metavar="log")

parser.add_option("-p", "--privatework", dest="privateWork", action = "store_true", default=False,
        help="activate Private Work option", metavar="privateWork")

parser.add_option("-r", "--ratio", dest="ratio", action = "store_true", default=False,
        help="activate ratio plot", metavar="ratio")

parser.add_option("--ratiotitle", dest="ratioTitle", default="#frac{signal}{background}",
        help="STR #frac{PROCESS}{PROCESS}", metavar="title")

parser.add_option("-k", "--ksscore", dest="KSscore", action = "store_true", default=False,
        help="activate KSscore", metavar="KSscore")

parser.add_option("-s", "--scalesignal", dest="scaleSignal", default=-1,
        help="-1 to scale Signal to background Integral, FLOAT to scale Signal with float value, False to not scale Signal",
        metavar="scaleSignal")

parser.add_option("--lumiscale", dest="lumiScale", default=41.5,
        help="FLOAT to scale Luminosity", metavar="lumiScale")

parser.add_option("--corr",dest="correlationMatrix",default=False,action="store_true",
        help="activate plotting of correlation matrix")

(options, args) = parser.parse_args()

#import Variable Selection
if not os.path.isabs(options.variableSelection):
    sys.path.append(basedir+"/variable_sets/")
    variable_set = __import__(options.variableSelection)
elif os.path.exists(options.variableSelection):
    variable_set = __import__(options.variableSelection)
else:
    sys.exit("ERROR: Variable Selection File does not exist!")

#get input directory path
if not os.path.isabs(options.inputDir):
    data_dir = basedir+"/workdir/"+options.inputDir
elif os.path.exists(options.inputDir):
    data_dir=options.inputDir
else:
    sys.exit("ERROR: Input Directory does not exist!")

#get output directory path
if not os.path.isabs(options.outputDir):
    plot_dir = basedir+"/workdir/"+options.outputDir
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
else: 
    plot_dir=options.outputDir
    if not os.path.exists(options.outputDir):
        os.makedirs(plot_dir)
   

# plotting options
plotOptions = {
    "ratio":        options.ratio,
    "ratioTitle":   options.ratioTitle,
    "logscale":     options.log,
    "scaleSignal":  float(options.scaleSignal),
    "lumiScale":    float(options.lumiScale),
    "KSscore":      options.KSscore,
    "privateWork":  options.privateWork,
    }
"""
   scaleSignal:
   -1:     scale to background Integral
   float:  scale with float value
   False:  dont scale
"""

# additional variables to plot
additional_variables = [
    ]

# variables that are not plotted
ignored_variables = [
    "Weight_XS",
    "Weight_GEN_nom",
    ]


# initialize plotter
plotter = variablePlotter(
    output_dir      = plot_dir,
    variable_set    = variable_set,
    add_vars        = additional_variables,
    ignored_vars    = ignored_variables,
    plotOptions     = plotOptions
    )

naming = options.naming
# add signal samples
plotter.addSample(
    sampleName      = "tt+Z",
    sampleFile      = data_dir+"/ttZ"+naming,
    plotColor       = ROOT.kOrange+7,
    signalSample    = True)

# add background samples
#samples temporarily removed for binary correlation
plotter.addSample(
    sampleName      = "tt+bb",
    sampleFile      = data_dir+"/ttbb"+naming,
    plotColor       = ROOT.kAzure+3)

plotter.addSample(
    sampleName      = "tt+cc",
    sampleFile      = data_dir+"/ttcc"+naming,
    plotColor       = ROOT.kAzure+8)

plotter.addSample(
    sampleName      = "tt+lf",
    sampleFile      = data_dir+"/ttlf"+naming,
    plotColor       = ROOT.kAzure-9)

plotter.addSample(
    sampleName      = "tt+H",
    sampleFile      = data_dir+"/ttH"+naming,
    plotColor       = ROOT.kRed+1,
    signalSample    = True)


# add JT categories
#plotter.addCategory("ge6j_ge3t")
#plotter.addCategory("5j_ge3t")
#plotter.addCategory("4j_ge3t")
plotter.addCategory("ge4j_3t")
plotter.addCategory("ge4j_ge4t")


# perform plotting routine
plotter.plot(saveKSValues = options.KSscore, plotCorrelationMatrix = options.correlationMatrix)


''' hopeless attempt to display difference in correlations of ttZ and ttH
# initialize plotter
plotter2 = variablePlotter(
    output_dir      = plot_dir+"_ttHonly",
    variable_set    = variable_set,
    add_vars        = additional_variables,
    ignored_vars    = ignored_variables,
    plotOptions     = plotOptions
    )

plotter2.addSample(
    sampleName      = "tt+H",
    sampleFile      = data_dir+"/ttH"+naming,
    plotColor       = ROOT.kRed+1,
    signalSample    = True)

# add JT categories
plotter2.addCategory("ge6j_ge3t")
plotter2.addCategory("5j_ge3t")
plotter2.addCategory("4j_ge3t")

#plotter.corr_histo.SaveAs(basedir+"/workdir/corr_hist1.root")
#plotter2.corr_histo.SaveAs(basedir+"/workdir/corr_hist2.root")

# perform plotting routine
plotter2.plot(saveKSValues = options.KSscore, plotCorrelationMatrix = options.correlationMatrix)


def plot_correlation_diff(categories=["ge6j_ge3t", "5j_ge3t", "4j_ge3t"]):
    for cat in categories:
        histfile = ROOT.TFile(plot_dir+"_ttHonly/"+cat+"_correlations.root")
        hist1 = ROOT.TH2D()
        hist1.Scale(10)
        histfile.GetObject("correlationMatrix", hist1)
        histfile2 = ROOT.TFile(plot_dir+"_ttZonly/"+cat+"_correlations.root")
        hist2 = ROOT.TH2D()
        histfile2.GetObject("correlationMatrix", hist2)
        #hist1.Add(hist2, -10.)
        
        # init canvas
        canvas = ROOT.TCanvas("", "", 5000, 5000)
        canvas.SetTopMargin(0.1)
        canvas.SetBottomMargin(0.3)
        canvas.SetRightMargin(0.12)
        canvas.SetLeftMargin(0.3)
        canvas.SetTicks(1,1)
        
        # draw histogram
        ROOT.gStyle.SetPalette(ROOT.kRedBlue)
        draw_option = "colz text1"
        hist1.DrawCopy(draw_option)

        # setup TLatex
        latex = ROOT.TLatex()
        latex.SetNDC()
        latex.SetTextColor(ROOT.kBlack)
        latex.SetTextSize(0.03)

        l = canvas.GetLeftMargin()
        t = canvas.GetTopMargin()

        # add category label
        latex.DrawLatex(l+0.001,1.-t+0.01, JTcut.getJTlabel(cat))
        
        canvas.SaveAs(plot_dir+"/"+cat+"_correlations_diff.pdf")
        
plot_correlation_diff() '''
