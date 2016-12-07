

import ROOT

theOutfile=ROOT.TFile("outfile.root","RECREATE")


theInfile=ROOT.TFile("infile.root","READ")


theHist = theInfile.Get("AK8MHist12")

ROOT.gStyle.SetOptFit(1111)
theCanvas = ROOT.TCanvas('theCanvas','')
theHist.Draw('hist')
    
theOutfile.cd()
theOutfile.Write()
theOutfile.Close()

