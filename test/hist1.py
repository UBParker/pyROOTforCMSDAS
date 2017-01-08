import ROOT

theInfile=ROOT.TFile("../samples/infile.root","READ")

theOutfile=ROOT.TFile("outfile.root","RECREATE")

theHist = theInfile.Get("AK8MHist16")

ROOT.gStyle.SetOptFit(1111)
theCanvas = ROOT.TCanvas('theCanvas','')
theHist.Draw('hist')
theCanvas.Update()
theCanvas.Draw()

theHist.Write() 
theCanvas.Write()
   
theOutfile.cd()
theOutfile.Write()
theOutfile.Close()
