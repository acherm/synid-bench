000200070317     H*�COPYRIGHT DATABOROUGH LTD 2005                                          
000300040512     H*�--------------------------------------------------------------------    
000400050901     H debug(*yes) copyright('Databorough Ltd. 2005') datedit(*dmy)             
000500040512                                                                                
000600040512     F**********************************************************************    
000700040512     F*�F i l e s                                                               
000800040512     F**********************************************************************    
000900050901     Fcntcmaintdcf   e             workstn                                      
001000050901     Fcntacs    uf   e           k disk                                         
001100050901     Fnamesidx  uf   e           k disk                                         
001200050901     Fslmen     if   e           k disk                                         
001300030414                                                                                
001800040512     D**********************************************************************    
001900040512     D*�D e f i n i t i o n s                                                   
002000040512     D**********************************************************************    
002100050901     D customer        s              5p 0                                      
002200050901     D product         s              2a                                        
002300040512                                                                                
002400040512     D valid           s               n                                        
002500040512     D errormsg        s            132a                                        
002600040512     D msgid           s              7a                                        
002700040513     D z1              s              5p 0                                      
002800040513     D statuses        s              1a   dim(37) ctdata perrcd(37)            
002900040512                                                                                
003000040512     D zdate           ds            11                                         
003100040512     D zday                           2a                                        
003200040512     D filler1                        1a                                        
003300040512     D zmth                           3a                                        
003400040512     D filler2                        1a                                        
003500040512     D zyr                            4a                                        
003600040512                                                                                
003601110922                                                                                
003700040512     D gotdate         s             10d   datfmt(*eur)                         
003800040512     D xmth            s              2p 0                                      
003900040512     D mth             s             36a                                        
004000040512                                                                                
004100040512     D rtnmsgtext      pr                  extpgm('RTNMSGTEXT')                 
004200040512     D                                7a   const                                
004300040512     D                              132a                                        
004400030414                                                                                
004500040512     C**********************************************************************    
004600040512     C*�M a i n l i n e   C o d e                                               
004700040512     C**********************************************************************    
004800040512     C*�Retrieve record                                                         
004900050901     C     cntacskey     chain(e)  rcntac                                       
005000050901     C                   if        not %found(cntacs)                           
005100040512     C                   eval      *inlr = *on                                  
005200040512     C                   return                                                 
005300040512     C                   endif                                                  
005400040512                                                                                
005500040512     C*�Set screen values                                                       
005600040512     C                   exsr      writescn                                     
005700050901     C                   eval      zmessage='Please make required changes.'     
005800030414                                                                                
005900040512     C*�Until Exit/Cancel                                                       
006000040512     C                   dow       not *in03                                    
006100040512     C                              and not *in12                               
006200030414                                                                                
006300040513     C*�Display screen                                                          
006400040512     C                   exfmt(e)  zzft01                                       
006500040512                                                                                
006600040512     C*�If Exit/Cancel                                                          
006700040512     C                   if        *in03                                        
006800040512     C                              or *in12                                    
006900040512     C                   leave                                                  
006901110922                                                                                
007000040512     C                   endif                                                  
007100040512                                                                                
007200040512     C*�Else validate                                                           
007300040512     C                   exsr      validate                                     
007400040513                                                                                
007500040513     C*�If valid                                                                
007600040512     C                   if        valid                                        
007700040513     C*�Update file and leave                                                   
007800040513     C                   exsr      updatefile                                   
007900040512     C                   leave                                                  
008000040513     C*�Else: If not valid                                                      
008100040512     C                   else                                                   
008200040513     C*�Display error message                                                   
008300040512     C                   eval      zmessage = errormsg                          
008400040513     C*�End: If valid                                                           
008500040512     C                   endif                                                  
008600030414                                                                                
008700040512     C*�End: Until Exit/Cancel                                                  
008800040512     C                   enddo                                                  
008900030414                                                                                
009000030414     C                   eval      *inlr = *on                                  
009100040512     C                   return                                                 
009200040512     C**********************************************************************    
009300040512     C*�L o g i c al   E n d   o f   P r o g r a m                              
009400040512     C**********************************************************************    
009500030414                                                                                
009600040512     C**********************************************************************    
009700040512     C     writescn      begsr                                                  
009800040512     C**********************************************************************    
009900040512     C*�Subroutine: Write screen                                                
010000040512     C**********************************************************************    
010100040512     C                   eval      zcusno = cusno                               
010200050901     C                   eval      zprpcde = prpcde                             
010300050901     C                   eval      zusernm = usernm                             
010400040512     C                   eval      ztelno = telno                               
010500040512     C                   eval      zfaxno = faxno                               
010600040512     C                   eval      zemail = email                               
010700050901     C     *YMD          move      lctdat        zlctdat                        
010800050901     C     *YMD          move      apdate        zapdate                        
010801110914     C**   *YMD          move      apudate       zapudate                       
010900050818     C                   eval      zsinit = sinit                               
011000040512     C                   eval      zstatus = status                             
011100040512                                                                                
011200040512     C                   endsr                                                  
011300040512     C**********************************************************************    
011400040512                                                                                
011500040513     C**********************************************************************    
011600040513     C     updatefile    begsr                                                  
011700040513     C**********************************************************************    
011800040513     C*�Subroutine: Update file                                                 
011900040513     C**********************************************************************    
012000050901     C                   eval      cusno = zcusno                               
012100050901     C                   eval      prpcde = zprpcde                             
012200050901     C                   eval      usernm = zusernm                             
012300050901     C                   eval      telno = ztelno                               
012301110914     C**                 eval      telno = ztelno                               
012400050901     C                   eval      faxno = zfaxno                               
012500050901     C                   eval      email = zemail                               
012600050901     C     *YMD          move      zlctdat       lctdat                         
012700050901     C     *YMD          move      zapdate       apdate                         
012800050901     C                   eval      sinit = zsinit                               
012900050901     C                   eval      status = zstatus                             
013000040513                                                                                
013100050901     C                   update(e) rcntac                                       
013200050901                                                                                
013300050901     C*�If update successful then update names index file                       
013400040513     C                   if        not %error                                   
013500050901                                                                                
013600050901     C                   eval      ixname = usernm                              
013700050901     C     ixname        chain(e)  namesidxf                                    
013800050901     C                   if        %found(namesidx)                             
013900050901     C                   eval      ixtelno = telno                              
014000050901     C                   eval      ixemail = email                              
014100050901     C                   update(e) namesidxf                                    
014200050901     C                   endif                                                  
014300050901                                                                                
014400040513     C                   endif                                                  
014500040513                                                                                
014600040513     C                   endsr                                                  
014700040513     C**********************************************************************    
014800040513                                                                                
014900040512     C**********************************************************************    
015000040512     C*�Subroutine: Validate screen                                             
015100040512     C**********************************************************************    
015200040512     C     validate      begsr                                                  
015300040512     C**********************************************************************    
015400040513     C                   eval      *in33 = *off                                 
015500040513     C                   eval      *in34 = *off                                 
015600040513     C                   eval      *in35 = *off                                 
015700040513     C                   eval      *in36 = *off                                 
015800040513     C                   eval      *in37 = *off                                 
015900040513     C                   eval      *in38 = *off                                 
016000040513     C                   eval      *in43 = *off                                 
016100040512                                                                                
016200040512     C                   eval      valid = *on                                  
016300040512                                                                                
016400050901     C*�Contact name                                                            
016500050901     C                   if        zusernm = *blanks                            
016600050901     C                   eval      *in33 = *on                                  
016700050901     C                   eval      msgid = 'OEM0020'                            
016800040512     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
016900040512     C                   eval      valid = *off                                 
017000040512     C                   leavesr                                                
017100040512     C                   endif                                                  
017200040513                                                                                
017300040513     C*�Telephone number                                                        
017400040513     C                   if        ztelno <> *blanks                            
017500040513     C     ' 0123456789' check     ztelno        z1                             
017600040513     C                   if        %found                                       
017700040513     C                   eval      *in34 = *on                                  
017800040513     C                   eval      msgid = 'OEM0014'                            
017900040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
018000040513     C                   eval      valid = *off                                 
018100040513     C                   leavesr                                                
018200040513     C                   endif                                                  
018300040513     C                   endif                                                  
018400040513                                                                                
018500040513     C*�Fax number                                                              
018600040513     C                   if        zfaxno <> *blanks                            
018700040513     C     ' 0123456789' check     zfaxno        z1                             
018800040513     C                   if        %found                                       
018900040513     C                   eval      *in35 = *on                                  
019000040513     C                   eval      msgid = 'OEM0015'                            
019100040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
019200040513     C                   eval      valid = *off                                 
019300040513     C                   leavesr                                                
019400040513     C                   endif                                                  
019500040513     C                   endif                                                  
019600040513                                                                                
019700050901     C*�Salesman                                                                
019800050901     C                   if        zsinit <> *blanks                            
019900050901     C     zsinit        setll(e)  rslmen                                       
020000050901     C                   if        not %equal(slmen)                            
020100050901     C                   eval      *in37 = *on                                  
020200050901     C                   eval      msgid = 'OEM0023'                            
020201110914     C***                eval      msgid = 'OEM0157'                            
020300040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
020400040513     C                   eval      valid = *off                                 
020500040513     C                   leavesr                                                
020600040513     C                   endif                                                  
020700040513     C                   endif                                                  
020800040513                                                                                
020900040513     C*�Status                                                                  
021000040513     C                   if        zstatus <> *blanks                           
021100040513     C                   eval      z1 = 1                                       
021200040513     C     zstatus       lookup    statuses(z1)                           77    
021300040513     C                   if        not %found                                   
021400050901     C                   eval      *in38 = *on                                  
021500040513     C                   eval      msgid = 'OEM0019'                            
021600040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
021700040513     C                   eval      valid = *off                                 
021800040513     C                   leavesr                                                
021900040513     C                   endif                                                  
022000040513     C                   endif                                                  
022100030414                                                                                
022200040512     C                   endsr                                                  
022300040512     C**********************************************************************    
022400040512                                                                                
022500040512     C**********************************************************************    
022600040512     C     *inzsr        begsr                                                  
022700040512     C**********************************************************************    
022800040512     C*�Subroutine: Perform Initialisation Routines                             
022900040512     C**********************************************************************    
023000040512     C*�Set screen values                                                       
023100040512     C*�- Program name                                                          
023200050901     C                   eval      zzpgm = 'CNTCMAINT'                          
023300040512     C*�- Date                                                                  
023400040512     C                   eval      mth='JanFebMarAprMayJunJulAugSepOctNovDec'   
023500040512     C                   move      *date         gotdate                        
023600040512     C                   extrct    gotdate:*d    zday                           
023700040512     C                   extrct    gotdate:*y    zyr                            
023800040512     C                   extrct    gotdate:*m    xmth                           
023900040512     C                   eval      zmth = %subst(mth:((xmth-1)*3)+1:3)          
024000040512     C                   eval      zzdate = zdate                               
024100050901                                                                                
024200050901     C*�- Protect key fields                                                    
024300040512     C                   eval      *in31 = *on                                  
024400050901     C                   eval      *in32 = *on                                  
024401110914     C***                eval      *in35 = *off                                 
024500050801                                                                                
024600050901     C*�Set customer number, product code                                       
024700050801     C                   eval      cusno = customer                             
024800050901     C                   eval      prpcde = product                             
024900040512                                                                                
025000040512     C                   endsr                                                  
025100040512     C**********************************************************************    
025200030414                                                                                
025300040512     C**********************************************************************    
025400040512     C*�N o n - E x e c u t a b l e   C o d e                                   
025500040512     C**********************************************************************    
025600040512     C     *entry        plist                                                  
025700050901     C                   parm                    customer                       
025800050901     C                   parm                    product                        
025900050901                                                                                
026000050901     C     cntacskey     klist                                                  
026100050901     C                   kfld                    cusno                          
026200050901     C                   kfld                    prpcde                         
026300040512     C**********************************************************************    
026400040513**                                                                              
026500040513 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ    
009300100713      /free                                                                     
009400100713        *inof = *on;                                                            
009500100714                                                                                
009600100714       //�For each STKGRP3 record                                               
009700100714       setll *loval stkgrp3r;                                                   
009800100714       read(e) stkgrp3r;                                                        
002900100714       dow not %eof(stkgrp3);                                                   
003000100714                                                                                
003100100714       trnhstcount = *zeros;                                                    
003101110914       //trnhstcnt = *zeros;                                                    
003200100714                                                                                
003300100714       //�Count TRNHST records                                                  
003400100714           setll TRNHSTK trnhstr;                                               
003500100714           reade(e) TRNHSTK trnhstr;                                            
003600100714           dow not %eof(trnhstl4) and not %error;                               
003700100714               trnhstcount = trnhstcount + 1;                                   
003800100714               reade(e) TRNHSTK  trnhstr;                                       
003900100714           enddo;                                                               
004000100714                                                                                
004100100714       //�Output totals for stock group 3  record                               
004200100714          if (*inof == 'ls');                                                             
004300100714             except headings;                                                   
004400100714             *inof = '*off';                                                      
004401110914          // *inoa = *off;                                                      
004500100714          endif;                                                                
004600100714                                                                                
004700100714          except totals;                                                        
004800100714                                                                                
004900100714       read(e) stkgrp3r;                                                        
005000100714       enddo;                                                                   
005100100714                                                                                
005200100713       //�Terminate program and exit                                            
005300100713       *inlr = *on;                                                             
005400100713       return;                                                                  
005500100713      /end-free                                                                 
005600100713     C**********************************************************************    
005700100713     C*�* I N Z S R                                                             
005800100713     C**********************************************************************    
005900100713     C     *inzsr        begsr                                                  
006000100713     C                   time                    tyme                           
006100100713     C                   z-add     *date         today                          
006200100714     C     TRNHSTK       klist                                                  
006300100714     C                   kfld                    xwagcd                         
006400100714     C                   kfld                    xwahcd                         
006500100714     C                   kfld                    xwaicd                         
006600100713     C                   endsr                                                  
006700100713     Oqsysprt   e            headings       1 01                                
006800100713     O                                           10 'X-Analysis'                
006900100714     O                                           60 'Audit log for file:'       
007000100714     O                                           68 'STKGRP3'                   
007100100713     O                                          132 'Databorough LTD.'          
007200100713     O          e            headings       1                                   
007300100913     O                                           10 'ZAUDSTKGP3'                
007400100713     O                       tyme               120 '  :  :  '                  
007500100713     O                       today              132 '  /  /    '                
007600100713     O          e            headings       2                                   
007700100713     O                                          127 'Page:'                     
007800100713     O                       page          z    132                             
007900100713     O          e            headings       1                                   
008000100714     O                                           60 'TRNHST'                    
008100100713     O          e            headings       2                                   
008200100713     O                                           60 'Records'                   
008300100714     O          e            totals         2                                   
008400100714     O                       xwagcd               4                             
008500100714     O                       xwahcd               8                             
008600100714     O                       xwaicd              12                             
008700100714     O                       xwiwtx              30                             
008800100714     O                       trnhstcount   1     60                             

