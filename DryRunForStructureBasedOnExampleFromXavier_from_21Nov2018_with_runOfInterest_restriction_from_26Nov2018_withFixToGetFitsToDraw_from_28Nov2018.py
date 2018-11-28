import ROOT
import math
import sys
#import FWCore.ParameterSet.Config as cms

#from FWCore.ParameterSet.VarParsing import VarParsing

#options = VarParsing ('python')

#options.register('defaults', '',
 #   VarParsing.multiplicity.singleton,
  #  VarParsing.varType.string,
   # 'baseline default settings to be used')
#options.register('inputFile', '',
 #   VarParsing.multiplicity.singleton,
  #  VarParsing.varType.string,
#"Path to input X tree and the name of the X tree, e.g. <path to file>/fileName.root"
#)

#Trying my original idea because this Var Parsing is not going well

from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('--inputFile', default='/isilon/hadoop/store/user/mhadley/Cosmics2017E/crab_2017E_Cosmics/181028_212128/0000/test_shallowGeneralProducer_30.root', help='Provide path to inputFile and the name of the inputFile, e.g. <path to inputFile>/inputFile.root')
args = vars(parser.parse_args())
inputFile = ROOT.TFile(args["inputFile"])
print 'inputFile is:', inputFile
almostFileName1 = str(inputFile)
print almostFileName1
almostFileName2 = almostFileName1.split('_')
print 'almostFileName2 is:', almostFileName2

print 'amostFileName2[0] is:', almostFileName2[0]
print 'almostFileName2[1] is:', almostFileName2[1]
print 'almostFileName2[5] is:', almostFileName2[5]
almostFileName3 =  almostFileName2[5]
print (str(almostFileName3).split('.'))
almostFileName4 = (str(almostFileName3).split('.'))
print almostFileName4
almostFileName5 = (almostFileName4[0])
print almostFileName5
number = str(almostFileName5)
print number
###Mess related to trying to use VarParsing like BTA cfg file
#inputFile = ROOT.TFile("$PWD/test_shallowGeneralProducer_30.root") #Now from 2017E Cosmics after an unplanned dump
#print options.inputFile
#inputFile = ROOT.TFile(options.inputFile)
#print 'inputFile is:', inputFile

#### end mess


t = inputFile.Get("testTree/tree")

#almostFileName1 = str(f)
#print 'almostFileName1 is:', almostFileName1
#almostFileName2 = almostFileName1.split('_')
#print 'almostFileName2 is:', almostFileName2
#print 'almostFileName2[0] is:', almostFileName2[0]
#print 'amostFileName2[1] is:', almostFileName2[1]
#print 'almostFileName2[12] is:', almostFileName2[12]
#print 'almostFileName2[13] is:', almostFileName2[13]
#print almostFileName2[13].split()
#almostFileName3 = almostFileName2[13].split()
#print 'almostFileName3[0] is:',  almostFileName3[0]
#almostFileName4 = str(almostFileName3[0])
#print almostFileName4
#print almostFileName4.split('.')
#almostFileName5 = almostFileName4.split('.')
#print 'almostFileName5 is:', almostFileName5
#print 'almostFilename5[0] is:', almostFileName5[0]
#number = str(almostFileName5[0])
#print number

fileName = 'test_shallowGeneralProducer_' + number
print 'fileName is:', fileName
#almostFileName5 = almostFileName4[:2]
#print almostFileName5


#almostFileName4 = (str(almostFileName3)).split('.')
#print almostFileName4[0]
#almostFileName5 = str(almostFileName4[0])
#print almostFileName5
#print almostFileName5.split('[')
#almostFileName6 = almostFileName5.split('[')
#almostFileName7 = almostFileName6[1]
#print almostFileName7
#print (str(almostFileName7))
#almostFileName8 = (str(almostFileName7))
#print almostFileName8.split(" ' ")
#print almostFileName8[0]
#print almostFileName8[1]
#print str(almostFileName4[0])
#almostFileName5 = str(almostFileName4[0])
#print 'almostFileName5 is:', almostFileName5
#print almostFileName5.split(" ' ")
#almostFileName6 = almostFileName5.split(" ' ")
#print almostFileName6[0]

#t.Print()


##Define some histograms
#h_ston_vs_time = ROOT.TH1F("ston_vs_time", "Signal to Noise vs. Time; Time (Lumi Sections); STON ", 1005, -5, 1000)
h_nclusters_vs_time = ROOT.TH1F("nclusters_vs_time", "nClusters vs. Time for %s; Time (Lumi Sections); nClusters"%(fileName), 1005, -5, 1000) #For the whole strips tracker
h_nclusters_vs_time_tid = ROOT.TH1F("nclusters_vs_time_tid", "nClusters vs. Time in the TID for %s; Time (Lumi Sections); nClusters" %(fileName), 1005, -5, 1000) # for TID
h_nclusters_vs_time_tec = ROOT.TH1F("nclusters_vs_time_tec", "nClusters vs. Time in the TEC for %s; Time (Lumi Sections); nClusters" %(fileName), 1005, -5, 1000) # for TEC


print "Got here after histo definitions!"

#Define some fitting functions

def my_expo(x,par):
    expo = math.exp((par[0]) + (par[1]) * (x[0]))
    return expo

print "Ok 7 got here after defining my expo"
    
def my_sum_of_two_expo(x,par):
    sum_of_two_expo = (math.exp((par[0]) + (par[1]) * (x[0]))) + (math.exp((par[2]) + (par[3]) * (x[0])))
    return sum_of_two_expo

print "Ok 8 got here after defining my_sum_of_two_expo"

def my_sum_of_three_expo(x,par):
    sum_of_three_expo = (math.exp((par[0]) + (par[1]) * (x[0]))) + (math.exp((par[2]) + (par[3]) * (x[0]))) + (math.exp((par[4]) + (par[5]) * (x[0])))
    return sum_of_three_expo

print "Ok 8 got here after defining my_sum_of_three_expo"

fit_one_expo = ROOT.TF1("fit_one_expo", my_expo, 0, 1000, 2)  #FIX ME RE: 0,1000
fit_two_expo = ROOT.TF1("fit_two_expo", my_sum_of_two_expo, 0,1000,4)
fit_three_expo = ROOT.TF1("fit_three_expo", my_sum_of_three_expo, 0, 1000, 6)
print "At fit_one_expo, fit_two_expo, fit_three_expo, I am ok"

fit_one_expo_tid = ROOT.TF1("fit_one_expo_tid", my_expo, 0, 1000, 2)
fit_two_expo_tid = ROOT.TF1("fit_two_expo_tid", my_sum_of_two_expo, 0, 1000, 4)
fit_three_expo_tid = ROOT.TF1("fit_three_expo_tid", my_sum_of_three_expo, 0, 1000, 6)
print "At fit_one_expo_tid, fit_two_expo_tid, fit_three_expo_tid, I am ok"

fit_one_expo_tec = ROOT.TF1("fit_one_expo_tec", my_expo, 0, 1000, 2)
fit_two_expo_tec = ROOT.TF1("fit_two_expo_tec", my_sum_of_two_expo, 0, 1000, 4)
fit_three_expo_tec = ROOT.TF1("fit_three_expo_tec", my_sum_of_three_expo, 0, 1000, 6)

print "At_fit_one_expo_tec, fit_two_expo_tec, fit_three_expo_tec, I am ok!"

print "Ok 9 got here after defining the fit_N_expo* where N = 1,2,3 and * is either nothing (whole tracker stuff) or _tid (tid stuff) or _tec (tec stuff)"
    
##Define some parameters that we can toggle as we want

#NumOfLumisThatWeCallItInteresting = 10
#I'm skeptical about this, I need to double check with Xavier, I think this is the wrong interpretation of event.lumi here

stonCut = 10 #To be fiddled with
for iev, event in enumerate(t,1):
    print "POODLES! run:", event.run
    runOfInterest = event.run
    
    if iev !=0:
        break
print "runOfInterest is:", runOfInterest
for iev, event in enumerate(t,1):
    #print "#################################"
    #print "run:", event.run, "lumi:", event.lumi, "event:", event.event
    #print "Number of clusters:", event.clustereta.size() #Didn't necessarily have to use clustereta.size, could have used cluster<somethingelse>.size, just being consistent with what Xavier did to make things easy

#print "####################################"
#print 'Total number of events is:', iev
    
 #   if event.lumi > minNumOfLumisThatWeCallItInteresting:
  #      print 'INTERESTING EVENT'
    if event.run == runOfInterest: #305090:
        for cluster in range(event.clustereta.size()):
            if event.clusterston[cluster] > stonCut:
                continue
            #print 'STON:', event.clusterston[cluster] 
            #h_ston_vs_time.AddBinContent(event.lumi, event.clusterston[cluster])
            h_nclusters_vs_time.AddBinContent(event.lumi, 1)
            if event.clustersubdetid[cluster] == 4: #4 is the TID
                #print 'event.clustersubdetid[cluster]', event.clustersubdetid[cluster] 
                h_nclusters_vs_time_tid.AddBinContent(event.lumi,1)     
                #print "Ok 2 got here to fill TID histo"
            if event.clustersubdetid[cluster] == 6: #6 is the TEC
                #print "Ok 3 got here to fill TEC histo"
                h_nclusters_vs_time_tec.AddBinContent(event.lumi,1)
#    if iev > 15000:
#        break
##Just here to speed up testing Actually ok don't use this ever it causes the fits to fail!!
###############################
#####################
##Some extra stuff here
#Event Info Plots (for future matching of consecutive runs)
#h_runnum = ROOT.TH1F("runnum","Run #", 200000, 200000, 400000)

#for event in t:
    #print event.run
 #   h_runnum.Fill(event.run)
    #print "I got here"

### End extra stuff that I was just playing around with
################################
############################

print '###################'
print 'Total number of events is:', iev

#h_ston_vs_time.Fit("expo", "S")
#h_nclusters_vs_time.Fit("expo", "S") #Commented out for speed, will want to comment this back in later

#Fitting for whole tracker plots
print "I reached the Fitting for whole tracker plots step"

fit_one_expo.SetParameters(10., .001)
print "At fit_one_expo.SetParameters, I am ok"
h_nclusters_vs_time.Fit("fit_one_expo", "R", "ChiSquare")
result_h_nclus_vs_time_fit_one_expo = h_nclusters_vs_time.Fit("fit_one_expo", "R", "ChiSquare")
print "At h_nclusters_vs_time.Fit fit_one_expo, I am ok"

print "I am now making the ouptut text file for the FitOneExpo of the whole tracker"
orig_stdout = sys.stdout
myFileOneExpo = open(fileName +'_WholeTracker_OneExpo.txt', 'w')
sys.stdout = myFileOneExpo
print "ChiSquare  :", fit_one_expo.GetChisquare()
print "Parameter 0:", fit_one_expo.GetParameter(0), "Parameter Error:", fit_one_expo.GetParError(0)
print "Parameter 1:", fit_one_expo.GetParameter(1), "Parameter Error:", fit_one_expo.GetParError(1)

sys.stdout = orig_stdout
myFileOneExpo.close()

print "I closed the output text file for the FitOneExpo of the whole tracker"

#Begin manipulations to get the parameters from the fit into a new function that I can actually have drawn for the fit_one_expo
par0_fit_one_expo = fit_one_expo.GetParameter(0)
par1_fit_one_expo = fit_one_expo.GetParameter(1)
print "par0_fit_one_expo is:", par0_fit_one_expo
print "par1_fit_one_expo is:", par1_fit_one_expo
par0_fit_one_expo_string = str(fit_one_expo.GetParameter(0))
par1_fit_one_expo_string = str(fit_one_expo.GetParameter(1))
print 'par0_fit_one_expo_string is:', par0_fit_one_expo_string
print 'par1_fit_one_expo_string is:', par1_fit_one_expo_string
#fit_one_expo_to_draw = ROOT.TF1("fit_one_expo_to_draw", fit_one_expo, 0, 1000)
fit_one_expo_to_draw = ROOT.TF1("fit_one_expo_to_draw", "TMath::Exp((%s) + (%s)*x)"%(par0_fit_one_expo_string,par1_fit_one_expo_string), 0, 1000)
print "checking again and having it print again, par0_fit_one_expo is:", par0_fit_one_expo
print "checking again and having it print again, par1_fit_one_ expo is:", par1_fit_one_expo
print "checking again and having it print again, par0_fit_one_expo_string is:", par0_fit_one_expo_string
print "checking again and having it print again, par1_fit_one_expo_string is:", par1_fit_one_expo_string
print "fit_one_expo_to_draw is:", fit_one_expo_to_draw
print "I reached where Mary has defined fit_one_expo_to_draw!!"

#fit_one_expo_to_draw.SetParameters(par0_fit_one_expo, par1_fit_one_expo)
#print "fit_one_expo_to_draw has these parameters (order that the they print out in is par0, par1):", fit_one_expo_to_draw.GetParameter(0), fit_one_expo_to_draw.GetParameter(1)

fit_two_expo.SetParameters(10., .001, 11.0, .002)
print "At fit_two_expo.SetParameters, I am ok!"
h_nclusters_vs_time.Fit("fit_two_expo", "R", "ChiSquare")
#result_h_nclus_vs_time_fit_two_expo = h_nclusters_vs_time.Fit("fit_two_expo", "R", "ChiSquare")
print "At h_nclusters_vs_time.Fit two expo, I am ok"

print "I am making the output text file for FitTwoExpo for the whole tracker!"
orig_stdout = sys.stdout
myFileTwoExpo = open(fileName +'_WholeTracker_TwoExpo.txt', 'w')
sys.stdout = myFileTwoExpo
print "ChiSquare  :", fit_two_expo.GetChisquare()
print "Parameter 0:", fit_two_expo.GetParameter(0), "Parameter Error:", fit_two_expo.GetParError(0)
print "Parameter 1:", fit_two_expo.GetParameter(1), "Parameter Error:", fit_two_expo.GetParError(1)
print "Parameter 2:", fit_two_expo.GetParameter(2), "Parameter Error:", fit_two_expo.GetParError(2)
print "Parameter 3:", fit_two_expo.GetParameter(3), "Parameter Error:", fit_two_expo.GetParError(3)

sys.stdout = orig_stdout
myFileTwoExpo.close()
print "I have closed the output text file for FitTwoExpo for the whole tracker plot!"

par0_fit_two_expo = fit_two_expo.GetParameter(0)
par1_fit_two_expo = fit_two_expo.GetParameter(1)
par2_fit_two_expo = fit_two_expo.GetParameter(2)
par3_fit_two_expo = fit_two_expo.GetParameter(3)
print "par0_fit_two_expo is:", par0_fit_two_expo
print "par1_fit_two_expo is:", par1_fit_two_expo
print "par2_fit_two_expo is:", par2_fit_two_expo
print "par3_fit_two_expo is:", par3_fit_two_expo
par0_fit_two_expo_string = str(fit_two_expo.GetParameter(0))
par1_fit_two_expo_string = str(fit_two_expo.GetParameter(1))
par2_fit_two_expo_string = str(fit_two_expo.GetParameter(2))
par3_fit_two_expo_string = str(fit_two_expo.GetParameter(3))
print 'par0_fit_two_expo_string is:', par0_fit_two_expo_string
print 'par1_fit_two_expo_string is:', par1_fit_two_expo_string
print "par2_fit_two_expo_string is:", par2_fit_two_expo_string
print "par3_fit_two_expo_string is:", par3_fit_two_expo_string

fit_two_expo_to_draw = ROOT.TF1("fit_two_expo_to_draw", "TMath::Exp((%s) + (%s)*x) +TMath::Exp((%s) + (%s)*x)"%(par0_fit_two_expo_string,par1_fit_two_expo_string, par2_fit_two_expo_string, par3_fit_two_expo_string), 0, 1000)
print "checking again and having it print again, par0_fit_two_expo is:", par0_fit_two_expo
print "checking again and having it print again, par1_fit_two_expo is:", par1_fit_two_expo
print "checking again and having it print again, par2_fit_two_expo is:", par2_fit_two_expo
print "checking again and having it print again, par3_fit_two_expo is:", par3_fit_two_expo
print "checking again and having it print again, par0_fit_two_expo_string is:", par0_fit_two_expo_string
print "checking again and having it print again, par1_fit_two_expo_string is:", par1_fit_two_expo_string
print "checking again and having it print again, par2_fit_two_expo_string is:", par2_fit_two_expo_string
print "checking again and having it print again, par3_fit_two_expo_string is:", par3_fit_two_expo_string
print "fit_two_expo_to_draw is:", fit_two_expo_to_draw
print "ARMADILLO! I reached where Mary has defined fit_two_expo_to_draw!!"

fit_three_expo.SetParameters(10., .001, 11.0, .002, 9., -.001)
print "At fit three expo SetParameters for the whole tracker, I am ok!"
h_nclusters_vs_time.Fit("fit_three_expo", "R", "ChiSquare")
print "At fit three expo FIT for the whole tracker, I am ok!"

print "I am making the output text file for FitThreeExpo for the whole tracker!"
orig_stdout = sys.stdout
myFileThreeExpo = open(fileName +'_WholeTracker_ThreeExpo.txt', 'w')
sys.stdout = myFileThreeExpo
print "ChiSquare  :", fit_three_expo.GetChisquare()
print "Parameter 0:", fit_three_expo.GetParameter(0), "Parameter Error:", fit_three_expo.GetParError(0)
print "Parameter 1:", fit_three_expo.GetParameter(1), "Parameter Error:", fit_three_expo.GetParError(1)
print "Parameter 2:", fit_three_expo.GetParameter(2), "Parameter Error:", fit_three_expo.GetParError(2)
print "Parameter 3:", fit_three_expo.GetParameter(3), "Parameter Error:", fit_three_expo.GetParError(3)
print "Parameter 4:", fit_three_expo.GetParameter(4), "Parameter Error:", fit_three_expo.GetParError(4)
print "Parameter 5:", fit_three_expo.GetParameter(5), "Parameter Error:", fit_three_expo.GetParError(5)

sys.stdout = orig_stdout
myFileThreeExpo.close()
print "I have closed the output text file for the FitThreeExpo for the whole tracker!"


par0_fit_three_expo = fit_three_expo.GetParameter(0)
par1_fit_three_expo = fit_three_expo.GetParameter(1)
par2_fit_three_expo = fit_three_expo.GetParameter(2)
par3_fit_three_expo = fit_three_expo.GetParameter(3)
par4_fit_three_expo = fit_three_expo.GetParameter(4)
par5_fit_three_expo = fit_three_expo.GetParameter(5)
print "par0_fit_three_expo is:", par0_fit_three_expo
print "par1_fit_three_expo is:", par1_fit_three_expo
print "par2_fit_three_expo is:", par2_fit_three_expo
print "par3_fit_three_expo is:", par3_fit_three_expo
print "par4_fit_three_expo is:", par4_fit_three_expo
print "par5_fit_three_expo is:", par5_fit_three_expo
par0_fit_three_expo_string = str(fit_three_expo.GetParameter(0))
par1_fit_three_expo_string = str(fit_three_expo.GetParameter(1))
par2_fit_three_expo_string = str(fit_three_expo.GetParameter(2))
par3_fit_three_expo_string = str(fit_three_expo.GetParameter(3))
par4_fit_three_expo_string = str(fit_three_expo.GetParameter(4))
par5_fit_three_expo_string = str(fit_three_expo.GetParameter(5))
print 'par0_fit_three_expo_string is:', par0_fit_three_expo_string
print 'par1_fit_three_expo_string is:', par1_fit_three_expo_string
print "par2_fit_three_expo_string is:", par2_fit_three_expo_string
print "par3_fit_three_expo_string is:", par3_fit_three_expo_string
print "par4_fit_three_expo_string is:", par4_fit_three_expo_string
print "par5_fit_three_expo_string is:", par5_fit_three_expo_string

fit_three_expo_to_draw = ROOT.TF1("fit_three_expo_to_draw", "TMath::Exp((%s) + (%s)*x) +TMath::Exp((%s) + (%s)*x) +TMath::Exp((%s) + (%s)*x)"%(par0_fit_three_expo_string,par1_fit_three_expo_string, par2_fit_three_expo_string, par3_fit_three_expo_string, par4_fit_three_expo_string, par5_fit_three_expo_string), 0, 1000)
print "checking again and having it print again, par0_fit_three_expo is:", par0_fit_three_expo
print "checking again and having it print again, par1_fit_three_expo is:", par1_fit_three_expo
print "checking again and having it print again, par2_fit_three_expo is:", par2_fit_three_expo
print "checking again and having it print again, par3_fit_three_expo is:", par3_fit_three_expo
print "checking again and having it print again, par4_fit_three_expo is:", par4_fit_three_expo
print "checking again and having it print again, par5_fit_three_expo is:", par5_fit_three_expo
print "checking again and having it print again, par0_fit_three_expo_string is:", par0_fit_three_expo_string
print "checking again and having it print again, par1_fit_three_expo_string is:", par1_fit_three_expo_string
print "checking again and having it print again, par2_fit_three_expo_string is:", par2_fit_three_expo_string
print "checking again and having it print again, par3_fit_three_expo_string is:", par3_fit_three_expo_string
print "checking again and having it print again, par4_fit_three_expo_string is:", par4_fit_three_expo_string
print "checking again and having it print again, par5_fit_three_expo_string is:", par5_fit_three_expo_string
print "fit_three_expo_to_draw is:", fit_three_expo_to_draw
print "PLATAPUS! I reached where Mary has defined fit_three_expo_to_draw!!"

#Fitting for TID plots
fit_one_expo_tid.SetParameters(10., .001)
print "At fit_one_expo_tid.SetParameters, I am ok!"
h_nclusters_vs_time_tid.Fit("fit_one_expo_tid", "R", "ChiSquare")
print "At h_nclusters_vs_time_tid.Fit for one expo tid, I am ok!!"

print "I am making the output text file for the OneExpoTid for the TID"

orig_stdout = sys.stdout
myFileOneExpo = open(fileName +'_TIDTracker_OneExpo.txt', 'w')
sys.stdout = myFileOneExpo
print "ChiSquare  :", fit_one_expo_tid.GetChisquare()
print "Parameter 0:", fit_one_expo_tid.GetParameter(0), "Parameter Error:", fit_one_expo_tid.GetParError(0)
print "Parameter 1:", fit_one_expo_tid.GetParameter(1), "Parameter Error:", fit_one_expo_tid.GetParError(1)

sys.stdout = orig_stdout
myFileOneExpo.close()
print "I have closed the output text file for the OneExpoTID for the TID!"

fit_two_expo_tid.SetParameters(10., .001, 11.0, .002)
print "At fit_two_expo_tid.SetParameters, I am ok!"
h_nclusters_vs_time_tid.Fit("fit_two_expo_tid", "R", "ChiSquare")
print "At h_nclusters_vs_time_tid.Fit for two_expo, I am ok!"

print "I am making the output text file for the FitTwoExpoTid for the Tid!!"
orig_stdout = sys.stdout
myFileTwoExpo = open(fileName +'_TIDTracker_TwoExpo.txt', 'w')
sys.stdout = myFileTwoExpo
print "ChiSquare  :", fit_two_expo_tid.GetChisquare()
print "Parameter 0:", fit_two_expo_tid.GetParameter(0), "Parameter Error:", fit_two_expo_tid.GetParError(0)
print "Parameter 1:", fit_two_expo_tid.GetParameter(1), "Parameter Error:", fit_two_expo_tid.GetParError(1)
print "Parameter 2:", fit_two_expo_tid.GetParameter(2), "Parameter Error:", fit_two_expo_tid.GetParError(2)
print "Parameter 3:", fit_two_expo_tid.GetParameter(3), "Parameter Error:", fit_two_expo_tid.GetParError(3)

sys.stdout = orig_stdout
myFileTwoExpo.close()
print "I have closed the output text file for the FitTwoExpoTid for the TID!!"

#fit_three_expo_tid.SetParameters(10., .001, 11.0, .002, 9., -.001)
#print "At fit_three_expo_tid.SetParameters, I am ok!"
#h_nclusters_vs_time_tid.Fit("fit_three_expo_tid", "R", "ChiSquare")
#print "At fit_three_expo_tid.Fit for the tid, I am ok!!"

#print "I am making the output file for the fit_three_expo_tid for the TID!"
#orig_stdout = sys.stdout
#myFileThreeExpo = open(fileName + '_TIDTracker_ThreeExpo.txt', 'w')
#sys.stdout = myFileThreeExpo
#print "ChiSquare  :", fit_three_expo_tid.GetChisquare()
#print "Parameter 0:", fit_three_expo_tid.GetParameter(0), "Parameter Error:", fit_three_expo_tid.GetParError(0)
#print "Parameter 1:", fit_three_expo_tid.GetParameter(1), "Parameter Error:", fit_three_expo_tid.GetParError(1)
#print "Parameter 2:", fit_three_expo_tid.GetParameter(2), "Parameter Error:", fit_three_expo_tid.GetParError(2)
#print "Parameter 3:", fit_three_expo_tid.GetParameter(3), "Parameter Error:", fit_three_expo_tid.GetParError(3)
#print "Parameter 4:", fit_three_expo_tid.GetParameter(4), "Parameter Error:", fit_three_expo_tid.GetParError(4)
#print "Parameter 5:", fit_three_expo_tid.GetParameter(5), "Parameter Error:", fit_three_expo_tid.GetParError(5)

#sys.stdout = orig_stdout
#myFileThreeExpo.close()
#print "I have closed the output text file for the FitThreeExpoTID for the TID!!"

#Fitting for TEC plots
fit_one_expo_tec.SetParameters(10., .001)
print "At fit_one_expo_tec.SetParameters, I am ok!"
h_nclusters_vs_time_tec.Fit("fit_one_expo_tec", "R", "ChiSquare")
print "At h_nclusters_vs_time_tec.Fit for one expo tec, I am ok!!"

print "I am making the output text file for the OneExpoTec for the TEC"

orig_stdout = sys.stdout
myFileOneExpo = open(fileName +'_TECTracker_OneExpo.txt', 'w')
sys.stdout = myFileOneExpo
print "ChiSquare  :", fit_one_expo_tec.GetChisquare()
print "Parameter 0:", fit_one_expo_tec.GetParameter(0), "Parameter Error:", fit_one_expo_tec.GetParError(0)
print "Parameter 1:", fit_one_expo_tec.GetParameter(1), "Parameter Error:", fit_one_expo_tec.GetParError(1)

sys.stdout = orig_stdout
myFileOneExpo.close()
print "I have closed the output text file for the OneExpoTEC for the TEC!"

fit_two_expo_tec.SetParameters(10., .001, 11.0, .002)
print "At fit_two_expo_tec.SetParameters, I am ok!"
h_nclusters_vs_time_tec.Fit("fit_two_expo_tec", "R", "ChiSquare")
print "At h_nclusters_vs_time_tec.Fit for two_expo, I am ok!"

print "I am making the output text file for the FitTwoExpoTec for the Tec!!"
orig_stdout = sys.stdout
myFileTwoExpo = open(fileName +'_TECTracker_TwoExpo.txt', 'w')
sys.stdout = myFileTwoExpo
print "ChiSquare  :", fit_two_expo_tec.GetChisquare()
print "Parameter 0:", fit_two_expo_tec.GetParameter(0), "Parameter Error:", fit_two_expo_tec.GetParError(0)
print "Parameter 1:", fit_two_expo_tec.GetParameter(1), "Parameter Error:", fit_two_expo_tec.GetParError(1)
print "Parameter 2:", fit_two_expo_tec.GetParameter(2), "Parameter Error:", fit_two_expo_tec.GetParError(2)
print "Parameter 3:", fit_two_expo_tec.GetParameter(3), "Parameter Error:", fit_two_expo_tec.GetParError(3)

sys.stdout = orig_stdout
myFileTwoExpo.close()
print "I have closed the output text file for the FitTwoExpoTec for the Tec!!"

#fit_three_expo_tec.SetParameters(10., .001, 11.0, .002, 9., -.001)
#print "At fit_three_expo_tec.SetParameters, I am ok!"
#h_nclusters_vs_time_tec.Fit("fit_three_expo_tec", "R", "ChiSquare")
#print "At fit_three_expo_tec.Fit for the tec, I am ok!!"

#print "I am making the output file for the fit_three_expo_tec for the Tec!"
#orig_stdout = sys.stdout
#myFileThreeExpo = open(fileName + '_TECTracker_ThreeExpo.txt', 'w')
#sys.stdout = myFileThreeExpo
#print "ChiSquare  :", fit_three_expo_tec.GetChisquare()
#print "Parameter 0:", fit_three_expo_tec.GetParameter(0), "Parameter Error:", fit_three_expo_tec.GetParError(0)
#print "Parameter 1:", fit_three_expo_tec.GetParameter(1), "Parameter Error:", fit_three_expo_tec.GetParError(1)
#print "Parameter 2:", fit_three_expo_tec.GetParameter(2), "Parameter Error:", fit_three_expo_tec.GetParError(2)
#print "Parameter 3:", fit_three_expo_tec.GetParameter(3), "Parameter Error:", fit_three_expo_tec.GetParError(3)
#print "Parameter 4:", fit_three_expo_tec.GetParameter(4), "Parameter Error:", fit_three_expo_tec.GetParError(4)
#print "Parameter 5:", fit_three_expo_tec.GetParameter(5), "Parameter Error:", fit_three_expo_tec.GetParError(5)

#sys.stdout = orig_stdout
#myFileThreeExpo.close()
#print "I have closed the output text file for the FitThreeExpoTec for the Tec!!"

#Draw and save plots

#Draw the runnum histo that we might use later for matching, right now since it's all run 305090, it's quite an uninformative histo
#c1 = ROOT.TCanvas()
#h_runnum.Draw()
#c1.SaveAs(fileName + "_runNumberHisto.pdf")

#c2 = ROOT.TCanvas()
#ROOT.gStyle.SetOptStat(0)
#h_ston_vs_time.Draw()
#ROOT.gPad.Update() #Seems to do nothing, ask Xavier about this tomorrow (or ask in genreal at group meeting)
#h_ston_vs_time_fit.SetLineColor(2)
#expo.Draw("SAME")
#c2.SaveAs(fileName + "_ston_vs_time_histo.pdf")

c3 = ROOT.TCanvas()
ROOT.gStyle.SetOptStat(0)
#ROOT.gStyle.SetOptFit(1111)

#h_nclusters_vs_time.Draw("expo")
h_nclusters_vs_time.Draw()
fit_one_expo_to_draw.SetLineColor(2)
fit_one_expo_to_draw.Draw("SAME")
fit_two_expo_to_draw.SetLineColor(3)
fit_two_expo_to_draw.Draw("SAME")
fit_three_expo_to_draw.SetLineColor(4)
fit_three_expo_to_draw.Draw("SAME")
c3.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit.pdf')
c3.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit.png')
c3.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit.eps')
c3.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit.root')
print "Ok, got here to draw whole tracker histo!"

#c4 = ROOT.TCanvas()
#ROOT.gStyle.SetOptStat(0)
#h_nclusters_vs_time_tid.Draw()
#fit_one_expo_tid.SetLineColor(2)
#fit_one_expo_tid.Draw("SAME")
#fit_two_expo_tid.SetLineColor(3)
#fit_two_expo_tid.Draw("SAME")
#fit_three_expo_tid.SetLineColor(4)
#fit_three_expo_tid.Draw("SAME")
#c4.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit_tid.pdf')
#c4.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit_tid.png')
#c4.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit_tid.eps')
#c4.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit_tid.root')

#print "Ok 4 I got here to draw tid histo"

#c5 = ROOT.TCanvas()
#ROOT.gStyle.SetOptStat(0)
#h_nclusters_vs_time_tec.Draw()
#fit_one_expo_tec.SetLineColor(2)
#fit_one_expo_tec.Draw("SAME")
#fit_two_expo_tec.SetLineColor(3)
#fit_two_expo_tec.Draw("SAME")
#fit_three_expo_tec.SetLineColor(4)
#fit_three_expo_tec.Draw("SAME")
#c5.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit_tec.pdf')
#c5.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit_tec.png')
#c5.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit_tec.eps')
#c5.SaveAs(fileName + "_" + str(runOfInterest) + "_" + '_nclusters_vs_time_histo_fit_tec.root')
#print "Ok got here to draw the tec histo"

print "Fini! Vive la France!"
