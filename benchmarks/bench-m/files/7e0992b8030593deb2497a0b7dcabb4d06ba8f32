(* ::Package:: *)

(* Wolfram Language package *)
t0=AbsoluteTime[];
SetDirectory["C:/Users/smi/Desktop/WaleedTransport/"];

Print["Configured Kernels: ",$ConfiguredKernels];
Print["Processor Count: ",$ProcessorCount];

(*BackScatterBoole = True;*)

a=-0.104;
Bins = {155, 178};

Get["MergerTransport/Merger2DProton.m"];
Print["Modules loaded ..."];

kernels=6
LaunchKernels[kernels];
Print[kernels," Kernels launched ..."];

{{MeanX, MeanY}, {ApertX, ApertY}, {BDV}, {BF}, {BA}, {BRxB}, {BDet}}={{0.0301277, 1.00623}, {0.01, 
  0.035}, {0.220899}, {0.451107}, {0.219769}, {0.219722}, {0.207816}};
  
ApertXOff = 0.03; 
ApertYOff = 0.;

(*CenterfitG1=0.96907;
CenterfitG2=0.973888;*)
BlinefitG1=0.965547;
BlinefitG2=0.974009;

rF = BF/BDV;
rA = BA/BDV;
rRxB = BRxB/BDV;
rDet = BDet/BRxB;

(*AlphaFromBlines = 178.20869281586448`/180*Pi;*)

AlphaFromBlinesCorr = 180.11/180.*Pi;

(*BfromCenter=0.221032;*)

BfromCentralBline=0.219679;

XAShift = 0.0;YAShift = 0.007188045691239971`;YRxBShift = 0.00677284727516161`;YDetShift = 0.015928000000000164`;
XRxBShift = 0.;XDetShift = 0.;

R = 0.999002;

xStart=0.02;
xEnd=0.14;
yStart=-0.03;
yEnd=0.04;
xyBins=bin2DGen[xStart,xEnd,yStart,yEnd,24,11];
 
IntMethod = {"GlobalAdaptive", Method -> "MultidimensionalRule"};

Print["Run started at ",DateString[],", Bins: ",Bins];
  
BinwYShiftPrec44OriginalBinsb0NewBGrad = 
 ParallelMap[
  AbsoluteTiming[
    BinIntShift[
     a, #, 
     {AlphaFromBlinesCorr, BfromCentralBline, rF, rRxB, rA, rDet, BlinefitG1, BlinefitG2}, {XAShift, YAShift, YRxBShift, XDetShift, YDetShift}, 
     {0.06, 0.059, 0.9, 0., -0.9, 0.1, 0.099, 0.9, 0., -0.9}, {ApertX, ApertY, ApertXOff, ApertYOff},
     {IntMethod, 4, 2, 0, 3}, {IntMethod, 4, 2, 0, 2}, {IntMethod, 3, 6, 0, 1}
     ]] &, xyBins[[Bins[[1]] ;; Bins[[2]]]], 
  Method -> "FinestGrained"];

Export["MergerTransport/NC_Prot_opt_da0/a"<>ToString[IntegerPart[a*10000]]<>"/TransferResult_08-09-20_NC_opt_G_da0_a"<>ToString[IntegerPart[a*10000]]<>"_"<>ToString[Bins[[1]]]<>"-"<>ToString[Bins[[2]]]<>".txt",BinwYShiftPrec44OriginalBinsb0NewBGrad,"Table"];
 
Print["a = ",IntegerPart[a*10000],"e-4"];
Print["Time consumption: ",(AbsoluteTime[]-t0)/3600.];
Print["MaxMemUse :",MaxMemoryUsed[]/1024/1024.," MB"];
CloseKernels[];
Quit[];

(* Wolfram Language package *)
