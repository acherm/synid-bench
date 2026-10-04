      /if defined(SVPWS_H)
      /eof
      /endif
      /define SVPWS_H

      /copy './qcpybooks/wsstruc_h.rpgle'

      * Estrucutura de datos con el último error...
     D SVPWS_ERDS_T    ds                  qualified template
     D   Errno                        4s 0
     D   Msg                         80a

      * Estrucutura de datos con datos del mensaje...
     D DSRTVM0300      ds                  qualified template
     D BytesReturned                 10i 0
     D BytesAvailable                10i 0
     D MsgSeverity                   10i 0
     D AlertIndex                    10i 0
     D AlertOption                    9
     D LogIndicator                   1
     D MsgId                          7
     D Reserved                       3
     D NbrSubstVars                  10i 0
     D CCSIDConvStsInd...
     D                               10i 0
     D CCSIDConvStsIndRplDta...
     D                               10i 0
     D CCSIDText                     10i 0
     D DftRpyOffSet                  10i 0
     D LenDftRpyRet                  10i 0
     D LenDftRpyAva                  10i 0
     D MsgOffSet                     10i 0
     D LenMsgRet                     10i 0
     D LenMsgAva                     10i 0
     D MsgHlpOffSet                  10i 0
     D LenMsgHlpRet                  10i 0
     D LenMsgHlpAva                  10i 0
     D SubVarOffSet                  10i 0
     D LenSubVarRet                  10i 0
     D LenSubVarAva                  10i 0
     D Reserved2                      1

      * Variable de error
     D erro            s             10i 0

      * ------------------------------------------------------------ *
      * SVPWS_parseParmBase(): Retorna los parametros de la DS Base  *
      *                                                              *
      *     peBase   (input)   DS de Parametros Base                 *
      *     peEmpr   (output)  Empresa                               *
      *     peSucu   (output)  Sucursal                              *
      *     peNivt   (output)  Tipo  de Intermediario                *
      *     peNivc   (output)  Codigo de Intermediario               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SVPWS_parseParmBase...
     D                 pr              n
     D   peBase                            const likeds ( paramBase )
     D   peEmpr                       1    options(*nopass:*omit)
     D   peSucu                       2    options(*nopass:*omit)
     D   peNivt                       1  0 options(*nopass:*omit)
     D   peNivc                       5  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SVPWS_getMsgs(): Retorna Mensaje de Error                    *
      *                                                              *
      *     peLibl   (input)   Biblioteca                            *
      *     peMsgF   (input)   Archivo de Mensajes                   *
      *     peMsgI   (input)   Id. de Mensaje                        *
      *     peMsgs   (output)  DS de Errores                         *
      *     peRepl   (input)   Variables de Reemplazo                *
      *     peLeng   (input)   Longitud de Campo peRepl              *
      *                                                              *
      * Retorna: Severidad de Error / -1 Error                       *
      * ------------------------------------------------------------ *

     D SVPWS_getMsgs...
     D                 pr            10i 0
     D   peLibl                      10    const
     D   peMsgF                      10    const
     D   peMsgI                       7    const
     D   peMsgs                            likeds ( paramMsgs )
     D   peRepl                   65535a   const
     D                                     options(*nopass:*omit:*varsize)
     D   peLeng                      10i 0 const options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SVPWS_inz(): Inicializa módulo.                              *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     D SVPWS_inz       pr

      * ------------------------------------------------------------ *
      * SVPWS_end(): Finaliza módulo.                                *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     D SVPWS_end       pr

      * ------------------------------------------------------------ *
      * SVPWS_error(): Retorna el último error del service program   *
      *                                                              *
      *     peEnbr   (output)  Número de error (opcional)            *
      *                                                              *
      * Retorna: Mensaje de error.                                   *
      * ------------------------------------------------------------ *
     D SVPWS_error     pr            80a
     D   peEnbr                      10i 0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SVPWS_chkParmBase(): Valida los parametros Base              *
      *                                                              *
      *     peBase   (input)   DS de Parametros Base                 *
      *     peMsgs   (output)  DS de Errores                         *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SVPWS_chkParmBase...
     D                 pr              n
     D   peBase                            const likeds ( paramBase )
     D   peMsgs                            likeds ( paramMsgs )

      * ------------------------------------------------------------ *
      * SVPWS_chkRoll(): Valida el parametro de Roll                 *
      *                                                              *
      *     peRoll   (input)   Parametro de Roll                     *
      *     peMsgs   (output)  DS de Errores                         *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SVPWS_chkRoll...
     D                 pr              n
     D   peRoll                       1    const
     D   peMsgs                            likeds ( paramMsgs )

      * ------------------------------------------------------------ *
      * SVPWS_chkOrde(): Valida ordenamiento de WS                   *
      *                                                              *
      *     pePgWs   (input)   WebServices                           *
      *     peFilt   (input)   Filtro WebServices                    *
      *     peMsgs   (output)  DS de Errores                         *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SVPWS_chkOrde...
     D                 pr              n
     D   pePgWs                      10    const
     D   peFilt                      10    const
     D   peMsgs                            likeds ( paramMsgs )

      * ------------------------------------------------------------ *
      * SVPWS_getCant(): Retorna cantidad                            *
      *                                                              *
      *     peCant   (input/output) Cantidad                         *
      * ------------------------------------------------------------ *

     D SVPWS_getCant...
     D                 pr             2  0
     D peCant                        10i 0 const

      * ------------------------------------------------------------ *
      * SVPWS_getGrupoRama(): Retorna Grupo para una Rama dada.      *
      *                                                              *
      *     peRama   (input) Rama                                    *
      *                                                              *
      * Retorna Grupo                                                *
      * ------------------------------------------------------------ *

     D SVPWS_getGrupoRama...
     D                 pr             1
     D peRama                         2  0 const

      * ------------------------------------------------------------ *
      * SVPWS_getGrupoRamaArch(): Retorna Grupo de Archivo por Rama  *
      *                                                              *
      *     peRama   (input) Rama                                    *
      *                                                              *
      * Retorna "V"=Vida / "T"= Transporte / "R" = Riesgos Varios    *
      * ------------------------------------------------------------ *

     D SVPWS_getGrupoRamaArch...
     D                 pr             1
     D peRama                         2  0 const
