000100040512     H*�--------------------------------------------------------------------    
000200040512     H*�COPYRIGHT DATABOROUGH cedit01 LTD 2004                                          
000300040512     H*�--------------------------------------------------------------------    
000400040512     H debug(*yes) copyright('Databorough Ltd. 2004') datedit(*dmy)             
000500040512                                                                                
000600040512     F**********************************************************************    
000700040512     F*�F i l e s                                                               
000800040512     F**********************************************************************    
000900040512     Fcusfmaintdcf   e             workstn                                      
001000040512     Fcusfl3    uf   e           k disk                                         
001100040513     Fdists     if   e           k disk                                         
001200030414                                                                                
001201110922                                                                                
001300040512     D**********************************************************************    
001400040512     D*�D e f i n i t i o n s                                                   
001500040512xxxxxD**********************************************************************    
001600040512     D customer        s              5p 0                                      
001700040512     D updated         s              1a                                        
001800040512                                                                                
001900040512     D valid           s               n                                        
002000040512     D errormsg        s            132a                                        
002100040512     D msgid           s              7a                                        
002200040513     D z1              s              5p 0                                      
002300040513     D statuses        s              1a   dim(37) ctdata perrcd(37)            
002400040512                                                                                
002500040512     D zdate           ds            11                                         
002600040512     D zday                           2a                                        
002700040512     D filler1                        1a                                        
002800040512     D zmth                           3a                                        
002900040512     D filler2                        1a                                        
003000040512     D zyr                            4a                                        
003100040512                                                                                
003200040512     D gotdate         s             10d   datfmt(*eur)                         
003300040512     D xmth            s              2p 0                                      
003400040512     D mth             s             36a                                        
003500040512                                                                                
003600040512     D rtnmsgtext      pr                  extpgm('RTNMSGTEXT')                 
003700040512     D                                7a   const                                
003800040512     D                              132a                                        
003900050801                                                                                
004000050801     D cusfsel         pr                  extpgm('CUSFSEL')                    
004100050801     D                                5p 0                                      
004200050818                                                                                
004300050818     D dspdists        pr                  extpgm('DSPDISTS')                   
004400050818     D                                2a                                        
004500050818                                                                                
004600050818     D wwccons         pr                  extpgm('WWCCONS')                    
004700050818     D                                5p 0                                      
004800050818                                                                                
004900050818     D wwrareas        pr                  extpgm('WWRAREAS')                   
005000050818     D                                3a                                        
005100030414                                                                                
005101110922                                                                                
005200040512     C**********************************************************************    
005300040512     C*�M a i n l i n e   C o d e                                               
005400040512     C**********************************************************************    
005500040512     C*�Retrieve record                                                         
005600040512     C     cusno         chain(e)  rcusf                                        
005700040512     C                   if        not %found(cusfl3)                           
005800040512     C                   eval      *inlr = *on                                  
005900040512     C                   return                                                 
006000040512     C                   endif                                                  
006100040512                                                                                
006200040512     C*�Set screen values                                                       
006300040512     C                   exsr      writescn                                     
006400070321     C                   eval      zmessage='Please make required changes.'     
006500030414                                                                                
006600040512     C*�Until Exit/Cancel                                                       
006700040512     C                   dow       not *in03                                    
006800040512     C                              and not *in12                               
006900030414                                                                                
007000040513     C*�Display screen                                                          
007100040512     C                   exfmt(e)  zzft01                                       
007200040512                                                                                
007300040512     C*�If Exit/Cancel                                                          
007400040512     C                   if        *in03                                        
007500040512     C                              or *in12                                    
007600040512     C                   leave                                                  
007700040512     C                   endif                                                  
007800050818                                                                                
007900050818     C*�Other Command Keys                                                      
008000050818     C                   select                                                 
008100050818     C                   when      *in08                                        
008200050818     C                   callp(e)  wwccons(zcusno)                              
008300050818     C                   iter                                                   
008400050818     C                   when      *in09                                        
008500050818     C                   callp(e)  dspdists(zdsdcde)                            
008600050818     C                   iter                                                   
008700050818     C                   when      *in10                                        
008800050818     C                   callp(e)  wwrareas(zsinit)                             
008900050818     C                   iter                                                   
008901110914     C**                 when      *in03                                        
008902110914     C**                 exsr      zexit                                        
009000050818     C                   endsl                                                  
009100040512                                                                                
009200040512     C*�Else validate                                                           
009300040512     C                   exsr      validate                                     
009400040513                                                                                
009500040513     C*�If valid                                                                
009600040512     C                   if        valid                                        
009700040513     C*�Update file and leave                                                   
009800040513     C                   exsr      updatefile                                   
009900040512     C                   leave                                                  
010000040513     C*�Else: If not valid                                                      
010100040512     C                   else                                                   
010200040513     C*�Display error message                                                   
010300040512     C                   eval      zmessage = errormsg                          
010400040513     C*�End: If valid                                                           
010500040512     C                   endif                                                  
010600030414                                                                                
010700040512     C*�End: Until Exit/Cancel                                                  
010800040512     C                   enddo                                                  
010900030414                                                                                
011000030414     C                   eval      *inlr = *on                                  
011100040512     C                   return                                                 
011200040512     C**********************************************************************    
011300040512     C*�L o g i c al   E n d   o f   P r o g r a m                              
011400040512     C**********************************************************************    
011500030414                                                                                
011600040512     C**********************************************************************    
011700040512     C     writescn      begsr                                                  
011800040512     C**********************************************************************    
011900040512     C*�Subroutine: Write screen                                                
012000040512     C**********************************************************************    
012100040512     C                   eval      zcusno = cusno                               
012200040512     C                   eval      zcname = cname                               
012300040512     C                   eval      zadd1 = add1                                 
012400040512     C                   eval      zadd2 = add2                                 
012500040512     C                   eval      zadd3 = add3                                 
012600040512     C                   eval      zadd4 = add4                                 
012700040512     C                   eval      zcntry = cntry                               
012800040512     C                   eval      zpscd = pscd                                 
012900040512     C                   eval      ztelno = telno                               
013000040512     C                   eval      zfaxno = faxno                               
013100040512     C                   eval      zemail = email                               
013200040512     C                   eval      zwebsit = websit                             
013300050802     C                   eval      zdsdcde = dsdcde                             
013400050818     C                   eval      zsinit = sinit                               
013500040512     C                   eval      zstatus = status                             
013600040512     C                   eval      zusernm = usernm                             
013700040512     C                   eval      zsalut = salut                               
013800040512     C                   eval      zjtitle = jtitle                             
013900040513     C     *YMD          move      lctdat        zlctdat                        
014000040513     C     *YMD          move      apdate        zapdate                        
014100040512                                                                                
014200040512     C                   endsr                                                  
014300040512     C**********************************************************************    
014400040512                                                                                
014500040513     C**********************************************************************    
014600040513     C     updatefile    begsr                                                  
014700040513     C**********************************************************************    
014800040513     C*�Subroutine: Update file                                                 
014900040513     C**********************************************************************    
015000040513     C                   eval      cusno = zcusno                               
015100040513     C                   eval      cname = zcname                               
015200040513     C                   eval      add1 = zadd1                                 
015300040513     C                   eval      add2 = zadd2                                 
015400040513     C                   eval      add3 = zadd3                                 
015500040513     C                   eval      add4 = zadd4                                 
015600040513     C                   eval      cntry = zcntry                               
015700040513     C                   eval      pscd = zpscd                                 
015800040513     C                   eval      telno = ztelno                               
015900040513     C                   eval      faxno = zfaxno                               
016000040513     C                   eval      email = zemail                               
016100040513     C                   eval      websit = zwebsit                             
016200050802     C                   eval      dsdcde = zdsdcde                             
016300050818     C                   eval      sinit = zsinit                               
016301110914     C***                eval      snote = znote                                
016400040513     C                   eval      status = zstatus                             
016500040513     C                   eval      usernm = zusernm                             
016600040513     C                   eval      salut = zsalut                               
016700040513     C                   eval      jtitle = zjtitle                             
016800040513     C     *YMD          move      zlctdat       lctdat                         
016900040513     C     *YMD          move      zapdate       apdate                         
017000040513                                                                                
017100040513     C                   update(e) rcusf                                        
017200040513     C                   if        not %error                                   
017300040513     C                   eval      updated = 'Y'                                
017400040513     C                   endif                                                  
017500040513                                                                                
017600040513     C                   endsr                                                  
017700040513     C**********************************************************************    
017800040513                                                                                
017900040512     C**********************************************************************    
018000040512     C*�Subroutine: Validate screen                                             
018100040512     C**********************************************************************    
018200040512     C     validate      begsr                                                  
018300040512     C**********************************************************************    
018400040512     C                   eval      *in32 = *off                                 
018500040513     C                   eval      *in33 = *off                                 
018600040513     C                   eval      *in34 = *off                                 
018700040513     C                   eval      *in35 = *off                                 
018800040513     C                   eval      *in36 = *off                                 
018900040513     C                   eval      *in37 = *off                                 
019000040513     C                   eval      *in38 = *off                                 
019100040513     C                   eval      *in39 = *off                                 
019200040513     C                   eval      *in40 = *off                                 
019300040513     C                   eval      *in41 = *off                                 
019400040513     C                   eval      *in42 = *off                                 
019500040513     C                   eval      *in43 = *off                                 
019600050818     C                   eval      *in44 = *off                                 
019700040512                                                                                
019800040512     C                   eval      valid = *on                                  
019900040512                                                                                
020000040512     C*�Customer name                                                           
020100040512     C                   if        zcname = *blanks                             
020200040512     C                   eval      *in32 = *on                                  
020300040512     C                   eval      msgid = 'OEM0012'                            
020400040512     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
020500040512     C                   eval      valid = *off                                 
020600040512     C                   leavesr                                                
020700040512     C                   endif                                                  
020800040513                                                                                
020900040513     C*�Telephone number                                                        
021000040513     C                   if        ztelno <> *blanks                            
021100040513     C     ' 0123456789' check     ztelno        z1                             
021200040513     C                   if        %found                                       
021300040513     C                   eval      *in34 = *on                                  
021400040513     C                   eval      msgid = 'OEM0014'                            
021500040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
021600040513     C                   eval      valid = *off                                 
021700040513     C                   leavesr                                                
021800040513     C                   endif                                                  
021900040513     C                   endif                                                  
022000040513                                                                                
022100040513     C*�Fax number                                                              
022200040513     C                   if        zfaxno <> *blanks                            
022300040513     C     ' 0123456789' check     zfaxno        z1                             
022400040513     C                   if        %found                                       
022500040513     C                   eval      *in35 = *on                                  
022600040513     C                   eval      msgid = 'OEM0015'                            
022700040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
022800040513     C                   eval      valid = *off                                 
022900040513     C                   leavesr                                                
023000040513     C                   endif                                                  
023100040513     C                   endif                                                  
023200040513                                                                                
023300040513     C*�Distributor                                                             
023400050802     C                   if        zdsdcde <> *blanks                           
023500050802     C     zdsdcde       setll(e)  rprods                                       
023600040513     C                   if        not %equal(dists)                            
023700040513     C                   eval      *in38 = *on                                  
023800040513     C                   eval      msgid = 'OEM0018'                            
023900040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
024000040513     C                   eval      valid = *off                                 
024100040513     C                   leavesr                                                
024200040513     C                   endif                                                  
024300040513     C                   endif                                                  
024400040513                                                                                
024500040513     C*�Status                                                                  
024600040513     C                   if        zstatus <> *blanks                           
024700040513     C                   eval      z1 = 1                                       
024800040513     C     zstatus       lookup    statuses(z1)                           77    
024900040513     C                   if        not %found                                   
025000040513     C                   eval      *in39 = *on                                  
025100040513     C                   eval      msgid = 'OEM0019'                            
025200040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
025300040513     C                   eval      valid = *off                                 
025400040513     C                   leavesr                                                
025500040513     C                   endif                                                  
025600040513     C                   endif                                                  
025700040513                                                                                
025800040513     C*�Contact                                                                 
025900040513     C                   if        zusernm = *blanks                            
026000040513     C                   eval      *in40 = *on                                  
026100040513     C                   eval      msgid = 'OEM0020'                            
026200040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
026300040513     C                   eval      valid = *off                                 
026400040513     C                   leavesr                                                
026500040513     C                   endif                                                  
026600040513                                                                                
026700040513     C*�Title                                                                   
026800040513     C                   if        zsalut <> *blanks                            
026900040513     C                   if        zsalut <> 'Mr'                               
027000040513     C                              and zsalut <> 'Mrs'                         
027100040513     C                              and zsalut <> 'Ms'                          
027200040513     C                              and zsalut <> 'Dr'                          
027300040513     C                              and zsalut <> 'Doctor'                      
027400040513     C                              and zsalut <> 'Professor'                   
027500040513     C                              and zsalut <> 'Sir'                         
027600040513     C                              and zsalut <> 'Lord'                        
027700040513     C                              and zsalut <> 'Lady'                        
027800040513     C                   eval      *in41 = *on                                  
027900040513     C                   eval      msgid = 'OEM0021'                            
028000040513     C                   callp(e)  rtnmsgtext(msgid:errormsg)                   
028100040513     C                   eval      valid = *off                                 
028200040513     C                   leavesr                                                
028300040513     C                   endif                                                  
028400040513     C                   endif                                                  
028500030414                                                                                
028600040512     C                   endsr                                                  
028700040512     C**********************************************************************    
028800040512                                                                                
028900040512     C**********************************************************************    
029000040512     C     *inzsr        begsr                                                  
029100040512     C**********************************************************************    
029200040512     C*�Subroutine: Perform Initialisation Routines                             
029300040512     C**********************************************************************    
029400040512     C*�Set screen values                                                       
029500040512     C*�- Program name                                                          
029600040512     C                   eval      zzpgm = 'CUSFMAINT'                          
029700040512     C*�- Date                                                                  
029800040512     C                   eval      mth='JanFebMarAprMayJunJulAugSepOctNovDec'   
029900040512     C                   move      *date         gotdate                        
030000040512     C                   extrct    gotdate:*d    zday                           
030100040512     C                   extrct    gotdate:*y    zyr                            
030200040512     C                   extrct    gotdate:*m    xmth                           
030300040512     C                   eval      zmth = %subst(mth:((xmth-1)*3)+1:3)          
030400040512     C                   eval      zzdate = zdate                               
030500040512     C*�- Protect customr number                                                
030600040512     C                   eval      *in31 = *on                                  
030700040512                                                                                
030800050801     C*�If customer number not provided then prompt                             
030900050801     C                   if        customer = *zeros                            
031000050801     C                   callp(e)  cusfsel(customer)                            
031100050801     C                   endif                                                  
031200050801                                                                                
031300050801     C*�Set customer number                                                     
031400050801     C                   eval      cusno = customer                             
031500040512                                                                                
031600040512     C*�Initialise updated flag                                                 
031700040512     C                   eval      updated = 'N'                                
031800040512                                                                                
031900040512     C                   endsr                                                  
032000040512     C**********************************************************************    
032100030414                                                                                
032200040512     C**********************************************************************    
032300040512     C*�N o n - E x e c u t a b l e   C o d e                                   
032400040512     C**********************************************************************    
032500040512     C     *entry        plist                                                  
032600040512     C                   parm                    customer                       
032700040512     C                   parm                    updated                        
032800040512     C**********************************************************************    
032900040513**                                                                              
033000040513 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                           
