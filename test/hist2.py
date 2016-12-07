

import ROOT
import array as a

theOutfile=ROOT.TFile("outfile.root","RECREATE")


# Bins are defined by an array 
ptBs =  a.array('d', [200, 300 , 400 , 500 , 800 ])
nptBs = len(ptBs) - 1

# Define a binned histogram for storing the peak of the gaussian fit to a Top mass spectrum in each Pt bin

hpeak = ROOT.TH1F("hpeak", " ;p_{T} of jet (GeV); Peak Location ",  nptBs, ptBs)  
  


# Open the input file

theInfile = ROOT.TFile("../samples/infile.root","READ")

# Choose which stage of the selection you would like to see (0-17)
theSelectionStage = 15

# Get the histograms of AK8 jet mass binned by Pt of the jet

hist_list = [ "AK8MPt200To300Hist" + str(theSelectionStage),    
              "AK8MPt300To400Hist" + str(theSelectionStage),    
              "AK8MPt400To500Hist" + str(theSelectionStage),    
              "AK8MPt500To800Hist" + str(theSelectionStage),    
              ]
              
# loop over histos and for each plot it and fit to a gaussian then save the mean              
              
for ihisto , histo in enumerate(hist_list) :
    theHist = theInfile.Get(histo )
    print "Now working with histogram named {}".format( histo )
    # Ensure proper error propogation
    theHist.Sumw2()
    theHist.SetDirectory(0)
    
    scaleis = 100.
    # If you want to scale the hist uncomment the line below
    #theHist.Scale(scaleis)
    
    # Change the number of bins from the value the histogram was initialized with
    theHist.Rebin(10)

    # Fitting the histogram to a Gaussian
    theFitFunc = ROOT.TF1("theFitFunc", "gaus", 110, 210 )
    theFitFunc.SetLineColor(1)
    theFitFunc.SetLineWidth(2)
    theFitFunc.SetLineStyle(2)
    theHist.Fit(theFitFunc,'R' )

    # Getting ampltitude, mean and width of fit
    amp_data    = theFitFunc.GetParameter(0);
    eamp_data   = theFitFunc.GetParError(0); 
    mean_data   = theFitFunc.GetParameter(1);
    emean_data  = theFitFunc.GetParError(1); 
    width_data  = theFitFunc.GetParameter(2);
    ewidth_data = theFitFunc.GetParError(2); 

    # Printing fit information
    print 'amp {} #pm eamp {}'.format(amp_data, eamp_data    ) 
    print 'mean_data   '+str(mean_data   ) + 'emean_data  '+str(emean_data  ) 
    print 'width_data {0:3.2f} #pm {1:1.2f} '.format(width_data , ewidth_data ) 
    
    ROOT.gStyle.SetOptFit(1111)
    c = ROOT.TCanvas('c','')
    
    theHist.Draw('hist')
    theFitFunc.Draw("same")
    
    # Set the maximum value for the y axis
    maxy= theHist.GetMaximum() 
    theHist.SetMaximum( maxy * 1.2)
    theHist.GetXaxis().SetRangeUser(80 , 250 )

    c.Update()
    c.Draw()

    c.Print('plots/'+ str(histo) + '_' + 'GaussianFit.png', 'png' )
    c.Print('plots/'+ str(histo) + '_' + 'GaussianFit.pdf', 'pdf' )
    c.Print('plots/'+ str(histo) + '_' + 'GaussianFit.root', 'root' )
   
# re-binning, scaling, plotting and fitting to a Gaussian.    
    
ROOT.gStyle.SetOptFit(1111)
theCanvas = ROOT.TCanvas('theCanvas','')



theOutfile.cd()
theOutfile.Write()
theOutfile.Close()

