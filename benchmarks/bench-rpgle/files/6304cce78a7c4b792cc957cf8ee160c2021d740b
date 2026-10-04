**free
// --------------------------------------------------------------------------------------------------
// Program Object:
//   Name : SRVXLS@SP : Picture Styling
//   Type : *MODULE
// Description :
//   These procedures handles the styling of pictures in workbooks.
// --------------------------------------------------------------------------------------------------
//   Pre-Compiler tags used by STRPREPRC to retrieve creation
//   commands from the source member.
// -------------------------------------------------
// >>PRE-COMPILER<<
//   >>CRTCMD<< CRTRPGMOD    MODULE(&LI/&OB) +
//                           SRCFILE(&SL/&SF) +
//                           SRCMBR(&SM);
//   >>COMPILE<<
//     >>PARM<< TRUNCNBR(*NO);
//     >>PARM<< DBGVIEW(*ALL);
//     >>PARM<< OPTION(*EVENTF);
//   >>END-COMPILE<<
//   >>EXECUTE<<
// >>END-PRE-COMPILER<<
// --------------------------------------------------------------------------------------------------
// Date        Developer         Change
// 2019-01-18  Nico Basson       Initial Code.
// --------------------------------------------------------------------------------------------------
/INCLUDE SRVSRC,SRV@H
ctl-opt nomain
        thread(*concurrent)
        stgmdl(*inherit) ;
// Framework ---------------------------------------------------------------------------------------
/DEFINE  SRVXLS
/INCLUDE SRVSRC,SRV@P
/INCLUDE SRVSRC,SRVXLS@T
// --------------------------------------------------------------------------------------------------
// Internal Function Prototypes oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
// --------------------------------------------------------------------------------------------------
// Create a new ClientAnchor Object used to Anchor a picture to a place in a sheet ooooooooooooooooo
dcl-pr f_NewAnchor object( *java : Anchor_class ) ;
   i_dx1   int(10) value ;
   i_dy1   int(10) value ;
   i_dx2   int(10) value ;
   i_dy2   int(10) value ;
   i_col1  int(10) value ;
   i_row1  int(10) value ;
   i_col2  int(10) value ;
   i_row2  int(10) value ;
end-pr ;
// --------------------------------------------------------------------------------------------------
// Globals <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
// --------------------------------------------------------------------------------------------------
// Workbook ----------------------------------------------------------------------------------------
dcl-s XSSF_Workbook object( *java
                          : XSSF_Workbook_class
                          )                                                                 import ;
// --------------------------------------------------------------------------------------------------
// Create a new ClientAnchor Object used to Anchor a picture to a place in a sheet ooooooooooooooooo
// --------------------------------------------------------------------------------------------------
dcl-proc f_NewAnchor export ;
   dcl-pi   f_NewAnchor object( *java : Anchor_class ) ;
      i_dx1   int(10) value ;
      i_dy1   int(10) value ;
      i_dx2   int(10) value ;
      i_dy2   int(10) value ;
      i_col1  int(10) value ;
      i_row1  int(10) value ;
      i_col2  int(10) value ;
      i_row2  int(10) value ;
   end-pi ;
   // --------------------------------------------------
   dcl-s Anchor  object( *java : Anchor_class ) ;
   // Get Helper object that helps create objects in XSSF Class jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
   dcl-pr j_getCreationHelper  object (*java : Helper_class )
                            extproc( *java
                                   : Workbook_class
                                   : 'getCreationHelper'
                                   ) ;
   end-pr ;
   // --------------------------------------------------
   dcl-s Helper object(*java : Helper_class ) ;
   // Create Client Anchor Object jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
   dcl-pr j_createClientAnchor  object (*java : Anchor_class )
                             extproc( *java
                                    : Helper_class
                                    : 'createClientAnchor'
                                    ) ;
   end-pr ;
   // Cell Coordinates jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
   dcl-pr setDx1 extproc( *java : Anchor_class : 'setDx1') ;
      dx1 int(10) value ;
   end-pr ;
   dcl-pr setDy1 extproc( *java : Anchor_class : 'setDy1') ;
      dy1 int(10) value ;
   end-pr ;
   dcl-pr setDx2 extproc( *java : Anchor_class : 'setDx2') ;
      dx2 int(10) value ;
   end-pr ;
   dcl-pr setDy2 extproc( *java : Anchor_class : 'setDy2') ;
      dy2 int(10) value ;
   end-pr ;
   dcl-pr setCol1 extproc( *java : Anchor_class : 'setCol1') ;
      col1 int(10) value ;
   end-pr ;
   dcl-pr setRow1 extproc( *java : Anchor_class : 'setRow1') ;
      row1 int(10) value ;
   end-pr ;
   dcl-pr setCol2 extproc( *java : Anchor_class : 'setCol2') ;
      col2 int(10) value ;
   end-pr ;
   dcl-pr setRow2 extproc( *java : Anchor_class : 'setRow2') ;
      row2 int(10) value ;
   end-pr ;
   // --------------------------------------------------------------------------------------------------
   monitor ;
      // ===========================================================
      // Create Helper Object -=-=-=-=-=-=-=-=-=-=-=-=-
      Helper = j_getCreationHelper( XSSF_Workbook ) ;

      // Create Client Anchor Object =-=-=-=-=-=-=-=-=-
      Anchor = j_createClientAnchor( Helper ) ;

      // Cell Coordinates -=-=-=-=-=-=-=-=-=-=-=-=-=-=-
      setDx1( Anchor : i_dx1 ) ;
      setDy1( Anchor : i_dy1 ) ;
      setDx2( Anchor : i_dx2 ) ;
      setDy2( Anchor : i_dy2 ) ;
      // -----------------------------------------------
      setCol1( Anchor : i_col1 ) ;
      setRow1( Anchor : i_row1 ) ;
      setCol2( Anchor : i_col2 ) ;
      setRow2( Anchor : i_row2 ) ;

      // -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
      return Anchor ;

      // ===========================================================
   on-error ;
      err_BubbleMsg() ;
   endmon ;
   // --------------------------------------------------------------------------------------------------
end-proc f_NewAnchor ;
// --------------------------------------------------------------------------------------------------
