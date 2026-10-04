      /if defined(SPVFAC_H)
      /eof
      /endif
      /define SPVFAC_H

      * Factura no Disponible...
     D SPVFAC_FACND    c                   const(0001)
      * Factura Duplicada...
     D SPVFAC_FACDU    c                   const(0002)
      * Factura Inexistente...
     D SPVFAC_FACIN    c                   const(0003)
      * Marca Erronea...
     D SPVFAC_MARER    c                   const(0004)
      * Cuit en Blanco...
     D SPVFAC_CUITB    c                   const(0005)

      * --------------------------------------------------- *
      * Estrucutura de datos con el último error
      * --------------------------------------------------- *
     D SPVFAC_ERDS_T   ds                  qualified
     D                                     based(template)
     D   Errno                        4s 0
     D   Msg                         80a

      * --------------------------------------------------- *
      * Estrucutura de datos Cnhfac
      * --------------------------------------------------- *
     D DsCnhfac_t      ds                  qualified template
     D accuit                        11
     D actifa                         2p 0
     D acsufa                         4p 0
     D acnrfa                         8p 0
     D acfefa                         8p 0
     D acfech                         8p 0
     D acsecu                         3p 0
     D acempr                         1
     D acsucu                         2
     D acartc                         2p 0
     D acpacp                         6p 0
     D accoma                         2
     D acnrma                         7p 0
     D acmoti                       350
     D acma01                         1
     D acma02                         1
     D acma03                         1
     D acma04                         1
     D acma05                         1
     D acma06                         1
     D acma07                         1
     D acma08                         1
     D acma09                         1
     D acma10                         1
     D acuser                        10
     D acdate                         6p 0
     D actime                         6p 0
     D acseco                         2p 0

      * ------------------------------------------------------------ *
      * SPVFAC_chkDispFac(): Valida Disponibilidad Factura ODP       *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peFech   (input)   Fecha                                 *
      *     peEmpr   (output)  Empresa                               *
      *     peSucu   (output)  Sucursal                              *
      *     peArtc   (output)  Codigo Area Tecnica                   *
      *     pePacp   (output)  Numero ODP                            *
      *     peSeco   (output)  Secuencia Comprobante de Pago ODP     *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_chkDispFac...
     D                 pr              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peFech                       8  0 options(*nopass:*omit)
     D   peEmpr                       1    options(*nopass:*omit)
     D   peSucu                       2    options(*nopass:*omit)
     D   peArtc                       2  0 options(*nopass:*omit)
     D   pePacp                       6  0 options(*nopass:*omit)
     D   peSeco                       2  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SPVFAC_setFac(): Graba Factura                               *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peFefa   (input)   Fecha Facura                          *
      *     peEmpr   (input)   Empresa                               *
      *     peSucu   (input)   Sucursal                              *
      *     peArtc   (input)   Codigo Area Tecnica                   *
      *     pePacp   (input)   Numero ODP                            *
      *     peComa   (input)   Codigo Mayor Auxiliar                 *
      *     peNrma   (input)   Numero Mayor Auxiliar                 *
      *     peMoti   (input)   Motivo                                *
      *     peUser   (input)   Usuario                               *
      *     peMar1   (input)   Marca Disponible                      *
      *     peSeco   (input)   Secuencia Comprobante ODP             *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_setFac...
     D                 pr              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peFefa                       8  0 const
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peArtc                       2  0 const
     D   pePacp                       6  0 const
     D   peComa                       2    const
     D   peNrma                       7  0 const
     D   peMoti                     350    const
     D   peUser                      10    const
     D   peMar1                       1    options(*nopass:*omit)
     D   peSeco                       2  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SPVFAC_updOdpFac(): Actualiza datos de ODP en la factura     *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peEmpr   (input)   Empresa                               *
      *     peSucu   (input)   Sucursal                              *
      *     peArtc   (input)   Codigo Area Tecnica                   *
      *     pePacp   (input)   Numero ODP                            *
      *     peUser   (input)   Usuario                               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_updOdpFac...
     D                 pr              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peArtc                       2  0 const
     D   pePacp                       6  0 const
     D   peUser                      10    const

      * ------------------------------------------------------------ *
      * SPVFAC_updFac(): Actualiza Estado en Factura                 *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peUser   (input)   Usuario                               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_updFac...
     D                 pr              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peUser                      10    const

      * ------------------------------------------------------------ *
      * SPVFAC_getEstFac(): Obitiene Disponibilidad Factura ODP      *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_getEstFac...
     D                 pr              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peFech                       8  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SPVFAC_getSec(): Obtiene Secuencia de nuevo registro         *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *                                                              *
      * Retorna: Secuencia                                           *
      * ------------------------------------------------------------ *

     D SPVFAC_getSec...
     D                 pr             3  0
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const

      * ------------------------------------------------------------ *
      * SPVFAC_chkFac(): Valida si Existe Factura en CNHFAC          *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_chkFac...
     D                 pr              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const

      * ------------------------------------------------------------ *
      * SPVFAC_getValSini(): Obtiene si valida o no siniestros       *
      *                                                              *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_getValSini...
     D                 pr              n
     D   peFech                       8  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SPVFAC_getValAdmi(): Obtiene si valida o no contaduria       *
      *                                                              *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_getValAdmi...
     D                 pr              n
     D   peFech                       8  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SPVFAC_getValLega(): Obtiene si valida o no legales          *
      *                                                              *
      *     peFech   (input)   Fecha                                 *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_getValLega...
     D                 pr              n
     D   peFech                       8  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SPVFAC_inz(): Inicializa módulo.                             *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     D SPVFAC_inz      pr

      * ------------------------------------------------------------ *
      * SPVFAC_end(): Finaliza módulo.                               *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     D SPVFAC_end      pr

      * ------------------------------------------------------------ *
      * SPVFAC_error(): Retorna el último error del service program  *
      *                                                              *
      *     peEnbr   (output)  Número de error (opcional)            *
      *                                                              *
      * Retorna: Mensaje de error.                                   *
      * ------------------------------------------------------------ *
     D SPVFAC_error    pr            80a
     D   peEnbr                      10i 0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * SPVFAC_updFacPacp(): Actualiza Estado en por nro de Comprob. *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peArtc   (input)   Codigo Area Tecnica                   *
      *     pePacp   (input)   Numero ODP                            *
      *     peUser   (input)   Usuario                               *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *

     D SPVFAC_updFacPacp...
     D                 pr              n
     D   peCuit                      11    const
     D   peArtc                       2  0 const
     D   pePacp                       6  0 const
     D   peUser                      10    const

      * ------------------------------------------------------------ *
      * SPVFAC_valRelAnulacion: Valida la relacion de anulaciones    *
      *                         por Tipo Comprobante                 *
      *                                                              *
      *     peFa1    ( input  ) Primer Tipo Comprobante              *
      *     peFa2    ( input  ) Segundo Tipo Comprobante             *
      *                                                              *
      * Retorna: *On / *Off                                          *
      * ------------------------------------------------------------ *
     D SPVFAC_valRelAnulacion...
     D                 pr              n
     D   peFa1                        2  0 const
     D   peFa2                        2  0 const

      * ------------------------------------------------------------ *
      * SPVFAC_getFac(): Retorna datos de Facturas.-                 *
      *                                                              *
      *     peCuit   (input)   CUIT                                  *
      *     peTifa   (input)   Tipo de Factura                       *
      *     peSufa   (input)   Sucursal de Factura                   *
      *     peNrfa   (input)   Numero de Factura                     *
      *     peDsFa   ( output ) Estructura de Facturas               *
      *     peDsFaC  ( output ) Cantidad de Facturas                 *
      *                                                              *
      * Retorna: *on = Si encontro / *off = si no encontro           *
      * ------------------------------------------------------------ *
     D SPVFAC_getFac...
     D                 pr              n
     D   peCuit                      11    const
     D   peTifa                       2  0 const
     D   peSufa                       4  0 const
     D   peNrfa                       8  0 const
     D   peDsFa                            likeds ( DsCnhfac_t ) dim(999)
     D                                     options(*nopass:*omit)
     D   peDsFaC                     10i 0 options(*nopass:*omit)


