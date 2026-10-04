**free
//-------------------------------------------------------------------*
//Empresa. . . . . . : IB Systems S.A.                               *
//Sistema. . . . . . : Sistema de Administracion de Tarjeta          *
//Programa . . . . . : SATW0002                                      *
//Descripcion. . . . : Consulta Alfabetica de Cliente                *
//Autor. . . . . . . : Staff IBSystems S.A.                          *
//Analista. . .  . . : VICTOR M HOWLEY.                              *
//Fecha Creacion . . : ENERO 11, 2022                                *
//-------------------------------------------------------------------*

//-------------------------------------------------------------------*
Ctl-opt OPTION(*SRCSTMT: *NODEBUGIO) BNDDIR('QC2LE');
//-------------------------------------------------------------------*

Dcl-pr ReadFromWeb  ExtProc('QtmhRdStin');
       szRtnBuffer  Char(1677310)Options(*Varsize);
       nBufLen      Int(10)Const;
       nRtnLen      Int(10);
       Errorcod     Char(8000)Options(*Varsize);
End-Pr;


Dcl-PR WriteToWeb  ExtProc('QtmhWrStout');
 DataVar     Char(1677310) Options(*Varsize);
 DataVarLen  Int(10)     Const;
 ErrorCode   Char(8000)  Options(*Varsize);
End-Pr;



dcl-pr Translate  ExtPgm('QDCXLATE');
     *N  packed(5:0) const;
     *N  char(1677310) Options(*varsize);
     *N  char(10)    const;
end-pr;


Dcl-PR  GetEnv       pointer   ExtProc('getenv');
 *N     pointer   value Options(*string);
End-Pr;


//-----------ALL DATA STRUCTURES------------------
Dcl-Ds     ErrDs       QUALIFIED;
 byteProv  Int(10)inz(0);
 byteAvail Int(10)inz(0);
End-Ds;


Dcl-C CRLF        x'0d25';
Dcl-S HTML        Char(100);
Dcl-S Url         Char(100);
Dcl-s ContentType Char(100);
Dcl-s Hlocation Char(100);
Dcl-s ReqMethod   Char(20);

   //Campos archivos//
Dcl-S Parm       Char(100) inz;
Dcl-S Par        Char(2) inz;
Dcl-S Par2       Char(2) inz;
Dcl-S pos        int(10);
Dcl-s RtnBuffer  Char(500)Inz;
Dcl-s RtnLen     Int(10);
Dcl-s nRtBufLen  int(10);



 Dcl-PR CONSUW001  extpgm('CONSUW001');
   FString         Char(1677310);
   Fpar            CHAr(2);
   FMSJ            CHAR(1677310);
   End-PR;

Dcl-s RESPONSE char(1677310);
DCL-S STRING   CHAR(1677310);



//limpia todos los campos
      html = 'Content-Type: text/html; '+crlf
                                        +crlf;
      WriteToWeb(HTML: %len(%trim(HTML)): ErrDs);

      URL  = %Str( GetEnv('REQUEST_URI') );
      ContentType = %str( GetEnv('CONTENT_TYPE') );
      Parm = '/SERVICE/';
      pos  = %scan (%Trim(Parm):URL) + %len(%Trim(Parm));
      par = %Subst(URL:pos:2);//parametro para condiciones

      ReadFromWeb(rtnBuffer: %size(rtnBuffer): rtnlen : ErrDs);

        STRING= %trim(rtnBuffer);
        Translate(%len(%trim(STRING)): STRING: 'QTCPEBC');



//    IF par = 'CO' or par ='VT' OR PAR = 'TS' or PAR = 'SW' or par='SV' or par = 'TR';
  //si la variable PAR es igual a "CO" LLAMAR A PROGRAMA PARA CONSULTAS (CONSUW001)
CLEAR RESPONSE;
        CALLP CONSUW001(STRING:PAR:RESPONSE);
      WriteToWeb(response: %len(%trim(response)): ErrDs);
//    endif;
        *INLR=*ON;
        return;


