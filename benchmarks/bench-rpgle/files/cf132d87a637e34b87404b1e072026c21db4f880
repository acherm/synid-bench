        Ctl-opt option(*srcstmt:*nodebugio);
        Ctl-opt dftactgrp(*no) actgrp(*caller);

        Dcl-s MessageText varchar(32740);
        Dcl-s MessageLength int(5);
        Dcl-s ResponseMsg Varchar(9999);
        Dcl-s ResponseHeader Varchar(1000);
        Dcl-s ResponsePos Packed(4);
        Dcl-s ReturnedSQLCode char(5);
        Dcl-s header Char(200);

        Dcl-c Url const('https://gorest.co.in/public-api/users');

        Dcl-pr system zoned(10:0) extproc('system');
          szcmd pointer Value Options(*String);
        End-pr;

        //***********************************************************************
        // MainLine
        //***********************************************************************
          *inlr = *on;

          Exec sql set option commit = *none;

          Exec sql CALL QSYS2.QCMDEXC('CHGJOB CCSID(37)');

          header =
                '<httpHeader>'                                              +
                     '<header name="Content-Type" value="text/plain">'+
                   '</header>'                                              +
                '</httpHeader>';


          Exec sql

            Select Coalesce(Varchar(ResponseMsg,9999),' '),
                   Varchar(ResponseHttpHeader,1000) into :ResponseMsg,
                                                         :ResponseHeader
            From Table(Systools.HttpGetClobVerbose(Trim(:Url),
                                                   Trim(:header)))
                                                    as InternalServices;

          Diagnostics();
          If ReturnedSqlCode = *Blanks;
            dsply 'OK response with HttpGetClobVerbose';
          Else;
            dsply 'Error';
          EndIf;
        //***********************************************************************
        // Diagnostics - get sql details
        //***********************************************************************
          Dcl-proc Diagnostics ;

            Exec sql GET DIAGNOSTICS CONDITION 1
              :ReturnedSqlCode = DB2_RETURNED_SQLCODE,
              :MessageLength = MESSAGE_LENGTH,
              :MessageText = MESSAGE_TEXT;


          End-proc ;
