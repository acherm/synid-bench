      /if defined(SVPDRV_H)
      /eof
      /endif
      /define SVPDRV_H

      * Descuento no pertenece a la Caracteristica...
     D SVPDRV_DESNC    c                   const(0001)
      * Caracteristica no Existente...
     D SVPDRV_CARNE    c                   const(0002)

      * --------------------------------------------------- *
      * Estrucutura de datos con el último error
      * --------------------------------------------------- *
     D SVPDRV_ERDS_T   ds                  qualified
     D                                     based(template)
     D   Errno                        4s 0
     D   Msg                         80a

      * --------------------------------------------------- *
      * Estrucutura de Caracteristicas
      * --------------------------------------------------- *
     D carac_t         ds                  qualified
     D                                     based(template)
     D   empr                         1a
     D   sucu                         2a
     D   rama                         2  0
     D   ccba                         3  0
     D   dcba                        25a
     D   cbae                         3a
     D   bloq                         1a
     D   tpcs                         2a
     D   tpcn                         2a
     D   ma01                         1a
     D   ma02                         1a
     D   ma03                         1a
     D   ma04                         1a
     D   ma05                         1a
     D   ma06                         1a
     D   ma07                         1a
     D   ma08                         1a
     D   ma09                         1a
     D   ma10                         1a
     D   ccbp                         3  0

      * --------------------------------------------------- *
      * Estrucutura de Coberturas
      * --------------------------------------------------- *
     D cober_t         ds                  qualified
     D                                     based(template)
     D   xcob                         3  0
     D   nive                         1  0
     D   recs                         5  2
     D   recn                         5  2
     D   bons                         5  2
     D   bonn                         5  2

      * --------------------------------------------------- *
      * Estrucutura de Coberturas por Arcd/Rama/Xpro
      * --------------------------------------------------- *
     D cobCa_t         ds                  qualified
     D                                     based(template)
     D   empr                         1a
     D   sucu                         2a
     D   arcd                         6  0
     D   rama                         2  0
     D   xpro                         3  0
     D   xcob                         3  0
     D   ccbp                         3  0
     D   nive                         1  0
     D   recs                         5  2
     D   recn                         5  2
     D   bons                         5  2
     D   bonn                         5  2

      * ------------------------------------------------------------ *
      * Estructura para Descuentos por Cobertura
      * ------------------------------------------------------------ *
     D descCo_t        ds                  qualified template
     D   xcob                         3  0
     D   niv1                         5  2
     D   niv2                         5  2
     D   niv3                         5  2
     D   niv4                         5  2
     D   niv5                         5  2
     D   niv6                         5  2
     D   niv7                         5  2
     D   niv8                         5  2
     D   niv9                         5  2

      * ------------------------------------------------------------ *
      * SVPDRV_chkDescuentoCarac(): Chequea si descuento pertenece   *
      * a la caracteristica                                          *
      *                                                              *
      *     peEmpr   (input)   Empresa                               *
      *     peSucu   (input)   Sucursal                              *
      *     peRama   (input)   Rama                                  *
      *     peCcba   (input)   Codigo de Caracteristica              *
      *     peCcbp   (input)   Codigo de Descuento                   *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     D SVPDRV_chkDescuentoCarac...
     D                 pr              n
     D   peEmpr                       1a   const
     D   peSucu                       2a   const
     D   peRama                       2  0 const
     D   peCcba                       3  0 const
     D   peCcbp                       3  0 const

      * ------------------------------------------------------------ *
      * SVPDRV_getDescuentoCarac(): Retornar el descuento de la carc.*
      *                                                              *
      *     peEmpr   (input)   Empresa                               *
      *     peSucu   (input)   Sucursal                              *
      *     peRama   (input)   Rama                                  *
      *     peCcba   (input)   Codigo de Caracteristica              *
      *                                                              *
      * Retorna: Codigo de Descuento                                 *
      * ------------------------------------------------------------ *
     D SVPDRV_getDescuentoCarac...
     D                 pr             3  0
     D   peEmpr                       1a   const
     D   peSucu                       2a   const
     D   peRama                       2  0 const
     D   peCcba                       3  0 const

      * ------------------------------------------------------------ *
      * SVPDRV_getCaracDescuento(): Retorna caracteristicas que      *
      * que tiene el descuento                                       *
      *                                                              *
      *     peCcbp   (input)   Codigo de Descuento                   *
      *     peLcar   (output)  Lista Caracteristicas                 *
      *     peLcarC  (output)  Cantidad Lista Caracteristicas        *
      *                                                              *
      * Retorna: Lista de Caracteristicas                            *
      * ------------------------------------------------------------ *
     D SVPDRV_getCaracDescuento...
     D                 pr              n
     D   peCcbp                       3  0 const
     D   peLcar                            likeds(carac_t) dim(99)
     D   peLcarC                     10i 0

      * ------------------------------------------------------------ *
      * SVPDRV_chkCoberturaDescuento(): Chequea si la cobertura es   *
      * afectada por el descuento                                    *
      *                                                              *
      *     peCcbp   (input)   Codigo de Descuento                   *
      *     peXcob   (input)   Cobertura                             *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     D SVPDRV_chkCoberturaDescuento...
     D                 pr              n
     D   peCcbp                       3  0 const
     D   peXcob                       3  0 const
     D   peFech                       8  0 options (*Omit:*Nopass)

      * ------------------------------------------------------------ *
      * SVPDRV_getCoberturaDescuento(): Retorna las coberturas       *
      * afectadas por el descuento                                   *
      *                                                              *
      *     peCcbp   (input)   Codigo de Descuento                   *
      *     peArcd   (input)   Codigo de Articulo                    *
      *     peRama   (input)   Codigo de Rama                        *
      *     peXpro   (input)   Codigo de Producto                    *
      *     peLcob   (output)  Lista Cobertura                       *
      *     peLcobC  (output)  Cantidad Cobertura                    *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     D SVPDRV_getCoberturaDescuento...
     D                 pr              n
     D   peCcbp                       3  0 const
     D   peArcd                       6  0 const
     D   peRama                       2  0 const
     D   peXpro                       3  0 const
     D   peLdes                            likeds(cobCa_t) dim(999)
     D   peLdesC                     10i 0
     D   peFech                       8  0 options (*Omit:*Nopass)

      * ------------------------------------------------------------ *
      * SVPDRV_getCoberturaDescuentoCab(): Retorna las coberturas    *
      * afectadas por el descuento. Filtro para Arcd/Rama/Xpro       *
      *                                                              *
      *     peCcbp   (input)   Codigo de Descuento                   *
      *     peArcd   (input)   Articulo                              *
      *     peRama   (input)   Rama                                  *
      *     peXpro   (input)   Producto                              *
      *     peLcob   (output)  Lista Cobertura                       *
      *     peLcobC  (output)  Cantidad Cobertura                    *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     D SVPDRV_getCoberturaDescuentoCab...
     D                 pr              n
     D   peCcbp                       3  0 const
     D   peArcd                       6  0 const
     D   peRama                       2  0 const
     D   peXpro                       3  0 const
     D   peLdes                            likeds(cobCa_t) dim(999)
     D   peLdesC                     10i 0

      * ------------------------------------------------------------ *
      * SVPDRV_getDescuentosCobertura(): Retorna los Descuentos      *
      * afectados por la cobertura                                   *
      *                                                              *
      *     peXcob   (input)   Cobertura                             *
      *     peLdes   (output)  Lista Descuentos                      *
      *     peLdesC  (output)  Cantidad Descuentos                   *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     D SVPDRV_getDescuentosCobertura...
     D                 pr              n
     D   peXcob                       3  0 const
     D   peLdes                            likeds(cobCa_t) dim(999)
     D   peLdesC                     10i 0
     D   peFech                       8  0 options (*Omit:*Nopass)

      * ------------------------------------------------------------ *
      * SVPDRV_chkDescuento(): Retorna si se realizaron Descuentos   *
      *                                                              *
      *     peNive   (input)  % por Niveles                          *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     D SVPDRV_chkDescuento...
     D                 pr              n
     D   peNive                            likeds(descCo_t)

      * ------------------------------------------------------------ *
      * SVPDRV_getDescuentosCobNiv():Retorna niveles de descuentos   *
      *                                                              *
      *     peLdes   (input)  Lista Descuentos                       *
      *     peLdec   (output) Lista de Coberturas x % Niveles        *
      *     peLdecC  (output) Cantidad de Lista                      *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     D SVPDRV_getDescuentosCobNiv...
     D                 pr              n
     D   peLdes                            likeds(cobCa_t) dim(999) const
     D   peLdesC                     10i 0
     D   peLdec                            likeds(descCo_t) dim(999)
     D   peLdecC                     10i 0

      * ------------------------------------------------------------ *
      * SVPDRV_chkCobList(): Retorna si Cobertura en Lista           *
      *                                                              *
      *     peLcob   (input)  Lista de Coberturas                    *
      *     peXcob   (input)  Cobertura                              *
      *                                                              *
      * Retorna: Posicion / 0 si no existe                           *
      * ------------------------------------------------------------ *
     D SVPDRV_chkCobList...
     D                 pr            10i 0
     D   peLcob                            likeds(descCo_t) dim(20) const
     D   peXcob                       3  0 const

      * ------------------------------------------------------------ *
      * SVPDRV_inz(): Inicializa módulo.                             *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     D SVPDRV_inz      pr

      * ------------------------------------------------------------ *
      * SVPDRV_end(): Finaliza módulo.                               *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     D SVPDRV_end      pr

      * ------------------------------------------------------------ *
      * SVPDRV_error(): Retorna el último error del service program  *
      *                                                              *
      *     peEnbr   (output)  Número de error (opcional)            *
      *                                                              *
      * Retorna: Mensaje de error.                                   *
      * ------------------------------------------------------------ *
     D SVPDRV_error    pr            80a
     D   peEnbr                      10i 0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SVPDRV_getListaCodBuenResultado(): Retorna Lista de Cód.     *
      *                                    de Buen Resultado         *
      *     peEmpr   (input)  Empresa                                *
      *     peSucu   (input)  Sucursal                               *
      *     peLBue   (output) Lista de Códigos                       *
      *     peLBueC  (output) Cantidad                               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     D SVPDRV_getCodBuenResultado...
     D                 pr              n
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peLBue                       3  0 dim(10)
     D   peLBueC                     10i 0

