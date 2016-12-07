# pyROOTforCMSDAS
A compilation of basic pyROOT scripts for use at CMS DAS@LPC 2017

To run from FNAL:

```
mkdir pyROOTExamples
cd pyROOTExamples

cmsrel CMSSW_8_0_22
cd CMSSW_8_0_22/src/
cmsenv

git clone https://github.com/UBParker/pyROOTforCMSDAS.git
cd pyROOTforCMSDAS/test/

python hist1.py

python hist2.py

```
