*SRCMBRTXT:Interbanking-Transferencias-Importador 
     H DFTACTGRP(*NO)  ACTGRP('QILE') BNDDIR('QC2LE')
     H DEBUG DATEDIT(*YMD) GENLVL(20)
     FBANUME    UF A E           K DISK
     FIBTRAN    O    E           K DISK
     F*----------------------------------------------------------------*
     FSGSYSV    IF   E             DISK
     F*  The system values file
     D*----------------------------------------------------------------*
     D               ESDS                  EXTNAME(@PSDS)
     D*----------------------------------------------------------------*
     D LDA           E DS                  EXTNAME(LDA)
     D*----------------------------------------------------------------*
     D*-------------------------------------------------------------------------
     D*Aca estan las definiciones de Prototipos para llamar a las API del IFS
     D*-------------------------------------------------------------------------
     D/COPY SDB01.SRC/QRPGSRC,IFSIO_H
     D/copy LE00525/socketsrpg,errno_h
     D readline        PR            10I 0
     D  fd                           10I 0 value
     D  text                           *   value
     D  maxlen                       10I 0 value
     D buf             S             45
     D bufer           S             29
     D buff            S             31
     D buf1            S            194
     D
     D*-------------------------------------------------------------------------
     DRECDS            DS
     D  RECLIN                 1    588
     D TIPREG                  1      1
     D BANDEB                  2      4
     D FECSOL                  5     12
     D NUMTRA                 13     19
     D NUMABO                 20     26
     D TIPOPE                 27     28
     D IMPORT                 29     45
     D SUCDEB                 46     49
     D NOMSOL                 50     78
     D TIPCUE                 79     80
     D NCUECM                 81     82
     D NUMCTA                 83     99
     D FSENDB                100    105
     D HSENDB                106    109
     D OPEDB1                110    111
     D OPEDB2                112    113
     D RECHDB                114    117
     D BANCRE                118    120
     D SUCCRE                121    124
     D NOMBEN                125    153
     D TIPCRE                154    155
     D CTACRE                156    172
     D FSENCR                173    178
     D HSENCR                179    182
     D OPECR1                183    184
     D OPECR2                185    186
     D RECHCR                187    190
     D OPECON                191    192
     D OPEAU1                193    194
     D OPEAU2                195    196
     D OPEAU3                197    198
     D FECAUT                199    204
     D HORAUT                205    208
     D ESTADO                209    210
     D FECEST                211    216
     D OBSER1                217    276
     D OBSER2                277    376
     D MACUNO                377    388
     D MACDOS                389    400
     D NUMREF                401    407
     D NUMENV                408    410
     D CONSOL                411    411
     D MARTIT                412    412
     D PRIVEZ                413    413
     D RIEABO                414    414
     D RIEBCO                415    415
     D TABEST                416    555
     D CTAESP                556    556
     D CUITOR                557    567
     D CUITCR                568    578
     D TAOFFD                579    583
     D TAOFFC                584    588
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
     D*
     DCODIG            DS
     DLINCOD                   1      8
     DWWNAME                   1      2
     DWWCODI                   3      8  0
     D*-------------------------------------------------------------------------
     D RC              S              7A
     D indo            S              8A
     D doc             S              8S 0
     D ndoc            S             15S 0
     D count           S              8S 0
     D path            S            255A
     D path_from       S            255A
     D path_f          S            255A
     D path_to         S            255A
     D path_out        S            255A
     D deno            S             50A
     D mesg            s            115A
     D err             S             10I 0
     D fdi             S             10I 0
     D fdo             S             10I 0
     D fdf             S             10I 0
     D fdt             S             10I 0
     D fdm             S             10I 0
     D errmsg          S            250A
     D p_dir           S               *
     D file_name       S            255A
     D newname         S            255A
     D line            S            591A
     D msg             S            200A
     D file            S             20A
     D prefix          S             12A
     D up              C                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     D lo              C                   'abcdefghijklmnopqrstuvwxyz'
     D CMDSTR          S           4096A   INZ(*BLANKS)
     D ec              S             10I 0
     D @EXC_TYP               40     42
     D @EXC_NUM               43     46
     D*-------------------------------------------------------------------------
     D  Shell          PR             7A
     D   Command                   4096A   VALUE
     D**********************************************************************
     c                   ExSr      CheckStruct
     c                   ExSr      ProcDir
     c                   ExSr      EndPgm
     C*-------------------------------------------------------------------------
     c     *INZSR        BegSr
     C*-------------------------------------------------------------------------
     C*
     c     1             Chain     SGSYSV
     c                   Move      AASFEI        CHSFEI            8
     C*
     C* Clave para BANUME
     C     WKEY18        KLIST
     C                   KFLD                    WNIPF1
     C                   KFLD                    WNIPF2
     C                   KFLD                    WNIPF3
     C                   KFLD                    WNIPF4
     C                   KFLD                    WNIPF5
     C*
     C     *LIKE         DEFINE    ITIRRN        WWIRRN
     c                   Eval      WNIPF1='IBTRAN'
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     SRNUME        BegSr
     C*-------------------------------------------------------------------------
     C     WKEY18        Chain     REBANUME                           99
+----C                   If        *IN99 = *ON
Move C                   Z-Add     *Zero         WNIULN
Move C                   Write     REBANUME
+----C                   Else
Move C                   Add       1             WNIULN
Move C                   Update    REBANUME
+----C                   EndIf
     C                   Z-Add     WNIULN        WWIRRN
     c*
     C                   EndSr
     C*-------------------------------------------------------------------------
     c     ProcDir       BegSr
     C*-------------------------------------------------------------------------
     C*
     c                   Eval      path='/home/Interbanking/'+
     c                                  'Recibidos'+x'00'
     c                   Eval      p_dir=opendir(%addr(path))
+----c                   If        p_dir = *NULL
Move c                   eval      errtxt='No se pudo leer:'+path+' Causa:'+
Move c                             errmsg
Move c                   ExSr      Abort
+----c                   EndIf
     C*
     c                   Move      *On           NoFileFound       1
     c                   Eval      p_dirent = readdir(p_dir)
+----c                   DoW       p_dirent <> *NULL
Move c                   Eval      file_name= %subst(d_name:1:d_namelen)
Move c                   Eval      file_name=%xlate(lo:up:file_name)
|+---c                   Eval      prefix = %subst(file_name:1:12)
|+---c                   if        prefix =  'PLL_TRANSFER'
     c                   Move      *Off          NoFileFound
||   c                   ExSr      ProcessFile
|+---c                   EndIf
Move c                   Eval      p_dirent = readdir(p_dir)
+----c                   EndDo
     C*
     c                   CallP     closedir(p_dir)
     C*
     c                   If        NoFileFound = *On
     c                   Eval      WWNCU1='No se encontraron archivos p/Proc.'
     c                   Eval      WWNCU2='Copie los archivos a procesar en: '
     c                   Eval      WWNCU3=path
     c                   Eval      WWNCB4='Presione F3 Para Salir            '
     c                   ExSr      DspErr
     C                   EndIf
     C*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     ProcessFile   BegSr
     C*-------------------------------------------------------------------------
     C*
     C* ... Abrir Archivo de Entrada
     c                   ExSr      OpenInputF
     C* ... Leer datos y escribir datos
     C                   Eval      buf=*blanks
+----c                   Eval      ec=read(fdi: %addr(line): %size(line))
+----c*                  DOW       ec=>0 or  line <> *blanks
+----c                   DOW       ec>0
     c                   Move      *blanks       wwtire            1
Move C                   Eval      wwtire=%subst(line:001:001)
     c                   Select
     C                   When      wwtire='1'
     c                   ExSr      ProcHeader
     C                   When      wwtire='2'
     c                   ExSr      ProcRecord
     C                   When      wwtire='3'
     c                   ExSr      ProcFooter
     c                   EndSl
+----c                   Eval      ec=read(fdi: %addr(line): %size(line))
+----C                   ENDDo
     c* .... Cerrar los archivos
     c                   CallP     closef(fdi)
     c*
     c                   Move      AASFEI        chsfei            8
     c                   Time                    wwhora            6 0
     c                   move      wwhora        chhora            6
     c                   Eval      newname=%trim(file_name)+'_'+%trim(@puser)+
     c                             '_'+chsfei+'_'+chhora
     c                   Eval      CmdStr='MOVE OBJ('''+%TRIM(path_f)+
     c                             ''') TOOBJ(''/home/Interbanking/'+
     c                             '/Procesados/'+%trim(newname)+''')'
     C                   Eval      rc=Shell(CmdStr)
     C*
     c                   Eval      WWNCU1='Se proceso el archivo:            '
     c                   Eval      WWNCU2=path
     c                   Eval      WWNCB4='Presione Intro Para Continuar     '
     c                   ExSr      DspErr
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     ProcHeader    BegSr
     C*-------------------------------------------------------------------------
     c*
     c                   Move      *Blanks       CODBAN            3
     c                   Move      *Blanks       NOMFIL            8
     c                   Move      *Zeros        FECPRO            8
     c*
Move C                   Eval      codban=%subst(line:002:003)
Move C                   Eval      nomfil=%subst(line:005:013)
Move C                   Eval      fecpro=%subst(line:013:008)
     c*
     c                   Move      fecpro        wwfepr            8 0
     c*
     c                   if        nomfil<>'TRANSFER'
     c                   eval      errtxt='El archivo no es un archivo de '+
     c                             'Transferencias de Interbanking:'
     c                             +%trim(file_name)
     c                   ExSr      Abort
     c                   EndIf
     c*
     c*                  if        wwfepr<>aasfei
     c*                  eval      errtxt='El archivo no es de la fecha de'+
     c*                            ' hoy:'+%trim(file_name)
     c*                  ExSr      Abort
     c*                  EndIf
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     ProcRecord    BegSr
     C*-------------------------------------------------------------------------
     c*
     C                   MoveL     line          RecLin
     c                   ExSr      SRNUME
     c                   Z-Add     WWIRRN        ITIRRN
     c                   Z-Add     AASFEI        ITFECH
     c                   Move      BANDEB        ITINBA
     c                   MoveL     FECSOL        ITFING
     c                   MoveL     NUMTRA        ITICHE
     c                   MoveL     NUMABO        ITNENT
     c                   MoveL     TIPOPE        ITITPR
     c                   Move      IMPORT        IT$IMP
     c                   Move      SUCDEB        ITDBSU
     c                   MoveL     NOMSOL        ITNYA1
     c                   MoveL     TIPCUE        ITTCDB
     c                   MoveL     NCUECM        ITCLDB
     c                   MoveL     NUMCTA        ITDF01
     c                   MoveL     FSENDB        ITFEMI
     c                   MoveL     HSENDB        ITHEMI
     c                   MoveL     OPEDB1        ITIPRA
     c                   MoveL     OPEDB2        ITIPRB
     c                   MoveL     RECHDB        ITICME
     c                   Move      BANCRE        ITIBAN
     c                   Move      SUCCRE        ITCRSU
     c                   MoveL     NOMBEN        ITNMCR
     c                   MoveL     TIPCRE        ITTCCR
     c                   MoveL     CTACRE        ITDF02
     c                   MoveL     FSENCR        ITFACR
     c                   MoveL     HSENCR        ITHTOM
     c                   MoveL     OPECR1        ITITD1
     c                   MoveL     OPECR2        ITITD2
     c                   MoveL     RECHCR        ITICMI
     c                   MoveL     OPECON        ITIR01
     c                   MoveL     OPEAU1        ITIR02
     c                   MoveL     OPEAU2        ITIR04
     c                   MoveL     OPEAU3        ITIR05
     c                   MoveL     FECAUT        ITFAU1
     c                   MoveL     HORAUT        ITHAU1
     c                   MoveL     ESTADO        ITCOTR
     c                   MoveL     FECEST        ITFUAS
     c                   MoveL     OBSER1        ITDTLI
     c                   MoveL     OBSER2        ITCBA1
     c                   MoveL     MACUNO        ITNGT1
     c                   MoveL     MACDOS        ITNGT2
     c                   Move      NUMREF        ITIRFR
     c                   MoveL     NUMENV        ITILOT
     c                   MoveL     CONSOL        ITINI1
     c                   MoveL     MARTIT        ITINI2
     c                   MoveL     PRIVEZ        ITINI3
     c                   MoveL     RIEABO        ITINI4
     c                   MoveL     RIEBCO        ITINI5
     c                   MoveL     TABEST        ITT160
     c                   MoveL     CTAESP        ITINI6
     c                   MoveL     CUITOR        ITCUI0
     c                   MoveL     CUITCR        ITCUI1
     c                   MoveL     TAOFFD        ITINU1
     c                   MoveL     TAOFFC        ITINU2
     c*
     c                   Write     REIBTRAN
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     ProcFooter    BegSr
     C*-------------------------------------------------------------------------
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     CheckStruct   BegSr
     C*-------------------------------------------------------------------------
     C*
     C* ... Check si existe el dir
     c                   Eval      path='/home/Interbanking'+
     c                                  x'00'
+----c                   If        Access(%addr(path): F_OK) < 0
|+---c                   if        errno = ENOENT
||   c                   eval      errtxt='No Existe el Dir.:'+path
||   c                   ExSr      IFSError
|+---C                   EndIf
|+---c                   if        errno = EACCES
||   c                   eval      errtxt='Usuario sin permiso al Dir.:'+path
||   c                   ExSr      IFSError
|+---C                   EndIf
+----c                   EndIf
     C*
     C* ... Check si existe el dir, lo creamos
     C*
     c                   Eval      path='/home/Interbanking'+x'00'
     c                   ExSr      EnsureDir
     c                   Eval      path='/home/Interbanking/Recibidos'+x'00'
     c                   ExSr      EnsureDir
     c                   Eval      path='/home/Interbanking/Procesados'+x'00'
     c                   ExSr      EnsureDir
     C*
     c                   EndSr
     c*-------------------------------------------------------------------------
     c     EnsureDir     BegSr
     c*-------------------------------------------------------------------------
     c*
+----c                   If        Access(%ADDR(path): F_OK) < 0
Move c                   eval      err= errno
Move c                   eval      errmsg= %str(strerror(errno))
|+---c                   if        err = ENOENT
||+--c                   if        mkdir(%addr(path): 0) < 0
|||  c                   eval      errtxt='Dir.:'+%trim(path)+' inexistente'+
|||  c                                    ' Y no pudo ser creado.'
|||  c                   ExSr      IFSError
||+--C                   EndIf
|+---C                   EndIf
+----C                   EndIf
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     Abort         BegSr
     C*-------------------------------------------------------------------------
     C*
     c                   Eval      errtxt='FATAL:'+%trim(errtxt)
     c                   ExSr      DspErr
     c                   ExSr      EndPgm
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     IFSError      BegSr
     C*-------------------------------------------------------------------------
     C*
     c                   eval      err= errno
     c                   eval      errmsg= %str(strerror(errno))
     c                   eval      err= errno
     c                   eval      errtxt=%trim(errtxt)+' Causa:'+errmsg
     c                   ExSr      Abort
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     c     OpenInputF    BegSr
     C*-------------------------------------------------------------------------
     c*
     c                   Eval      path_from='/home/Interbanking/'+
     c                                  'Recibidos/'+
     c                                  %trim(file_name)+x'00'
     c                   Eval      path_f='/home/Interbanking/'+
     c                                  'Recibidos/'+
     c                                  %trim(file_name)
     c*                  Eval      fdi = open(%addr(path_from): O_RDONLY +
     c*                                       O_TEXTDATA     )
     c                   Eval      fdi = open(%addr(path_from): O_RDONLY
     c                                                       )
+----c                   If        fdi  < 0
Move c                   Eval      errtxt='No se pudo abrir:'+path_from
Move c                   ExSr      IFSError
+----C                   EndIf
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c     EndPgm        BegSr
     C*-------------------------------------------------------------------------
     C*
     c                   SetOn                                        LR
     C                   Return
     C*
     c                   EndSr
     C*-------------------------------------------------------------------------
     C* DSPERR: Mostrar Mensaje de Error
     C*-------------------------------------------------------------------------
     C     DSPERR        BEGSR
     C                   CALL      'BAER00RS'
     C                   PARM                    WWNCU1
     C                   PARM                    WWNCU2
     C                   PARM                    WWNCU3
     C                   PARM                    WWNCU4
     C                   PARM                    WWNCB1
     C                   PARM                    WWNCB2
     C                   PARM                    WWNCB3
     C                   PARM                    WWNCB4
     C                   ENDSR
     C*=========================================================================
     P readline        B                   export
     D  readline       PI            10I 0
     D   fd                          10I 0 value
     D   text                          *   value
     D   maxlen                      10I 0 value
     D
     D rdbuf           S           1024A   static
     D rdpos           S             10I 0 static
     D rdlen           S             10I 0 static
     D
     D p_retstr        S               *
     D RetStr          S          32766A   based(p_retstr)
     D len             S             10I 0
     c
     c                   eval      len = 0
     c                   eval      p_retstr = text
     c                   eval      %subst(RetStr:1:MaxLen) = *blanks
     c
+----c                   dow       1 = 1
Move c
Move c* Load the buffer
|+---c                   if        rdpos>=rdlen
||   c                   eval      rdpos = 0
||   c                   eval      rdlen=read(fd:%addr(rdbuf):%size(rdbuf))
||   c
||+--c                   if        rdlen < 1
|||  c                   return    -1
||+--c                   endif
|+---c                   endif
Move c
Move c* Is this the end of the line?
Move c                   eval      rdpos = rdpos + 1
|+---c                   if        %subst(rdbuf:rdpos:1) = x'25'
||   c                   return    len
|+---c                   endif
Move c
Move C* Otherwise, add it to the text string.
|+---c                   if        %subst(rdbuf:rdpos:1) <> x'0d'
||   c                               and len<>maxlen
||   c                   eval      len = len + 1
||   c                   eval      %subst(retstr:len:1) =
||   c                               %subst(rdbuf:rdpos:1)
|+---c                   endif
Move c
+----c                   enddo
     c
     c                   return    len
     P                 E
      *-------------------------------------------------------------------------

     P*---------------------------------------------------------------------
     P* PROCEDIMIENTOS DEBEN DECLARARSE DESPUES DE LA HOJA O, SI ESTA EXISTE
     P*---------------------------------------------------------------------
     P Shell           B                   EXPORT
     D  Shell          PI             7A
     D   Command                   4096A   VALUE
     D CommLen         S             15  5

     C                   Call      'QCMDEXC'
     c                   PARM                    Command
     C                   PARM      1024          CommLen
     C                   Return    'CPF0000'
     c     *PSSR         BEGSR
     C                   Return    @EXC_TYP+@EXC_NUM
     c                   ENDSR
     c
     P Shell           E
     C*=========================================================================
      /define ERRNO_LOAD_PROCEDURE
      /copy LE00525/socketsrpg,errno_h
