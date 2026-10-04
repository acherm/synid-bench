      /if defined(COWLOG_H)
      /eof
      /endif
      /define COWLOG_H

     D COWLOG_SUCCESS  c                   const('1')
     D COWLOG_FAIL     c                   const('0')

      * --------------------------------------------------- *
      * Estrucutura de datos de tabla Logppr
      * --------------------------------------------------- *
     D DsLogppr_t      ds                  qualified template
     D  pridta                        7  0
     D  prider                       10
     D  prerrs                       10
     D  prrequ                      250
     D  prresp                     1000
     D  prdaex                      600
     D  pruser                      200
     D  prtusu                       10
     D  prnivl                       10
     D  prtime                        8  0
     D  prdate                        8  0

      * ------------------------------------------------------------ *
      * COWLOG_create(): Crea archivo de log.                        *
      *                                                              *
      *    peBase     (input)    Base                                *
      *    peNctw     (input)    Número de Cotización                *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_create   pr             1N
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const

      * ------------------------------------------------------------ *
      * COWLOG_log(): Loguea acción                                  *
      *                                                              *
      *    peBase     (input)    Base                                *
      *    peNctw     (input)    Número de Cotización                *
      *    peLog      (input)    Log                                 *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_log      pr             1N
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const
     D  peLog                     65535a   varying value

      * ------------------------------------------------------------ *
      * COWLOG_logb(): Log básico (servicio + resultado)             *
      *                                                              *
      *    peBase     (input)    Base                                *
      *    peNctw     (input)    Número de Cotización                *
      *    peLog      (input)    Log                                 *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_logb     pr             1N
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const
     D  peLog                     65535a   varying value

      * ------------------------------------------------------------ *
      * COWLOG_inz(): Inicializa Módulo                              *
      *                                                              *
      * retorna: void                                                *
      * ------------------------------------------------------------ *
     D COWLOG_inz      pr

      * ------------------------------------------------------------ *
      * COWLOG_end(): Finaliza   Módulo                              *
      *                                                              *
      * retorna: void                                                *
      * ------------------------------------------------------------ *
     D COWLOG_end      pr

      * ------------------------------------------------------------ *
      * COWLOG_error(): Retornar error del módulo                    *
      *                                                              *
      *    peErrn     (input)    Número de error (opcional)          *
      *                                                              *
      * retorna: Mensaje de error                                    *
      * ------------------------------------------------------------ *
     D COWLOG_error    pr            80a
     D  peErrn                       10i 0 options(*nopass : *omit)

      * ------------------------------------------------------------ *
      * COWLOG_logcon(): Loguear ejecución de consulta               *
      *                                                              *
      *    peWebs     (input)    Nombre de WebService                *
      *    peBase     (input)    Base                                *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_logcon   pr             1N
     D  peWebs                      256a   const
     D  peBase                             likeds(paramBase) const

      * ------------------------------------------------------------ *
      * COWLOG_apilog(): Loguea acción de API                        *
      *                                                              *
      *    peNcta     (input)    Número de Cotización                *
      *    peNivc     (input)    Numero de Intermediario             *
      *    peLog      (input)    Log                                 *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_apilog   pr             1N
     D  peNcta                        7  0 const
     D  peNivc                        5  0 const
     D  peLog                     65535a   varying value

      * ------------------------------------------------------------ *
      * COWLOG_createAPI: Crea archivo de log para API.              *
      *                                                              *
      *    peNcta     (input)    Número de Cotización                *
      *    peNivc     (input)    Codigo de Intermediario             *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_createAPI...
     D                 pr             1n
     D  peNcta                        7  0 const
     D  peNivc                        5  0 const

      * ------------------------------------------------------------ *
      * COWLOG_isLoguearAutoGestion: Determina si loguea por         *
      *                              Autogestion                     *
      *                                                              *
      * retorna: *ON si debe loguear / *OFF si no debe loguear       *
      * ------------------------------------------------------------ *
     D COWLOG_isLoguearAutoGestion...
     D                 pr             1n

      * ------------------------------------------------------------ *
      * COWLOG_logConAutoGestion: Graba registro en Log Autogestion  *
      *                                                              *
      *    peEmpr     (input)    Empresa                             *
      *    peSucu     (input)    Sucursal                            *
      *    peTdoc     (input)    Tipo Documento                      *
      *    peNdoc     (input)    Numero Documento                    *
      *    peWebs     (input)    Nombre de WebService                *
      *                                                              *
      * retorna: *ON si todo Ok / *OFF si error                      *
      * ------------------------------------------------------------ *
     D COWLOG_logConAutoGestion...
     D                 pr             1n
     D  peEmpr                        1a   const
     D  peSucu                        2a   const
     D  peTdoc                        2  0 const
     D  peNdoc                       11  0 const
     D  peWebs                      256a   const

      * ------------------------------------------------------------ *
      * COWLOG_spolog(): Loguea acción de SuperPoliza                *
      *                                                              *
      *    peArcd     (input)    Artículo                            *
      *    peSpol     (input)    SuperPoliza                         *
      *    peLog      (input)    Log                                 *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_spolog   pr             1N
     D  peArcd                        6  0 const
     D  peSpol                        9  0 const
     D  peLog                     65535a   varying value

      * ------------------------------------------------------------ *
      * COWLOG_createSPOL(): Crea archivo de log de Super poliza     *
      *                                                              *
      *    peArcd     (input)    Articulo                            *
      *    peSpol     (input)    SuperPoliza                         *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_createSPOL...
     D                 pr             1N
     D  peArcd                        6  0 const
     D  peSpol                        9  0 const

      * ------------------------------------------------------------ *
      * isLoguearSPOL(): Recupera si debe o no loguear SuperPoliza   *
      *                                                              *
      * Retorna: *ON si debe loguear o *OFF si no.                   *
      * ------------------------------------------------------------ *
     D isLoguearSPOL   pr             1N

      * ------------------------------------------------------------ *
      * COWLOG_createPgm : Crea archivo de log para PGM              *
      *                                                              *
      *    peName     (input)    Nombre del Programa                 *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_createPgm...
     D                 pr             1n
     D  peName                       10    const

      * ------------------------------------------------------------ *
      * COWLOG_pgmLog(): Loguea acción de Programa                   *
      *                                                              *
      *    peName     (input)    Nombre del programa                 *
      *    peLog      (input)    Log                                 *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_pgmLog   pr             1N
     D  peName                       10    const
     D  peLog                     65535a   varying value

      * ------------------------------------------------------------ *
      * isLoguearPgm: Recupera si debe o no loguear.                 *
      *    peName     (input)    Nombre del servicio                 *
      *                                                              *
      * Retorna: *ON si debe loguear o *OFF si no.                   *
      * ------------------------------------------------------------ *
     D isLoguearPgm    pr             1N
     D  peName                       10    const

      * ------------------------------------------------------------ *
      * COWLOG_loglin(): Loguear login                               *
      *                                                              *
      *    peEmpr     (input)    Empresa                             *
      *    peSucu     (input)    Sucursal                            *
      *    peCuit     (input)    Cuit                                *
      *    peNrag     (input)    Numero de Agencia                   *
      *    peUsri     (input)    Usuario interno                     *
      *                                                              *
      * retorna: SUCCESS o FAIL                                      *
      * ------------------------------------------------------------ *
     D COWLOG_loglin   pr             1N
     D  peEmpr                        1a   const
     D  peSucu                        2a   const
     D  peCuit                       11a   const
     D  peNrag                        5  0 const
     D  peUsri                        1a   const

      * ----------------------------------------------------------------- *
      * COWLOG_setLogppr(): Graba datos en el archivo Logppr              *
      *                                                                   *
      *          peDspr   ( input  ) Estrutura de Logppr                  *
      *                                                                   *
      * retorna: SUCCESS o FAIL                                      *
      * ----------------------------------------------------------------- *
     D COWLOG_setLogppr...
     D                 pr             1n
     D   peDspr                            likeds( dsLogppr_t ) const

      * ----------------------------------------------------------------- *
      * COWLOG_dltLogppr(): Elimina datos en el archivo Logppr            *
      *                                                                   *
      *          peDspr   ( input  ) Estrutura de Logppr                  *
      *                                                                   *
      * retorna: SUCCESS o FAIL                                      *
      * ----------------------------------------------------------------- *
     D COWLOG_dltLogppr...
     D                 pr             1n
     D   peDspr                            likeds( dsLogppr_t ) const

