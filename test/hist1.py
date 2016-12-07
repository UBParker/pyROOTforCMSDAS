

import ROOT

theOutfile=ROOT.TFile("outfile.root","RECREATE")


theInfile=ROOT.TFile("../samples/infile.root","READ")


theHist = theInfile.Get("AK8MHist16")

ROOT.gStyle.SetOptFit(1111)
theCanvas = ROOT.TCanvas('theCanvas','')
theHist.Draw('hist')
    
theOutfile.cd()
theOutfile.Write()
theOutfile.Close()

