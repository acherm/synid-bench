**free

/copy ../cb_rpgle/genericHeaders/controlOptions.rpgle

dcl-f jh7TMPIN               usage(*update:*delete:*output) usrOpn;
dcl-f jh7LOG                 usage(*update:*delete:*output) keyed;
dcl-f jh7ENV10               keyed;
//dcl-f jh7ENV20L1             keyed;
dcl-f jh7CFG30L1             keyed;

/copy ../cb_rpgle/print/qprint_dclf.rpgle

// Procedure Interface
Dcl-pi *n;
   is_dataQueueName          char(10);
   is_dataQueueLibrary       char(10);
   is_endQueueName           char(10);
   is_endQueueLibrary        char(10);
End-pi;

dcl-pr PENVPGMAAA_  extPgm(PENVPGMAAA);
  *n               likeds(enviornment);
end-pr;
dcl-s  PENVPGMAAA            char(10);

/copy cb/general_dcl.rpgle
/copy cb/generalIp_dcl.rpgle

dcl-ds enviornment         likeds(enviornmentTemplate);

/copy ../cb_rpgle/constants/trueFalse.rpgle
/copy ../cb_rpgle/genericHeaders/programStatusDataStructure.rpgle
/copy cb/environment_ds.rpgle

/copy cb/getField_dcl.rpgle
/copy cb/svr_parseMshSegment_dcl.rpgle

dcl-pr QRCVDTAQ            extPgm('QRCVDTAQ');
   *n                        char( 10); // Queue Name
   *n                        char( 10); // Queue Library
   *n                      packed(5:0); // Queue Size
   *n                        char( 10); // Data get
   *n                      packed(5:0); // Wait time 
end-pr;

dcl-pr QCLRDTAQ            extPgm('QCLRDTAQ');  
   *n                        char(10); // Queue Name
   *n                        char(10); // Queue Library
end-pr;

/copy ../cb_rpgle/utility/jmis03cl_dcl.rpgle

dcl-s Err                    char(  7) inz;
dcl-s CallPgmCtr            zoned(1:0) inz;
dcl-s Misc1000               char(1000) inz;

dcl-s environmentFoundForMessage char(  1) inz(*blank);

dcl-s posStartBlock        zoned(5:0) inz;
dcl-s posSegmentTerminator zoned(5:0) inz;

err = executeCommand('OVRPRTF FILE(QSYSPRT) MAXRCDS(*NOMAX) SHARE(*YES) OVRSCOPE(*JOB)');
qPrintOpen();

//=========================================================================
//   M A I N   P R O G R A M
//=========================================================================


is_dataQueueName    = %upper(is_dataQueueName   );
is_dataQueueLibrary = %upper(is_dataQueueLibrary);
is_endQueueName     = %upper(is_endQueueName    );
is_endQueueLibrary  = %upper(is_endQueueLibrary );

if is_dataQueueLibrary = *blank;
  is_dataQueueLibrary = '*LIBL';
endif;

if is_endQueueLibrary = *blank;
  is_endQueueLibrary = '*LIBL';
endif;
err = *blank;
//Err = CheckObj(is_dataQueueLibrary:is_dataQueueName:'*DTAQ');

if Err <> *blank;
  qPrintLog('<<<Error with data queue ' + %trim(is_dataQueueLibrary) + '/' + %trim(is_dataQueueName) + ' Object Type: *DTAQ RtvObjDesc0100 ' + Err);
else;
//  Err = CheckObj(is_endQueueLibrary:is_endQueueName:'*DTAQ');
  if Err <> *blank;
    qPrintLog('<<<Error with end queue ' + %trim(is_endQueueLibrary) + '/' + %trim(is_endQueueName) + ' Object Type: *DTAQ RtvObjDesc0100 ' + Err);
  else;
    qPrintLog('*** Clean out end data queue');
    ClearEndDataQ();
    qPrintLog('*** Create Tempory Files.');
    jmis03cl('QTEMP':'jh7TMPIN ':'*LIBL':'jh7TMPIN ');
    jmis03cl('QTEMP':'jh7TMPK  ':'*LIBL':'jh7TMPK  ');
    jmis03cl('QTEMP':'jh7TMPR  ':'*LIBL':'jh7TMPR  ');
    jmis03cl('QTEMP':'jh7TMPR2 ':'*LIBL':'jh7TMPR2 ');
    jmis03cl('QTEMP':'jh7TMPD  ':'*LIBL':'jh7TMPD  ');
    qPrintLog('*** Override Temp Files.');
    err = executeCommand('OVRDBF FILE(jhTMP7IN) TOFILE(QTEMP/jh7TMPIN) OVRSCOPE(*JOB)');
    err = executeCommand('OVRDBF FILE(jh7TMPK)  TOFILE(QTEMP/jh7TMPK)  OVRSCOPE(*JOB)');
    err = executeCommand('OVRDBF FILE(jh7TMPR)  TOFILE(QTEMP/jh7TMPR)  OVRSCOPE(*JOB)');
    err = executeCommand('OVRDBF FILE(jh7TMPR2) TOFILE(QTEMP/jh7TMPR2) OVRSCOPE(*JOB)');
    err = executeCommand('OVRDBF FILE(jh7TMPD)  TOFILE(QTEMP/jh7TMPD)  OVRSCOPE(*JOB)');
    qPrintLog('*** Clean Out Temp Files.');
    err = executeCommand('CLRPFM FILE(QTEMP/jh7TMPIN) ');
    err = executeCommand('CLRPFM FILE(QTEMP/jh7TMPD ) ');
    err = executeCommand('CLRPFM FILE(QTEMP/jh7TMPK ) ');
    err = executeCommand('CLRPFM FILE(QTEMP/jh7TMPR ) ');
    err = executeCommand('CLRPFM FILE(QTEMP/jh7TMPR2) ');
    qPrintLog('*** Server Data Queue Starting.');
    open jh7tmpIn;
    dow 'Day' <> 'Night';
      if 'END' = ReadEndDataQueue;
        qPrintLog('*** Server Ending From Data Queue End.');
        leave;
      endif;
      ReadDataQueue();
      qPrintLog('*** Reading Data Queue.');
      if In7Data <> *blank;
        qPrintLog('*** Working with HL7 Data.');
        exsr WriteSr;
        close jh7TmpIn;
        exsr callProgramsForMessage;
        qPrintLog('*** CLEAR TEMP FILE: QTEMP/jh7TMPIN.');
        Err = err = executeCommand('CLRPFM FILE(QTEMP/jh7TMPIN)');
        open jh7TMPIn;
      endif;
      LogData = *blank;
      In7Data = *blank;
    enddo;
    qPrintLog('*** All Done!');
    close jh7TmpIn;
  endif;
endif;
qPrintClose();

err = executeCommand('DLTOVR FILE(jh7TMPIN ) ');
err = executeCommand('DLTOVR FILE(jh7TMPK  ) ');
err = executeCommand('DLTOVR FILE(jh7TMPR  ) ');
err = executeCommand('DLTOVR FILE(jh7TMPR2 ) ');
err = executeCommand('DLTOVR FILE(jh7TMPD  ) ');
err = executeCommand('DLTOVR FILE(QSYSPRT  ) ');

err = executeCommand('RCLRSC ');

*inlr = *on;
//#----------------------------------------------------------------------------
begsr WriteSr;
  IN7COUNTER = 1;
  LogData    = In7Data;
  LOGCOUNTER = IN7COUNTER;
  LOGDATIM   = %timeStamp();
  LOGJOB#    = %char(pgmPsds.jobNumber);
  write LOGFILER;
  write HL7TMPINR;
  exsr parseMshSegment;
endsr;
//#----------------------------------------------------------------------------
//
// Copy books subroutines.
//
/copy cb/getField.rpgle
/copy cb/callProgramsForMessage.rpgle

/copy cb/svr_parseMshSegment.rpgle
/copy cb/svr_srSetEnvProgramsToCall.rpgle
/copy cb/svr_srSetEnvSperators.rpgle
//#----------------------------------------------------------------------------
dcl-proc CLEARTEMPFILES;
  dcl-pi CLEARTEMPFILES       char(7);
  end-pi;
  qPrintLog('*** CLEAR TEMP FILE: QTEMP/jh7TMPD.');
  err = executeCommand('CLRPFM FILE(QTEMP/jh7TMPD)');

  qPrintLog('*** CLEAR TEMP FILE: QTEMP/jh7TMPK.');
  err = executeCommand('CLRPFM FILE(QTEMP/jh7TMPK)');

  qPrintLog('*** CLEAR TEMP FILE: QTEMP/jh7TMPR.');
  err = executeCommand('CLRPFM FILE(QTEMP/jh7TMPR)');

  return 'CLEAN  ';
end-proc CLEARTEMPFILES;
//#----------------------------------------------------------------------------
dcl-proc ReadEndDataQueue;
  dcl-pi *n                   char(10);
  end-pi;

// CRTDTAQ DTAQ(jh7ENDDTAQ) MAXLEN(10) SIZE(*MAX2GB)

  dcl-s EndQueueData          char(10);
  dcl-s EndQueueSize        packed(5:0);
  dcl-s EndQueueWait        packed(5:0);

  EndQueueSize = 10;
  EndQueueWait = 0;

  QRCVDTAQ(is_endQueueName:is_endQueueLibrary:EndQueueSize:In7Data:EndQueueWait);

  return EndQueueData;
end-proc;
//#----------------------------------------------------------------------------
dcl-proc ClearEndDataQ;

  QCLRDTAQ(is_endQueueName:is_endQueueLibrary);

end-proc;
//#----------------------------------------------------------------------------
dcl-proc ReadDataQueue;

// CRTDTAQ DTAQ(SHINQ) MAXLEN(32000) SIZE(*MAX2GB) TEXT('This is used to end the hl7 data queue interface')

  dcl-s DataQueueSize       packed(5:0);
  dcl-s DataQueueWait       packed(5:0);

  DataQueueSize = 32000;
  DataQueueWait = 10;

  QRCVDTAQ(is_dataQueueName:is_dataQueueLibrary:DataQueueSize:In7Data:DataQueueWait);

end-proc;
//#----------------------------------------------------------------------------
/copy ../cb_rpgle/generalSystemOs/executeCommand.rpgle
/copy ../cb_rpgle/print/qprint_print.rpgle
