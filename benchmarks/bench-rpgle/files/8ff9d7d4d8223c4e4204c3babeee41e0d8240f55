**free

/copy ../cb_rpgle/genericHeaders/controlOptions.rpgle
//#----------------------------------------------------------------------------
//
//  Write XML file.
//
//#----------------------------------------------------------------------------

dcl-f JH7TMPR                keyed usrOpn;                                       // HOLD REPORT
//dcl-f JH7TMPD                // H USROPN;                                        // HOLD DOCUMENT INFO HOLD DTD
/copy cb/dclf_JH7TMPD_tempPageFormat.rpgle
/copy cb/dclf_JH7TMPK_tempKeys.rpgle
dcl-f JH7DTD70L1             keyed usrOpn;
dcl-f JH7XML10L1             keyed usrOpn; // XML File Locations

/copy ../cb_rpgle/print/qprint_dclf.rpgle

// Procedure Interface
dcl-pi *n;
  enviornment             likeds(enviornmentTemplate);
end-pi;

/copy ../cb_rpgle/ifsStmf/openFile.rpgle
/copy ../cb_rpgle/ifsStmf/writeFile.rpgle
/copy ../cb_rpgle/ifsStmf/closeFile.rpgle

/copy cb/general_dcl.rpgle
/copy cb/environment_ds.rpgle
/copy ../cb_rpgle/constants/trueFalse.rpgle
/copy ../cb_rpgle/genericHeaders/programStatusDataStructure.rpgle

dcl-c cCONTAINER                 'cCONTAINER';
dcl-c DATA                      'Data';
dcl-c cDATE                      'Date';
dcl-c cDESCRIPTION               'Description';
dcl-c cDOCUMENT                  'DOCUMENT';
dcl-c cFILEDATASTART             '<![CDATA[';
dcl-c cFILEDATASTOP              ']]>';
dcl-c FILENAME                  'FileName';
dcl-c cFILES                     'Files';
dcl-c cFOLDER                    'FOLDER';
dcl-c cHEADER                    'Header';
dcl-c cINDEXING                  'Indexing';
dcl-c cINDEXVALUES               'IndexValues';
dcl-c cIMPORTPATH                'ImportPath';
dcl-c cKEYWORD                   'Keyword';
dcl-c cLF                        X'25';
dcl-c cOBJECT                    'Object';
dcl-c cPROCESS                   'Process';
dcl-c cPROPERETY                 'Property';
dcl-c cREQUEST                   'Request';
dcl-c cTYPE                      'Type';
dcl-c cTYPEIDTAG                 'TypeID';
dcl-c cVALUE                     'Value';
dcl-c cWORKFLOWVAL               'WorkFlowValues';
dcl-c cWORKFLOWVAR               'WorkFlowVariable';
dcl-c cNAMETAG                   'Name';
dcl-c cSEARCHABLETAG             'Searchable';

dcl-s SP                    char(28) dim(10);
dcl-s FILE_1             pointer;
dcl-s FILE_2             pointer;
dcl-s FilNam_1              char(200);
dcl-s FilNam_1B             char(200);
dcl-s FilNam_2              char(200);
dcl-s FilNam_2B             char(200);
dcl-s ReportFile1        pointer;
dcl-s ReportFile2        pointer;
dcl-s ReportFileName1       char(200);
dcl-s ReportFileName2       char(200);
dcl-s ReportFileName     varchar(100);

dcl-s RC                     int(10:0);
dcl-s ERR                   char(7);
dcl-s Couter               zoned(9:0) inz(0);
dcl-ds *N;
  TIMENOW             timeStamp;
  TIMEDATE                 char(22) Pos(1);
end-ds;




SP(1) = '';
SP(2) = '**';
SP(3) = '****';
SP(4) = '******';
SP(5) = '********';
SP(6) = '**********';
SP(7) = '************';
SP(8) = '**************';
SP(9) = '****************';

TIMENOW = %timeStamp();
//#----------------------------------------------------------------------------
  openJH7TMPD();
  openJH7TMPK();
  open JH7TMPR;
  open JH7DTD70L1;
  open JH7XML10L1;
  if enviornment.logToPrinter = 'Y';
    qPrintOpen();
  endif;
//#-----------------------------
chain (enviornment.id) HL7XML10R;
if %found(JH7XML10L1);
  
  XML10LOG = %upper(XML10LOG);
  
  ERR = yOpenIfsFile;

  read HL7TMPDR;                                                        //    I
  ERR = DtdTags;                                                        // Write DTD
  ERR = StartFreeLine('<' + cREQUEST + ' ' + cTYPE +                         // Start Request line
    '="IMPORT" version="1.02" JH7="' + pgmPsds.compileDate + '_' + pgmPsds.compileTime + '" >');

  ERR = StartTag(cHEADER);                                               // Start Header line
  ERR = ConvertToHeader;                                                // Write Header Line
  ERR = StopTag(cHEADER);                                                // Stop Header Line
  
  ERR = StartTag('Keys');
  loopThroughkeys();
  ERR = StopTag('Keys');
  
  
  ERR = WriteFolderObj;                                                 // Start Object Folder
  ERR = WriteDocumeObj;                                                 // Start Object Documen

  ERR = StopTag(cREQUEST);                                               // Stop REquest Tag
  yCloseIfsFile();                                                      // (All done. Bye Dave)

else;
  qPrintLog('<<< No config in HL7XML10 for nviornment ' + %trim(enviornment.id) + '.');
endif;
  //#-----------------------------
  closeJH7TMPK();
  closeJH7TMPD();
  close JH7TMPR;
  close JH7DTD70L1;
  close JH7XML10L1;
  qPrintClose();
  
if enviornment.testingFlag = 'Y';
  *inlr = *on;
endif;
return;
//#----------------------------------------------------------------------------
dcl-proc ConvertToHeader;
  dcl-pi ConvertToHeader      char(7);
  end-pi;
//  dcl-s KEY                   char(10) inz('_CONVERTTO');
//  dcl-s TmpEnvPath            char(100) inz;

//  ERR = StartTag(cFILES);
//  chain (KOBJ:KGROUP) HL7TMPKR2;
//  if K2TMPVAL = 'y' or K2TMPVAL = 'Y';
//    if %eof(JH7TMPD) = *off;
//      ERR = FreeLine('<ConvertTo Value="application/vnd.ibm-modca"' +
//      '" TopMargin="'   + %trim(D3TOPMAR)  +
//      '" LeftMargin="'  + %trim(D3LFTMAR)  +
//      '" PageWidth="'   + %trim(D3PAGWTH)  +
//      '" PageLength="'  + %trim(D3PAGLEN)  +
//      '" LineSpacing="' + %trim(D3LINSPC)  +
//      '" FontWidth="'   + %trim(D3FNTWTH)  +
//      '" RecLength="'   + %trim(D3RECLNG)  +
//      '" LinesPerPage="'+ %trim(D3LINPAG)  +
//      '" OverlayName="' + %trim(D3OVERLAY) +
//      '" />');
//    else;
//      ERR = FreeLine('<ConvertTo Value="application/vnd.ibm-modca" />');
//    endif;
//  endif;
//  TmpEnvPath = tempKeyGetValue('_PATHNAME1');
//  if TmpEnvPath = *blank;
//    TmpEnvPath = ENVPATH;
//  endif;
//  ERR = StartFreeLine('<' + cIMPORTPATH + ' ' + cVALUE + '="' + %trim(TmpEnvPath) + '" />');

//  ERR = %char(SETTAB('-'));
//  ERR = StopTag(cFILES);                                               //      Stop File line
  return 'HEADER ';
end-proc ConvertToHeader;
//#----------------------------------------------------------------------------
dcl-proc FreeLine;
  dcl-pi FreeLine             char(7);
    INSTRIN               varchar(32767) value;
  end-pi;
  dcl-s ERR                   char(7) inz;

  ERR =  WriteLineToIFS(ApplyTab(%trimR(INSTRIN)));

  ERR = %char(SETTAB('-'));
  return 'FREELIN';
end-proc FreeLine;
//#----------------------------------------------------------------------------
dcl-proc StartFreeLine;
  dcl-pi StartFreeLine        char(7);
    INSTRIN               varchar(32767) value;
  end-pi;
  dcl-s ERR                   char(7) inz;

  ERR =  WriteLineToIFS(ApplyTab(
  %trimR(INSTRIN)));
  return 'FREELIN';
end-proc StartFreeLine;
//#----------------------------------------------------------------------------
dcl-proc WriteLineToIFS;
  dcl-pi WriteLineToIFS       char(7);
    INSTRIN               varchar(32767) value;
  end-pi;

  rc = ifsWriteFile(%trimR(INSTRIN) + cLF: FILE_1);

  if XML10LOG = 'Y';
    rc = ifsWriteFile(%trimR(INSTRIN) + cLF: FILE_2);
  endif;

  return 'WRTIFS ';
end-proc WriteLineToIFS;
//#----------------------------------------------------------------------------
dcl-proc WriteReportFile;
  dcl-pi WriteReportFile      char(7);
    INSTRIN               varchar(32767) value;
  end-pi;

  rc = ifsWriteFile(INSTRIN + cLF: ReportFile1);

  if XML10LOG = 'Y';
    rc = ifsWriteFile(INSTRIN + cLF: ReportFile2);
  endif;

  return 'WRTIFS ';
end-proc WriteReportFile;
//#----------------------------------------------------------------------------
dcl-proc ApplyTab;
  dcl-pi ApplyTab          varchar(32767);
    INSTRIN               varchar(32767) value;
  end-pi;
  return CleanTab( %trim(SP(SETTAB('+'))) + %trimR(INSTRIN) );
end-proc ApplyTab;
//#----------------------------------------------------------------------------
dcl-proc SetTab;
  dcl-pi SetTab              zoned(9:0);
    INSTRIN                  char(1) value;
  end-pi;

  if INSTRIN = '+';
    Couter = Couter + 1;
  endif;
  if INSTRIN = '-';
    Couter = Couter - 1;
  endif;
  if Couter < 1;
    Couter = 1;
  endif;
  return Couter;
end-proc SetTab;
//#----------------------------------------------------------------------------
dcl-proc CleanTab;
  dcl-pi CleanTab          varchar(32767);
    INSTRIN               varchar(32767) value;
  end-pi;

  dcl-c STARTCHAR                 '<';
  dcl-s start                zoned(5:0) inz(1);
  dcl-s WrkStr                char(1) inz;
  dcl-s WrkCtr               zoned(5:0) inz(1);

  if INSTRIN <> *blank OR  '**' = %SUBST(INSTRIN:1:2);
    dow %SUBST(INSTRIN:WrkCtr:1) <> StartChar AND %LEN(%trimR(INSTRIN)) > WrkCtr;
      if %SUBST(INSTRIN:WrkCtr:1) = '*';
        %SUBST(INSTRIN:WrkCtr:1) = ' ';
      endif;
      WrkCtr = WrkCtr + 1;
    enddo;
  endif;
  return INSTRIN;
end-proc CleanTab;
//#----------------------------------------------------------------------------
dcl-proc StartTag;
  dcl-pi StartTag             char(7);                                // <tag>
    INSTRIN               varchar(32767) value;
  end-pi;
  dcl-s ERR                   char(7) inz;
  ERR =  WriteLineToIFS(ApplyTab('<' + INSTRIN + '>'  ));
  return 'STARTAG';
end-proc StartTag;
//#----------------------------------------------------------------------------
dcl-proc StopTag;
  dcl-pi StopTag              char(7);
    INSTRIN               varchar(32767) value;
  end-pi;
  dcl-s ERR                   char(7) inz;
  ERR = %char(SETTAB('-'));
  ERR =  WriteLineToIFS(ApplyTab('</' + INSTRIN  + '>'  ));
  ERR = %char(SETTAB('-'));
  return 'STOPTAG';
end-proc StopTag;
//#----------------------------------------------------------------------------
dcl-proc DtdTags;
  dcl-pi DtdTags              char(7);
  end-pi;
  dcl-s ERR                   char(7) inz;
  read HL7170R;
  dow %eof(JH7DTD70L1) = *OFF;
    ERR = WriteLineToIFS(DATLIN);
    read HL7170R;
  enddo;
  return 'DtdTags';
end-proc DtdTags;
//#----------------------------------------------------------------------------
dcl-proc WriteKeywordTag;
  dcl-pi Writekeywordtag      char(7);
  end-pi;
  dcl-s ERR                   char(7);
  dcl-s StringLine            char(32767);

  StringLine = '<' + cKEYWORD + ' ' + cNAMETAG + '="' + %trimR(TMPKEY) + '"' + ' ' + cVALUE + '="'+ %trimR(TMPVAL) + '" ' + cTYPE + '="';
//  select;
//    when TMPTYPEX   = 'I';
//      StringLine = %trim(StringLine) + cINDEXING;
//    when TMPTYPEX   = 'W';
//      StringLine = %trim(StringLine) + cWORKFLOWVAR;
//    other;
//  endsl;

//  if TMPSERCH <> *blank AND TMPTYPEX <> 'W';
//    StringLine = %trim(StringLine) + '" ' + cSEARCHABLETAG + '="' + %trim(TMPSERCH);
//  endif;
  ERR = FreeLine(%trim(StringLine) + '" />');
  return 'KEYTAG ';
end-proc;
//#----------------------------------------------------------------------------
dcl-proc WriteValueTags;
  dcl-pi WriteValueTags       char(7);
  end-pi;
//  dcl-s ERR                   char(7);
//  dcl-s TMPSTR                char(32000);
//  select;
//    when TMPKEYT = 'K';
//      ERR = WriteKeywordTag;
//    when TMPKEYT = 'C';
//      ERR = FreeLine('<' + cCONTAINER + ' ' +
//      cNAMETAG + '="' + %trimR(TMPKEY) + '" ' +
//      cTYPE + '="' + %trimR(TMPVAL) + '" />');
//    when TMPKEYT = 'P';
//      ERR = FreeLine('<' + cPROPERETY + ' ' +
//      cNAMETAG + '="' + %trimR(TMPVAL) + '" ' +
//      cTYPE + '="' + %trimR(TMPKEY) + '" />');
//    when TMPKEYT = 'R';
//      TMPSTR  =      '<' + cPROCESS + ' ' +
//      cNAMETAG + '="' + %trimR(TMPVAL) + '" ' +
//      cTYPEIDTAG +'="';
//      select;
//        when TMPcTYPEX = '2';
//          TMPSTR = %trim(TMPSTR) + '02';
//        other;
//          TMPSTR = %trim(TMPSTR) + '01';
//      endsl;
//      ERR = FreeLine(%trim(TMPSTR) + '" />' );
//    when TMPKEYT = 'D';
//      ERR = FreeLine('<' + cDESCRIPTION + ' ' +
//      cVALUE + '="' + %trimR(TMPVAL) + '" />' );
//    other;
//  endsl;
  return 'ValueTa';
end-proc;
//#----------------------------------------------------------------------------
dcl-proc WriteIndexTags;
  dcl-pi WriteIndexTags       char(7);
    INSTR                    char(1) value;
  end-pi;
//  dcl-s ERR                   char(7);
//  dcl-s kobj                  char(1);
//  dcl-s kgroup                char(1) inz('I');
//  kobj = INSTR;
//  chain (KOBJ:KGROUP) HL7TMPKR;
//  if %FOUND(2L1) = *ON;
//    TMPVAL = CleanStringForX(TMPVAL);
//    ERR = StartTag(cINDEXVALUES);
//    dou %eof(JH7TMPKL1) = *ON;
//      ERR = WriteValueTags;
//      reade (KOBJ:KGROUP) HL7TMPKR;
//      TMPVAL = CleanStringForX(TMPVAL);
//    enddo;
//    ERR = StopTag(cINDEXVALUES);
//  endif;
  return 'IndexTa';
end-proc;
//#----------------------------------------------------------------------------
dcl-proc WriteWorkflowTags;
  dcl-pi WriteWorkflowTags      char(7);
    INSTR                    char(1) value;
  end-pi;
//  dcl-s ERR                   char(7);
//  dcl-s kobj                  char(1);
//  dcl-s kgroup                char(1) inz('W');
//  kobj = INSTR;
//  chain (KOBJ:KGROUP) HL7TMPKR;
//  TMPVAL = CleanStringForX(TMPVAL);
//  if %FOUND(JH7TMPKL1) = *ON;
//    ERR = StartTag(cWORKFLOWVAL);
//    dou %eof(JH7TMPKL1) = *ON;
//      ERR = WriteValueTags;
//      reade (KOBJ:KGROUP) HL7TMPKR;
//      TMPVAL = CleanStringForX(TMPVAL);
//    enddo;
//    ERR = StopTag(cWORKFLOWVAL);
//  endif;
  return 'WorkFlo';
end-proc WriteWorkflowTags;
//#----------------------------------------------------------------------------
dcl-proc WriteReport;
  dcl-pi WriteReport          char(7);
  end-pi;
  dcl-s ERR                   char(7) inz;
  dcl-s linebuff              char(500) inz;
  dcl-s ttt                   char(1) inz('s');


  ERR = OpenReportFile;
  read HL7TMPRR;
  *IN70 = %eof();
  dou *In70 = *On;
    Err = WriteReportFile(%trimR(TMPRPT));
    read HL7TMPRR;
    *IN70 = %eof();
  enddo;
  ERR = CloseReportFile;

  ERR = %char(SETTAB('-'));
  return 'REPORT ';
end-proc;
//#----------------------------------------------------------------------------
dcl-proc yOpenIfsFile;
  dcl-pi yOpenIfsFile          ind;
  end-pi;

  FILNAM_1 = %trim(XML10PATH) + 'FROM.HL7.' + %trim(TIMEDATE) + '.' + %trim(%char(pgmPsds.jobNumber)) + '.TMP';
  FILE_1 = ifsOpenFile(%trimR(FilNam_1):'w, codepage=819');                                               // 850 437
  ifsCloseFile(FILE_1);
  FILE_1 = ifsOpenFile(%trimR(FilNam_1):'w');
  if FILE_1 = *null;
    qPrintLog('<<< Open of file '+FILNAM_1+ 'failed.');
  endif;
  if XML10LOG = 'Y';
    FILNAM_2 = %trim(XML10LOGPT) + 'FROM.HL7.' + %trim(TIMEDATE) + '.' + %trim(%char(pgmPsds.jobNumber)) + '.TMP';
    FILE_2 = ifsOpenFile(%trimR(FilNam_2): 'w, codepage=819');                                             // 850
    ifsCloseFile(FILE_2);
    FILE_2 = ifsOpenFile(%trimR(FilNam_2):'w');
    if FILE_2 = *null;
      qPrintLog('<<< Open of file '+FILNAM_2+'failed.');
    endif;
  endif;
  return true;
end-proc;
//#----------------------------------------------------------------------------
dcl-proc yCloseIfsFile;
//  dcl-pi yCloseIfsFile         ind;
//  end-pi;
  ifsCloseFile( FILE_1 );
  FILNAM_1B = 'FROM.HL7.' + %trim(TIMEDATE) + '.' + %trim(%char(pgmPsds.jobNumber)) + '.XML';
  ERR = executeCommand('RNM OBJ("' + %trim(FILNAM_1) + '") NEWOBJ("' + %trim(FILNAM_1B) + '")');
  if XML10LOG = 'Y';
    ifsCloseFile( FILE_2 );
    FILNAM_2B = 'FROM.HL7.' + %trim(TIMEDATE) + '.'  + %trim(%char(pgmPsds.jobNumber)) + '.XML';
    ERR = executeCommand('RNM OBJ("' +  %trim(FILNAM_2) + '") NEWOBJ("' + %trim(FILNAM_2B) + '")');
  endif;
//  return true;
end-proc;
//#----------------------------------------------------------------------------
dcl-proc OpenReportFile;
  dcl-pi OpenReportFile       char(7);
  end-pi;

//  dcl-s FileExt               char(10) inz('_FILEEXT1');

//  chain FileExt HL7TMPKR2;
//  if %Found(JH7TMPKL2) = *Off;
//    K2TMPVAL = *blank;
//  endif;
//  ReportFileName1 = %trim(XML10PATH) + 'FROM.HL7.' + %trim(TIMEDATE) + '.' + %trim(%char(pgmPsds.jobNumber)) + '.' + %trim(K2TMPVAL);
//  ReportFileName = 'FROM.HL7.' + %trim(TIMEDATE) + '.' + %trim(%char(pgmPsds.jobNumber)) + '.' + %trim(K2TMPVAL);
//  ReportFile1 = ifsOpenFile(%trim(ReportFileName1):'w, codepage=819');
//  rc = ifsCloseFile(ReportFile1);
//  ReportFile1=ifsOpenFile(%trim(ReportFileName1):'w');
//  if ReportFile1 = *null;
//    qPrintLog('<<< Open of file ' + ReportFileName1 + 'failed.');
//  endif;
//  if XML10LOG = 'Y';
//    ReportFileName2 = %trim(XML10LOGPT) + 'FROM.HL7.' + %trim(TIMEDATE) + '.' + %trim(%char(pgmPsds.jobNumber)) + '.' + %trim(K2TMPVAL);
//    ReportFile2 = ifsOpenFile(%trim(ReportFileName2):'w, codepage=819');
//    rc = ifsCloseFile(ReportFile2);
//    ReportFile2=ifsOpenFile(%trim(ReportFileName2):'w');
//    if ReportFile2 = *null;
//      qPrintLog('<<< Open of file ' + ReportFileName2 + 'failed.');
//    endif;
//  endif;
  return 'OPENRPT';
end-proc;
//#----------------------------------------------------------------------------
dcl-proc CloseReportFile;
  dcl-pi CloseReportFile      char(7);
  end-pi;
  ifsCloseFile(ReportFile1);
  if XML10LOG = 'Y';
    ifsCloseFile(ReportFile2);
  endif;
  return 'CLOSERP';
end-proc CloseReportFile;
//#----------------------------------------------------------------------------
dcl-proc WriteFolderObj;
  dcl-pi WriteFolderObj       char(7);
  end-pi;
  dcl-s ERR                   char(7);
  dcl-s Key                   char(1) inz('F');

//  chain (KOBJ:KGROUP) HL7TMPKR;
//  if %FOUND(JH7TMPKL1) = *ON;
//    ERR = StartFreeLine('<' + cOBJECT + ' ' + cTYPE + '="' + cFOLDER + '" >' );
//    ERR = WriteIndexTags(Key);
//    ERR = WriteWorkflowTags(Key);
//    ERR = StopTag(cOBJECT);
 // endif;


  return 'ObjFold';
end-proc WriteFolderObj;
//#----------------------------------------------------------------------------
dcl-proc WriteDocumeObj;
  dcl-pi WriteDocumeObj       char(7);
  end-pi;
  dcl-s ERR                   char(7);
  dcl-s Key                   char(1) inz('D');

  ERR = StartFreeLine('<' + cOBJECT + ' ' + cTYPE + '="' + cDOCUMENT + '" >' );
  ERR = WriteIndexTags(Key);
  ERR = WriteWorkflowTags(Key);
  ERR = StartTag(cFILES);                                              // Start Files Tag
  if tempKeyGetValue('_WHERERPT1') <> 'EXTERNAL';
    ERR = WriteReport;                                                //  81 Write Report
  else;
    ReportFileName = tempKeyGetValue('_FILENAME1');
  endif;
  ERR = %char(SETTAB('+'));
  ERR = FreeLine('<FileType Value="' + %trimr(D3FILETYP1) + '" />'); // text/plain
  if D3DATATYP1 <> *blank;
    ERR = StartFreeLine('<' + FILENAME + ' ' + cVALUE + '="' + ReportFileName  + '" Encoding="' + %trimR(D3DATATYP1) + '" />');//  Text
  else;
    ERR = StartFreeLine('<' + FILENAME + ' ' + cVALUE + '="' + ReportFileName  + '" />');
  endif;                                                              // -/
  ERR = %char(SETTAB('-'));
  ERR = StopTag(cFILES);                                               // Stop Files Tag
  ERR = StopTag(cOBJECT);
  return 'ObjDoc';
end-proc WriteDocumeObj;
//#----------------------------------------------------------------------------
dcl-proc CleanStringForX;

  dcl-pi CleanStringForX   varchar(32767);
    InString              varchar(32767);
  end-pi;

  dcl-s Pos                  zoned(5:0) inz(1);
  dcl-s CurrentChar           char(1) inz;

  if InString <> *blank;
    dow Pos < %Len(%trimr(InString));
      CurrentChar = %Subst(InString:Pos:1);
      select;
        when '&' = CurrentChar;
          InString = %Replace('&amp;':InString:Pos:1);
        when '<' = CurrentChar;
          InString = %Replace('&lt;':InString:Pos:1);
        when '>' = CurrentChar;
          InString = %Replace('&gt;':InString:Pos:1);
        when X'7D' = CurrentChar;
          InString = %Replace('&apos;':InString:Pos:1);
        when '"' = CurrentChar;
          InString = %Replace('&quot;':InString:Pos:1);
        other;
      endsl;
      Pos = Pos + 1;
    enddo;
  endif;
  return InString;
end-proc;
//#----------------------------------------------------------------------------
dcl-proc loopThroughkeys;
  setll *start JH7TMPK;
  read JH7TMPK;
  dou %eof(JH7TMPK);
    Err = Writekeywordtag();
    read JH7TMPK;
  enddo;
end-proc;
//#----------------------------------------------------------------------------
/copy ../cb_rpgle/print/qprint_print.rpgle
/copy ../cb_rpgle/generalSystemOs/executeCommand.rpgle

/copy cb/tempKeys.rpgle
/copy cb/proc_JH7TMPD_tempPageFormat.rpgle
/copy cb/proc_JH7TMPK_tempKeys.rpgle