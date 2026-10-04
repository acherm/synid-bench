      /if defined(COWVEH_H)
      /eof
      /endif
      /define COWVEH_H

      /copy './qcpybooks/svpfma_h.rpgle'
      /copy './qcpybooks/svpint_h.rpgle'
      /copy './qcpybooks/cowgrai_h.rpgle'
      /copy './qcpybooks/spvveh_h.rpgle'
      /copy './qcpybooks/cowrtv_h.rpgle'
      /copy './qcpybooks/svpval_h.rpgle'
      /copy './qcpybooks/svpws_h.rpgle'
      /copy './qcpybooks/czwutl_h.rpgle'
      /copy './qcpybooks/svpcob_h.rpgle'
      /copy './qcpybooks/svplrc_h.rpgle'
      /copy './qcpybooks/wsstruc_h.rpgle'
      /copy './qcpybooks/svpbue_h.rpgle'
      /copy './qcpybooks/svpren_h.rpgle'
      /copy './qcpybooks/svpvls_h.rpgle'
      /copy './qcpybooks/svpdau_h.rpgle'
      /copy './qcpybooks/prwase_h.rpgle'

      * Año de Vehículo Invalido para Emision...
     D COWVEH_ANIONP   c                   const(0001)
      * No puede mantener Cobertura...
     D COWVEH_NOCOB    c                   const(0002)
      * Mantuvo Cobertura...
     D COWVEH_SICOB    c                   const(0003)

     D cobVeh          ds                  qualified based(template)
     D   cobl                         2
     D   cobd                        40
     D   rast                         1
     D   cras                         3  0
     D   insp                         1
     D   sele                         1
     D   prim                        15p 2
     D   prem                        15p 2
     D   cdft                         1
     D   ifra                        15p 2
     D   rcle                        15p 2
     D   rcco                        15p 2
     D   rcac                        15p 2
     D   lrce                        15p 2
     D   claj                         3  0

     D cob225          ds                  qualified based(template) dim(99)
     D   cobc                         2
     D   coss                         2
     D   ccrc                         1
     D
     D textdeta        ds                  qualified based(template)
     D   tpnl                         3  0
     D   tpds                        79
      *
     D dsCarac_t       ds                  qualified based(template)
     D t4Empr                         1
     D t4Sucu                         2
     D t4Nivt                         1P 0
     D t4Nivc                         5P 0
     D t4Nctw                         7P 0
     D t4Rama                         2P 0
     D t4Arse                         2P 0
     D t4Poco                         4P 0
     D t4Cobl                         2
     D t4Ccbp                         3P 0
     D t4Pcbp                         5P 2
     D t4ma01                         1
     D t4ma02                         1
     D t4ma03                         1
     D t4ma04                         1
     D t4ma05                         1
      *
     D vehi_t          ds                  qualified based(template)
     D  nroComponente                 4P 0
     D  patente                      25
     D  chasis                       25
     D  motor                        25
     D  sumaAsegurada                15p 2

      * -----------------------------------------------------------
      * Datos Prod.Art. Rama Automotores Scoring
      * -----------------------------------------------------------
     D dsctwet3_t      ds                  qualified based(template)
     D  t3Empr                        1
     D  t3Sucu                        2
     D  t3Nivt                        1  0
     D  t3Nivc                        5  0
     D  t3Nctw                        7  0
     D  t3Rama                        2  0
     D  t3Arse                        2  0
     D  t3Poco                        4  0
     D  t3Taaj                        2  0
     D  t3Cosg                        4
     D  t3Tiaj                        1
     D  t3Tiac                        1
     D  t3Vefa                        1
     D  t3Corc                        7  4
     D  t3Coca                        7  4
     D  t3Mar1                        1
     D  t3Mar2                        1
     D  t3Mar3                        1
     D  t3Mar4                        1
     D  t3Mar5                        1
     D  t3Strg                        1
     D  t3User                       10
     D  t3Time                        6  0
     D  t3Date                        8  0
     D  t3Cant                        2  0

      * -----------------------------------------------------------*
      * Descuentos de vehiculos.                                   *
      *------------------------------------------------------------*
     D dsCtwet4_t      ds                  qualified template
     D  t4empr                        1
     D  t4sucu                        2
     D  t4nivt                        1p 0
     D  t4nivc                        5p 0
     D  t4nctw                        7p 0
     D  t4rama                        2p 0
     D  t4arse                        2p 0
     D  t4poco                        4p 0
     D  t4cobl                        2
     D  t4ccbp                        3p 0
     D  t4pcbp                        5p 2
     D  t4ma01                        1
     D  t4ma02                        1
     D  t4ma03                        1
     D  t4ma04                        1
     D  t4ma05                        1

      * -----------------------------------------------------------*
      * Cabecera de cotizacion -                                   *
      *------------------------------------------------------------*
     D dsCtwet0_t      ds                  qualified template
     D  t0empr                        1a
     D  t0sucu                        2a
     D  t0nivt                        1p 0
     D  t0nivc                        5p 0
     D  t0nctw                        7p 0
     D  t0rama                        2p 0
     D  t0arse                        2p 0
     D  t0poco                        4p 0
     D  t0vhmc                        3a
     D  t0vhmo                        3a
     D  t0vhcs                        3a
     D  t0vhde                       40a
     D  t0vhcr                        3a
     D  t0vhan                        4p 0
     D  t0vhni                        1a
     D  t0moto                       25a
     D  t0chas                       25a
     D  t0vhca                        2p 0
     D  t0vhv1                        1p 0
     D  t0vhv2                        1p 0
     D  t0mtdf                        1a
     D  t0vhct                        2p 0
     D  t0vhuv                        2p 0
     D  t0vhvu                       15p 2
     D  t0m0km                        1a
     D  t0rcle                       15p 2
     D  t0rcco                       15p 2
     D  t0rcac                       15p 2
     D  t0lrce                       15p 2
     D  t0claj                        3p 0
     D  t0copo                        5p 0
     D  t0cops                        1p 0
     D  t0scta                        1p 0
     D  t0mgnc                        1a
     D  t0rgnc                        9p 2
     D  t0ruta                       16p 0
     D  t0tmat                        3a
     D  t0nmat                       25a
     D  t0ctre                        5p 0
     D  t0rebr                        1p 0
     D  t0nmer                       40a
     D  t0aver                        1a
     D  t0mar4                        1a
     D  t0iris                        1a
     D  t0cesv                        1a
     D  t0ma01                        1a
     D  t0ma02                        1a
     D  t0ma03                        1a
     D  t0ma04                        1a
     D  t0ma05                        1a
     D  t0clin                        1a
     D  t0sast                       13p 0
     D  t0acrc                        7p 0
     D  t0dweb                        1a
     D  t0pweb                        5p 2

      * -----------------------------------------------------------
      * Datos Prod.Art. Rama Automotores Scoring
      * -----------------------------------------------------------
     D dsCtwet5_t      ds                  qualified template
     D  t5empr                        1a
     D  t5sucu                        2a
     D  t5nivt                        1p 0
     D  t5nivc                        5p 0
     D  t5nctw                        7p 0
     D  t5rama                        2p 0
     D  t5arse                        2p 0
     D  t5poco                        4p 0
     D  t5suop                        3p 0
     D  t5cert                        9p 0
     D  t5poli                        7p 0
     D  t5cdaÑ                        4p 0
     D  t5daÑl                      200a
     D  t5edaÑ                        1a
     D  t5mar1                        1a
     D  t5mar2                        1a
     D  t5mar3                        1a
     D  t5mar4                        1a
     D  t5mar5                        1a
     D  t5mar6                        1a
     D  t5mar7                        1a
     D  t5mar8                        1a
     D  t5mar9                        1a
     D  t5mar0                        1a
     D  t5user                       10a
     D  t5date                        8p 0
     D  t5time                        6p 0

      * -----------------------------------------------------------
      * Factores Multiplicativos
      * -----------------------------------------------------------
     D dsCtwEt7_t      ds                  qualified template
     D  t7empr                        1a
     D  t7sucu                        2a
     D  t7nivt                        1  0
     D  t7nivc                        5  0
     D  t7nctw                        7  0
     D  t7rama                        2  0
     D  t7arse                        2  0
     D  t7poco                        4  0
     D  t7cobl                        2a
     D  t7ccoe                        3  0
     D  t7coef                        7  4
     D  t7mar2                        1a
     D  t7date                        8  0
     D  t7time                        6  0
     D  t7user                       10a

      * -----------------------------------------------------------
      * Factores Multiplicativos
      * -----------------------------------------------------------
     D factores_t      ds                  qualified template
     D  cobl                          2a
     D  ccoe                          3  0
     D  dcoe                         25
     D  coef                          7  4
     D  mar2                          1a

      * -----------------------------------------------------------------*
      * COWVEH_cotizarWeb():  Recibe todos los datos del vehiculo y de - *
      *                       vuelve las posibles coberturas, primas y   *
      *                       bonificaciones                             *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peNrrp  -  Plan de Pago                           *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de IVA                          *
      *                peAcce  -  Lista de Accesorios                    *
      *        Output:                                                   *
      *                peCtre  -  Código de Tarifa                       *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  Bonificaciones por cobertura           *
      *                peImpu  -  Impuestos                              *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * -----------------------------------------------------------------*
     D COWVEH_cotizarWeb...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0 const
     D   pePoco                       4  0   const
     D   peVhan                       4      const
     D   peVhmc                       3      const
     D   peVhmo                       3      const
     D   peVhcs                       3      const
     D   peVhvu                      15  2   const
     D   peMgnc                       1      const
     D   peRgnc                       7  2   const
     D   peCopo                       5  0   const
     D   peCops                       1  0   const
     D   peScta                       1  0   const
     D   peClin                       1      const
     D   peBure                       1  0   const
     D   peNrrp                       3  0   const
     D   peTipe                       1      const
     D   peCiva                       2  0   const
     D   peAcce                            likeds( AccVeh_t ) dim(100)const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh) dim (20)
     D   peBoni                            likeds(bonVeh) dim (99)
     D   peImpu                            likeds(Impuesto) dim (99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)
      * ---------------------------------------------------------------- *
      * COWVEH_reCotizar():   Recibe todos los datos del vehículo y de - *
      *                       vuelve las posibles coberturas, primas y   *
      *                       bonificaciones                             *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peNrrp  -  Plan de Pago                           *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de IVA                          *
      *                peAcce  -  Lista de Accesorios                    *
      *        Output:                                                   *
      *                peCtre  -  Código de Tarifa                       *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  Bonificaciones por cobertura           *
      *                peImpu  -  Impuestos                              *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_reCotizarWeb...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peVhvu                      15  2 const
     D   peMgnc                       1    const
     D   peRgnc                       7  2 const
     D   peCopo                       5  0 const
     D   peCops                       1  0 const
     D   peScta                       1  0 const
     D   peClin                       1    const
     D   peBure                       1  0 const
     D   peNrrp                       3  0 const
     D   peTipe                       1    const
     D   peCiva                       2  0 const
     D   peAcce                            likeds( AccVeh_t ) dim(100)const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh)  dim(20)
     D   peBoni                            likeds(bonVeh)  dim(99)
     D   peImpu                            likeds(Impuesto) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)
      * -----------------------------------------------------------------*
      * COWVEH_anioVehiculo():Valida que el año del vehículo sea valido  *
      *                       para la emisión.                           *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peVhan  -  Año del Vehículo                       *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_anioVehiculo...
     D                 pr              n
     D   peVhan                       4    const
     D
      * ---------------------------------------------------------------- *
      * COWVEH_codigoTarifa():Busca la tarifa dependiendo de la fecha    *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peFtar  -  Fecha de tarifa                        *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_codigoTarifa...
     D                 pr             5  0
     D   peFtar                       8  0 const
      * ---------------------------------------------------------------- *
      * COWVEH_saveCabecera   ():Graba cabecera de la cotizacion de auto *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peCfpg  -  Código Forma de Pago                   *
      *                peTipe  -  Tipo de Persona                        *
      *                peCtre  -  Código de Tarifa                       *
      *                pePweb  -  % Descuento Web                        *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_saveCabecera...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0   const
     D   pePoco                       4  0   const
     D   peVhan                       4      const
     D   peVhmc                       3      const
     D   peVhmo                       3      const
     D   peVhcs                       3      const
     D   peVhvu                      15  2   const
     D   peMgnc                       1      const
     D   peRgnc                       7  2   const
     D   peCopo                       5  0   const
     D   peCops                       1  0   const
     D   peScta                       1  0   const
     D   peClin                       1      const
     D   peBure                       1  0   const
     D   peCfpg                       1  0   const
     D   peTipe                       1      const
     D   peCtre                       5  0   const
     D   peDesE                       5  2   const

      * ---------------------------------------------------------------- *
      * COWVEH_porcAjuste()  : obtener porcentaje de ajuste automatico   *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peArcd  -  Artículo                               *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_porcAjuste...
     D                 pr             3  0
     D   peArcd                       6  0  const
     D   peRama                       2  0  const
     D   peArse                       2  0  const
      * ---------------------------------------------------------------- *
      * COWVEH_getTablaRC()  :obtener la tabla RC.                       *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_getTablaRC...
     D                 pr              n
     D   peCtre                       5  0  const
     D   peScta                       1  0  const
     D   peMone                       2     const
     D   peMgnc                       1     const
     D   peVhni                       1     const
     D   peVhca                       2  0  const
     D   peVhv1                       1  0  const
     D   peVhv2                       1  0
     D   peFemi                       8  0  const
     D   peMtdf                       1     const
     D   peTarc                       2  0
     D   peTair                       2  0
      * ---------------------------------------------------------------- *
      * COWVEH_codigoZona()  :Busca la Zona a la que Pertenece el auto   *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_codigoZona...
     D                 pr             1  0
     D   peCopo                       5  0 const
     D   peCops                       1  0 const
      * ---------------------------------------------------------------- *
      * COWVEH_vehiculo0km() :Valida si es un 0KM o no                   *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peVhan  -  Año del Vehículo                       *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_vehiculo0km...
     D                 pr             1
     D   peVhan                       4    const
      * ---------------------------------------------------------------- *
      * COWVEH_saveCoberturas   ():Graba coberturas de la cotizacion auto*
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peCfpg  -  Código Forma de Pago                   *
      *                peTipe  -  Tipo de Persona                        *
      *                peCtre  -  Código de Tarifa                       *
      *                                                                  *
      *        Output:                                                   *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                pePaxc  -  Bonificaciones por cobertura           *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_saveCoberturas...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0 const
     D   pePoco                       4  0   const
     D   peVhan                       4      const
     D   peVhmc                       3      const
     D   peVhmo                       3      const
     D   peVhcs                       3      const
     D   peVhvu                      15  2   const
     D   peMgnc                       1      const
     D   peRgnc                       7  2   const
     D   peCopo                       5  0   const
     D   peCops                       1  0   const
     D   peScta                       1  0   const
     D   peClin                       1      const
     D   peBure                       1  0   const
     D   peCfpg                       1  0   const
     D   peTipe                       1      const
     D   peCtre                       5  0   const
     D   pePaxc                            likeds(cobVeh) dim (20)
     D   peBoni                            likeds(BonVeh) dim (99)
     D   peImpu                            likeds(Impuesto) dim(99)
      * ---------------------------------------------------------------- *
      * COWVEH_saveCoberturasRec():Graba coberturas de cotizacion de auto*
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peCfpg  -  Código Forma de Pago                   *
      *                peTipe  -  Tipo de Persona                        *
      *                peCtre  -  Código de Tarifa                       *
      *                                                                  *
      *        Output:                                                   *
      *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  bonificacion por cobertura             *
      *
      * ---------------------------------------------------------------- *
     D COWVEH_saveCoberturasRec...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0 const
     D   pePoco                       4  0   const
     D   peVhan                       4      const
     D   peVhmc                       3      const
     D   peVhmo                       3      const
     D   peVhcs                       3      const
     D   peVhvu                      15  2   const
     D   peMgnc                       1      const
     D   peRgnc                       7  2   const
     D   peCopo                       5  0   const
     D   peCops                       1  0   const
     D   peScta                       1  0   const
     D   peClin                       1      const
     D   peBure                       1  0   const
     D   peCfpg                       1  0   const
     D   peTipe                       1      const
     D   peCtre                       5  0   const
     D   pePaxc                            likeds(cobVeh)  dim(20)
     D   peBoni                            likeds(bonVeh)  dim(99)
     D   peImpu                            likeds(Impuesto) dim(99)
      * ---------------------------------------------------------------- *
      * COWVEH_getCoberturas():Busca posibles coberturas para el auto    *
      *                                                                  *
      *        Input:                                                    *
      *                peVhan  -  Año del Vehículo                       *
      *                peTiou  -  Tipo operacion usuario                 *
      *                peStou  -  Subtipo operacion usuario              *
      *                peStos  -  Subtipo operacion sistema              *
      *        Output:                                                   *
      *                                                                  *
      *                peCveh  -  Coberturas                             *
      *                peccob  -  Cant de coberturas                     *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_getCoberturas...
     D                 pr              n
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peScta                       1  0 const
     D   peTiou                       1  0 const
     D   peStou                       2  0 const
     D   peStos                       2  0 const
     D   peCveh                            likeds(cob225) dim(99)
     D   peCcob                       2  0
      * ---------------------------------------------------------------- *
      * COWVEH_getPrimas  ():Selecciona el monto de la cobertura RC      *
      *                     dependiendo de la forma de cobertura RC      *
      *        Input :                                                   *
      *                                                                  *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhan  -  Año del Vehículo                       *
      *                peMgnc  -  Marca GNC                              *
      *                peVhvu  -  Suma Asegurada                         *
      *                peScta  -  Zona de Riesgo                         *
      *                peCtre  -  Código de Tarifa                       *
      *                peArcd  -  Número de Artículo                     *
      *                peMone  -  Código Moneda                          *
      *                peCobl  -  Letra de Cobertura                     *
      *                peCcrc  -  Forma de Cobertura                     *
      *                pePrac  -  Importe prima de accidente             *
      *                pePrin  -  Importe prima de incendio              *
      *                pePrro  -  Importe prima de robo                  *
      *                pePrrc  -  Importe prima de rc                    *
      *                pePrce  -  Prima RC exterior                      *
      *                pePrap  -  Prima accidentes personales            *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_getPrimas...
     D                 pr              n
     D   peVhmc                       3      const
     D   peVhmo                       3      const
     D   peVhcs                       3      const
     D   peVhan                       4      const
     D   peMgnc                       1      const
     D   peVhvu                      15  2   const
     D   peScta                       1  0   const
     D   peCtre                       5  0   const
     D   peArcd                       6  0   const
     D   peMone                       2      const
     D   peCobl                       2      const
     D   peCoss                       2      const
     D   peCcrc                       1      const
     D   pePrac                      15  2
     D   pePrin                      15  2
     D   pePrro                      15  2
     D   pePrrc                      15  2
     D   pePrce                      15  2
     D   pePrap                      15  2
     D   peIfrx                      15  2
      * ---------------------------------------------------------------- *
      * COWVEH_getRastreador():Busca si el vehiculo debe tener rastreador*
      *                        o no.                                     *
      *        Input :                                                   *
      *                                                                  *
      *                peCobl  -  Cobertura                              *
      *                peVhvu  -  Suma Asegurada                         *
      *                peTiou  -  Tipo operacion usuario                 *
      *                peStou  -  Subtipo operacion usuario              *
      *                peStos  -  Subtipo operacion sistema              *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_getRastreador...
     D                 pr             1
     D   peCobl                       2    const
     D   peVhvu                      15  2 const
     D   peTiou                       1  0 const
     D   peStou                       2  0 const
     D   peStos                       2  0 const
      * ---------------------------------------------------------------- *
      * COWVEH_getInspeccion():Busca si el vehiculo debe tener inspeccion*
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peCobl  -  Cobertura                              *
      *                peVhan  -  Año del Vehículo                       *
      *                peTiou  -  Tipo operacion usuario                 *
      *                peStou  -  Subtipo operacion usuario              *
      *                peStos  -  Subtipo operacion sistema              *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_getInspeccion...
     D                 pr             1
     D   peCobl                       2    const
     D   peVhan                       4    const
     D   peTiou                       1  0 const
     D   peStou                       2  0 const
     D   peStos                       2  0 const
      * ---------------------------------------------------------------- *
      * COWVEH_chkCobertura():Busca si el vehiculo debe tener inspeccion *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peCobl  -  Cobertura                              *
      *                peVhan  -  Año del Vehículo                       *
      *                peTiou  -  Tipo operacion usuario                 *
      *                peStou  -  Subtipo operacion usuario              *
      *                peStos  -  Subtipo operacion sistema              *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_chkCobertura...
     D                 pr              n
     D   peCobl                       2    const
     D   peVhan                       4    const
     D   peTiou                       1  0 const
     D   peStou                       2  0 const
     D   peStos                       2  0 const
      * ------------------------------------------------------------ *
      * COWVEH_saveDescuentos   ():Graba Descuentos de cotización de *
      *                          Autos                               *
      *                                                              *
      *        Input :                                               *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Nro. de Componente                 *
      *                peCobl  -  Letra de Cobertura                 *
      *                                                              *
      *        Output:                                               *
      *                peBoni  -  Bonificacion por cobertura         *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_saveDescuentos...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peCobl                       2    const
     D** peBoni                            likeds(bonveh) dim (99)
      * ------------------------------------------------------------ *
      * COWVEH_saveDescuentosRec():Graba Descuentos de la Recotiza-  *
      *                            ción.                             *
      *                                                              *
      *        Input :                                               *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Nro. de Componente                 *
      *                peCobl  -  Letra Cobertura                    *
      *                peBoni  -  Bonificaciones                     *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_saveDescuentosRec...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peBoni                            likeds(bonVeh) dim (99) const
      * ------------------------------------------------------------ *
      * COWVEH_detalleCobertura(): Buscar el texto de las coberturas *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Letra Cobertura                    *
      *                peScta  -  Zona de riesgo                     *
      *                peCobl  -  Letra Cobertura                    *
      *                                                              *
      *        Output:                                               *
      *                                                              *
      *                peTxtd  -  Texto detalle                      *
      *                peTxtdC -  Cantidad de lineas                 *
      *                peErro  -  Indicador de Error                 *
      *                peMsgs  -  Estructura de Error                *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_detalleCobertura...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peScta                       1  0 const
     D   peCobl                       2    const
     D   peTxtd                            likeds(textdeta) dim (999)
     D   peTxtdC                     10i 0
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)
      * ------------------------------------------------------------ *
      * COWVEH_deletePoco(): Elimina los componentes de autos aso-   *
      *                      ciados a la cotización.                 *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Numero de componente               *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_deletePoco...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
      * ------------------------------------------------------------ *
      * COWVEH_deleteCabecera(): Elimina cabecera de cotizacion de   *
      *                          auto                                *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Numero de componente               *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_deleteCabecera...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
      * ------------------------------------------------------------ *
      * COWVEH_deleteCoberturas(): Elimina cabecera de cotizacion de *
      *                            auto                              *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Numero de componente               *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_deleteCoberturas...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
      * ------------------------------------------------------------ *
      * COWVEH_deleteBonificaciones:Elimina cabecera de cotizacion de*
      *                            auto                              *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Numero de componente               *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_deleteBonificaciones...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
      * ---------------------------------------------------------------- *
      * COWVEH_getDuracion  ():Busca la duracion de la cobertura         *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peArcd  -  Número de Artículo .                   *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_getDuracion...
     D                 pr             2  0
     D   peArcd                       6  0 const
      * ------------------------------------------------------------ *
      * COWVEH_origenVehiculo: Busca si el vehiculo es nacional o    *
      *                        importado                             *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peVhmc  -  Marca del Vehículo                 *
      *                peVhmo  -  Modelo del Vehículo                *
      *                peVhcs  -  SubModelo del Vehículo             *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_origenVehiculo...
     D                 pr             1
     D   peVhmc                       3      const
     D   peVhmo                       3      const
     D   peVhcs                       3      const
      * ------------------------------------------------------------ *
      * COWVEH_getDescuentos ():Obtiene los descuentos y actualiza   *
      *                         las coberturas.                      *
      *                                                              *
      *        Input :                                               *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Nro. de Componente                 *
      *                peCobl  -  Letra Cobertura                    *
      *                peBoni  -  Bonificacion/Descuento             *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_getDescuentos...
     D                 pr             5  2
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peCobl                       2    const
      * ------------------------------------------------------------ *
      * COWVEH_aplicaDescuentos():Aplica los descuentos y actualiza  *
      *                           las coberturas.                    *
      *                                                              *
      *        Input :                                               *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Nro. de Componente                 *
      *                peCobl  -  Letra Cobertura                    *
      *                peBoni  -  Bonificacion/Descuento             *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_aplicaDescuentos...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peCobl                       2    const
     D   pePbon                       5  2 const
      * ------------------------------------------------------------ *
      * COWVEH_selectCobertura(): Indica la cobertura que fue        *
      *                           seleccionada.                      *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Letra Cobertura                    *
      *                peCobl  -  Letra Cobertura                    *
      *                                                              *
      *        Output:                                               *
      *                                                              *
      *                peErro  -  Indicador de Error                 *
      *                peMsgs  -  Estructura de Error                *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_selectCobertura...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peCobl                       2    const
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)
      * ------------------------------------------------------------ *
      * COWVEH_sumSelecCobertura():  suma la prima de las coberturas *
      *                              que fueron seleccionadas.       *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Numero de Componente               *
      *                pePrim  -  Prima Total                        *
      *                pePrem  -  Premio Total                       *
      *                peSeri  -  sellado riesgo                     *
      *                peSeem  -  sellado de la empresa              *
      *                peImpi  -  impuestos internos                 *
      *                peSers  -  servicios sociales                 *
      *                peTssn  -  tasa super. seg. nacion.           *
      *                peIpr1  -  impuesto valor agregado            *
      *                peIpr4  -  iva-resp.no inscripto              *
      *                peIpr3  -  iva-importe percepcion             *
      *                peIpr6  -  componente premio 6                *
      *                peIpr7  -  componente premio 7                *
      *                peIpr8  -  componente del premio 8            *
      *                peIpr9  -  componente del premio 9            *
      *                                                              *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_sumSelecCobertura...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   pePrim                      15  2
     D   pePrem                      15  2
     D   peSeri                      15  2
     D   peSeem                      15  2
     D   peImpi                      15  2
     D   peSers                      15  2
     D   peTssn                      15  2
     D   peIpr1                      15  2
     D   peIpr4                      15  2
     D   peIpr3                      15  2
     D   peIpr6                      15  2
     D   peIpr7                      15  2
     D   peIpr8                      15  2
     D   peIpr9                      15  2
      * ------------------------------------------------------------ *
      * COWVEH_updprimasCob  (): Actualiza el valor de la prima y el *
      *                          premio por componente y cobertura   *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Número de Componente               *
      *                peCobl  -  Letra de Cobertura                 *
      *                pePrim  -  Monto Prima                        *
      *                pePrem  -  Monto Premio                       *
      *                peSeri  -  sellado riesgo                      *
      *                peSeem  -  sellado de la empresa               *
      *                peImpi  -  impuestos internos                  *
      *                peSers  -  servicios sociales                  *
      *                peTssn  -  tasa super. seg. nacion.            *
      *                peIpr1  -  impuesto valor agregado             *
      *                peIpr4  -  iva-resp.no inscripto               *
      *                peIpr3  -  iva-importe percepcion              *
      *                peIpr6  -  componente premio 6                 *
      *                peIpr7  -  componente premio 7                 *
      *                peIpr8  -  componente del premio 8             *
      *                peIpr9  -  componente del premio 9             *
      *                                                              *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_updprimasCob...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peCobl                       2    const
     D   pePrim                      15  2 const
     D   pePrem                      15  2 const
     D   peSeri                      15  2   const
     D   peSeem                      15  2   const
     D   peImpi                      15  2   const
     D   peSers                      15  2   const
     D   peTssn                      15  2   const
     D   peIpr1                      15  2   const
     D   peIpr4                      15  2   const
     D   peIpr3                      15  2   const
     D   peIpr6                      15  2   const
     D   peIpr7                      15  2   const
     D   peIpr8                      15  2   const
     D   peIpr9                      15  2   const
      * ------------------------------------------------------------ *
      * COWVEH_setImportesVeh (): llama a los servicios necesarios   *
      *                           para actualizar los importes.      *
      *                                                              *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Nro de Componente                  *
      *                                                              *
      *                                                              *
      *                                                              *
      * -------------------------------------------------------------*
     D COWVEH_setImportesVeh...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
      * ------------------------------------------------------------ *
      * COWVEH_getSumaSiniestrablePoco()devuelve la suma siniestrable*
      *                                 por componente               *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Número de Componente               *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_getSumaSiniestrablePoco...
     D                 pr            13  0
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
      * -----------------------------------------------------------------*
      * COWVEH_cotizador ():  Recibe todos los datos del vehiculo y de - *
      *                       vuelve las posibles coberturas, primas y   *
      *                       bonificaciones                             *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peCfpg  -  Código Forma de Pago                   *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de IVA                          *
      *                peNrrp  -  Plan de Pago                           *
      *                peAcce  -  Accesorios                             *
      *                peDesE  -  Descuento Especial                     *
      *                peTaaj  -  Código de Cuestionario                 *
      *                peScor  -  Scoring                                *
      *        Output:                                                   *
      *                peCtre  -  Código de Tarifa                       *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  Bonificaciones por cobertura           *
      *                peImpu  -  Impuestos                              *
      *                peFact  -  Factores Multiplicativos               *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * -----------------------------------------------------------------*
     D COWVEH_cotizador...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0 const
     D   pePoco                       4  0   const
     D   peVhan                       4      const
     D   peVhmc                       3      const
     D   peVhmo                       3      const
     D   peVhcs                       3      const
     D   peVhvu                      15  2   const
     D   peMgnc                       1      const
     D   peRgnc                       7  2   const
     D   peCopo                       5  0   const
     D   peCops                       1  0   const
     D   peScta                       1  0   const
     D   peClin                       1      const
     D   peBure                       1  0   const
     D   peCfpg                       1  0   const
     D   peTipe                       1      const
     D   peCiva                       2  0   const
     D   peNrpp                       3  0   const
     D   peAcce                            likeds(AccVeh_t) dim(100) const
     D   peDesE                       5  2 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh) dim (20)
     D   peBoni                            likeds(bonVeh) dim (99)
     D   peImpu                            likeds(Impuesto) dim (99)
     D   peFact                            likeds(factores_t) dim(999)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)
      * ------------------------------------------------------------ *
      * COWVEH_setPrimasPorProvincias(): llama a los servicios para  *
      *                                  actualizar las primas por   *
      *                                  provincia.                  *
      *        Input :                                               *
      *                                                              *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                               *
      *                peArse  -  Cant. Pólizas por Rama             *
      *                pePoco  -  Nro de Componente                  *
      *                pePrim  -  Prima del Componente               *
      *                pePrem  -  Premio del componente              *
      *                pePrem  -  Premio del componente              *
      *                peIndo  -  Indicador de Operacion (Save/Dlt)  *
      *                                                              *
      * -------------------------------------------------------------*
     D COWVEH_setPrimasPorProvincias...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   pePrim                      15  2 const
     D   pePrem                      15  2 const
     D   peIndo                       1    const
      * ---------------------------------------------------------------- *
      * COWVEH_getCoberturaPorDefault(): obtener cobertura default       *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peArcd  -  Artículo                               *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_getCoberturaPorDefault...
     D                 pr             2
     D   peArcd                       6  0  const
     D   peRama                       2  0  const
     D   peArse                       2  0  const
      * ---------------------------------------------------------------- *
      * COWVEH_chkAccesorios():Validar que la suma de accesorios no su-  *
      *                        pere el %maximo permitido                 *
      *        Input :                                                   *
      *                                                                  *
      *                peCobl  -  Cobertura                              *
      *                peVhan  -  Año del Vehículo                       *
      *                peTiou  -  Tipo operacion usuario                 *
      *                peStou  -  Subtipo operacion usuario              *
      *                peStos  -  Subtipo operacion sistema              *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_chkAccesorios...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peCobl                       2    const
     D   peSuma                      15  2 const
      * ------------------------------------------------------------ *
      * COWVEH_inz(): Inicializa módulo.                             *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     D COWVEH_inz      pr
      * ------------------------------------------------------------ *
      * COWVEH_end():  Finaliza módulo.                              *
      *                                                              *
      * void                                                         *
      * ------------------------------------------------------------ *
     D COWVEH_end      pr
      * ------------------------------------------------------------ *
      * COWVEH_error(): Retorna el último error del service program  *
      *                                                              *
      *     peEnbr   (output)  Número de error (opcional)            *
      *                                                              *
      * Retorna: Mensaje de error.                                   *
      * ------------------------------------------------------------ *
     D COWVEH_error    pr            80a
     D   peEnbr                      10i 0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * COWVEH_saveAccesorios(): Salvar accesorios de un vehículo.   *
      *                                                              *
      *        peBase  (input)  Parámetro Base                       *
      *        peNctw  (input)  Número de Cotización                 *
      *        peRama  (input)  Rama                                 *
      *        peArse  (input)  Secuencia de Rama en Artículo        *
      *        pePoco  (input)  Número de Componente                 *
      *        peAcce  (input)  Lista de Accesorios                  *
      *                                                              *
      * ------------------------------------------------------------ *
     D COWVEH_saveAccesorios...
     D                 pr             1n
     D  peBase                             likeds(paramBase) const
     D  peNctw                        7  0 const
     D  peRama                        2  0 const
     D  peArse                        2  0 const
     D  pePoco                        4  0 const
     D  peAcce                             likeds(AccVeh_t) dim(100) const
      * ---------------------------------------------------------------- *
      * COWVEH_setCoberturaPorDefecto(): selecciona cobertura por        *
      *                                  defecto                         *
      *                                                                  *
      *        Input :                                                   *
      *                peBase  -  Parametros Base                        *
      *                peNctw  -  Nro. Cotizacion                        *
      *                peArcd  -  Artículo                               *
      *                peRama  -  Coberturas                             *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro de Componente                      *
      *                peCcob  -  Cantidad de Coberturas                 *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                                                                  *
      * Retorna *on / *off                                               *
      * ---------------------------------------------------------------- *
     D COWVEH_setCoberturaPorDefecto...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peArcd                       6  0  const
     D   peRama                       2  0  const
     D   peArse                       2  0  const
     D   pePoco                       4  0  const
     D   peCcob                       2  0  const
     D   pePaxc                            likeds(cobVeh) dim(20)

      * ---------------------------------------------------------------- *
      * COWVEH_getCaracteristicas() : Retornar Registros de Ctwet4       *
      *                                                                  *
      *     peBase  (input)   Base                                       *
      *     peNctw  (input)   Nro. Cotización                            *
      *     peDsCt4 (output)  Registro con Ctwte4                        *
      *                                                                  *
      * Retorna *on/*off                                                 *
      * ---------------------------------------------------------------- *
     D COWVEH_getCaracteristicas...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 options(*nopass:*omit)
     D   peArse                       2  0 options(*nopass:*omit)
     D   pePoco                       4  0 options(*nopass:*omit)
     D   peCobl                       2    options(*nopass:*omit)
     D   peCcbp                       3  0 options(*nopass:*omit)
     D   peDsCt4                           likeds(dsCarac_t)
     D                                     options(*nopass:*omit) dim(999)
     D   peDsCt4C                    10i 0 options(*nopass:*omit)

      * -------------------------------------------------------------*
      * COWVEH_getListaBuenResultado: Retorna Lista cod. de Buen     *
      *                               Resultado, también valida      *
      *                               si el productor tiene          *
      *                               tratamiento especial, contiene *
      *                               marca de Habilitar o no mostrar*
      *                               la misma.-                     *
      *                                                              *
      *          peBase   (input)   Parámetros Base                  *
      *          peNctw   (input)   Número de Cotizacion             *
      *          peBure   (input)   Años de Buen Resultado           *
      *          peLbure  (output)  Lista de Cod. de buen resultado  *
      *          peLbureC (output)  Cantidad                         *
      *          peHabi   (output)  Habilita / No Habilita           *
      *          peErro   (output)  Error                            *
      *          peMsgs   (output)  Mensaje de Error                 *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_getListaBuenResultado...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peBure                       1  0 const
     D   peLbure                           likeds(dsBure_t) dim(99)
     D   peLbureC                    10i 0
     D   peHabi                       1
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

      * -------------------------------------------------------------*
      * COWVEH_updInspeccionReno: Actualiza Requiere Inspeccion,     *
      *                           por cambio de cobertura para una   *
      *                           Renovacion.-                       *
      *                                                              *
      *          peBase   ( input  )  Parámetros Base                *
      *          peNctw   ( input  )  Número de Cotizacion           *
      *          peRama   ( input  )  Rama                           *
      *          peArse   ( input  )  Cant. Pólizas por Rama         *
      *          pePoco   ( input  )  Nro. de Componente             *
      *          pePaxc   ( output )  Coberturas Prima a Premio      *
      *                                                              *
      * Retorna *on = Actualizo / *off = No actualizo                *
      * -------------------------------------------------------------*
     D COWVEH_updInspeccionReno...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   pePaxc                            likeds(cobVeh) dim(20)

      * ------------------------------------------------------------ *
      * COWVEH_setRecargoComercial: Graba Recargo Comercial de Autos *
      *                                                              *
      *          peBase   ( input  ) Base                            *
      *          peNctw   ( input  ) Número de Cotización            *
      *          peRama   ( input  ) Rama                            *
      *          peArse   ( input  ) Cant. Pólizas por Rama          *
      *          pePoco   ( input  ) Nro. de Componente              *
      *          peCobl   ( input  ) Letra Cobertura                 *
      *          peCcbp   ( input  ) Codigo de Recargo               *
      *          pePcbp   ( input  ) % de Recargo                    *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_setRecargoComercial...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peCobl                       2    const
     D   peCcbp                       3  0 const
     D   pePcbp                       5  2 const

      * ------------------------------------------------------------ *
      * COWVEH_getSumaMinima(): Recupera suma asegurada mínima       *
      *                                                              *
      *     peFemi   (input)   Fecha a la cual controlar             *
      *                                                              *
      * Retorna: Importe de Suma Mínima (puede ser cero)             *
      * ------------------------------------------------------------ *
     D COWVEH_getSumaMinima...
     D                 pr            15  2
     D   peFemi                       8  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * COWVEH_getSumaMaxima(): Recupera suma asegurada máxima       *
      *                                                              *
      *     peFemi   (input)   Fecha a la cual controlar             *
      *                                                              *
      * Retorna: Importe de Suma Máxima (puede ser cero)             *
      * ------------------------------------------------------------ *
     D COWVEH_getSumaMaxima...
     D                 pr            15  2
     D   peFemi                       8  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * COWVEH_chkSumaMinima(): Controla Suma aseg > a suma mínima   *
      *                                                              *
      *     peVhvu   (input)   Suma asegurada                        *
      *     peFemi   (input)   Fecha a la cual controlar             *
      *                                                              *
      * Retorna: *ON OK, *OFF no OK                                  *
      * ------------------------------------------------------------ *
     D COWVEH_chkSumaMinima...
     D                 pr             1N
     D   peVhvu                      15  2
     D   peFemi                       8  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * COWVEH_chkSumaMaxima(): Controla Suma aseg > a suma mínima   *
      *                                                              *
      *     peVhvu   (input)   Suma asegurada                        *
      *     peFemi   (input)   Fecha a la cual controlar             *
      *                                                              *
      * Retorna: *ON OK, *OFF no OK                                  *
      * ------------------------------------------------------------ *
     D COWVEH_chkSumaMaxima...
     D                 pr             1N
     D   peVhvu                      15  2
     D   peFemi                       8  0 options(*nopass:*omit)

      * ------------------------------------------------------------ *
      * COWVEH_confirmarInspeccion(): Retorna si confirma inspeccion *
      *                                                              *
      *        Input :                                               *
      *                peBase  -  Base                               *
      *                peNctw  -  Número de Cotización               *
      *        Input Opcionales:                                     *
      *                peRama  -  Rama                               *
      *                peArse  -  Arse                               *
      *                pePoco  -  Componente                         *
      *                                                              *
      * Retorna *On / *Off                                           *
      * -------------------------------------------------------------*
     D COWVEH_confirmarInspeccion...
     D                 pr              n
     D   peBase                            Likeds( paramBase ) Const
     D   peNctw                       7  0 Const
     D   peRama                       2  0 Options( *Omit : *Nopass )
     D   peArse                       2  0 Options( *Omit : *Nopass )
     D   pePoco                       4  0 Options( *Omit : *Nopass )

      * -----------------------------------------------------------------*
      * COWVEH_cotizarWeb()2:  Recibe todos los datos del vehiculo y de  *
      *                       vuelve las posibles coberturas, primas y   *
      *                       bonificaciones                             *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peNrrp  -  Plan de Pago                           *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de IVA                          *
      *                peAcce  -  Lista de Accesorios                    *
      *                peDesE  -  Descuento Especial                     *
      *        Output:                                                   *
      *                peCtre  -  Código de Tarifa                       *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  Bonificaciones por cobertura           *
      *                peImpu  -  Impuestos                              *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * -----------------------------------------------------------------*
     D COWVEH_cotizarWeb2...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0   const
     D   peRama                       2  0   const
     D   peArse                       2  0 const
     D   pePoco                       4  0   const
     D   peVhan                       4      const
     D   peVhmc                       3      const
     D   peVhmo                       3      const
     D   peVhcs                       3      const
     D   peVhvu                      15  2   const
     D   peMgnc                       1      const
     D   peRgnc                       7  2   const
     D   peCopo                       5  0   const
     D   peCops                       1  0   const
     D   peScta                       1  0   const
     D   peClin                       1      const
     D   peBure                       1  0   const
     D   peNrrp                       3  0   const
     D   peTipe                       1      const
     D   peCiva                       2  0   const
     D   peAcce                            likeds( AccVeh_t ) dim(100)const
     D   peDesE                       5  2 const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh) dim (20)
     D   peBoni                            likeds(bonVeh) dim (99)
     D   peImpu                            likeds(Impuesto) dim (99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

      * ---------------------------------------------------------------- *
      * COWVEH_reCotizarWeb2()recibe todos los datos del vehículo y de - *
      *                       vuelve las posibles coberturas, primas y   *
      *                       bonificaciones                             *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peNrrp  -  Plan de Pago                           *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de IVA                          *
      *                peAcce  -  Lista de Accesorios                    *
      *                peDesE  -  Descuento Especial                     *
      *        Output:                                                   *
      *                peCtre  -  Código de Tarifa                       *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  Bonificaciones por cobertura           *
      *                peImpu  -  Impuestos                              *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_reCotizarWeb2...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peVhvu                      15  2 const
     D   peMgnc                       1    const
     D   peRgnc                       7  2 const
     D   peCopo                       5  0 const
     D   peCops                       1  0 const
     D   peScta                       1  0 const
     D   peClin                       1    const
     D   peBure                       1  0 const
     D   peNrrp                       3  0 const
     D   peTipe                       1    const
     D   peCiva                       2  0 const
     D   peAcce                            likeds( AccVeh_t ) dim(100)const
     D   peDesE                       5  2 const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh)  dim(20)
     D   peBoni                            likeds(bonVeh)  dim(99)
     D   peImpu                            likeds(Impuesto) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

      * ------------------------------------------------------------ *
      * COWVEH_chkEndosoPoliza() Valida si poliza a modificar aplica *
      *                          para cambio de datos en vehiculo    *
      *                          Patente - Chasis - Motor            *
      * Input :                                                      *
      *         peBase          - Base                               *
      *         peUser          - Usuario                            *
      *         peArcd          - Codigo Articulo                    *
      *         peSpol          - Numero Superpoliza                 *
      *         peRama          - Codigo Rama                        *
      *         peArse          - Numero Polizas por Rama            *
      *         peOper          - Numero Operacion                   *
      *         pePoli          - Numero Poliza                      *
      *                                                              *
      * Output :                                                     *
      *         peError         - Indicador de Error                 *
      *         peMsgs          - Estructura de Error                *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_chkEndosoPoliza...
     D                 pr              n
     D peBase                              likeds(paramBase)       const
     D peUser                        50                            const
     D peArcd                         6  0                         const
     D peSpol                         9  0                         const
     D peRama                         2  0                         const
     D peArse                         2  0                         const
     D peOper                         7  0                         const
     D pePoli                         7  0                         const
     D peError                       10i 0
     D peMsgs                              likeds(paramMsgs)

      * ------------------------------------------------------------ *
      * COWVEH_chkEndosoComponente() Valida si componente de la      *
      *                              poliza a modificar aplica para  *
      *                              endoso Patente - Chasis - Motor *
      * Input :                                                      *
      *         peBase          - Base                               *
      *         peUser          - Usuario                            *
      *         peArcd          - Codigo Articulo                    *
      *         peSpol          - Numero Superpoliza                 *
      *         peRama          - Codigo Rama                        *
      *         peArse          - Numero Polizas por Rama            *
      *         peOper          - Numero Operacion                   *
      *         pePoli          - Numero Poliza                      *
      *         pePoco          - Numero Componente                  *
      *         peNmat          - Patente                            *
      *         peChas          - Chasis                             *
      *         peMoto          - Motor                              *
      *         peSuas          - Importe Suma Asegurada             *
      *                                                              *
      * Output :                                                     *
      *         peChgV          - Cambio de Valores Componente       *
      *         peError         - Indicador de Error                 *
      *         peMsgs          - Estructura de Error                *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_chkEndosoComponente...
     D                 pr              n
     D peBase                              likeds(paramBase) const
     D peUser                        50                      const
     D peArcd                         6  0                   const
     D peSpol                         9  0                   const
     D peRama                         2  0                   const
     D peArse                         2  0                   const
     D peOper                         7  0                   const
     D pePoli                         7  0                   const
     D pePoco                         4  0                   const
     D peNmat                        25                      const
     D peChas                        25                      const
     D peMoto                        25                      const
     D peSuas                        15  2                   const
     D peChgV                          n
     D peError                       10i 0
     D peMsgs                              likeds(paramMsgs)

      * ------------------------------------------------------------ *
      * COWVEH_setEndosoPoliza() Cambia datos en vehiculo            *
      *                          Patente - Chasis - Motor            *
      * Input :                                                      *
      *         peBase          - Base                               *
      *         peUser          - Usuario                            *
      *         peArcd          - Codigo Articulo                    *
      *         peSpol          - Numero Superpoliza                 *
      *         peRama          - Codigo Rama                        *
      *         peArse          - Numero Polizas por Rama            *
      *         peOper          - Numero Operacion                   *
      *         pePoli          - Numero Poliza                      *
      *                                                              *
      * Output :                                                     *
      *         NroCotizacion   - Numero Cotizacion generada         *
      *         peVfde          - Vigencia Fecha Desde               *
      *         peVfha          - Vigencia Fecha Hasta               *
      *         peError         - Indicador de Error                 *
      *         peMsgs          - Estructura de Error                *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_setEndosoPoliza...
     D                 pr              n
     D peBase                              likeds(paramBase)       const
     D peUser                        50                            const
     D peArcd                         6  0                         const
     D peSpol                         9  0                         const
     D peRama                         2  0                         const
     D peArse                         2  0                         const
     D peOper                         7  0                         const
     D pePoli                         7  0                         const
     D peNctw                         7  0
     D peVfde                         8  0
     D peVfha                         8  0
     D peError                       10i 0
     D peMsgs                              likeds(paramMsgs)

      * ------------------------------------------------------------ *
      * COWVEH_setEndosoComponente() Graba componente de la poliza   *
      *                              endoso Patente - Chasis - Motor *
      * Input :                                                      *
      *         peBase          - Base                               *
      *         peUser          - Usuario                            *
      *         peArcd          - Codigo Articulo                    *
      *         peSpol          - Numero Superpoliza                 *
      *         peRama          - Codigo Rama                        *
      *         peArse          - Numero Polizas por Rama            *
      *         peOper          - Numero Operacion                   *
      *         pePoli          - Numero Poliza                      *
      *         peNctw          - Numero Cotizacion Web              *
      *         pePoco          - Numero Componente                  *
      *         peNmat          - Patente                            *
      *         peChas          - Chasis                             *
      *         peMoto          - Motor                              *
      *         peSuas          - Importe Suma Asegurada             *
      *                                                              *
      * Output :                                                     *
      *         peError         - Indicador de Error                 *
      *         peMsgs          - Estructura de Error                *
      *                                                              *
      * Retorna *on / *off                                           *
      * -------------------------------------------------------------*
     D COWVEH_setEndosoComponente...
     D                 pr              n
     D peBase                              likeds(paramBase)    const
     D peUser                        50                         const
     D peArcd                         6  0                      const
     D peSpol                         9  0                      const
     D peRama                         2  0                      const
     D peArse                         2  0                      const
     D peOper                         7  0                      const
     D pePoli                         7  0                      const
     D peNctw                         7  0                      const
     D pePoco                         4  0                      const
     D peNmat                        25                         const
     D peChas                        25                         const
     D peMoto                        25                         const
     D peSuas                        15  2                      const
     D peError                       10i 0
     D peMsgs                              likeds(paramMsgs)

      * ---------------------------------------------------------------- *
      * COWVEH_getCoberturasGaus():Busca posibles coberturas para el auto*
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Nro. Cotizacion                        *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peScta  -  Zona de Riesgo                         *
      *                peTiou  -  Tipo operacion usuario                 *
      *                peStou  -  Subtipo operacion usuario              *
      *                peStos  -  Subtipo operacion sistema              *
      *        Output:                                                   *
      *                peCveh  -  Coberturas                             *
      *                peccob  -  Cant de coberturas                     *
      *                                                                  *
      * ---------------------------------------------------------------- *

     D COWVEH_getCoberturasGaus...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peScta                       1  0 const
     D   peTiou                       1  0 const
     D   peStou                       2  0 const
     D   peStos                       2  0 const
     D   peCveh                            likeds(cob225) dim(99)
     D   peCcob                       2  0

      * ------------------------------------------------------------ *
      * COWVEH_deletePocoScoring(): Elimina registros en ctwet3      *
      *                                                              *
      *     peBase   ( input  ) Base                                 *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                                 *
      *     peArse   ( input  ) Cant. Pólizas por Rama               *
      *     pePoco   ( input  ) Número de componente                 *
      *                                                              *
      * ------------------------------------------------------------ *
     D COWVEH_deletePocoScoring...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const

      * ------------------------------------------------------------ *
      * COWVEH_getCtwet3(): Retorna registro ctwet3.                 *
      *                                                              *
      *     peEmpr   ( input  ) Empresa                              *
      *     peSucu   ( input  ) Sucursal                             *
      *     peNivt   ( input  ) Nivel de Intermediario               *
      *     peNivc   ( input  ) Código de Intermediario              *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                      (Opcional) *
      *     peArse   ( input  ) Cant. Pólizas por Rama    (Opcional) *
      *     pePoco   ( input  ) Número de Bien Asegurado  (Opcional) *
      *     peTaaj   ( input  ) Código de Cuestionario    (Opcional) *
      *     peCosg   ( input  ) Código de Pregunta        (Opcional) *
      *     peDst3   ( output ) Estru. de ctwet3                     *
      *     peDst3C  ( output ) Cant. de registros                   *
      *     peForm   ( input  ) Formatear Valores                    *
      *                                                              *
      * Retorna: *on = Si existe /  *off = No existe                 *
      * ------------------------------------------------------------ *
     D COWVEH_getCtwet3...
     D                 pr              n
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peNivt                       1  0 const
     D   peNivc                       5  0 const
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *nopass : *omit ) const
     D   peArse                       2  0 options( *nopass : *omit ) const
     D   pePoco                       4  0 options( *nopass : *omit ) const
     D   peTaaj                       2  0 options( *nopass : *omit ) const
     D   peCosg                       4    options( *nopass : *omit ) const
     D   peDst3                            likeds ( dsctwet3_t ) dim( 999 )
     D                                     options( *nopass : *omit )
     D   peDst3C                     10i 0 options( *nopass : *omit )
     D   peForm                       1    options( *nopass : *omit )

      * ------------------------------------------------------------ *
      * COWVEH_chkCtwet3(): Valida que exista registro en ctwet3.    *
      *                                                              *
      *     peEmpr   ( input  ) Empresa                              *
      *     peSucu   ( input  ) Sucursal                             *
      *     peNivt   ( input  ) Nivel de Intermediario               *
      *     peNivc   ( input  ) Código de Intermediario              *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                      (Opcional) *
      *     peArse   ( input  ) Cant. Pólizas por Rama    (Opcional) *
      *     pePoco   ( input  ) Número de Bien Asegurado  (Opcional) *
      *     peTaaj   ( input  ) Código de Cuestionario    (Opcional) *
      *     peCosg   ( input  ) Código de Pregunta        (Opcional) *
      *                                                              *
      * Retorna: *on = Si existe /  *off = No existe                 *
      * ------------------------------------------------------------ *
     D COWVEH_chkCtwet3...
     D                 pr              n
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peNivt                       1  0 const
     D   peNivc                       5  0 const
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *nopass : *omit ) const
     D   peArse                       2  0 options( *nopass : *omit ) const
     D   pePoco                       4  0 options( *nopass : *omit ) const
     D   peTaaj                       2  0 options( *nopass : *omit ) const
     D   peCosg                       4    options( *nopass : *omit ) const

      * ------------------------------------------------------------ *
      * COWVEH_setCtwet3(): Grabar registro en ctwet3.               *
      *                                                              *
      *     peDst3   ( input  ) Estructura de ctwet3.                *
      *                                                              *
      * Retorna: *on = Si existe /  *off = No existe                 *
      * ------------------------------------------------------------ *
     D COWVEH_setCtwet3...
     D                 pr              n
     D   peDst3                            likeds( dsCtwet3_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_updCtwet3(): Actualiza registro en ctwet3.            *
      *                                                              *
      *     peDst3   ( input  ) Estructura de ctwet3.                *
      *                                                              *
      * Retorna: *on = Si actualizo /  *off = No actualizo           *
      * ------------------------------------------------------------ *
     D COWVEH_updCtwet3...
     D                 pr              n
     D   peDst3                            likeds( dsCtwet3_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_saveScoring(): Graba Cabecera de Scoring WEB.         *
      *                                                              *
      *     peBase   ( input  ) Base                                 *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                                 *
      *     peArse   ( input  ) Cant. Pólizas por Rama               *
      *     pePoco   ( input  ) Número de Componente                 *
      *     peTaaj   ( input  ) Código de Cuestionario               *
      *     peScor   ( input  ) Estructura de preguntas              *
      *                                                              *
      * Retorna: *on = Si grabo /  *off = No grabo                   *
      * ------------------------------------------------------------ *
     D COWVEH_saveScoring...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const

      * ------------------------------------------------------------ *
      * COWVEH_validaPreguntas: Valida preguntas de Scoring.         *
      *                                                              *
      *     peBase   ( input  ) Base                                 *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                                 *
      *     peArse   ( input  ) Cant. Pólizas por Rama               *
      *     pePoco   ( input  ) Número de Componente                 *
      *     peTaaj   ( input  ) Código de Cuestionario               *
      *     peScor   ( input  ) Estructura de preguntas              *
      *     peErro   ( output ) Indicador de Error                   *
      *     peMsgs   ( output ) Estructura de Error                  *
      *                                                              *
      * Retorna: *on / *off                                          *
      * ------------------------------------------------------------ *
     D COWVEH_validaPreguntas...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

      * ------------------------------------------------------------ *
      * COWVEH_updScoring(): Actualiza Cabecera de Scoring WEB.      *
      *                                                              *
      *     peBase   ( input  ) Base                                 *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                                 *
      *     peArse   ( input  ) Cant. Pólizas por Rama               *
      *     pePoco   ( input  ) Número de Componente                 *
      *     peTaaj   ( input  ) Código de Cuestionario               *
      *     peItem   ( input  ) Estructura de preguntas              *
      *                                                              *
      * Retorna: *on = Si Actualizo / *off = No Actualizo            *
      * ------------------------------------------------------------ *
     D COWVEH_updScoring...
     D                 pr              n
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peTaaj                       2  0 const
     D   peItem                            likeds(items_t) dim(200) const

      * ------------------------------------------------------------ *
      * COWVEH_getPrimasXCoberturas() : Retorna datos de la tabla    *
      *                                 CTWETC.                      *
      *                                                              *
      *        Input :                                               *
      *                peEmpr  -  Empresa                            *
      *                peSucu  -  Sucursal                           *
      *                peNivt  -  Nivel de Intermediario             *
      *                peNivc  -  Código de Intermediario            *
      *                peNctw  -  Número de cotización               *
      *                peRama  -  Rama                    (Opcional) *
      *                peArse  -  Cant. Pólizas por Rama  (Opcional) *
      *                pePoco  -  Nro de Componente       (Opcional) *
      *                peCobl  -  Código de Cobertura     (Opcional) *
      *        Output:                                               *
      *                peDsTc  -  Est. Primas por Coberturas         *
      *                peDsTcC -  Cant. Primas por Coberturas        *
      *                                                              *
      * Retorna: *on = Si encontro / *off = No Encontro              *
      * -------------------------------------------------------------*
     D COWVEH_getPrimasXCoberturas...
     D                 pr              n
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peNivt                       1  0 const
     D   peNivc                       5  0 const
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *nopass : *omit ) const
     D   peArse                       2  0 options( *nopass : *omit ) const
     D   pePoco                       4  0 options( *nopass : *omit ) const
     D   peCobl                       2    options( *nopass : *omit ) const
     D   peDsTc                            likeds( dsCtwetc_t ) dim( 99 )
     D                                     options( *nopass : *omit )
     D   peDsTcC                     10i 0 options( *nopass : *omit )

      * ------------------------------------------------------------ *
      * COWVEH_updPrimasXCoberturas() : Actualiza datos de la tabla  *
      *                                 CTWETC.                      *
      *                                                              *
      *           peDsTc  -  Est. Primas por Coberturas              *
      *                                                              *
      * Retorna: *on = Actualizo   / *off = No Actualizo             *
      * -------------------------------------------------------------*
     D COWVEH_updPrimasXCoberturas...
     D                 pr              n
     D   peDsTc                            likeds( dsCtwetc_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_aplicaScoring: Aplica prima de Scoring.               *
      *                                                              *
      *     peBase   ( input  ) Base                                 *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                                 *
      *     peArse   ( input  ) Cant. Pólizas por Rama               *
      *     pePoco   ( input  ) Número de Componente                 *
      *     peTaaj   ( input  ) Código de Cuestionario               *
      *     peScor   ( input  ) Estructura de preguntas              *
      *     peErro   ( output ) Indicador de Error                   *
      *     peMsgs   ( output ) Estructura de Error                  *
      *     peCobl   ( input  ) Código de Cobertura      (Opcional)  *
      *                                                              *
      * Retorna: *on / *off                                          *
      * ------------------------------------------------------------ *
     D COWVEH_aplicaScoring...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)
     D   peCobl                       2    options( *nopass : *omit )

      * ---------------------------------------------------------------- *
      * COWVEH_cotizarWeb3(): Recibe todos los datos del vehículo y de - *
      *                       vuelve las posibles coberturas, primas y   *
      *                       bonificaciones.                            *
      *                                                                  *
      * ********************** Deprecated ****************************** *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peNrpp  -  Plan de Pago                           *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de Iva                          *
      *                peAcce  -  Lista de Accesorios                    *
      *                peDesE  -  Descuento Especial                     *
      *                peTaaj  -  Código de Cuestionario                 *
      *                peScor  -  Estructura de Preguntas                *
      *        Output:                                                   *
      *                peCtre  -  Código de Tarifa                       *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  Bonificaciones por cobertura           *
      *                peImpu  -  Impuestos                              *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_cotizarWeb3...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peVhvu                      15  2 const
     D   peMgnc                       1    const
     D   peRgnc                       7  2 const
     D   peCopo                       5  0 const
     D   peCops                       1  0 const
     D   peScta                       1  0 const
     D   peClin                       1    const
     D   peBure                       1  0 const
     D   peNrpp                       3  0 const
     D   peTipe                       1    const
     D   peCiva                       2  0 const
     D   peAcce                            likeds(AccVeh_t) dim(100) const
     D   peDesE                       5  2 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh) dim(20)
     D   peBoni                            likeds(bonVeh) dim(99)
     D   peImpu                            likeds(Impuesto) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

      * ---------------------------------------------------------------- *
      * COWVEH_reCotizarWeb3: Recibe todos los datos del vehículo y de - *
      *                       vuelve las posibles coberturas, primas y   *
      *                       bonificaciones.                            *
      *                                                                  *
      * ********************** Deprecated ****************************** *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peNrpp  -  Plan de Pago                           *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de Iva                          *
      *                peAcce  -  Lista de Accesorios                    *
      *                peDesE  -  Descuento Especial                     *
      *                peTaaj  -  Código de Cuestionario                 *
      *                peScor  -  Estructura de Preguntas                *
      *        Output:                                                   *
      *                peCtre  -  Código de Tarifa                       *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  Bonificaciones por cobertura           *
      *                peImpu  -  Impuestos                              *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_reCotizarWeb3...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peVhvu                      15  2 const
     D   peMgnc                       1    const
     D   peRgnc                       7  2 const
     D   peCopo                       5  0 const
     D   peCops                       1  0 const
     D   peScta                       1  0 const
     D   peClin                       1    const
     D   peBure                       1  0 const
     D   peNrpp                       3  0 const
     D   peTipe                       1    const
     D   peCiva                       2  0 const
     D   peAcce                            likeds( AccVeh_t ) dim(100) const
     D   peDesE                       5  2 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh)  dim(20)
     D   peBoni                            likeds(bonVeh)  dim(99)
     D   peImpu                            likeds(Impuesto) dim(99)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

      * ------------------------------------------------------------ *
      * COWVEH_chkScoringEnCotizacion(): Retorna si existe Cotizaci- *
      *                                  ón guardada o vigente de    *
      *                                  Scoring.                    *
      *                                                              *
      *        Input :                                               *
      *                peEmpr  -  Empresa                            *
      *                peSucu  -  Sucursal                           *
      *                peTaaj  -  Código de Cuestionario             *
      *                peCosg  -  Código de Pregunta      (Opcional) *
      *                                                              *
      * Retorna: *on = Si encontro / *off = No Encontro              *
      * -------------------------------------------------------------*
     D COWVEH_chkScoringEnCotizacion...
     D                 pr              n
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peTaaj                       2  0 const
     D   peCosg                       4    options( *nopass : *omit ) const

      * ---------------------------------------------------------------- *
      * COWVEH_getPorcCob2():devuelve dependiendo de la letra el % de    *
      *                     cobertura de accidente, incendio y Robo.     *
      *        Input :                                                   *
      *                                                                  *
      *                peTair  -  número de tabla air                    *
      *                peScta  -  sub-tabla air                          *
      *                peMone  -  codigo de moneda                       *
      *                peVhan  -  año del vehículo                       *
      *                peVhca  -  capitulo del vehículo                  *
      *                peVhv2  -  capitulo variante air                  *
      *                peCobl  -  Cobertura                              *
      *                pePcox  -  0/00 cobertura                         *
      *                pePacx  -  % accidentes                           *
      *                pePinx  -  % incendio                             *
      *                peProx  -  % robo                                 *
      *                peIfrx  -  Franquicia                             *
      *                peCtre  -  Codigo de Tarifa                       *
      *                peMtdf  -  Marca de Tarifa Diferencial            *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_getPorcCob2...
     D                 pr              n
     D   peTair                       2  0 const
     D   peScta                       1  0 const
     D   peMone                       2    const
     D   peVhan                       4    const
     D   peVhvu                      15  2 const
     D   peVhca                       2  0 const
     D   peVhv1                       1  0 const
     D   peVhv2                       1  0 const
     D   peCobl                       2    const
     D   peCoss                       2    const
     D   pePcox                       7  4
     D   pePacx                       7  4
     D   pePinx                       7  4
     D   peProx                       7  4
     D   peiFrx                      15  2
     D   peCtre                       5  0 const
     D   peMtdf                       1a   const

      * ------------------------------------------------------------ *
      * COWVEH_chkEndoso(): Valida si poliza a modificar aplica      *
      *                     para ser endosada                        *
      *                                                              *
      *     peBase  ( input  )  Parametros Base                      *
      *     peArcd  ( input  )  Codigo Articulo                      *
      *     peSpol  ( input  )  Numero Superpoliza                   *
      *     peRama  ( input  )  Codigo Rama                          *
      *     peArse  ( input  )  Numero Polizas por Rama              *
      *     peOper  ( input  )  Numero Operacion                     *
      *     pePoli  ( input  )  Numero Poliza                        *
      *     peUser  ( input  )  Usuario                              *
      *     peTiou  ( input  )  Tipo de operacion                    *
      *     peStou  ( input  )  Subtipo Usuario                      *
      *     peStos  ( input  )  subtipo Sistema                      *
      *     peErro  ( output )  Indicador de Error                   *
      *     peMsgs  ( output )  Estructura de Error                  *
      *                                                              *
      * Retorna *off = Error / *on = Valida Ok                       *
      * -------------------------------------------------------------*
     d COWVEH_chkEndoso...
     d                 pr              n
     d  peBase                             const likeds(paramBase)
     d  peArcd                        6  0 const
     d  peSpol                        9  0 const
     d  peRama                        2  0 const
     d  peArse                        2  0 const
     d  peOper                        7  0 const
     d  pePoli                        7  0 const
     d  peUser                       50    const
     d  peTiou                        1  0 const
     d  peStou                        2  0 const
     d  peStos                        2  0 const
     d  peErro                       10i 0
     d  peMsgs                             likeds(paramMsgs)

      * ------------------------------------------------------------ *
      * COWVEH_chkCtwet4(): Valida si existen Descuentos             *
      *                                                              *
      *    peBase   ( input  )  Base                                 *
      *    peNctw   ( input  )  Nro. Cotización                      *
      *    peRama   ( input  )  Rama                    ( opcional ) *
      *    peArse   ( input  )  Secuencia articulo rama ( opcional ) *
      *    pePoco   ( input  )  Nro de Componente       ( opcional ) *
      *    peCobl   ( input  )  Codigo de Cobertura     ( opcional ) *
      *    peCcbp   ( input  )  Codigo de descuento     ( opcional ) *
      *                                                              *
      * Retorna *on = Encontró / *off = No encontró                  *
      * ------------------------------------------------------------ *
     D COWVEH_chkCtwet4...
     D                 pr              n
     D   peBase                            likeds(paramBase)
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *omit : *nopass ) const
     D   peArse                       2  0 options( *omit : *nopass ) const
     D   pePoco                       4  0 options( *omit : *nopass ) const
     D   peCobl                       2    options( *omit : *nopass ) const
     D   peCcbp                       3  0 options( *omit : *nopass ) const

      * ------------------------------------------------------------ *
      * COWVEH_getCtwet4(): Obtener Listado de Descuentos            *
      *                                                              *
      *    peBase   ( input  )  Base                                 *
      *    peNctw   ( input  )  Nro. Cotización                      *
      *    peRama   ( input  )  Rama                    ( opcional ) *
      *    peArse   ( input  )  Secuencia articulo rama ( opcional ) *
      *    pePoco   ( input  )  Nro de Componente       ( opcional ) *
      *    peCobl   ( input  )  Codigo de Cobertura     ( opcional ) *
      *    peCcbp   ( input  )  Codigo de descuento     ( opcional ) *
      *    peDsT4   ( input  )  Estructura descuentos   ( opcional ) *
      *    peDsT4c  ( input  )  cantidad de descuentos  ( opcional ) *
      *                                                              *
      * Retorna *on = Encontró / *off = No encontró                  *
      * ------------------------------------------------------------ *
     D COWVEH_getCtwet4...
     D                 pr              n
     D   peBase                            likeds(paramBase)
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *omit : *nopass ) const
     D   peArse                       2  0 options( *omit : *nopass ) const
     D   pePoco                       4  0 options( *omit : *nopass ) const
     D   peCobl                       2    options( *omit : *nopass ) const
     D   peCcbp                       3  0 options( *omit : *nopass ) const
     D   peDsT4                            likeds( dsCtwet4_t ) dim( 9999 )
     D                                     options( *omit : *nopass )
     D   peDsT4c                     10i 0 options( *omit : *nopass )

      * ------------------------------------------------------------ *
      * COWVEH_setCtwet4(): Grabar informacion de descuentos         *
      *                                                              *
      *    peDsT4   ( input  )  Estructura descuentos   ( opcional ) *
      *                                                              *
      * Retorna *on = Grabo OK / *off = No Grabo                     *
      * ------------------------------------------------------------ *
     D COWVEH_setCtwet4...
     D                 pr              n
     D   peDsT4                            likeds( dsCtwet4_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_updCtwet4(): Actualiza informacion de descuentos      *
      *                                                              *
      *    peDsT4   ( input  )  Estructura descuentos   ( opcional ) *
      *                                                              *
      * Retorna *on = Grabo OK / *off = No Grabo                     *
      * ------------------------------------------------------------ *
     D COWVEH_updCtwet4...
     D                 pr              n
     D   peDsT4                            likeds( dsCtwet4_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_chkCtwet0(): Valida si existen Vehiculo               *
      *                                                              *
      *    peBase   ( input  )  Base                                 *
      *    peNctw   ( input  )  Nro. Cotización                      *
      *    peRama   ( input  )  Rama                    ( opcional ) *
      *    pePoco   ( input  )  Nro de Componente       ( opcional ) *
      *    peArse   ( input  )  Secuencia articulo rama ( opcional ) *
      *                                                              *
      * Retorna *on = Encontró / *off = No encontró                  *
      * ------------------------------------------------------------ *
     D COWVEH_chkCtwet0...
     D                 pr              n
     D   peBase                            likeds(paramBase)
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *omit : *nopass ) const
     D   pePoco                       4  0 options( *omit : *nopass ) const
     D   peArse                       2  0 options( *omit : *nopass ) const

      * ------------------------------------------------------------ *
      * COWVEH_getCtwet0(): Obtener Listado de Vehiculos             *
      *                                                              *
      *    peBase   ( input  )  Base                                 *
      *    peNctw   ( input  )  Nro. Cotización                      *
      *    peRama   ( input  )  Rama                    ( opcional ) *
      *    pePoco   ( input  )  Nro de Componente       ( opcional ) *
      *    peArse   ( input  )  Secuencia articulo rama ( opcional ) *
      *    peDsT0   ( input  )  Estructura vehiculos    ( opcional ) *
      *    peDsT0c  ( input  )  cantidad de vehiculos   ( opcional ) *
      *                                                              *
      * Retorna *on = Encontró / *off = No encontró                  *
      * ------------------------------------------------------------ *
     D COWVEH_getCtwet0...
     D                 pr              n
     D   peBase                            likeds(paramBase)
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *omit : *nopass ) const
     D   pePoco                       4  0 options( *omit : *nopass ) const
     D   peArse                       2  0 options( *omit : *nopass ) const
     D   peDsT0                            likeds( dsCtwet0_t ) dim( 9999 )
     D                                     options( *omit : *nopass )
     D   peDsT0c                     10i 0 options( *omit : *nopass )

      * ------------------------------------------------------------ *
      * COWVEH_setCtwet0(): Grabar informacion de Vehiculos          *
      *                                                              *
      *    peDsT0   ( input  )  Estructura descuentos   ( opcional ) *
      *                                                              *
      * Retorna *on = Grabo OK / *off = No Grabo                     *
      * ------------------------------------------------------------ *
     D COWVEH_setCtwet0...
     D                 pr              n
     D   peDsT0                            likeds ( dsCtwet0_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_updCtwet0(): Actualiza informacion de Vehiculo        *
      *                                                              *
      *    peDsT0   ( input  )  Estructura descuentos   ( opcional ) *
      *                                                              *
      * Retorna *on = Grabo OK / *off = No Grabo                     *
      * ------------------------------------------------------------ *
     D COWVEH_updCtwet0...
     D                 pr              n
     D   peDsT0                            likeds( dsCtwet0_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_chkCtwetc(): Valida si existen Cobertura por Vehiculo *
      *                                                              *
      *    peBase   ( input  )  Base                                 *
      *    peNctw   ( input  )  Nro. Cotización                      *
      *    peRama   ( input  )  Rama                    ( opcional ) *
      *    pePoco   ( input  )  Nro de Componente       ( opcional ) *
      *    peArse   ( input  )  Secuencia articulo rama ( opcional ) *
      *                                                              *
      * Retorna *on = Encontró / *off = No encontró                  *
      * ------------------------------------------------------------ *
     D COWVEH_chkCtwetc...
     D                 pr              n
     D   peBase                            likeds(paramBase)
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *omit : *nopass ) const
     D   peArse                       2  0 options( *omit : *nopass ) const
     D   pePoco                       4  0 options( *omit : *nopass ) const
     D   peCobl                       2    options( *omit : *nopass ) const

      * ------------------------------------------------------------ *
      * COWVEH_setCtwetc(): Grabar informacion de Cobertura por      *
      *                     vehiculo                                 *
      *                                                              *
      *    peDsTC   ( input  )  Estructura Cob. x Vehic.( opcional ) *
      *                                                              *
      * Retorna *on = Grabo OK / *off = No Grabo                     *
      * ------------------------------------------------------------ *
     D COWVEH_setCtwetc...
     D                 pr              n
     D   peDsTC                            likeds ( dsCtwetC_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_chkCtwet5(): Valida si existen Carta de daños/restri- *
      *                     ciones de cobertura                      *
      *                                                              *
      *    peBase   ( input  )  Base                                 *
      *    peNctw   ( input  )  Nro. Cotización                      *
      *    peRama   ( input  )  Rama                    ( opcional ) *
      *    peArse   ( input  )  Secuencia articulo rama ( opcional ) *
      *    pePoco   ( input  )  Nro de Componente       ( opcional ) *
      *    peCdañ   ( input  )  Código de Daño          ( opcional ) *
      *                                                              *
      * Retorna *on = Encontró / *off = No encontró                  *
      * ------------------------------------------------------------ *
     D COWVEH_chkCtwet5...
     D                 pr              n
     D   peBase                            likeds(paramBase)
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *omit : *nopass ) const
     D   peArse                       2  0 options( *omit : *nopass ) const
     D   pePoco                       4  0 options( *omit : *nopass ) const
     D   peCdaÑ                       4  0 options( *omit : *nopass ) const

      * ------------------------------------------------------------ *
      * COWVEH_setCtwet5(): Grabar informacion de Carta de daño y    *
      *                     restriccione de cobertura                *
      *                                                              *
      *    peDsT5   ( input  )  Estructura de Daños.    ( opcional ) *
      *                                                              *
      * Retorna *on = Grabo OK / *off = No Grabo                     *
      * ------------------------------------------------------------ *
     D COWVEH_setCtwet5...
     D                 pr              n
     D   peDsT5                            likeds ( dsCtwet5_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_getCtwet5(): Obtener datos de carta de daños y restri-*
      *                     cciones de cobertura
      *                                                              *
      *    peBase   ( input  )  Base                                 *
      *    peNctw   ( input  )  Nro. Cotización                      *
      *    peRama   ( input  )  Rama                    ( opcional ) *
      *    peArse   ( input  )  Secuencia articulo rama ( opcional ) *
      *    pePoco   ( input  )  Nro de Componente       ( opcional ) *
      *    peCdaÑ   ( input  )  Código de Daño          ( opcional ) *
      *    peDsT5   ( input  )  Estructura de Daños     ( opcional ) *
      *    peDsT5c  ( input  )  cantidad de Daños       ( opcional ) *
      *                                                              *
      * Retorna *on = Encontró / *off = No encontró                  *
      * ------------------------------------------------------------ *
     D COWVEH_getCtwet5...
     D                 pr              n
     D   peBase                            likeds(paramBase)
     D   peNctw                       7  0 const
     D   peRama                       2  0 options( *omit : *nopass ) const
     D   peArse                       2  0 options( *omit : *nopass ) const
     D   pePoco                       4  0 options( *omit : *nopass ) const
     D   peCdaÑ                       4  0 options( *omit : *nopass ) const
     D   peDsT5                            likeds( dsCtwet5_t ) dim( 9999 )
     D                                     options( *omit : *nopass )
     D   peDsT5c                     10i 0 options( *omit : *nopass )

      * ------------------------------------------------------------ *
      * COWVEH_updCtwet5(): Actualiza informacion de Daños           *
      *                                                              *
      *    peDsT5   ( input  )  Estructura descuentos   ( opcional ) *
      *                                                              *
      * Retorna *on = Actualizo OK / *off = No Actualizo             *
      * ------------------------------------------------------------ *
     D COWVEH_updCtwet5...
     D                 pr              n
     D   peDsT5                            likeds( dsCtwet5_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_deletePocoFactores(): Elimina registro de CTWET7      *
      *                                                              *
      *     peBase   ( input  ) Base                                 *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                                 *
      *     peArse   ( input  ) Cant. Pólizas por Rama               *
      *     pePoco   ( input  ) Número de componente                 *
      *                                                              *
      * ------------------------------------------------------------ *
     D COWVEH_deletePocoFactores...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const

      * ------------------------------------------------------------ *
      * COWVEH_setCtwet7(): Grabar registro en ctwet7.               *
      *                                                              *
      *     peDst7   ( input  ) Estructura de ctwet7.                *
      *                                                              *
      * Retorna: *on = Si existe /  *off = No existe                 *
      * ------------------------------------------------------------ *
     D COWVEH_setCtwet7...
     D                 pr              n
     D   peDst7                            likeds( dsCtwet7_t ) const

      * ------------------------------------------------------------ *
      * COWVEH_aplicaFactores: Aplica Factores.                      *
      *                                                              *
      *     peBase   ( input  ) Base                                 *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                                 *
      *     peArse   ( input  ) Cant. Pólizas por Rama               *
      *     pePoco   ( input  ) Número de Componente                 *
      *     peCobl   ( input  ) Cobertura                            *
      *                                                              *
      * Retorna: void                                                *
      * ------------------------------------------------------------ *
     D COWVEH_aplicaFactores...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peCobl                       2a   const

      * ------------------------------------------------------------ *
      * COWVEH_getTarifaUsada: Obtiene Tarifa usada para el auto     *
      *                                                              *
      *     peBase   ( input  ) Base                                 *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                                 *
      *     peArse   ( input  ) Cant. Pólizas por Rama               *
      *     pePoco   ( input  ) Número de Componente                 *
      *                                                              *
      * Retorna: Tarifa Usada                                        *
      * ------------------------------------------------------------ *
     D COWVEH_getTarifaUsada...
     D                 pr             5  0
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const

      * ------------------------------------------------------------ *
      * COWVEH_getCtwet7(): Retorna registro ctwet7.                 *
      *                                                              *
      *     peEmpr   ( input  ) Empresa                              *
      *     peSucu   ( input  ) Sucursal                             *
      *     peNivt   ( input  ) Nivel de Intermediario               *
      *     peNivc   ( input  ) Código de Intermediario              *
      *     peNctw   ( input  ) Número de Cotización                 *
      *     peRama   ( input  ) Rama                                 *
      *     peArse   ( input  ) Cant. Pólizas por Rama               *
      *     peDst7   ( output ) Estru. de ctwet3                     *
      *     peDst7C  ( output ) Cant. de registros                   *
      *     pePoco   ( input  ) Número de Bien Asegurado  (Opcional) *
      *     peCobl   ( input  ) Cobertura                 (Opcional) *
      *                                                              *
      * Retorna: *on = Si existe /  *off = No existe                 *
      * ------------------------------------------------------------ *
     D COWVEH_getCtwet7...
     D                 pr              n
     D   peEmpr                       1    const
     D   peSucu                       2    const
     D   peNivt                       1  0 const
     D   peNivc                       5  0 const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   peDst7                            likeds (dsctwet7_t) dim(999)
     D   peDst7C                     10i 0
     D   pePoco                       4  0 options(*nopass:*omit) const
     D   peCobl                       2a   options(*nopass:*omit) const

      * ---------------------------------------------------------------- *
      * COWVEH_cotizarWeb4(): Recibe todos los datos del vehículo y de - *
      *                       vuelve las posibles coberturas, primas y   *
      *                       bonificaciones.                            *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peNrpp  -  Plan de Pago                           *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de Iva                          *
      *                peAcce  -  Lista de Accesorios                    *
      *                peDesE  -  Descuento Especial                     *
      *                peTaaj  -  Código de Cuestionario                 *
      *                peScor  -  Estructura de Preguntas                *
      *        Output:                                                   *
      *                peCtre  -  Código de Tarifa                       *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  Bonificaciones por cobertura           *
      *                peImpu  -  Impuestos                              *
      *                peFact  -  Factores Multiplicativo                *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_cotizarWeb4...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peVhvu                      15  2 const
     D   peMgnc                       1    const
     D   peRgnc                       7  2 const
     D   peCopo                       5  0 const
     D   peCops                       1  0 const
     D   peScta                       1  0 const
     D   peClin                       1    const
     D   peBure                       1  0 const
     D   peNrpp                       3  0 const
     D   peTipe                       1    const
     D   peCiva                       2  0 const
     D   peAcce                            likeds(AccVeh_t) dim(100) const
     D   peDesE                       5  2 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh) dim(20)
     D   peBoni                            likeds(bonVeh) dim(99)
     D   peImpu                            likeds(Impuesto) dim(99)
     D   peFact                            likeds(factores_t) dim(999)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

      * ---------------------------------------------------------------- *
      * COWVEH_reCotizarWeb4: Recibe todos los datos del vehículo y de - *
      *                       vuelve las posibles coberturas, primas y   *
      *                       bonificaciones.                            *
      *                                                                  *
      *        Input :                                                   *
      *                                                                  *
      *                peBase  -  Base                                   *
      *                peNctw  -  Número de Cotización                   *
      *                peRama  -  Rama                                   *
      *                peArse  -  Cant. Pólizas por Rama                 *
      *                pePoco  -  Nro. de Componente                     *
      *                peVhan  -  Año del Vehículo                       *
      *                peVhmc  -  Marca del Vehículo                     *
      *                peVhmo  -  Modelo del Vehículo                    *
      *                peVhcs  -  SubModelo del Vehículo                 *
      *                peVhvu  -  Suma Asegurada                         *
      *                peMgnc  -  Marca de GNC(S o N)                    *
      *                peRgnc  -  Valor del GNC                          *
      *                peCopo  -  Código Postal                          *
      *                peCops  -  Sufijo Código Postal                   *
      *                peScta  -  Zona de Riesgo                         *
      *                peClin  -  Cliente Integral                       *
      *                peBure  -  Código de Buen Resultado               *
      *                peNrpp  -  Plan de Pago                           *
      *                peTipe  -  Tipo de Persona                        *
      *                peCiva  -  Código de Iva                          *
      *                peAcce  -  Lista de Accesorios                    *
      *                peDesE  -  Descuento Especial                     *
      *                peTaaj  -  Código de Cuestionario                 *
      *                peScor  -  Estructura de Preguntas                *
      *        Output:                                                   *
      *                peCtre  -  Código de Tarifa                       *
      *                pePaxc  -  Coberturas Prima a Premio              *
      *                peBoni  -  Bonificaciones por cobertura           *
      *                peImpu  -  Impuestos                              *
      *                peFact  -  Factores Multiplicativos               *
      *                peErro  -  Indicador de Error                     *
      *                peMsgs  -  Estructura de Error                    *
      *                                                                  *
      * ---------------------------------------------------------------- *
     D COWVEH_reCotizarWeb4...
     D                 pr
     D   peBase                            likeds(paramBase) const
     D   peNctw                       7  0 const
     D   peRama                       2  0 const
     D   peArse                       2  0 const
     D   pePoco                       4  0 const
     D   peVhan                       4    const
     D   peVhmc                       3    const
     D   peVhmo                       3    const
     D   peVhcs                       3    const
     D   peVhvu                      15  2 const
     D   peMgnc                       1    const
     D   peRgnc                       7  2 const
     D   peCopo                       5  0 const
     D   peCops                       1  0 const
     D   peScta                       1  0 const
     D   peClin                       1    const
     D   peBure                       1  0 const
     D   peNrpp                       3  0 const
     D   peTipe                       1    const
     D   peCiva                       2  0 const
     D   peAcce                            likeds( AccVeh_t ) dim(100) const
     D   peDesE                       5  2 const
     D   peTaaj                       2  0 const
     D   peScor                            likeds(preguntas_t) dim(200) const
     D   peCtre                       5  0
     D   pePaxc                            likeds(cobVeh)  dim(20)
     D   peBoni                            likeds(bonVeh)  dim(99)
     D   peImpu                            likeds(Impuesto) dim(99)
     D   peFact                            likeds(factores_t) dim(999)
     D   peErro                      10i 0
     D   peMsgs                            likeds(paramMsgs)

