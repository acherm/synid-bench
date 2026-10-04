*SRCMBRTXT:Link-Host to Host-Programa Principal   
     H DFTACTGRP(*NO) ACTGRP(*NEW)
     H  BNDDIR('LE00525/TO10BD')
     H  BNDDIR('QSYS/QC2LE')

     FSGSYSV    IF   E             DISK
     FLICONN    IF   E           K DISK
     FLIMSGC    IF   E           K DISK
     FLIMSGD    IF   E           K DISK
     FLIMTRN    IF   E           K DISK
     FLIFLDS    IF   E           K DISK
     FBANUME    UF A E           K DISK
     FLINKF     O    E             DISK

     D/copy le00525/socketsrpg,socket_h
     D/copy le00525/socketsrpg,sockutil_h
     D/copy le00525/socketsrpg,errno_h
     D* Definición de Prototipos
     D/copy sdb02.src/qrpgsrc,lihh00PR
     D* Definición de Constantes
     D/copy sdb02.src/qrpgsrc,lihh00co

     D* Estructura para contener el estado de la Conexión
     D ConnDS          DS
     D* ... Estado de la conexión
     D  sConnStatus                   1A
     D  sConnName                     6A
     D* ... N ormal o A lternativo
     D  sProcType                     1A
     D* ... Definiciones de Campos (P/Evitar acceso a archivos)
     D  mBitsXLong                    1S 0 DIM(128)
     D  mDtaType                      1A   DIM(128)
     D  mLongMax                      4S 0 DIM(128)
     D  mLongMin                      3S 0 DIM(128)
     D* ... Mensaje de Entrada
     D  iMsgType                      4S 0
     D  iMsgTypeC                     4A   Overlay(iMsgType)
     D  iISOLen                       3P 0
     D  iISOStr                     768
     D* ... Arrays de Trabajo
     D  wMsgFldVal                  255A   DIM(128)
     D  wMsgFldBmp                  128A
     D  wMsgFldVlen                   3S 0 DIM(128)
     D* ... Mensaje de Salida
     D  oMsgType                      4S 0
     D  oMsgTypeC                     4A   Overlay(oMsgType)
     D  oISOLen                       3P 0
     D  oISOStr                     768

     D*-------------------------
     D* Declaración de Variables
     D*-------------------------
     C* ... Para las API TCP/IP
     D lsock           S             10I 0
     D csock           S             10I 0

     D UsrCmd          S              1A
     D isRunning       S               N   INZ(*ON)

     C     Restart       Tag
     C                   If        OpenChanel(ConnNme)
     C*                  Goto      Restart
     C                   EndIf
     C                   Eval      sConnStatus=CO_STOFFLINE
     C                   DoW       isRunning
     C                   If        ReadChanel()
     C                   CallP     CloseChanel()
     C                   Goto      Restart
     C                   EndIf
     C                   CallP     MessageManager(AM_CMPRCMSG)
     C                   ExSr      DoUserCommands
     C                   If        WriteChanel()
     C                   CallP     CloseChanel()
     C                   Goto      Restart
     C                   EndIf
     C                   EndDo
     C                   Exsr      EndPgm
     C*-----------------------------------------------------------------------
     C* DoCommands: Verifica y Efectúa comandos de este adapatador
     C*-----------------------------------------------------------------------
     C     DoUserCommandsBegSr
     C*
     C                   Eval      UsrCmd=GetUsrCmd(ConnNme)
     C                   Select
     C                   When      UsrCmd=CO_CMQUIT
     C                   CallP     MessageManager(AM_CMGENLOGOFF)
     C                   Eval      isRunning = *OFF
     C                   When      UsrCmd=CO_CMLOGOFF
     C                   CallP     MessageManager(AM_CMGENLOGOFF)
     C                   When      UsrCmd=CO_CMLOGON
     C                   CallP     MessageManager(AM_CMGENLOGON)
     C                   When      UsrCmd=CO_CMNOTIFY
     C                   ExSr      WriteStsInfo
     C                   EndSl
     C*
     C                   EndSr
     C*-----------------------------------------------------------------------
     C* WriteStsInfo: Escribir en cola de Datos información de Status
     C*-----------------------------------------------------------------------
     C     WriteStsInfo  BegSr
     C                   EndSr
     C*-----------------------------------------------------------------------
     C* *INZSR: Inicializacion
     C*-----------------------------------------------------------------------
     C     *INZSR        BegSr
     C*
     C     *ENTRY        Plist
     C                   Parm                    ConnNme           6
     C                   Parm                    ProcType          1
     C*
     C     KeyBANUME     KList
     C                   KFld                    WNIPF1
     C                   KFld                    WNIPF2
     C     KeyLIMTRN     KList
     C                   KFld                    TRNMSG
     C                   KFld                    TRCTRN
     C*
     C                   EndSr
     C*-----------------------------------------------------------------------
     C* *PSSR : Rutina de Error
     C*-----------------------------------------------------------------------
     C     *PSSR         BegSr
     C                   Exsr      EndPgm
     C                   EndSr
     C*-----------------------------------------------------------------------
     C* EndPgm: Finalización del Programa
     C*-----------------------------------------------------------------------
     C     EndPgm        BegSr
     C                   CallP     CloseChanel()
     C                   Eval      *INLR=*ON
     C                   Return
     C                   EndSr

      /define ERRNO_LOAD_PROCEDURE
      /copy le00525/socketsrpg,errno_h

     C/copy sdb02.src/qrpgsrc,LIHH00CH
     C/copy sdb02.src/qrpgsrc,LIHH00CU
     C/copy sdb02.src/qrpgsrc,LIHH00DE
     C/copy sdb02.src/qrpgsrc,LIHH00EN
     C/copy sdb02.src/qrpgsrc,LIHH00MM
     C/copy sdb02.src/qrpgsrc,LIHH00ET
