  **free

  ctl-opt option(*srcstmt) dftactgrp(*no) ;

  dcl-pr OpenFile pointer extproc('_C_IFS_fopen') ;
    *n pointer value ;  // File name
    *n pointer value ;  // File mode
  end-pr ;

  dcl-pr WriteFile pointer extproc('_C_IFS_fputs') ;
    *n pointer value ;  // String to write
    *n pointer value ;  // Open mode
  end-pr ;

  dcl-pr CloseFile extproc('_C_IFS_fclose') ;
    *n pointer value ;  // Misc pointer
  end-pr ;

  dcl-s PathFile char(50) ;
  dcl-s OpenMode char(100) ;
  dcl-s FilePtr pointer inz ;
  dcl-s SndData char(32767) ;
  dcl-s i packed(3) ;

  PathFile = '/tmp/test_write.txt' + x'00' ;
  OpenMode = 'w, o_ccsid=1252' + x'00' ;
  FilePtr = OpenFile(%addr(PathFile):%addr(OpenMode)) ;

  if (FilePtr = *null) ;
    dsply ('Unable to open file (1)') ;
    return ;
  endif ;

  CloseFile(%addr(PathFile)) ;
  OpenMode = 'w' + x'00' ;  // Clear file, then write to file
  FilePtr = OpenFile(%addr(PathFile):%addr(OpenMode)) ;

  if (FilePtr = *null) ;
     dsply ('Unable to open file (2)') ;
     return ;
  endif ;

  for i = 1 to 10 ;
    SndData = 'Write No. ' + %char(i) ;
    WriteFile(%addr(SndData):FilePtr) ;
  endfor ;
  
  CloseFile(%addr(PathFile)) ;
