**free
// ref: https://www.rpgpgm.com/2015/08/display-screens-of-results-without.html
ctl-opt dftactgrp(*no) ;

// dcl-pr QCMDEXC extpgm ;
// *n char(13) const ;
// *n packed(15:5) const ;
// end-pr ;
dcl-pr sleep uns(10) extproc(*cwiden:'sleep');
   wdelay   uns(10);
end-pr;

dcl-f TESTDSPF workstn ;

dcl-s i packed(2) ;

wdelay = 2;

for i = 1 to 10 ;
   FLD001 = FLD002 ;
   FLD002 = 'Step = ' + %char(i) ;
   write SCREEN1 ;
   sleep(wdelay) ;
endfor ;

exfmt SCREEN2 ;

*inlr = *on ;