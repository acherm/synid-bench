     H option(*srcstmt:*noshowcpy) actgrp(*new) dftactgrp(*no)
     H bnddir('HDIILE/HDIBDIR')
     H alwnull(*usrctl)
      * ************************************************************ *
      * WSRAXP: QUOM Versión 2                                       *
      *         Asegurado de una póliza.                             *
      * ------------------------------------------------------------ *
      * Sergio Fernandez                     *05-Jun-2017            *
      * ------------------------------------------------------------ *
      * Modificaciones:                                              *
      * JSN 28/02/2019 - Recompilacion por cambio en la estructura   *
      *                  PAHASE_T                                    *
      *                                                              *
      * ************************************************************ *
     Fsehni2    if   e           k disk
     Fgntnac    if   e           k disk
     Fset001    if   e           k disk
     Fpahec1    if   e           k disk
     Fgnhda7    if   e           k disk
     Fgnttce    if   e           k disk
     Fpahed004  if   e           k disk    rename(p1hed004:p1hed0)

      /copy './qcpybooks/rest_h.rpgle'
      /copy './qcpybooks/svprest_h.rpgle'
      /copy './qcpybooks/cowlog_h.rpgle'

     D WSLASE          pr                  ExtPgm('WSLASE')
     D   peBase                            likeds(paramBase) const
     D   peAsen                       7  0 const
     D   peDase                            likeds(pahase_t)
     D   peMase                            likeds(dsMail_t) dim(100)
     D   peMaseC                     10i 0
     D   peErro                            like(paramErro)
     D   peMsgs                            likeds(paramMsgs)

     D empr            s              1a
     D sucu            s              2a
     D nivt            s              1a
     D nivc            s              5a
     D nit1            s              1a
     D niv1            s              5a
     D rama            s              2a
     D poli            s              7a

     D uri             s            512a
     D mail            s             50a
     D tipo            s             50a
     D url             s           3000a   varying
     D rc              s              1n
     D rc2             s             10i 0
     D @@nit1          s              1  0
     D @@niv1          s              5  0
     D @@rama          s              2  0
     D @@repl          s          65535a
     D peErro          s             10i 0
     D x               s             10i 0
     D @@fnac          s             10a
     D fnac            s             10d
     D cops            s              1a

     D peMsgs          ds                  likeds(paramMsgs)
     D peBase          ds                  likeds(paramBase)
     D peDase          ds                  likeds(pahase_t)
     D peMase          ds                  likeds(dsMail_t) dim(100)
     D peMaseC         s             10i 0
     D k1hni2          ds                  likerec(s1hni2:*key)
     D k1hed0          ds                  likerec(p1hed0:*key)
     D k1hec1          ds                  likerec(p1hec1:*key)

     D psds           sds                  qualified
     D  this                         10a   overlay(psds:1)

      /free

       *inlr = *on;

       rc  = REST_getUri( psds.this : uri );
       if rc = *off;
          return;
       endif;
       url = %trim(uri);

       // ------------------------------------------
       // Obtener los parámetros de la URL
       // ------------------------------------------
       empr = REST_getNextPart(url);
       sucu = REST_getNextPart(url);
       nivt = REST_getNextPart(url);
       nivc = REST_getNextPart(url);
       nit1 = REST_getNextPart(url);
       niv1 = REST_getNextPart(url);
       rama = REST_getNextPart(url);
       poli = REST_getNextPart(url);

       if SVPREST_chkBase(empr:sucu:nivt:nivc:nit1:niv1:peMsgs) = *off;
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : peMsgs.peMsid
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          SVPREST_end();
          close *all;
          return;
       endif;

       if %check( '0123456789' : %trim(rama) ) <> 0;
          @@repl = rama;
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'RAM0001'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'RAM0001'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       @@rama = %dec( rama : 2 : 0 );
       setll @@rama set001;
       if not %equal;
          @@repl = rama;
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'RAM0001'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'RAM0001'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       if %check( '0123456789' : %trim(poli) ) <> 0;
          %subst(@@repl:1:2) = rama;
          %subst(@@repl:3:7) = poli;
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'POL0001'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'RAM0001'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       k1hed0.d0empr = empr;
       k1hed0.d0sucu = sucu;
       k1hed0.d0rama = %dec( rama : 2 : 0 );
       k1hed0.d0poli = %dec( poli : 7 : 0 );
       setgt  %kds(k1hed0:4) pahed004;
       readpe %kds(k1hed0:4) pahed004;
       if %eof;
          %subst(@@repl:1:2) = rama;
          %subst(@@repl:3:7) = poli;
          SVPWS_getMsgs( '*LIBL'
                       : 'WSVMSG'
                       : 'POL0001'
                       : peMsgs
                       : %trim(@@repl)
                       : %len(%trim(@@repl)) );
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : 'RAM0001'
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       k1hec1.c1empr = d0empr;
       k1hec1.c1sucu = d0sucu;
       k1hec1.c1arcd = d0arcd;
       k1hec1.c1spol = d0spol;

       setgt %kds(k1hec1:4) pahec1;
       readpe %kds(k1hec1:4) pahec1;
       if %eof;
          c1asen = 0;
       endif;

       clear peBase;
       clear peMase;
       clear peDase;
       clear peMsgs;

       peMaseC = 0;
       peErro  = 0;

       peBase.peEmpr = empr;
       peBase.peSucu = sucu;
       peBase.peNivt = %dec( nivt : 1 : 0 );
       peBase.peNivc = %dec( nivc : 5 : 0 );
       peBase.peNit1 = %dec( nit1 : 1 : 0 );
       peBase.peNiv1 = %dec( niv1 : 5 : 0 );

       COWLOG_logcon('WSRAXP':peBase);

       WSLASE( peBase
             : c1asen
             : peDase
             : peMase
             : peMaseC
             : peErro
             : peMsgs );

       if peErro = -1;
          rc = REST_writeHeader( 400
                               : *omit
                               : *omit
                               : peMsgs.peMsid
                               : peMsgs.peMsev
                               : peMsgs.peMsg1
                               : peMsgs.peMsg2 );
          REST_end();
          close *all;
          return;
       endif;

       monitor;
         fnac = %date(peDase.asfnac:*iso);
         @@fnac = %char(fnac:*iso);
        on-error;
         @@fnac = *blanks;
       endmon;

       chain peDase.ascnac gntnac;
       if not %found;
          acdnac = *blanks;
       endif;

       cops = %editc(peDase.ascops:'X');

       REST_writeHeader();
       REST_write('<?xml version="1.0" encoding="ISO-8859-1"?>');
       REST_writeXmlLine( 'aseguradoPoliza' : '*BEG');

        REST_writeXmlLine( 'codigoAsegurado' : %char(peDase.asasen));
        REST_writeXmlLine( 'nombreAsegurado' : %trim(peDase.asnomb));
        REST_writeXmlLine( 'fechaNacimiento' : %trim(@@fnac));
        REST_writeXmlLine( 'codigoDocumento' : %char(peDase.astido));
        REST_writeXmlLine( 'tipoDocumento'   : %trim(peDase.asdatd));
        REST_writeXmlLine( 'nroDocumento'    : %trim(%char(peDase.asnrdo)));
        REST_writeXmlLine( 'codigoCondFiscal': %char(peDase.asciva));
        REST_writeXmlLine( 'condiFiscal'     : %trim(peDase.asncil));
        REST_writeXmlLine( 'codigoNacionalidad': %char(peDase.ascnac));
        REST_writeXmlLine( 'nacionalidad'    : %trim(acdnac));
        REST_writeXmlLine( 'cuit'            : %trim(peDase.ascuit));
        REST_writeXmlLine( 'codigoPais'      : '6'                 );
        REST_writeXmlLine( 'pais'            : %trim(peDase.aspaid));
        REST_writeXmlLine( 'codigoProvincia' : %trim(peDase.asproc));
        REST_writeXmlLine( 'provincia'       : %trim(peDase.asprod));
        REST_writeXmlLine( 'localidad'       : %trim(peDase.asloca));
        REST_writeXmlLine( 'codigoPostal'    : %trim(%char(peDase.ascopo)));
        REST_writeXmlLine('sufijoCodigoPostal':cops                       );
        REST_writeXmlLine( 'domicilio'       : %trim(peDase.asdomi));
        REST_writeXmlLine( 'telParticular'   : %trim(peDase.astel2));
        REST_writeXmlLine( 'telLaboral'      : %trim(peDase.astel4));
        REST_writeXmlLine( 'telCelular'      : %trim(peDase.astel6));
        REST_writeXmlLine( 'nroFax'          : %trim(peDase.astel8));

        REST_writeXmlLine( 'correos' : '*BEG' );

        setll c1asen gnhda7;
        reade c1asen gnhda7;
        dow not %eof;

            chain dfctce gnttce;
            if not %found;
               cedtce = *blanks;
            endif;

            REST_writeXmlLine( 'correo' : '*BEG' );
             REST_writeXmlLine( 'tipoCorreo' : %trim(cedtce) );
             REST_writeXmlLine( 'direccionCorreo' : %trim(dfmail) );
            REST_writeXmlLine( 'correo' : '*END' );

         reade c1asen gnhda7;
        enddo;

        REST_writeXmlLine( 'correos' : '*END' );

       REST_writeXmlLine( 'aseguradoPoliza' : '*END');

       REST_end();

       close *all;

       return;

      /end-free
