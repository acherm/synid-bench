*SRCMBRTXT:LINK:TRANSF.REDES-VER2-ANALIZA C.A.    
     H DFTACTGRP(*NO)  ACTGRP('QILE')
     H DATEDIT(*YMD)
     H******************************************************************
     H*                                                                *
     H*  APPLICATION CODE : SD V00 01                                  *
     H*                                                                *
     H*  APPLICATION NAME : Sistema Integrado De Bancos                *
     H*                                                                *
     H*  PROGRAM NAME     : AC0089R1                                   *
     H*                                                                *
     H*  PROGRAM TITLE    : GENERA MOVIMIENTOS EN liter2               *
     H*                                                                *
     H*  DATE GENERATED   : 28/11/13                                   *
     H*                                                                *
     H*  AUTHOR           : PR00525                                    *
     H*                                                                *
     H*  NOTAS            :                                            *
     H*                                                                *
     H*                                                                *
     H******************************************************************
     FACCTAC    IP   E           K DISK
     FLITER2    UF A E           K DISK
     FBAICCL    IF   E           K DISK
     FBADCCL01  IF   E           K DISK
     FBAPFIS    IF   E           K DISK
     FBAPJUR    IF   E           K DISK
     FLISERJ    UF   E           K DISK
     FQSYSPRT   O    F  132        PRINTER
     F*-------------------------------------------------------------------------
     D  NormalizaName  PR            30A
     D    Name                       30A
     D*-------------------------------------------------------------------------
     D*>DATASTRUCTURE : MYPSDS
     D*>DESCRIPTION   : Data structure containing program status information
     D*>USE           : Retrieve program status information
     D*>RELATEDFUNCT  : sys_cmd
     D*-------------------------------------------------------------------------
     DMYPSDS          SDS
     D @PRC_NAM          *PROC
     D @PGM_STS          *STATUS
     D @PRV_STS               16     20S 0
     D @LIN_NUM               21     28
     D @ROU_NAM          *ROUTINE
     D @PAR_CNT          *PARMS
     D @EXC_TYP               40     42
     D @EXC_NUM               43     46
     D @PGM_LIB               81     90
     D @EXC_DTA               91    170
     D @EXC_IDE              171    174
     D @DAT_RUN              191    198
     D @DAT_YEA              199    200S 0
     D @LAS_FIL              201    208
     D @FIL_INF              209    243
     D @JOB_NAM              244    253
     D @USR_NAM              254    263
     D @JOB_NUM              264    269S 0
     D @JOB_NUM_C            264    269
     D @PJOBN                264    269  0
     D @JOB_DTE              270    275S 0
     D @RUN_DTE              276    281S 0
     D @RUN_TIM              282    287S 0
     D @CRT_DTE              288    293
     D @CRT_TIM              294    299
     D @CPL_LVL              300    303
     D @SRC_FIL              304    313
     D @SRC_MBR              324    333
     D @PRC_PGM              334    343
     D @PRC_MOD              344    353
     d*-------------------------------------------------------------------------
     D CTADS           DS
     D  CTALNK                 1     20
     D  LINSUC                 1      3  0
     D  LINFI2                 4      4
     D  LINGRP                 5      6
     D  LINFIL                 7      9  0
     D  LINCAH                10     16  0
     F*-------------------------------------------------------------------------
     C                   ExSr      EsCtaAProcesar
     c     CtaAProcesar  CabEq     'N'           Next
     c                   ExSr      ChkLimite
     c                   ExSr      DetEstCta
     c                   ExSr      DetEstPadron
     c                   ExSr      DetEstReset
     c*
     c                   Select
     c                   When      Resetear=*On
     c                   ExSr      AddReset
     c                   When      EstCta='NORMAL' and EstPadron='EXISTE'
     c                   ExSr      CompTitulares
     c                   If        Titulares <> 'IGUALES'
     c                   ExSr      AddBaja
     c                   ExSr      AddAlta
     c                   Else
     c                   ExSr      CompHabilit
     c                   If        CbioEstHab = 'SI'
     c                   ExSr      AddMod
     c                   EndIf
     c                   EndIf
     c                   When      EstCta='NORMAL' and EstPadron='NOEXISTE'
|    C                   ExSr      BuscaFirmantes
     c                   ExSr      AddAlta
     c                   When      EstCta='BAJA' and EstPadron='EXISTE'
     c                   ExSr      AddBaja
     c                   EndSl
     c*
     C     NEXT          Tag
     C*-------------------------------------------------------------------------
     C* CompTitulares: Comparar si los titulares no cambiaron
     C*-------------------------------------------------------------------------
     C     CompTitulares BegSr
     c*
     c                   MoveL(P)  'IGUALES  '   Titulares        10
|    C                   ExSr      BuscaFirmantes
     c                   If        WWCUI1 <> TMCUI1 Or
     c                             WWNYAP <> TMNYAP Or
     c                             WWCUI2 <> TMCUI2 Or
     c                             WWNYA1 <> TMNYA1 Or
     c                             WWCUI3 <> TMCUI3 Or
     c                             WWNYA2 <> TMNYA2
     c                   MoveL(P)  'DISTINTOS'   Titulares        10
     c                   EndIf
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     C* DetEstCta: Determinar el estado de la cuenta
     C*-------------------------------------------------------------------------
     C     DetEstCta     BegSr
     c*
     c                   MoveL(p)  'NORMAL'      EstCta           10
     c*
     c* ... Si esta BAJA tratar como baja
+----C                   If        FUFBAJ <> 0
     c                   MoveL(P)  'BAJA'        EstCta
     c                   EndIf
     c*
     c* ... Si esta INMOVILIZADA tratar como baja
+----C                   If        FUISGC = 'IN'
     c                   MoveL(P)  'BAJA'        EstCta
     c                   EndIf
     c*
     c* ... Si esta Bloqueo 7 tratar como baja
+----C                   If        FUIBAC = 7
|    c                   MoveL(P)  'BAJA'        EstCta
+----c                   EndIf
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     C* CompHabilit   : Determinar si cambio el estado de habilitacion
     C*-------------------------------------------------------------------------
     C     CompHabilit   BegSr
     c*
     c                   Move      'NO'          CbioEstHab        2
     c                   Move      'NO'          CbioEstHab        2
     c                   Move      '0'           EstActual         1
     c                   ExSr      getWWCSTS
     c*
     c* ... TMCSTS = Estado de Habilitación '0' Habilitad '1' inhabilitada
     c                   If        TMCSTS <> WWCSTS
     c                   Move      'SI'          CbioEstHab        2
     c                   EndIf
     c                   EndSr
     C*-------------------------------------------------------------------------
     c* getWWCSTS: Obtener el estado de habilitacion de la cuenta
     C*-------------------------------------------------------------------------
     c     getWWCSTS     BegSr
     c*
     c                   Move      '5'           WWCSTS            1
     c*
+----C                   If        FUIBAC = 7
     c                   Move      '1'           WWCSTS
     c                   EndIf
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     C* EsCtaAProcesar: Determinar si esta es una cuenta a procesar
     C*-------------------------------------------------------------------------
     C     EsCtaAProcesarBegSr
     C*
     c                   Move      'S'           CtaAProcesar      1
|    C     FUIMON        IFNE      1
     c                   Move      'N'           CtaAProcesar      1
     c                   LeaveSr
+----C                   Endif
     C*
     C     KOS000        Chain     REBAICCL                           99
+----C                   IF        *IN99 = *OFF
|+---C                   If        OSININ = 0 OR FUIGRC='03'
||   c                   ExSr      ProcPF1
|<   C                   Else
||   c                   ExSr      ProcPJ1
|+---C                   Endif
+----C                   Endif
     c*
     C                   EndSr
     C*-------------------------------------------------------------------------
     c* DetEstReset: Indica si se debe resetear la cuenta
     c*              Si se encuentra el registro liter2RESETCA0000012345678901
     c*              En el archivo LISERJ, se generará una baja para cada reg.
     c*              que hubiera en el liter2 y se generará una nueva alta
     C*-------------------------------------------------------------------------
     c     DetEstReset   BegSr
     c*
     c                   Move      *Off          Resetear          1
     c                   Move      *Blanks       WWDACO           30
     C                   Move      FUISUC        WWISUC            5
     C                   Move      FUICAH        WWiCAH           11
     c                   Eval      WWDACO = 'liter2RESETCA'+
     c                                      WWISUC+
     c                                      WWICAH
     c*
     c     WWDACO        Chain     RELISERJ                           99
     c                   If        *in99 = *Off
     c                   Move      *On           Resetear          1
     c                   Endif
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c*
     C*-------------------------------------------------------------------------
     c     DetEstPadron  BegSr
     c*
     c                   MoveL(P)  'NOEXISTE'    EstPadron        10
     c*
     c* ... Buscar en registros de maestro (TMACTL='M')
     c*
     C                   Move      'M'           WWACTL
     C     KTM000        SetGt     REliter2
     C     KTM000        ReadPe    REliter2                               97
     c                   If        *in97 = *Off
     c                   MoveL(P)  'EXISTE    '  EstPadron
     c                   if        TMIASK = 'B'
     c                   MoveL(P)  'NOEXISTE  '  EstPadron
     c                   EndIf
     c                   Else
     c*
     c* ... Buscar en registros Históricos (TMACTL='H')
     c*
     C                   Move      'H'           WWACTL
     C     KTM000        SetGt     REliter2
     C     KTM000        ReadPe    REliter2                               97
     c                   If        *in97 = *Off
     c                   MoveL(P)  'EXISTE  '    EstPadron
     c                   if        TMIASK = 'B'
     c                   MoveL(P)  'NOEXISTE'    EstPadron        10
     c                   EndIf
     C                   EndIf
     C                   EndIf
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     c* ChkLimite : Determina cuantos reg se deben procesar 0=TODOS (Lo normal)
     C*-------------------------------------------------------------------------
     C     ChkLimite     BegSr
     C*
+----C                   If        PALIM <> 0
|+---C                   If        Count > PALIM
||   C                   SetOn                                        LR
||   C                   Return
|+---C                   EndIf
+----C                   EndIf
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     BuscaFirmantesBegSr
     C*
     C                   Move      *BLANKS       WWERRO           40
     C                   Z-Add     *ZERO         WWCUI2
     C                   Move      *BLANKS       WWNYA1
     C                   Z-Add     *ZERO         WWCUI3
     C                   Move      *BLANKS       WWNYA2
     C*
     c                   SetOff                                       25
     C     KOS000        Chain     REBAICCL                           99
+----C                   IF        *IN99 = *ON
|    C                   Eval      WWERRO='Cuenta Cliente No Encontrada'
|    C                   Except    DETERR
|    c                   SetOn                                        25
|    C                   LeaveSr
+----C                   EndIf
+----C                   If        OSININ = 0 OR FUIGRC='03'
|    c                   ExSr      ProcPF
+----C                   Else
|    c                   ExSr      ProcPJ
+----C                   Endif
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     ProcPJ        BegSr
     C*
     C                   Move      'J'           WWTIPP
     C*
     C     KAO000        Chain     REBAPJUR                           99
+----C                   If        *IN99 = *ON
|    C                   Eval      WWERRO='Pers.Jur.No Encontrada      '
|    C                   Except    DETERR
|    c                   SetOn                                        25
|    C                   LeaveSr
+----C                   EndIf
     C*
     C*                  Eval      WWCUI1=AOICUI
     C                   MOVE      AOICUI        WWCUI1
     C                   Eval      WWNYAP=NormalizaName(AONRSO)
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C*ProcPJ1
     C*-------------------------------------------------------------------------
     C     ProcPJ1       BegSr
     C*
     C*
     C     KAO000        Chain     REBAPJUR                           99
+----C                   If        *IN99 = *Off
|+---C                   If        AOIGRC= 'IH'
||   c                   Move      'N'           CtaAProcesar      1
|+---C                   Endif
+----C                   EndIf
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     ProcPF        BegSr
     C*
     C                   Move      'F'           WWTIPP
     C*
     C                   Z-Add     1             WWITTL
     C     KOT003        Chain     REBADCCL                           99
+----C                   IF        *IN99 = *ON
|    C                   Eval      WWERRO='Primer Firmante No Encontrado'
|    C                   Except    DETERR
|    c                   SetOn                                        25
|    C                   LeaveSr
+----C                   EndIf
     C     KPF000        Chain     REBAPFIS                           99
+----C                   If        *IN99 = *ON AND NOT %FOUND()
|    C                   Eval      WWERRO='Pers.Fis.No Encontrada      '
|    C                   Except    DETERR
|    c                   SetOn                                        25
|    C                   LeaveSr
+----C                   EndIf
     C                   Eval      WWNYAP=NormalizaName(A#NYAP)
     C                   MOVE      A#ICUI        WWCUI1
     C*                  Eval      WWCUI1=A#ICUI
     C*
     C                   Z-Add     2             WWITTL
     C     KOT003        Chain     REBADCCL                           99
+----C                   IF        *IN99 = *OFF
|    C     KPF000        Chain     REBAPFIS                           99
|+---C                   If        *IN99 = *OFF
||   C                   Eval      WWNYA1=NormalizaName(A#NYAP)
||   C                   Eval      WWCUI2=A#ICUI
|+---C                   Endif
+----C                   EndIf
     C*
     C                   Z-Add     3             WWITTL
     C     KOT003        Chain     REBADCCL                           99
+----C                   IF        *IN99 = *OFF
|    C     KPF000        Chain     REBAPFIS                           99
|+---C                   If        *IN99 = *OFF
||   C                   Eval      WWNYA2=NormalizaName(A#NYAP)
||   C                   Eval      WWCUI3=A#ICUI
|+---C                   EndIf
+----C                   EnDIf
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C*ProcPF1:
     C*-------------------------------------------------------------------------
     C     ProcPF1       BegSr
     C*
     C                   Z-Add     1             WWITTL
     C     KOT003        Chain     REBADCCL                           99
+----C                   IF        *IN99 = *OFF
|    C     KPF000        Chain     REBAPFIS                           99
|+---C                   If        *IN99 = *OFF
||+--C                   If        A#IGRC= 'IH'
|||  c                   Move      'N'           CtaAProcesar      1
|||  c                   Goto      EndPPF1
||+--C                   Endif
|+---C                   Endif
+----C                   EndIf
     C*
     C                   Z-Add     2             WWITTL
     C     KOT003        Chain     REBADCCL                           99
+----C                   IF        *IN99 = *OFF
|    C     KPF000        Chain     REBAPFIS                           99
|+---C                   If        *IN99 = *OFF
||+--C                   If        A#IGRC= 'IH'
|||  c                   Move      'N'           CtaAProcesar      1
|||  c                   Goto      EndPPF1
||+--C                   Endif
|+---C                   Endif
+----C                   EndIf
     C*
     C                   Z-Add     3             WWITTL
     C     KOT003        Chain     REBADCCL                           99
+----C                   IF        *IN99 = *OFF
|    C     KPF000        Chain     REBAPFIS                           99
|+---C                   If        *IN99 = *OFF
||+--C                   If        A#IGRC= 'IH'
|||  c                   Move      'N'           CtaAProcesar      1
|||  c                   Goto      EndPPF1
||+--C                   Endif
|+---C                   EndIf
+----C                   EnDIf
     C*
     C     EndPPF1       EndSr
     C*-------------------------------------------------------------------------
     C     GetLINKFmt    BegSr
     C                   Z-ADD     FUISUC        LINSUC
     C                   MOVE      FUIGRC        LINGRP
     C                   Z-ADD     FUICAH        LINCAH
     C                   Z-ADD     *ZEROS        LINFIL
     C                   MOVE      *ZEROS        LINFI2
     C*
     C                   MOVE      CTALNK        WWNCTA
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     GetCBU        BegSr
+----C     FUISGC        IFEQ      'CE'
|    C                   Z-ADD     3             WWTIPO            2 0
+----C                   ELSE
|    C                   Z-ADD     2             WWTIPO
+----C                   ENDIF
     C                   Z-ADD     *ZEROS        WWBLQ1            8 0
     C                   Z-ADD     *ZEROS        WWBLQ2           14 0
     C                   Z-ADD     *ZEROS        WWBLQ3           22 0
     C                   CALL      'CBU000RG'
     C                   PARM                    WWTIPO
     C                   PARM                    FUISUC
     C                   PARM                    FUICAH
     C                   PARM                    WWBLQ1
     C                   PARM                    WWBLQ2
     C                   PARM                    WWBLQ3
     C*
     C                   MOVE      WWBLQ3        WWNCBU
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     AddAlta       BegSr
     C*
     C                   Move      'N'           TMACTL
     C                   Move      WWISUB        TMISUB
     C                   Z-Add     FUISUC        TMISUC
     C                   Z-Add     FUICAH        TMICCC
     C                   Z-Add     FUIMON        TMIMON
     C*
     C                   ExSr      GetLINKFmt
     C                   Move      WWNCTA        TMNCTA
     C*
     C                   ExSr      GetCBU
     C                   Move      WWNCBU        TMNCBU
     C*
     C                   ExSr      GetWWCSTS
     C                   Move      WWCSTS        TMCSTS
     C*
     C                   Move      WWTIPP        TMTIPP
     C                   Z-Add     WWCUI1        TMCUI1
     C                   Move      WWNYAP        TMNYAP
     C                   Z-Add     WWCUI2        TMCUI2
     C                   Move      WWNYA1        TMNYA1
     C                   Z-Add     WWCUI3        TMCUI3
     C                   Move      WWNYA2        TMNYA2
     C                   Z-Add     *DATE         TMFALT
     C                   Z-Add     *DATE         TMFASI
     C                   Z-Add     *ZERO         TMITMO
     C                   Move      'A'           TMIASK
     C                   MOVE      @USR_NAM      TMIUSR
     C                   Time                    TMHORA
     C                   MoveL(P)  'ALTA'        TMREFD
     C                   Move      WWIDAR        TMIDAR
     C                   Move      *BLANKS       TMDF05
     C                   Move      *BLANKS       TMDF06
     C                   Z-Add     *ZERO         TM$A05
     C                   Z-Add     *ZERO         TM$A06
     C*
     C                   Write     REliter2
     C                   Add       1             Count
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     AddBaja       BegSr
     C*
     C                   Move      'N'           TMACTL
     C                   Move      WWISUB        TMISUB
     C                   Z-Add     FUISUC        TMISUC
     C                   Z-Add     FUICAH        TMICCC
     C                   Z-Add     FUIMON        TMIMON
     C*
     C                   ExSr      GetLINKFmt
     C                   Move      WWNCTA        TMNCTA
     C*
     C                   ExSr      GetCBU
     C                   Move      WWNCBU        TMNCBU
     C*
     C                   Move      WWCSTS        TMCSTS
     C                   Move      WWTIPP        TMTIPP
     C                   Z-Add     WWCUI1        TMCUI1
     C                   Move      WWNYAP        TMNYAP
     C                   Z-Add     WWCUI2        TMCUI2
     C                   Move      WWNYA1        TMNYA1
     C                   Z-Add     WWCUI3        TMCUI3
     C                   Move      WWNYA2        TMNYA2
     C                   Z-Add     *DATE         TMFASI
     C                   Z-Add     *ZERO         TMITMO
     C                   Move      'B'           TMIASK
     C                   MOVE      @USR_NAM      TMIUSR
     C                   Time                    TMHORA
     C                   MoveL(P)  'BAJA'        TMREFD
     C                   Move      WWIDAR        TMIDAR
     C                   Move      *BLANKS       TMDF05
     C                   Move      *BLANKS       TMDF06
     C                   Z-Add     *ZERO         TM$A05
     C                   Z-Add     *ZERO         TM$A06
     C*
     C                   Write     REliter2
     C                   Add       1             Count
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     C     AddMod        BegSr
     C*
     C                   Move      'N'           TMACTL
     C                   Move      WWISUB        TMISUB
     C                   Z-Add     FUISUC        TMISUC
     C                   Z-Add     FUICAH        TMICCC
     C                   Z-Add     FUIMON        TMIMON
     C*
     C                   ExSr      GetLINKFmt
     C                   Move      WWNCTA        TMNCTA
     C*
     C                   ExSr      GetCBU
     C                   Move      WWNCBU        TMNCBU
     C*
     C                   ExSr      GetWWCSTS
     C                   Move      WWCSTS        TMCSTS
     C*
     C                   Move      WWTIPP        TMTIPP
     C                   Z-Add     WWCUI1        TMCUI1
     C                   Move      WWNYAP        TMNYAP
     C                   Z-Add     WWCUI2        TMCUI2
     C                   Move      WWNYA1        TMNYA1
     C                   Z-Add     WWCUI3        TMCUI3
     C                   Move      WWNYA2        TMNYA2
     C                   Z-Add     *DATE         TMFASI
     C                   Z-Add     *ZERO         TMITMO
     C                   Move      'M'           TMIASK
     C                   MOVE      @USR_NAM      TMIUSR
     C                   Time                    TMHORA
     C                   MoveL(P)  'MODI'        TMREFD
     C                   Move      WWIDAR        TMIDAR
     C                   Move      *BLANKS       TMDF05
     C                   Move      *BLANKS       TMDF06
     C                   Z-Add     *ZERO         TM$A05
     C                   Z-Add     *ZERO         TM$A06
     C*
     C                   Write     REliter2
     C                   Add       1             Count
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     c* AddReset      En el archivo LISERJ, se generará una baja para cada reg.
     c*               que hubiera en el liter2 y se generará una nueva alta
     C*-------------------------------------------------------------------------
     c     AddReset      BegSr
     c*
     c* ... Buscar en registros Históricos (TMACTL='H')
     C                   Move      'H'           WWACTL
     C     KTM000        Chain     REliter2                           99
     c                   If        *in99 = *Off
     C                   Move      'N'           TMACTL
     C                   Z-Add     *DATE         TMFASI
     C                   Z-Add     *ZERO         TMITMO
     C                   Move      'B'           TMIASK
     C                   MoveL(P)  'BAJA'        TMREFD
     C                   MOVE      @USR_NAM      TMIUSR
     C                   Time                    TMHORA
     c                   Write     REliter2
     c*
|    C                   ExSr      BuscaFirmantes
     c                   ExSr      AddAlta
     c*
     c     WWDACO        Chain     RELISERJ                           99
     c                   If        *in99 = *Off
     c                   Delete    RELISERJ
     c                   Endif
     c*
     c                   Endif
     c*
     c                   EndSr
     C*-------------------------------------------------------------------------
     C     *INZSR        BegSr
     C*
     C     *ENTRY        PLIST
     C                   PARM                    PAIDAR
     C                   PARM                    PALIM            15 0
     C*
     C     *LIKE         Define    TMACTL        WWACTL
     C     *LIKE         Define    TMISUB        WWISUB
     C     *LIKE         Define    OTITTL        WWITTL
     C     *LIKE         Define    TMCUI1        WWCUI1
     C     *LIKE         Define    TMNYAP        WWNYAP
     C     *LIKE         Define    TMCUI2        WWCUI2
     C     *LIKE         Define    TMNYA1        WWNYA1
     C     *LIKE         Define    TMCUI3        WWCUI3
     C     *LIKE         Define    TMNYA1        WWNYA2
     C     *LIKE         Define    TMNCBU        WWNCBU
     C     *LIKE         Define    TMNCTA        WWNCTA
     C     *LIKE         Define    TMTIPP        WWTIPP
     C     *LIKE         Define    TMCSTS        WWCSTS
     C     *LIKE         Define    TMIDAR        WWIDAR
     C     *LIKE         Define    TMIDAR        PAIDAR
     C*
     C                   Move      'AC'          WWISUB
     C                   Move      'M'           WWACTL
     C                   Move      PAIDAR        WWIDAR
     C*
     C     KTM000        KLIST
     C                   KFld                    WWACTL
     C                   KFld                    WWISUB
     C                   KFld                    FUISUC
     C                   KFld                    FUICAH
     C     KOS000        KLIST
     C                   KFld                    FUISUC
     C                   KFld                    FUICCL
     C     KOT003        KLIST
     C                   KFld                    FUISUC
     C                   KFld                    FUICCL
     C                   KFld                    WWITTL
     C     KAO000        KLIST
     C                   KFld                    OSITIN
     C                   KFld                    OSININ
     C     KPF000        KLIST
     C                   KFld                    OTITDO
     C                   KFld                    OTINDO
     C*
     C                   Z-Add     *ZERO         Count            15 0
     C*
     C                   EndSr
     C*-------------------------------------------------------------------------
     OQSYSPRT   E            DETERR
     O                       WWERRO           +   1
     O                       WWISUB           +   1
     O                       FUISUC           +   1
     O                       FUICCL           +   1
     O                       WWITTL           +   1
     C*=========================================================================
     P NormalizaName   B
     D  NormalizaName  PI            30A
     D    Name                       30A
     D*
     D up              C                   'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     D lo              C                   'abcdefghijklmnopqrstuvwxyz'
     D Symbols         C                   '|°¬]"Ñ$%&/()=?\¡¿*+¨[!{}_-;,:.<>'
     D SymBlanks       C                   '                                '
     D Acentos         C                   'Ã¦#áéíóúäëïöüãõàèìòùâêîôû@'
     D AceBlanks       C                   'NnNAEIOUAEIOUAOAEIOUAEIOU '
     D Apos            C                   ''''
     D APosBlank       C                   ' '
     D*
     C                   Eval      NAME = %XLATE(Symbols:SymBlanks:NAME)
     C                   Eval      NAME = %XLATE(Acentos:AceBlanks:NAME)
     C                   Eval      NAME = %XLATE(Apos:AposBlank:NAME)
     C                   Eval      NAME = %XLATE(lo:up:NAME)
     C                   Eval      NAME = %SCANRPL('':'':NAME)
     C                   Return    NAME
     P NormalizaName   E
