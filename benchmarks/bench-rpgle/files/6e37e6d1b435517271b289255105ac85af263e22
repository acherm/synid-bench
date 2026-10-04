*SRCMBRTXT:UIF - Genera archivo XML para UIF      
     H DFTACTGRP(*NO)  ACTGRP('QILE') BNDDIR('QC2LE')
     H DEBUG DATEDIT(*YMD) GENLVL(20)
     F*----------------------------------------------------------------*
     FSGSYSV    IF   E           K DISK
     D*-------------------------------------------------------------------------
     D*Aca estan las definiciones de Prototipos para llamar a las API del IFS
     D*-------------------------------------------------------------------------
     D/COPY SDB01.SRC/QRPGSRC,IFSIO_H
     D/copy LE00525/socketsrpg,errno_h
     D readline        PR            10I 0
     D  fd                           10I 0 value
     D  text                           *   value
     D  maxlen                       10I 0 value
     D bufer           S             69
     D
     D*-------------------------------------------------------------------------
     DERRDS            DS
     D ERRTXT                  1    255
     D WWNCU1                  1     55
     D WWNCU2                 56    110
     D WWNCU3                111    165
     D WWNCU4                166    220
     D WWNCB1                221    275
     D WWNCB2                276    330
     D WWNCB3                331    385
     D WWNCB4                386    440
     D*-------------------------------------------------------------------------
     D rc              S             10I 0
     D indo            S              8A
     D doc             S              8S 0
     D ndoc            S             15S 0
     D count           S              8S 0
     D path            S            255A
     D path_from       S            255A
     D path_to         S            255A
     D path_out        S            255A
     D deno            S             50A
     D mesg            s            115A
     D err             S             10I 0
     D fdf             S             10I 0
     D fdt             S             10I 0
     D fdm             S             10I 0
     D errmsg          S            250A
     D p_dir           S               *
     D file_name       S            255A
     D wwwtab          S              6A
     D wwwtag          S             12A
     D wwwta1          S             12A
     D line            S           1024A
     D up              C                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     D lo              C                   'abcdefghijklmnopqrstuvwxyz'
     D*-------------------------------------------------------------------------
     c                   ExSr      CheckStruct
     c                   ExSr      ProcDir
     c                   ExSr      EndPgm
|    C*-------------------------------------------------------------------------
     c     CheckStruct   BegSr
|    C*-------------------------------------------------------------------------
|    C*
|    C* ... Check si existe el directorio UIF
     c                   Eval      path='/home/UIF'+x'00'
     c                   If        Access(%addr(path): F_OK) < 0
     c                   if        errno = ENOENT
     c                   eval      errtxt='No Existe el Dir.:'+path
     c                   ExSr      IFSError
+----C                   EndIf
     c                   if        errno = EACCES
     c                   eval      errtxt='Usuario sin permiso al Dir.:'+path
     c                   ExSr      IFSError
+----C                   EndIf
     c                   EndIf
|    C*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     ProcDir       BegSr
     C*-------------------------------------------------------------------------
     C*
     c                   Eval      path='/home/UIF'+x'00'
     c                   Eval      p_dir=opendir(%addr(path))
     c                   If        p_dir = *NULL
     c                   eval      errtxt='No se pudo leer:'+path+' Causa:'+
     c                             errmsg
     c                   ExSr      Abort
     c                   EndIf
     C*
     c                   Eval      p_dirent = readdir(p_dir)
     c                   DoW       p_dirent <> *NULL
     c                   ExSr      ProcessFile
     c                   Eval      p_dirent = readdir(p_dir)
     c                   EndDo
     C*
     c                   CallP     closedir(p_dir)
     C*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     ProcessFile   BegSr
     C*-------------------------------------------------------------------------
     C*
     C* ... Abrir Archivo de Entrada
     c                   ExSr      OpenInputF
     C* ... Leer datos y escribir datos
     C                   Eval      bufer=*blanks
     c* Genera la cabecera del archivo XML
     c                   exsr      PrtHead
     c* Genera el cuerpo del archivo XML
     c                   exsr      PrtFilCnt
|    c* .... Cerrar los archivos
     c                   CallP     closef(fdf)
|    c*
     c                   EndSr
|    C*-------------------------------------------------------------------------
|    c* PrtHead: Genera la cabera del archivo XML
|    C*-------------------------------------------------------------------------
     c     PrtHead       BegSr
|    c*
     c                   exsr      OpenRefresh
|    c* CABECERA
|    C                   Eval      %subst(bufer:001:020)='<?xml version="1.0" '
|    C                   Eval      %subst(bufer:021:067)='encoding="utf-8"?>'
|    C                   Eval      %subst(bufer:068:002)=X'0D'+X'25'
     c                   CALLP     write(fdf: %addr(bufer): %size(bufer))
|    C                   Eval      %subst(bufer:001:066)='<Operacion>'
|    C                   Eval      %subst(bufer:068:002)=X'0D'+X'25'
     c                   CALLP     write(fdf: %addr(bufer): %size(bufer))
|    C                   Eval      %subst(bufer:001:019)='  <Entidades_Financ'
|    C                   Eval      %subst(bufer:020:019)='ieras_Alta_Cliente_'
|    C                   Eval      %subst(bufer:040:019)='Persona_F92sica Ver'
|    C                   Eval      %subst(bufer:060:028)='sion="1.1">'
|    C                   Eval      %subst(bufer:068:002)=X'0D'+X'25'
     c                   CALLP     write(fdf: %addr(bufer): %size(bufer))
|    c*
     c                   EndSr
|    C*-------------------------------------------------------------------------
|    c* PrtFilCnt: Genera refresh de archivos enviados por la entidad
|    C*-------------------------------------------------------------------------
     c     PrtFilCnt     BegSr
|    c*
     C                   Eval      bufer=*blanks
     c*                  movel     '    '        wwwtab
     c                   movel     '<Apellido>'  wwwtag
|    C                   Eval      %subst(bufer:001:014)=%subst(wwwtab:001:004)
     c                                                   +wwwtag
|    C                   Eval      %subst(bufer:015:006)='Prueba'
|    C                   Eval      %subst(bufer:022:011)=%subst(wwwtag:001:001)
     c                                                   +'/'+
     c                                                   %subst(wwwtag:002:009)
|    C                   Eval      %subst(bufer:067:002)=X'0D'+X'25'
     c                   CALLP     write(fdf: %addr(bufer): %size(bufer))
     C                   Eval      bufer=*blanks
     c                   movel     '<Segundo_Ape'wwwtag
     c                   movel     'llido>'      wwwta1
|    C                   Eval      %subst(bufer:001:022)=%subst(wwwtab:001:004)
     c                                                   +wwwtag+%TRIM(wwwta1)
|    C                   Eval      %subst(bufer:023:006)='Prueba'
|    C                   Eval      %subst(bufer:030:018)=%subst(wwwtag:001:001)
     c                                                   +'/'+
     c                                                   %subst(wwwtag:002:018)
|    C                   Eval      %subst(bufer:049:002)=X'0D'+X'25'
     c                   CALLP     write(fdf: %addr(bufer): %size(bufer))
     C                   Eval      bufer=*blanks
     c                   movel     '<Nombre>'    wwwtag
|    C                   Eval      %subst(bufer:001:012)=%subst(wwwtab:001:004)
     c                                                   +wwwtag
|    C                   Eval      %subst(bufer:013:006)='Prueba'
|    C                   Eval      %subst(bufer:020:009)=%subst(wwwtag:001:001)
     c                                                   +'/'+
     c                                                   %subst(wwwtag:002:007)
|    C                   Eval      %subst(bufer:030:002)=X'0D'+X'25'
     c                   CALLP     write(fdf: %addr(bufer): %size(bufer))
     C                   Eval      bufer=*blanks
     c                   movel     '<Segundo_Nom'wwwtag
     c                   movel     'bre>'        wwwta1
|    C                   Eval      %subst(bufer:001:020)=%subst(wwwtab:001:004)
     c                                                   +wwwtag+%TRIM(wwwta1)
|    C                   Eval      %subst(bufer:021:006)='Prueba'
|    C                   Eval      %subst(bufer:028:016)=%subst(wwwtag:001:001)
     c                                                   +'/'+
     c                                                   %subst(wwwtag:002:015)
|    C                   Eval      %subst(bufer:041:002)=X'0D'+X'25'
     c                   CALLP     write(fdf: %addr(bufer): %size(bufer))
     C                   Eval      bufer=*blanks
     c                   movel     '<Tipo_docume'wwwtag
     c                   movel     'nto>'        wwwta1
|    C                   Eval      %subst(bufer:001:020)=%subst(wwwtab:001:004)
     c                                                   +wwwtag+%TRIM(wwwta1)
|    C                   Eval      %subst(bufer:021:006)='Prueba'
|    C                   Eval      %subst(bufer:028:016)=%subst(wwwtag:001:001)
     c                                                   +'/'+
     c                                                   %subst(wwwtag:002:015)
|    C                   Eval      %subst(bufer:041:002)=X'0D'+X'25'
     c                   CALLP     write(fdf: %addr(bufer): %size(bufer))
     C                   Eval      bufer=*blanks
     c                   movel     '<N94mero_Doc'wwwtag
     c                   movel     'umento>'     wwwta1
|    C                   Eval      %subst(bufer:001:023)=%subst(wwwtab:001:004)
     c                                                   +wwwtag+%TRIM(wwwta1)
|    C                   Eval      %subst(bufer:024:006)='Prueba'
|    C                   Eval      %subst(bufer:031:020)=%subst(wwwtag:001:001)
     c                                                   +'/'+
     c                                                   %subst(wwwtag:002:019)
|    C                   Eval      %subst(bufer:052:002)=X'0D'+X'25'
     c                   CALLP     write(fdf: %addr(bufer): %size(bufer))
     C                   Eval      bufer=*blanks

|    c*
     c                   EndSr
|    C*-------------------------------------------------------------------------
     c     OpenInputF    BegSr
|    C*-------------------------------------------------------------------------
|    c*
     c                   Eval      path_from='/home/UIF/1.xml'+x'00'
     c                   Eval      fdf = open(%addr(path_from): O_RDONLY +
     c                                        O_TEXTDATA     )
     c                   If        fdf  < 0
     c                   Eval      errtxt='No se pudo abrir:'+path_from
     c                   ExSr      IFSError
+----C                   EndIf
|    c*
     c                   EndSr
|    C*-------------------------------------------------------------------------
     c     OpenRefresh   BegSr
|    C*-------------------------------------------------------------------------
|    C*
|    C     *LOVAL        SETLL     SGSYSV
|    C                   READ      SGSYSV                                 99
     c                   MOVE      AASFEI        FECHA             6
     c                   EVAL      path_from='/home/UIF/1.xml'+x'00'
     c                   EVAL      fdf=open(%addr(path_from):
     c                                  O_CREAT + O_WRONLY + O_TRUNC +
     c                                  O_CODEPAGE :
     c                                  S_IWUSR+S_IRUSR+S_IRGRP+S_IROTH:
     c                                  01252   )
     c                   callp     closef(fdf)
     c                   EVAL      fdf=open(%addr(path_from):
     c                                   O_WRONLY+O_TEXTDATA)
     c                   If        fdf  < 0
     c                   Eval      errtxt='No se pudo abrir:'+path_from
     c                   ExSr      IFSError
     c                   end
|    c*
     c                   EndSr
|    C*-------------------------------------------------------------------------
     c     IFSError      BegSr
|    C*
     c                   eval      err= errno
     c                   eval      errmsg= %str(strerror(errno))
     c                   eval      err= errno
     c                   eval      errtxt=%trim(errtxt)+' Causa:'+errmsg
     c                   ExSr      Abort
|    C*
|    C                   EndSr
|    C*-------------------------------------------------------------------------
     c     Abort         BegSr
|    C*-------------------------------------------------------------------------
|    C*
     c                   Eval      errtxt='FATAL:'+%trim(errtxt)
     c                   ExSr      DspErr
     c                   ExSr      EndPgm
|    c*
     c                   EndSr
|    C*-------------------------------------------------------------------------
     c     EndPgm        BegSr
|    C*-------------------------------------------------------------------------
|    C*
     c                   SetOn                                        LR
|    C                   Return
|    C*
     c                   EndSr
|    C*-------------------------------------------------------------------------
|    C* DSPERR: Mostrar Mensaje de Error
|    C*-------------------------------------------------------------------------
|    C     DSPERR        BEGSR
|    C                   CALL      'BAER00RS'
|    C                   PARM                    WWNCU1
|    C                   PARM                    WWNCU2
|    C                   PARM                    WWNCU3
|    C                   PARM                    WWNCU4
|    C                   PARM                    WWNCB1
|    C                   PARM                    WWNCB2
|    C                   PARM                    WWNCB3
|    C                   PARM                    WWNCB4
|    C                   ENDSR
|    C*=========================================================================
     P readline        B                   export
     D  readline       PI            10I 0
     D   fd                          10I 0 value
     D   text                          *   value
     D   maxlen                      10I 0 value

     D rdbuf           S           1024A   static
     D rdpos           S             10I 0 static
     D rdlen           S             10I 0 static

     D p_retstr        S               *
     D RetStr          S          32766A   based(p_retstr)
     D len             S             10I 0

     c                   eval      len = 0
     c                   eval      p_retstr = text
     c                   eval      %subst(RetStr:1:MaxLen) = *blanks

     c                   dow       1 = 1

|    c* Load the buffer
     c                   if        rdpos>=rdlen
     c                   eval      rdpos = 0
     c                   eval      rdlen=read(fd:%addr(rdbuf):%size(rdbuf))

     c                   if        rdlen < 1
     c                   return    -1
     c                   endif
     c                   endif

|    c* Is this the end of the line?
     c                   eval      rdpos = rdpos + 1
     c                   if        %subst(rdbuf:rdpos:1) = x'25'
     c                   return    len
     c                   endif

|    C* Otherwise, add it to the text string.
     c                   if        %subst(rdbuf:rdpos:1) <> x'0d'
     c                               and len<>maxlen
     c                   eval      len = len + 1
     c                   eval      %subst(retstr:len:1) =
     c                               %subst(rdbuf:rdpos:1)
     c                   endif

     c                   enddo

     c                   return    len
     P                 E
|     *-------------------------------------------------------------------------

|    C*=========================================================================
      /define ERRNO_LOAD_PROCEDURE
      /copy LE00525/socketsrpg,errno_h
