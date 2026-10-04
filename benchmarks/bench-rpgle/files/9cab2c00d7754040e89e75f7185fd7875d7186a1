**FREE
//****************************************************************************************
//  (C) Copyright 2005 Credentials Solutions, LLC
//  All Rights Reserved
//
//     * * * *  Credentials Confidential Source * * * * * * *
//  THIS PROGRAM IS AN UNPUBLISHED WORK FULLY PROTECTED BY THE
//  UNITED STATES COPYRIGHT LAWS AND IS CONSIDERED A TRADE
//  SECRET BELONGING TO THE COPYRIGHT HOLDER.
//
//\B Standard Backout Instructions:
//\B   Re-compile prior version of program in PGMCOMPARE/RPG_PREV1
//\B Special Backout Instructions:
//\B   Cannot go back to previous version 2/11/16 because dvinstitf1
//\B   fields are now out of date.
//****************************************************************************************
//
//  PROGRAM - UTCRED_SC  is the Credentials School Maintenance Application
//
//  Author      : KMK
//  Date Written: 02/04/2005
//
//  All File Maint apps are structured the same:
//
//  when the user clicks a function link, it executes script
//  that sets the action code and submits the form.  The action
//  is examined and the next screen is set and WrtPanel runs
//
//  Normal submits of the form simply have action = blanks and
//  FORM contains the func ID that is in progress
//****************************************************************************************
//  Change History:
// -------- ------------------------------------------------------------------------------
// 07/07/20 SG  Allow JSON requests and Responses
// 05/14/19 SG  Modularised the code as per new architecture
// 04/18/19 LCC Made each section on the CCS tab an accordion
//              Added Diploma Options and a DP Maint. screen
//              Parking Permits are now displayed up to the valid to date
//              Images can now be viewed from the PDF tab using PDFCGI2
// 11/26/18 SAS Increase max formats to 15 instead of 5
// 11/02/18 KMK updated admin fax to new number, from 446-7424
// 10/25/18 LCC Changed wording for the document (3rd party pdf) security options
//              Forcing XPHONE to display PP and DP for call logging purposes
//              All info underneath "TranscriptsPlus Options" in CCS is removed for XPHONE
//              The text for document/3rd party pdf security options are now in a CTDATA
// 10/10/18 LCC Changed School Resend Options
//              Added new "Allow Resends:" option named "Case-by-case
//              Standardized resend fields by making certain options dropdowns
//              Resend options moved to CICCSOPT1 from DVINSTITF1
//              Implemented a new, dynamic resend policy template
//              CICCSOPT1 records can be created for non-live schools
// 09/04/18 LCC The Accounting group now has view-only access
// 08/31/18 JWG Added display/edit of IATT_GENED for filter attach opts
//              Quick Fix robo date and time for display when down on CCS tab
// 07/27/18 DDZ Added display of pdf security in CCS tab
// 07/20/18 DDZ Fixed display of isigner values on TP tab
// 07/10/18 LCC Added banner messages to the CCS tab for ROBO Status'
//              Changed info banner message for eSS only schools
// 06/04/18 DDZ Added isigner and imemo_brib to TP tab
// 04/19/18 JWG Remove group restriction on updatin itp_on_tp2
//              Added testing prefilled links for tp/tp5 for doc and IT
//              Add BOG prefilled link for PP schools that have BOG
//              Minor fixes to table headers on CCS screen
// 03/16/18 JWG Added new prototypes and copybooks for file maint
//              this standardizes the implementation of using the apps
//              replaced old calls with new modutfile calls
//              Fixed problems with buffer size and removed fice change
//              when in edit mode, removed most cllcfile references
// 10/24/17 LCC School information dropdown removed; info moved to tables in CCS
//              additional rows added to the CCS tab, existing rows rearranged
// 09/26/17 MRB Added 009998 for CSRs
// 09/20/17 SAS on change fice, make sure to fill TP variables
// 09/15/17 LCC "Length of ID used for sha calculation" must now range from 1 to 10
//              School live warning messages have been disabled for all users
//              located at Northfield and Vegas viewing schools live on TP
//              Fixed "Update" button bugfixes from 8/6 and 8/8
//              "Year Qualifier" now added to General Transcript Parameters
//              Removed unneeded edits for lhas_multi
// 08/14/17 SAS Removed restriction for vegas to take phone calls
// 08/10/17 SAS Added fields to Basic Tab in school options to update
//               ipassmin and ipassmax
// 08/08/17 LCC "Update" button bugfix for PDF tab
// 08/06/17 LCC "Edit" button fixed on TP tab
//              fixed "Update" button on LOC and PDF tabs
//              itb_noothr is now editable from the "Locs" tab
//              message translation for UIC on contacts tab
//              edits added for lhas_multi and icolor_tph
// 06/02/17 SAS fix bug with checkFile
// 05/12/17 SAS Added FILE Maint screen for E2, changed how we display
//               results of chk_pdf
// 04/18/17 DDZ Added panel translations so fice change stays on current tab
// 03/31/17 DDZ Fix fice change bug and changed to never display UTFILEDSP submit
// 03/15/17 DDZ Changed to use new email validation in MODVALID
// 03/06/17 SAS Add check for surpressed images in chk_pdf
// 03/04/17 JJG Remove references to TP_Q1_Rate in DVINSTIT5
// 03/02/17 JWG Added new value to sha method for TOD conversion schls
//              Added rtnerrs to panels that use call to utfiledsp
// 02/14/17 JWG Added write error check for dupe contact records
//              changed calls to crmfunc to use new named versions
// 02/04/17 JWG Removed reference to user library
// 01/31/17 TDR Added support for copying the the Form ID when writing
//              new format records
// 01/17/16 HAD Added support for Manual eRM Upload field
// 01/07/16 HAD Added support for Robo Mnt Change Code, Robo Bill Cycle
//              and Robo Bill Months fields for TP
// 12/20/16 HAD Removed TP5 links on TP CCS options screen and related
//              message files
// 11/30/16 HAD Added eduCheck options section in CCS
// 11/17/16 JWG Added xlate to color fields
//              changed special links to tp order form from doc grp to IT
// 09/22/16 SAS Added EDU screen and changed navigation bar to fit more opts
// 08/31/16 BXM Added "Electronic Signatures" to "Authorization Methods"
//              on CCS screen for schools that accept them.
// 07/20/16 BXM Added ability to turn E-Signatures on and off for schools
//              Added ability to supress school name/city/state
//              Added ability to change: idisc_pdf, idisc_3pdf, idisc_elec,
//              idisc_prsh, idisc_3rsh, idisc_ersh, iprohtrans, isid_shaln,
//              isha_methd, idis_dob, idis_nam, idis_sid, idis_ssn, issn_iptyp
// 07/06/16 LCC Updated '([SELECT' replacement for eRoboMail PRT Options
//              Added 2 new return mail values - no email and no email
//              except for FedEx orders.
//              Removed Brinda hardcoded user ID.
//              Removed Consent Fax # for ToD Consent forms.
// 05/20/16 JWG Added new parseinp sp/ds and web prototype
//              Added new color fields and allow colors to be updated
//              changed call to UTFILEDSP to use a pgm control ds
//              Modified some screens slightly to use core css
//              Gave Doc group ability to have links to new TP UI app
// 05/09/16 KMK Added electornic help text for DIRECT schools
// 03/22/16 KMK Added electornic options to show for DIRECT schools
// 02/11/16 TDR Adding support for new online location table
//              Changed file maintenance from iframe to program calls
// 01/22/16 TDR Added FedEx only option to remail dropdown
// 11/11/15 TDR Fixed orientation error when adding new format records
// 10/28/15 TDR Updated PDF & PRT screens to support new TPPDFFLD1 table
// 09/22/15 TDR Updated chk_pdf to support new image filenames
//              Added check to default JWGCSS to TP5
//              Created dynamic @appl_name support test pgm name
// 08/19/15 SAS increased hregistrar variable to 35a per KMK request
// 08/17/15 SAS Adding new input field for career cruising high school
//               code manipulation and for ichargecrz code for testing
// 08/10/15 KMK Allow Registrar text field to max at 35
// 07/08/15 JWG Allowing CRMs to always update ESS screen
// 06/22/15 SAS Added more description to TP Tab based off of CRM
//               tool kit documentation
//              Added class="ci-input" to input tags in html
// 06/17/15 JWG Added years to CCS screen in tpopts for auto auth,
//              electronic, and pdf eligibility
//              Fixed js function for hiding and showing fice groups
//              Added ToD/ESS phone link on XPHONE fice
// 05/20/15 SAS Add eSS and ToD check for (((ES))) to display info
// 05/15/15 SAS Adding information text instead of error of confirm
// 05/12/15 SAS Adding logic to KMKs changes on 4/02 for schools
//              live with both TP and eSS/ToD moved to live_services
//              Brought cicore_dev.css to pages
//              fixed how error messages go out to page
//              Updated all buttons to ci-button-color class
// 05/06/15 SAS Made query for which permits to skip in future sales
//              more efficient and easier to read
// 04/02/15 KMK Added transfer information for TP/ESS/TOD schools
// 03/31/15 SAS Removed TOD_Mas90 and ess_mast90, they are in the iframe
//              johnny added on 01/02/15
// 03/30/15 SAS Added TOD_MAS90 code and ess_mast90 to basic tab
//              Added ierm_paper to PRT screen for batch paper indicator
// 03/25/15 KMK Added ability to check image existence
// 03/11/15 DDZ Added IPDF_XOFF, IPDF_YOFF, IPDF_SCALE, ICOVER_MSG, and IS_LIAISON
//              Added a check that bogtype is not blank before displaying
// 02/16/15 DDZ Made checkbox available to everyone in ET send methods
// 02/13/15 JWG Fixed issue with watermark not being set for erobomail
//              when the orientation is changed
//              Removed disabled check box for send array type AL
// 01/24/15 KMK added XPHONE for CSRs to log phone calls under
// 01/02/15 JWG Added a new ESS option in the banner
//              ESS is a panel that has an iframe to UTCREDFILE
//              iframe source is encoded using encdecfld procedure
// 11/26/14 JWG Fixed issue with date conversion for rush dates
// 10/28/14 SAS add 'C' for converting option for ischmsgctl
// 10/27/14 SAS add drop down for INOREASON N or blank
// 10/24/14 SAS add drop down for ISCHMSGCTL T or blank
// 10/20/14 SAS add check box array for IET_SENDA for IT for all FICEs
// 10/01/14 SAS add check box array for IET_SENDA and logic to determine
//              if we need to prohibit orders taken over the phone
//              add cgi house keeping functions
//              cleaned up bad HTML, missing or extra tags
//              took away live parking plus order form link
// 09/24/14 JJG add 'AL' for eSS network sender to IET_SENDA
// 08/18/14 SAS changed dsptmstamp to *4YR for a MM-DD-YYYY format
//              fixed BOG permit text going out to CCS screen
// 08/15/14 SAS added Transcript go live date ilive_tp
// 08/14/14 SAS Show Parking go live date calling get_master from opts_2pp
//              show future parking permits sales and availability (opts_gvar2)
//              added BOG to header if GA_USRTYPE was a B
// 08/14/14 KMK Show ON/OFF date times instead of skipping them
// 08/07/14 KMK Show Kiosk only options for customer service
// 07/15/14 KMK started to auto set the live erm date field
// 07/10/14 MRB Updated form id lookup to use fice functions
// 03/10/14 JWG Add prntxoff and prntyoff to PRT screen
// 09/27/13 JWG Fix retrieval of send array for CCS display
// 09/09/13 TDR Added eRoboMail indication for Transcripts and
//              changed order of CCS display for TP is befor PP
// 08/30/13 MRB Added get live and get test fice functions
// 07/22/13 JWG Add edit for link 3pdf needing to be filled if
//              AE is set and cannot contain credentials url
//              Fix issue with edit button on GA screen
// 07/09/13 JWG Rmv CSM grp id from CRM and IT options
// 07/02/13 JWG New edits for tm_attctl for A, C, and blank, if C,
//              PC must be present, fix CRS dsply scrn for IT and OPS
// 05/30/13 JWG Fix issue with opacity not placing a "." in field
//              Fix issue with print watermark not getting set correctly
// 05/15/13 JJG Chg allowed values for ITM_ATTCTL to ' ', 'A', 'C'
// 03/21/13 JWG Chg pdf h/f/w to use new instit fields
//              Rmv old pdf land and port fields for h/f/w
// 03/02/13 JWG Chg watermark flds to only set when blanks
//              Display watermark values on PDF screen
// 01/28/12 MRB Increased size of formds array
// 12/20/12 JWG Add fedex and rush date time on off fields
// 12/05/12 JWG fix edit for num to print for prt testing
// 11/30/12 KMK add live date to logic for a live school
// 11/06/12 JWG Add cover page tel num to PRT screen
// 10/29/12 KMK Add fields for network schl codes
// 10/27/12 JWG Allow ITS grp to edit BSC screen
//              Add partner required field to BSC screen
// 10/09/12 JWG Add fields for network schl codes
// 10/05/12 JWG Add alternative school codes to BSC screen
//              Add tp# to print to the PRT screen
// 09/21/12 JWG Move remail fields to PRT screen
//              Chg dropdowns for Resend options on CS screen
// 09/07/12 JWG Added order links for PPTEST
// 09/05/12 JJG remove ido_amcas, ido_lsdas, ido_phrcas
// 08/23/12 JWG Add memo rate for erobomail to TP screen
// 08/16/12 JWG Added new PRT screen for CRED print fields
//              fixed edits for TP screen to not clear h-fields
// 07/01/12 JJG added new value of "R" to IALW_PUNAM field
// 06/01/12 JWG Fix display of remail and resend options
// 05/22/12 JWG Remove group edits for PDF options, add edit
//              for AE and AC to check for orientation not blank
//              Display all PDF options, no hidden html
//              Fix edits for land and port fields
//              Remove all tpparser fields
// 05/09/12 JWG Move PDF options from TP to new PDF panel
//              ADD resend and remail options to CS panel
// 03/23/12 JWG CHG do not update live sending dates for test fices
// 01/27/12 JWG ADD PP sale dates, temp date, and temp days to CCS
// 12/02/11 KMK ADD Update descirption for PDF import chargers
// 11/21/11 JWG ADD verify outbound pdf to TP screen
// 11/14/11 JWG ADD electronic yrs to the basic screen view only
// 10/22/11 JWG ADD Fice group to Basic screen, also view only flds
//              CHG basic screen to match others, removed unused options ions
// 09/30/11 JWG ADD back office system to basic screen for view only
// 09/23/11 JWG CHG crms allowed to upd pdf opts if not live
// 08/16/11 MRB added pre filled CE and DP order links
// 08/08/11 JWG CHG CRM ability to update CCS dbs with school info
//              CHG CSM ability to update sim schools with info
// 08/03/11 MRB added pre filled parking and meeting order link
// 07/29/11 JWG added entity fice field to tp update screens
// 06/28/11 MRB Fixed DP and CE order links
// 06/24/11 JWG Removed all code, ctdatas, etc related to old screens
//              added kiosk, entity fice fields to tp update
//              added fice change to all non-edit screens
//              added separate edit for tp numeric fields
//              pdf field updates in separate routine
// 05/25/11 JWG fixed small problem with date compare for GA
// 05/20/11 JWG turned new ccs screen live, plan on purging old scrn
//              in a week
// 05/13/11 JWG Added update ability for 3rd prty link to schl site
// 04/28/11 JWG IT_TST link is awaiting approval from CRMS
//              reworked maintenance edit and addition for
//              adding/updating options to ccsopt2 dbs
// 04/12/11 JWG changed msgnums in wrtpanlget for edit bsc scrn
// 04/08/11 JWG Fixed update for landscape/portrait
// 03/25/11 JWG added iregistrar to TP Panel for updating
//              Fixed problem with contact Phone number
//              changed how pdf fields put to screen
// 03/21/11 JJG Changed pgm to implement ITP_ORIENT field and          A
//              changed _RCO land/port to _HVO
// 03/18/11 JWG CCS screen just about ready to go need approval from AFA
//              PDF options in place in TP section, just need edits
// 03/16/11 JWG Added some PDF info to TP test panel
//              Removed old DV code, converted more SR's to free
// 03/15/11 JWG Adding PDF info to TP section, CCS sect still IP
//              converted SR's to free code
// 03/14/11 JWG Working on new CCS section with added features
//              brought in api protoypes for stdin/out/envrec
//              converted zcgihskpng and other SR's to free
// 02/25/11 JWG Added Auth Upload Yes/No to CCS section
// 02/17/11 KMK Correct blank space in CCS Resend Options
// 01/21/11 JWG Added memo rate for avow to TP section
// 12/10/10 WGG removed Danielle and other hardcoding not needed
// 10/29/10 JWG fixed html_mnt1, removed hard to follow JS
// 10/01/10 JWG fixed tst page headers, fixed resend msg to scrn
// 09/10/10 JJG removed remaining EV support rtns
// 08/03/10 KMK Pricing not showing for new rate per
// 07/22/10 JWG Add users to new CCS Panel for Test
//              condensed charges into one pop up
// 07/21/10 KMK Allow Danielle to update Resend Control Database
// 07/16/10 KMK Correct bad code for tp_q_rate and tp_q_base
// 07/14/10 JWG add ipdfuplmod to TP edit and display html
// 07/11/10 JJG added cibinddir and actgrp(*NEW)
// 07/08/10 KMK Only set LIVE_XML date when XO, XML for OBOR
// 06/30/10 JWG now coding prices with tp_q_base and tp_q_rate
// 06/25/10 JWG changed style sheet to external and removed majority
//              of the msgfiles associated with styles
// 06/21/10 JWG Fixed html_tst to check if ichargetm is coded
//              if it is a 'Y' it will iter, otherwise ((STOP)) and leave
// 06/17/10 KMK Fixed TST_OPT so they hide what CCS not suppose to see
// 06/13/10 JJG chngd program so that no one but JJG/WGG can
//              update the ISSN_CNTRL with a value of 'F'
// 06/11/10 JWG moved AFA to start on new screen
// 06/04/10 JWG moved DCT and KTL over to new screen for testing
// 06/02/10 JWG Fixed opthead positioning
// 06/01/10 JWG Made some updates to dropdowns, made field_4096 bigger
//              added new sr to handle ptext beginning with '!'
//              setup #DSP_TST to tested by some CS Reps tomorrow
// 05/28/10 MRB Updated Parking options on Customer Service Screen
//          JWG Added Anne's excel sheet to CICCSOPT2, fixed up some
//              html for the popup window
// 05/27/10 JWG #DSP_TST panel working along with #EDTMNT and #POPUP
//              #DSP_TST allows users to pick from a dropdown info
//              pertaining to school policies, charg info, contact,
//              etc. #POPUP displays the info selected in popup windows.
//              #EDTMNT gives Anne and IT the ability to update the info
//              that goes out to the screen.
// 05/21/10 JWG begin working on new ccs section called #DSP_TST for now
// 05/18/10 JWG fixed coding of live dates that are demonstration univ
// 05/11/10 KMK Correct CICCSOPT1 panel for HEMAIL1 and HEMAIL2
// 04/21/10 JWG changed hardcoded userid's to be based on groupid
// 04/20/10 WGG Removed Anne Kavanaugh hard coding
//          JWG added panel for CICCSOPT1
// 04/19/10 JJG Added IFORCE_PDF and rearranged fields and converted
//              TP routine to Free code
// 04/15/10 MRB Added GT routine for customer service info
// 04/12/10 JWG changed opts_tp to check group id instead of just KMKCCS
// 04/09/10 MRB Updated CE order link, it still had DP applid
// 04/08/10 MRB added CE routine for customer service info for ASCP
// 04/07/10 JJG added comments on issn_cntrl field
// 04/06/10 JJG added issn_cntrl to upd_tp
// 04/05/10 JWG added ilive_xml,edi,dir,spdf,3pdf to upd_tp
// 03/11/10 MRB Converted Customer Service Banner to non image
// 03/02/10 KMK Fixed - itm_dftbas was missing move to DVINSTITF1
//  9/01/09 WGG Removed CBTCCS, added MHFCCS, added AMKCCS
//  7/30/09 WGG Removed MSHCCS codings
//  7/23/09 JWG In accordance with PCI sales CCS ID's no longer
//              have access to place orders
//  7/14/09 JWG Added dvclientf2 to remove hardcoding userids
//              for edit buttons
//****************************************************************************************
// File specifications
//****************************************************************************************
ctl-opt option(*NOXREF:*NODEBUGIO:*SRCSTMT) dftactgrp(*NO) actgrp(*NEW)
        bnddir('CIBINDDIR':'QC2LE':'YAJL');
        // bnddir('CIBINDDIR':'QC2LE');                                 //SG01

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Input Files

dcl-f dvclientf1 usage(*update) keyed usropn;
dcl-f dvinstitf1 usage(*update) keyed usropn;
dcl-f dvinstitf3 usage(*update:*delete:*output) keyed usropn;
dcl-f d2master1 usage(*update:*output) keyed usropn;
dcl-f e2master1 usage(*update:*output) keyed usropn;
dcl-f ciccsopt1 usage(*update:*output) keyed usropn;
dcl-f ciccsopt2 usage(*update:*delete:*output) keyed usropn;
dcl-f tploc1 usage(*update:*delete:*output) keyed usropn;
dcl-f tppdffld1 usage(*update:*delete:*output) keyed usropn;
dcl-f ciccsoptwk keyed usropn rename(ccsopt2rec:wrkccsrec) extfile('CICCSOPT2') prefix(Z:1);
dcl-f dvclientf2 keyed usropn;
dcl-f dvinstitl4 keyed usropn rename(contact:cntct_l4);
dcl-f dvinstitl7 keyed usropn;
dcl-f dvinstit5 keyed usropn;
dcl-f d2tiers1 keyed usropn;
dcl-f gamaster1 keyed usropn;
dcl-f gaoption1# keyed usropn;
dcl-f formid1c keyed usropn;
dcl-f tpfrees1 keyed usropn;

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Copy Books (Declaration)

// These constants profile the fields in parsinp_ds
dcl-c HTML_NAME_LEN 25;
dcl-c HTML_DATA_LEN 500;
dcl-c MAX_INPUT_DIM 125;
dcl-c BUFIN_LEN 32000;

/copy rpgcopy,parsedsbas
/copy rpgcopy,parseds300
/copy rpgcopy,parsinp_ds
/copy rpgcopy,dvdtaara
/copy rpgcopy,cllcpsds
/copy rpgcopy,$srvrav_ds
/copy rpgcopy,$srvrm2_ds
/copy rpgcopy,statusds
/copy rpgcopy,messageds
/copy rpgcopy,zhskpg_ds

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Prototypes

/copy prototypes,apigetenv
/copy prototypes,apistdin
/copy prototypes,apistdout
/copy prototypes,crmfunc
/copy prototypes,date_fmts
/copy prototypes,dvlogerror
/copy prototypes,dates
/copy prototypes,fice
/copy prototypes,slstx
/copy prototypes,tploc
/include prototypes,utfile
/copy prototypes,valid
/copy prototypes,validst
/copy prototypes,validtel
/copy prototypes,validzip
/include prototypes,web
/include prototypes,zsystemcmd
/copy prototypes,exists_ifs

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// CGI specific variables

// Variables for the CGI interface API for QtmhWrStout.
dcl-s BufOut char(10240) inz;

// Define line feed that is required when writing data to std output.
dcl-c LINEFEED x'15';

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Constants

dcl-c FALSE '0';
dcl-c TRUE '1';

dcl-c BREAK '<br>';

dcl-c PROD_NAME 'UTCRED_SC';
dcl-c TEST_NAME 'UTCRED_SCT';

dcl-c PROD_LIBRARY '*LIBL   ';

dcl-c YEAR_WRITTEN '2019';

dcl-c MAIN_FILE 'main.html';
dcl-c #FATALERROR 'fatalError.html';
dcl-c #DSP_PRNT 'prt_eRoboMailSetup.html';
dcl-c #POPUP 'pop_openPopUp.html';
dcl-c #DSP_PDF 'pdf_tpFieldSetup.html';
dcl-c #EDTMNT 'mnt_schoolOptions.html';
dcl-c #DSP_LOC 'loc_schoolOnlineCode.html';
dcl-c #DSP_ESS 'ess_instituteTPData.html';
dcl-c #DSP_EDU 'edu_instituteTPData.html';
dcl-c #DSP_TP 'dtp_tpDataInfo.html';
dcl-c #DSP_GA 'dga_instituteGAData.html';
dcl-c #DSP_CNT 'dct_schoolContacts.html';
dcl-c #DSP_CCS 'dcs_customerService.html';
dcl-c #CON_EDIT 'dce_editContact.html';
dcl-c #DSP_BSC 'dbs_basicSchoolinfo.html';
dcl-c #DSP_CSR 'csr_institResendData.html';
dcl-c FORMATMAX 15;

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Filepath variables used for locating html files

dcl-s rootFilepath varchar(100) inz;
dcl-s panelFile char(25);
dcl-s panel char(25);

dcl-c WF_FILEPATH '/wf/';
dcl-c PROD_DIR 'p/';
dcl-c TEST_DIR 't/';
dcl-c STAGING_DIR 's/';
dcl-c SLASH '/';

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Local Variables

dcl-s ci packed(5) inz;
dcl-s conf char(300) dim(50) inz;

dcl-s ei packed(5) inz;
dcl-s errs char(300) dim(50) inz;

dcl-s pf# packed(3) inz;
dcl-s pdfs char(90) dim(50) inz;

dcl-ds errline len(300);
   errtext char(300) pos(1);
   err_indic char(1) pos(1);
   err_msg# char(4) pos(2);
end-ds;

dcl-s @appl_name char(10) inz('UTCRED_SC');
dcl-s a1 packed(9:0) inz;
dcl-s added ind inz(FALSE);
dcl-s add_head char(1) inz('0');
dcl-s add_mode char(1) inz('0');
dcl-s admin_fax char(12) inz('847-446-0488');
dcl-s imageFile char(40);
dcl-s ar_seq# char(1) dim(99) inz;

dcl-s byte2 char(2);
dcl-s byte3 char(3);
dcl-s byte4 char(4);
dcl-s byte6 char(6);
dcl-s byte9 char(9);
dcl-s byte10 char(10);
dcl-s byte20 char(20);
dcl-s byte50 char(50);
dcl-s byte70 char(70);
dcl-s byte100 char(100);
dcl-s byte200 char(200);
dcl-s byte500 char(500);

dcl-s checkzip char(20);
dcl-s condition char(10);
dcl-s ctdataSignerValue char(1);
dcl-s cycle_time zoned(6:0) inz;
dcl-s tpxcode char(1);
dcl-s tpxcode2 char(2);
dcl-s d2InvcPrices varchar(50);
dcl-s d2CcPrices char(50);
dcl-s d2TaxStates varchar(200);
dcl-s compString char(10);
dcl-s editModeArray ind dim(3) inz(FALSE);
dcl-s editMode char(1) inz('0');

dcl-s info char(90) dim(40) inz;
dcl-s fi packed(5:0) inz;
dcl-s warning char(120) dim(40) inz;
dcl-s wrIdx packed(5:0) inz;

dcl-s fax_chrg packed(5:2) inz;
dcl-s ficeChange ind inz(FALSE);

dcl-s fileAccess char(10) inz;
dcl-s fileIdx zoned(3:0) inz(0);
dcl-s fov char(1) inz;
dcl-s fov_fice char(6) inz;
dcl-s formcnt packed(3:0) inz;
dcl-s formatIdx zoned(2:0) inz(0);
dcl-s formatTot zoned(2:0) inz(0);

dcl-s formId char(10);
dcl-s frebiefice char(6) inz;
dcl-s go_livedt char(50);

dcl-s happlid char(2) inz;
dcl-s haveTpFree ind inz;
dcl-s haveasci char(1) inz('0');
dcl-s havedir char(1) inz('0');
dcl-s haveedi char(1) inz('0');
dcl-s haveerm char(1) inz('0');
dcl-s havexml char(1) inz('0');
dcl-s havespdf char(1) inz('0');
dcl-s have3pdf char(1) inz('0');
dcl-s have_fax char(1);
dcl-s hcolor_pri char(7);
dcl-s hcolor_sec char(7);
dcl-s hcolor_tph char(7);
dcl-s hcolor_txt char(7);
dcl-s hcoloptpri char(1);
dcl-s hcoloptsec char(1);
dcl-s hchkimgtyp char(1) inz;
dcl-s hformatcd char(1);
dcl-s hlocationcd char(1);
dcl-s hhas_multi char(1);
dcl-s hnewfrmtcd char(1);
dcl-s hnewonlncd char(1);
dcl-s hseqnce packed(3:0) inz;
dcl-s htext char(512) inz;
dcl-s hvrfy_outb char(1);
dcl-s h_aac char(1);
dcl-s h_cnr char(1);
dcl-s htp_orient char(1);
dcl-s hnew_orient char(1);

dcl-s idx packed(9:0) inz;
dcl-s idx1 packed(9:0) inz;
dcl-s imageOff char(1) inz;
dcl-s institChain ind;
dcl-s iter_ctl char(1) inz;
dcl-s krec_id char(1);
dcl-s lidx packed(3:0) inz;
dcl-s locationTot zoned(3:0) inz(0);
dcl-s locIdx zoned(3:0) inz(0);
dcl-s loopIdx packed(3:0) inz;
dcl-s lp packed(3:0) inz;
dcl-s monthInvalid ind;
dcl-s monthSize packed(2:0) inz;
dcl-s needRecord2 ind inz('0');
dcl-s needRecord3 ind inz('0');

dcl-s opcdcnt packed(3:0) inz;
dcl-s phnapplid char(2) inz;
dcl-s prevEi packed(3:0) inz;
dcl-s prevCi packed(3:0) inz;
dcl-s taxStatesArr char(2) dim(100);
dcl-s schcnt_eml char(70);
dcl-s schcnt_nam char(50);
dcl-s schcnt_tel char(20);
dcl-s schfax_num char(20);
dcl-s selected char(1) inz;
dcl-s setOppsite char(1);
dcl-s signerIdx zoned(3) inz;
dcl-s skippedAuth ind;
dcl-s taxIdx zoned(2:0) inz(0);

dcl-s tempMessage like(errs);
dcl-s the_rate packed(5:2) inz;
dcl-s the_recid char(2);
dcl-s tierIdx zoned(2:0) inz(0);
dcl-s value char(20);

dcl-s wfullname char(50);
dcl-s wrk_fice char(6) inz;
dcl-s wrhandle packed(5:2) inz;
dcl-s wrhdlcod packed(5:2) inz;
dcl-s xrhandle char(70);
dcl-s xrhdlcod char(90);

dcl-s yschname char(50);
dcl-s zrobomaint packed(7:2) inz;
dcl-s zet_ibp_rt packed(3:2) inz;
dcl-s zet_ibf_rt packed(3:2) inz;
dcl-s zkiosk_ip# packed(3:0) inz;
dcl-s zmemoa_rat packed(3:2) inz;
dcl-s zmemod_rat packed(3:2) inz;
dcl-s zmemoe_rat packed(3:2) inz;
dcl-s zmemod_avw packed(3:2) inz;
dcl-s zmemo_brib packed(3:2) inz;
dcl-s zmemom_rat packed(3:2) inz;
dcl-s zet_minchg packed(7:2) inz;
dcl-s zdisc_pdf  packed(5:2) inz;
dcl-s zdisc_3pdf packed(5:2) inz;
dcl-s zdisc_elec packed(5:2) inz;
dcl-s zdisc_prsh packed(5:2) inz;
dcl-s zdisc_3rsh packed(5:2) inz;
dcl-s zdisc_ersh packed(5:2) inz;
dcl-s zssn_len zoned(2:0) inz;
dcl-s zsid_shaln zoned(2:0) inz;
dcl-s ztp#_toprt packed(5:0) inz;
dcl-s zcs_rsnd_# zoned(3:0) inz;
dcl-s zcs_rsnd_w zoned(2:0) inz;
dcl-s zfdx_dtoff packed(9:0) inz;
dcl-s zfdx_tmoff packed(4:0) inz;
dcl-s zfdx_dton  packed(9:0) inz;
dcl-s zfdx_tmon  packed(4:0) inz;
dcl-s zrsh_dtoff packed(9:0) inz;
dcl-s zrsh_tmoff packed(4:0) inz;
dcl-s zrsh_dton  packed(9:0) inz;
dcl-s zrsh_tmon  packed(4:0) inz;

dcl-s hdlLogic char(1);
dcl-s hdlAmount packed(5:2) inz;
dcl-s checkValue char(1);
dcl-s effectiveDate like(cycle_date);
dcl-s fileToProcess like(panel);
dcl-s formAction char(75);
dcl-s getThisMsg# char(10);
dcl-s helpText varchar(700) inz;
dcl-s kiosktext varchar(50) inz;
dcl-s rowtext1 like(ztext);
dcl-s rowtext2 like(ztext);

// Indicators
dcl-s institl4Found ind inz;
dcl-s haveCCSdata ind;
dcl-s haveETsenda ind inz(FALSE);
dcl-s haveGAoptions ind inz(FALSE);
dcl-s haveKioskItems ind inz(FALSE);
dcl-s haveTPoptions ind inz(FALSE);
dcl-s isContact ind inz(FALSE);
dcl-s isEqual ind inz(FALSE);
dcl-s isTest ind inz(FALSE);
dcl-s optselected ind inz(FALSE);
dcl-s point2Staging ind inz(FALSE);
dcl-s hasOtherOptions ind inz;

// PSSR variables
dcl-s pssrRoutine char(100) inz;
dcl-s pssrTriggeredVar char(40) inz;

dcl-s httpAccept char(10) inz(*blank);                               //SG01

dcl-ds subVars_t qualified template;
   count packed(3);
   parm like(HTML_PARM) dim(5);
end-ds;

// Define all h-fields here
dcl-ds h_fields;
   hcover_msg char(1);
   hchargecrz char(1);
   hedt_t_sid char(1);
   herm_paper char(1);
   het_senda char(36);
   hno_phone char(1);
   hprohtrans char(1);
   har_etsend char(2) dim(18) overlay(het_senda);
   hforce_ets char(1);
   hforce_pdf char(1);
   hmemom_rat char(4);
   hsch_sname char(12);
   hschname char(50);
   hsid_char1 char(1);
   hsid_fmt char(1);
   hsid_shaln char(2);
   hsha_methd char(1);
   hdis_dob char(1);
   hdis_nam char(1);
   hdis_sid char(1);
   hdis_ssn char(1);
   hsortname char(50);
   hssn_cntrl char(1);
   hssn_iptyp char(1);
   hformid char(10);
   hcover_tel char(25);
   hcredp_onl char(1);
   hpdf_scale char(3);
   hpdf_xoff char(4);
   hpdf_yoff char(4);
   hprint_ab char(2);
   hprint_att char(2);
   hprntscale char(3);
   hprntxoff char(4);
   hprntyoff char(4);
   hprtnr_req char(1);
   hregistrar char(35);
   hrobo_cycl char(1);
   hrobo_cycm char(8);
   har_robocm char(2) dim(4) overlay(hrobo_cycm);
   hrobo_mntc char(1);
   hs_act char(4);
   hs_atp char(6);
   hs_ccd char(6);
   hs_ceebact char(6);
   hs_cruz char(10);
   hpassmin char(2);
   hpassmax char(2);
   hs_esis char(8);
   hs_ipeds char(6);
   hs_liaison char(6);
   hs_nchelp char(8);
   hs_opeid char(8);
   hs_spdefic char(6);
   hs_usis char(6);
   htp#_toprt char(3);
   htp_reml_c char(1);
   htp_rsnd_# char(2);
   htp_rsnd_w char(2);
   hcs_rsnd_# char(3);
   hcs_rsnd_c char(1);
   hcs_rsnd_w char(2);
   hfdx_dtoff char(8);
   hfdx_tmoff char(4);
   hfdx_dton char(8);
   hfdx_tmon char(4);
   hrsh_dtoff char(8);
   hrsh_tmoff char(4);
   hrsh_dton char(8);
   hrsh_tmon char(4);
   hschmsgctl char(1);
   hnoreason char(1);
   htb_noothr char(1);
   hreasoncds char(15);
   hmouse_sig char(1);
   htp_supcty char(1);
   htm_year_q char(1);
   hdisc_pdf char(7);
   hdisc_3pdf char(7);
   hdisc_elec char(7);
   hdisc_prsh char(7);
   hdisc_3rsh char(7);
   hdisc_ersh char(7);
   hpdfscrty char(1);
   hpdf3_all char(1);
   hmemo_brib char(4);
   halwslfatt char(1);
end-ds;

dcl-s hatt_gened char(1) inz;
dcl-s henty_fice char(6) inz;
dcl-s hgroup_id char(3);
dcl-s hkiosk_ip# char(1);
dcl-s hlink_3pdf char(80);
dcl-s hmemod_avw char(4);
dcl-s hmnt_grp char(3);
dcl-s hmnt_seq char(3);
dcl-s hpdfuplmod char(1);
dcl-s hprtuplmod char(1);

// Table of 4 letter Salutations
dcl-s salut char(4) ctdata dim(5) perrcd(5);

// Table of gened types
dcl-s gened_typ char(5) ctdata dim(7) perrcd(1);

// Table of school message control options
dcl-s schmsgopt char(1) ctdata dim(3);
dcl-s schtxtopt char(35) dim(3) alt(schmsgopt);

// Table of inoreason options
dcl-s norsnopt char(1) ctdata dim(2);
dcl-s norsntxt char(35) dim(2) alt(norsnopt);

// Table of itb_noothr options
dcl-s noothopt char(1) ctdata dim(2);
dcl-s noothtxt char(35) dim(2) alt(noothopt);

// Table of 1-digit record id - to description
dcl-s tab_conlet char(1) dim(24) ctdata;
dcl-s tab_condes char(70) dim(24) alt(tab_conlet);

dcl-s conlet_ptr pointer inz(%addr(tab_conlet));
dcl-ds *n based(conlet_ptr);
   ar_conlet char(1) dim(24);
end-ds;

dcl-s condes_ptr pointer inz(%addr(tab_condes));
dcl-ds *n based(condes_ptr);
   ar_condes char(70) dim(24);
end-ds;

dcl-c ets_size 12;
dcl-s et_send char(2) dim(ets_size) ctdata;
dcl-s et_descrpt char(60) dim(ets_size) alt(et_send);

dcl-c signer_size 8;
dcl-s pdfSigner char(1) dim(signer_size) ctdata;
dcl-s pdfSignerText char(50) dim(signer_size) alt(pdfSigner);

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Data Structures

dcl-c locationMax 10;
dcl-ds locationDs likerec(tplocrec) dim(locationMax);

dcl-ds ccstateds extname('CICCSTAT1');
   ccs_data char(150) pos(1);
end-ds;

dcl-ds credUser likeds(credUser_t);

dcl-ds dvlogparm;
   lgprogram char(10) inz;
   lgerrno char(2) inz;
   lguserid char(10) inz;
   lgmessag char(80) inz;
   lgrmtaddr char(20) inz;
   lgemaddr char(50) inz;
end-ds;

dcl-ds formds qualified dim(15);
   id char(10);
   code char(1);
   desc char(30);
end-ds;

dcl-ds keys;
   vals char(300) inz;
   hkeys char(50) dim(6) overlay(vals);
end-ds;

dcl-ds *n;
   @result char(55) pos(1);
   @reslt_RC char(2) pos(1);
   @reslt_RCM char(1) pos(3);
   @reslt_tel char(25) pos(6);
   @reslt_idp char(4) pos(33);
   @reslt_msk char(15) pos(36);
   // spare 5 bytes for expansion of etel_mask in 51-55
end-ds;

dcl-s cycle_date zoned(8:0);

dcl-ds formats qualified dim(formatMax);
   formatcd char(1);
   orientation char(1);
   description char(35);
   noPdfHeader char(1) inz;
   noPdfFooter char(1) inz;
   noPdfWater char(1) inz;
   noPdfGrade char(1) inz;
   noPrtHeader char(1) inz;
   noPrtFooter char(1) inz;
   noPrtWater char(1) inz;
end-ds;

dcl-ds productList qualified;
   hasPP ind inz(FALSE);
   ppLiveDate char(50);
   hasCE ind inz(FALSE);
   ceLiveDate char(50);
   hasDP ind inz(FALSE);
   dpLiveDate char(50);
   hasTP ind inz(FALSE);
   hasD2 ind inz(FALSE);
   hasESS ind inz(FALSE);
   numProducts packed(3) inz(0);
end-ds;

dcl-ds whattodo len(70);
   whattodo5 char(5);
   wtd_sk char(12);
   wtd_user char(10);
   wtd_fice char(6);
   wtd_strt char(2);
end-ds;

dcl-ds getMsgDs len(10);
   getMsg# char(4);
   getMsgParms char(5);
   getMsgOvr char(1);
end-ds;

// ***************************************************************************************
// Start of CGI Program execution section...
// ***************************************************************************************

httpAccept = getHttpAccept();                                        //SG01

if panel = '#FATALERR ';
   // If coming from *PSSR write a panel and end
   panel = #FATALERROR;
   ei += 1;
   errs(ei) = 'FATAL EXCEPTION OCCURRED';
   condition = 'FATALERR';
else;
   // Run the Generic CGI Housekeeping Routine to get the environment variables
   exsr zcgihskpg;
   clear condition;

   if bufIn = *blanks;
      hscrn_next = 'LOG';
   else;
      // Process input buffer
      if %subst(EResp:1:3) = 'GET';
         exsr doGet;
      else;
         exsr doPost;
      endif;
   endif;

endif;

if hscrn_next = 'LOG';

elseif hscrn_next = '303'; // Redirected to a different URL
else;
   fileToProcess = MAIN_FILE;
   if panel = #POPUP or panel = #FATALERROR;
      fileToProcess = panel;
   endif;
   // if client accepts json, change panelFile to json suffix        //SG01
   if httpAccept = 'json';                                           //SG01
      fileToProcess = setPanelToJSON(fileToProcess:httpAccept);      //SG01
   endif;                                                            //SG01
   web_processFile(%trim(rootFilePath):fileToProcess:%paddr('GETVARVALUES'):
                   %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
endif;

// Return to caller
close *all;
return;

// ***************************************************************************************
// Handle "GET" == Process whatToDo LIST
// ***************************************************************************************
begsr doGet;

   whattodo = bufin;
   whattodo = %xlate(x'00':' ':whattodo);
   whattodo = %xlate('*':' ':whattodo);

   // Check buffer contents for special parm of START
   select;
   when whattodo5 = 'START';
      huserid = wtd_user;
      hsignonkey = wtd_sk;
      exsr checksign;

      if condition = 'bad-sign';
         hscrn_next = 'INV';
      else;
         hscrn_next = 'MNU';
      endif;
      exsr setpanel;

   // Check buffer contents for special parm of QUICK
   when whattodo5 = 'QUICK';
      hnufice = wtd_fice;
      hsignonkey = wtd_sk;
      huserid = wtd_user;
      exsr checksign;

      if condition = 'bad-sign';
         hscrn_next = 'INV';
      else;
         hfice = hnufice;
         wrk_fice = hfice;
         exsr getSchoolDetails;

         select;
         when wtd_strt = 'TP';
            hscrn_next = 'DTP';
            exsr fill_tp;
         when wtd_strt = 'CT';
            hscrn_next = 'DCT';
         when wtd_strt = 'CS';
            hscrn_next = 'DCS';
            exsr fill_tp;
            exsr live_services;
            productList = getProductList(hfice);
         other;
            hscrn_next = 'DBS';
            exsr fillSchoolBasics;
         endsl;
      endif;

      exsr setpanel;

   // Check buffer contents for special parm of START
   when whattodo5 = 'POPUP';
      hsignonkey = %subst(whattodo:6:12);
      happlid = %subst(whattodo:18:2);
      hgroup_id = %subst(whattodo:20:3);
      hfice = %subst(whattodo:23:6);
      huserid = %subst(whattodo:29:10);
      exsr checksign;

      if condition = 'bad-sign';
         hscrn_next = 'INV';
      else;
         hscrn_next = 'POP';
         wrk_fice = hfice;
         exsr getSchoolDetails;
      endif;

      exsr setpanel;
   endsl;

endsr;

// ***************************************************************************************
// Handle "POST" == Run parseinp and process screens
// ***************************************************************************************
begsr doPost;

   exsr parseInp;

   if h_action <> 'OFF' and h_action <> 'CLR';
      exsr checksign;

      if condition = 'bad-sign';
         hscrn_next = 'OFF';
         exsr setpanel;
         clear h_action;
         leavesr;
      endif;

   endif;

   clear ei;
   clear errs;
   wrk_fice = hfice;
   exsr getSchoolDetails;

   // Perform Screen Processing based upon the type of screen

   if h_action = 'CHF';
      if hnufice <> *blanks;
         wrk_fice = hnufice;
         exsr getSchoolDetails;
         if institChain;
            ficeChange = TRUE;
         endif;
      endif;
      clear h_action;
      hgroup_id = '000';
      hseqnce = 0;
   endif;

   select;

   // Action Codes control all processing
   when h_action = 'OFF';

   // Basic Details Display
   when h_action = 'DBS';
      hscrn_next = 'DBS';
      exsr setpanel;
      exsr fillSchoolBasics;

   // Detail TP Display
   when h_action = 'DTP';
      hscrn_next = 'DTP';
      exsr setpanel;
      exsr fill_tp;

   // Detail PDF/Print Display
   when h_action = 'PDF';
      clear fmMultiFileKeys;
      clear fmKeys;
      mfk# = 1;

      hscrn_next = 'PDF';
      exsr get_formats;
      exsr setpanel;

   // Detail GA Display
   when h_action = 'DGA';
      hscrn_next = 'DGA';
      exsr setpanel;
      hedi_v_deg = iedi_v_deg;

   // Display Contact Scree
   when h_action = 'DCT';
      hscrn_next = 'DCT';
      exsr setpanel;

   when h_action = 'CSR';
      hscrn_next = 'CSR';
      exsr setpanel;
      editMode = FALSE;
      get_csopt();

   // Display Customer Service Screen
   when h_action = 'DCS';
      hgroup_id = '000';
      hseqnce = 0;
      hscrn_next = 'DCS';
      exsr setpanel;
      exsr fill_tp;
      exsr live_services;
      productList = getProductList(hfice);

   when h_action = 'PRT';
      hscrn_next = 'PRT';
      exsr setpanel;
      exsr getPrintRecs;
      exsr fill_prt;

   when h_action = 'ESS';
      clear fmMultiFileKeys;
      clear fmKeys;
      mfk# = 1;

      hscrn_next = 'ESS';
      exsr setpanel;

   when h_action = 'EDU';
      hscrn_next = 'EDU';
      exsr setpanel;
      if not %open(d2master1);
         open d2master1;
      endif;

      // Check if we have to put out creation button
      chain(n) (hfice) d2master;
      if not %found(d2master1);
         needRecord2 = TRUE;
      else;
         needRecord2 = FALSE;
      endif;

      if not %open(e2master1);
         open e2master1;
      endif;

      // Check if we have to put out creation button
      chain(n) (hfice) e2master;
      if not %found(e2master1);
         needRecord3 = TRUE;
      else;
         needRecord3 = FALSE;
      endif;

      editModeArray(1) = FALSE;
      editModeArray(2) = FALSE;
      editModeArray(3) = FALSE;

   when h_action = 'LOC';
      hscrn_next = 'LOC';
      exsr setpanel;
      locationDs = tploc_getLocations(hfice:locationTot);

      if hlocationcd = *blanks and locationTot > 0;
         hlocationcd = locationDs(1).ltms_onlin;
         hkeys(2) = locationDs(1).ltms_onlin;
      endif;

   when h_action = 'MNT';
      hgroup_id  = '000';
      hseqnce = 0;
      hscrn_next = 'MNT';
      clear h_key;

      exsr setpanel;
      if editMode = TRUE;
         exsr get_ciopts;
      endif;

   // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   // MNU panel processing

   when hscrn_type = 'MNU';
      wrk_fice = hfice;
      if hnufice <> hfice;
         wrk_fice = hnufice;
      endif;

      exsr getSchoolDetails;

      select;
      other;
         hscrn_next = 'DBS';
         exsr fillSchoolBasics;
      endsl;

      exsr setpanel;

   // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   // DBS panel processing

   when hscrn_type = 'DBS';

      select;
      when h_action = 'EDT';
         editMode = TRUE;

      when h_action = 'UPD';
         exsr upd_bsc;
      endsl;

      hscrn_next = 'DBS';
      exsr fillSchoolBasics;
      exsr setpanel;

   // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   // DTP panel processing for TPlus Fields

   when hscrn_type = 'DTP';

      select;
      when h_action = 'CXL';
      when h_action = 'EDT';
         editMode = TRUE;
      when h_action = 'UPD';
         exsr upd_tp;
      endsl;

      hscrn_next = 'DTP';
      exsr setpanel;
      exsr fill_tp;

   // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   // DPP panel processing for PDF/Print Fields

   when hscrn_type = 'PDF';
      exsr get_formats;

      select;
      when h_action = 'CXL';
         editMode = FALSE;
      when h_action = 'VEW';
         editMode = FALSE;
      when h_action = 'EDT';
         if %scan('U':cau_ccs) > 0;
            editMode = TRUE;
         else;
            ei += 1;
            errs(ei) = 'You do not have authority to edit a format.';
            editMode = FALSE;
         endif;
      when h_action = 'CHK';
         exsr chk_pdf;
      when h_action = 'ADD';
         if %scan('U':cau_ccs) > 0;
            editMode = TRUE;
            exsr add_pdf;
         else;
            ei += 1;
            errs(ei) = 'You do not have authority to add a new format.';
            editMode = FALSE;
         endif;
      when h_action = 'DEL';
         exsr del_pdf;
         exsr get_formats;
      when h_action = 'UPD';
         editMode = TRUE;

         statusDs = utfile_update('TPPDFFLD1':'SCHMNT':pgm_name:h_action:huserid:cau_grp_id:
                                   TEST_NAME:fmFields:fmStatus:hfice:hformatcd);

         if statusDs.code = ERROR;
            ei += 1;
            errs(ei) = 'Failed To Update';
         else;
            if fmStatus.numErrors > 0;
               ei = fmStatus.numErrors;
               errs = fmStatus.errors;
            endif;
            if fmStatus.numConfirm > 0;
               ci = fmStatus.numConfirm;
               conf = fmStatus.confirm;
            endif;
         endif;
      other;
      endsl;

      hscrn_next = 'PDF';
      exsr setpanel;
      exsr get_formats;

   when hscrn_type = 'PRT';
      exsr getPrintRecs;
      select;
      when h_action = 'EDT';
         editMode = TRUE;
      when h_action = 'UPD';
         // Editing error will make edit mode true for user to fix
         exsr upd_prt;
      when h_action = 'CHK';
         exsr chk_pdf;
      endsl;

      hscrn_next = 'PRT';
      exsr setpanel;
      exsr fill_prt;

   // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   // DGA panel processing for Generic Applcation

   when hscrn_type = 'DGA';
      select;
      when h_action = 'CXL';
      when h_action = 'EDT';
         editMode = TRUE;
      when h_action = 'UPD';
         exsr upd_ga;
      endsl;

      hscrn_next = 'DGA';
      exsr setpanel;
      hedi_v_deg = iedi_v_deg;

   when hscrn_type = 'CSR';
      if h_action = 'EDT';
         editMode = TRUE;
      elseif h_action = 'CXL';
         editMode = FALSE;
      elseif h_action = 'UPD';
         editMode = TRUE;
         exsr pp_edt_csr;
         if ei = 0;
            exsr upd_csopts;
            if ei = 0;
               editMode = FALSE;
            endif;
         endif;
      endif;

      hscrn_next = 'CSR';
      exsr setpanel;
      get_csopt();

   when hscrn_type = 'DCS';
      hscrn_next = 'DCS';
      exsr fill_tp;
      exsr setpanel;
      exsr live_services;
      productList = getProductList(hfice);

   when hscrn_type = 'MNT';
      select;
      when h_action = 'RFR';
         hgroup_id = '000';
      when h_action = 'GET';
         if hmnt_grp = '999';
            add_head = TRUE;
            clear hgroup_id;
            clear hmnt_seq;
            clear htitle;
            clear htext;
         endif;
      when h_action = 'EDT';
         editMode = TRUE;
      when h_action = 'NEW';
         add_mode = TRUE;
         clear htitle;
         clear htext;
      when h_action = 'ADD' or h_action = 'AD2';
         exsr csopt_edt;
         if ei = 0;
            exsr csopt_add;
         else;
            if hmnt_grp = '999';
               add_head = TRUE;
            else;
               add_mode = TRUE;
            endif;
         endif;
      when h_action = 'DEL';
         exsr csopt_del;
      when h_action = 'UPD';
         exsr csopt_edt;
         if ei = 0;
            exsr csopt_upd;
         else;
            editMode = TRUE;
         endif;
      when h_action = 'HDR';    // Only for fice: 000000
      endsl;

      hscrn_next = 'MNT';
      exsr setpanel;
      if editMode = TRUE;
         exsr get_ciopts;
      endif;

   // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   // Detail Contact Display

   when hscrn_type = 'DCT';

      select;
      // Add/Edit a Residence Name/Address
      when h_action = 'EDT';
         if h_key <> *blanks;
            exsr fill_con;
         else;
            exsr next_seq#;
         endif;
         hscrn_next = 'DCE';
         editMode = TRUE;
      // Create the New Contact Record
      when h_action = 'ADD';
         exsr pp_conedt;
         if condition = *blanks;
            exsr pp_conadd;
            hscrn_next = 'DCT';
         else;
            hscrn_next = 'DCE';
            editMode = TRUE;
         endif;
      // Update Contact Information
      when h_action = 'UPD';
         exsr pp_conedt;
         if condition = *blanks;
            exsr pp_conupd;
            hscrn_next = 'DCT';
         else;
            hscrn_next = 'DCE';
            editMode = TRUE;
         endif;
      // Delete a Contact
      when h_action = 'DEL';
         exsr pp_condel;
         if condition <> *blanks;
         endif;
         clear h_key;
         hscrn_next = 'DCT';

      other;
         hscrn_next = 'DCT';
      endsl;

      exsr setpanel;

   // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   // ESS panel processing

   when hscrn_type = 'ESS';

      select;
      when h_action = 'EDT';
         editMode = TRUE;
      when h_action = 'UPD';
         editMode = FALSE;

         statusDs = utfile_update('DVINSTITF1':'ESS':pgm_name:h_action:huserid:cau_grp_id:
                                   TEST_NAME:fmFields:fmStatus:hfice);

         if statusDs.code = ERROR;
            ei += 1;
            errs(ei) = 'Failed To Update';
         else;
            if fmStatus.numErrors > 0;
               ei = fmStatus.numErrors;
               errs = fmStatus.errors;
            endif;
            if fmStatus.numConfirm > 0;
               ci = fmStatus.numConfirm;
               conf = fmStatus.confirm;
            endif;
         endif;
      endsl;

      hscrn_next = 'ESS';
      exsr setpanel;

   // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   // EDU panel processing

   when hscrn_type = 'EDU';
      if not %open(d2master1);
         open d2master1;
      endif;

      // Check if we have to put out creation button
      chain(n) (hfice) d2master;
      if not %found(d2master1);
         needRecord2 = TRUE;
      else;
         needRecord2 = FALSE;
      endif;

      if not %open(e2master1);
         open e2master1;
      endif;

      // Check if we have to put out creation button
      chain(n) (hfice) e2master;
      if not %found(e2master1);
         needRecord3 = TRUE;
      else;
         needRecord3 = FALSE;
      endif;

      select;
      when h_action = 'EDT';
         editModeArray(1) = TRUE;

      when h_action = 'MAS';
         editModeArray(2) = TRUE;

      when h_action = 'E2E';
         editModeArray(3) = TRUE;

      // Update the DVINSTITF1 record - look at changing action
      when h_action = 'UPD';
         editModeArray(1) = FALSE;
         statusDs = utfile_update('DVINSTITF1':'EDU':pgm_name:h_action:huserid:cau_grp_id:
                                   TEST_NAME:fmFields:fmStatus:hfice);

         if statusDs.code = ERROR;
            ei += 1;
            errs(ei) = 'Failed To Update';
         else;
            if fmStatus.numErrors > 0;
               ei = fmStatus.numErrors;
               errs = fmStatus.errors;
            endif;
            if fmStatus.numConfirm > 0;
               ci = fmStatus.numConfirm;
               conf = fmStatus.confirm;
            endif;
         endif;

      // Update the D2MASTER1 record - look at changing action
      when h_action = 'UP2';
         editModeArray(2) = FALSE;
         statusDs = utfile_update('D2MASTER1':'':pgm_name:h_action:huserid:cau_grp_id:
                                   TEST_NAME:fmFields:fmStatus:hfice);

         if statusDs.code = ERROR;
            ei += 1;
            errs(ei) = 'Failed To Update';
         else;
            if fmStatus.numErrors > 0;
               ei = fmStatus.numErrors;
               errs = fmStatus.errors;
            endif;
            if fmStatus.numConfirm > 0;
               ci = fmStatus.numConfirm;
               conf = fmStatus.confirm;
            endif;
         endif;

      // Update the E2MASTER1 record - look at changing action
      when h_action = 'UP3';
         editModeArray(3) = FALSE;
         statusDs = utfile_update('E2MASTER1':'':pgm_name:h_action:huserid:cau_grp_id:
                                   TEST_NAME:fmFields:fmStatus:hfice);

         if statusDs.code = ERROR;
            ei += 1;
            errs(ei) = 'Failed To Update';
         else;
            if fmStatus.numErrors > 0;
               ei = fmStatus.numErrors;
               errs = fmStatus.errors;
            endif;
            if fmStatus.numConfirm > 0;
               ci = fmStatus.numConfirm;
               conf = fmStatus.confirm;
            endif;
         endif;

      when h_action = 'NEW';
         editModeArray(2) = TRUE;
         if not %open(d2master1);
            open d2master1;
         endif;

         chain (hfice) d2master;
         if not %found(d2master1);
            mfice = hfice;
            mamt_schl = 0;
            mamt_extra = 0;
            write d2master;
            needRecord2 = FALSE;
         else;
            unlock d2master1;
         endif;

      when h_action = 'NW2';
         editModeArray(3) = TRUE;
         if not %open(e2master1);
            open e2master1;
         endif;

         chain (hfice) e2master;
         if not %found(e2master1);
            mfice = hfice;
            mamt_schl = 0;
            mamt_extra = 0;
            write e2master;
            needRecord3 = FALSE;
         else;
            unlock e2master1;
         endif;

      endsl;

      hscrn_next = 'EDU';
      exsr setPanel;

   // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   // LOC panel processing

   when hscrn_type = 'LOC';
      locationDs = tploc_getLocations(hfice:locationTot);
      if ficeChange;
         clear hlocationcd;
      endif;

      if hlocationcd = *blanks and locationTot > 0;
         hlocationcd = locationDs(1).ltms_onlin;
      endif;

      select;
      when h_action = 'CXL';
         editMode = FALSE;
      when h_action = 'VEW';
         editMode = FALSE;
      when h_action = 'EDT';
         if cau_grp_id = 'IT' or cau_grp_id = 'CRM';
            editMode = TRUE;
         else;
            ei += 1;
            errs(ei) = 'You do not have authority to edit a location.';
            editMode = FALSE;
         endif;
      when h_action = 'ADD';
         if cau_grp_id = 'IT' or cau_grp_id = 'CRM';
            editMode = TRUE;
            exsr addLocation;
         else;
            ei += 1;
            errs(ei) = 'You do not have authority to add a new location.';
            editMode = FALSE;
         endif;
      when h_action = 'DEL';
         exsr deleteLocation;
         locationDs = tploc_getLocations(hfice:locationTot);
         if hlocationcd = *blanks and locationTot > 0;
            hlocationcd = locationDs(1).ltms_onlin;
         endif;
      when h_action = 'UPD';
         editMode = TRUE;
         if ei = 0;
            statusDs = utfile_update('TPLOC1':'':pgm_name:h_action:huserid:cau_grp_id:
                                      TEST_NAME:fmFields:fmStatus:hfice:hlocationcd);

            if statusDs.code = ERROR;
               ei += 1;
               errs(ei) = 'Failed To Update';
            else;
               if fmStatus.numErrors > 0;
                  ei = fmStatus.numErrors;
                  errs = fmStatus.errors;
               endif;
               if fmStatus.numConfirm > 0;
                  ci = fmStatus.numConfirm;
                  conf = fmStatus.confirm;
               endif;
            endif;
         endif;

      other;
      endsl;

      hscrn_next = 'LOC';
      exsr setpanel;

      if hlocationcd = *blanks and locationTot > 0;
         hlocationcd = locationDs(1).ltms_onlin;
         hkeys(2) = locationDs(1).ltms_onlin;
      endif;

   other;
      ei += 1;
      errs(ei) = 'Invalid Screen Type/Action: ' + hscrn_type + '/' + h_action;

      hgroup_id  = '000';
      hseqnce = 0;
      hscrn_next = 'DCS';
      exsr fill_tp;
      exsr setpanel;
      exsr live_services;
      productList = getProductList(hfice);
   endsl;

   h_action = *blanks;

endsr;

// ***************************************************************************************
// *INZSR: Program initialization Routine
// ***************************************************************************************
begsr *inzsr;

   in dvdtaara;

   msg_defalt = 'SC_';
   msg_file = ('CSMESSAGES*LIBL     ');
   cycle_date = %dec(%date():*iso);
   cycle_time = %dec(%time():*iso);

   if point2Staging;
      rootFilepath = WF_FILEPATH + STAGING_DIR + PROD_NAME + SLASH;
      formAction = PROD_NAME + '.pgm';
      isTest = FALSE;
   elseif pgm_Name = PROD_NAME;
/IF NOT DEFINED(DEVELOPMENT)
      rootFilePath = WF_FILEPATH + PROD_DIR + PROD_NAME + SLASH;
/ELSE
      rootFilePath = WF_FILEPATH + TEST_DIR + PROD_NAME + SLASH;
/ENDIF
      formAction = PROD_NAME + '.pgm';
      isTest = FALSE;
   else;
      rootFilePath = WF_FILEPATH + TEST_DIR + PROD_NAME + SLASH;
      formAction = TEST_NAME + '.pgm';
      isTest = TRUE;
   endif;

   open dvclientf1;

   if pgm_name = TEST_NAME;
      isTest = TRUE;
   endif;

endsr;

/copy rpgcopy,messagesr
/copy rpgcopy,$pssr_sr
/copy rpgcopy,zcgihskpg
/copy rpgcopy,$srvrav_sr

// ***************************************************************************************
// add_pdf: Add a new TPPDFFLD1 record
// ***************************************************************************************
begsr add_pdf;

   if hnewfrmtcd = *blanks;
      ei += 1;
      errs(ei) = 'You must input an Format Code.';
      editMode = FALSE;
      leavesr;
   endif;

   if formatTot >= formatMax;
      ei += 1;
      errs(ei) = 'Maximum of ' + %char(formatMax) + ' formats allowed per Fice.';
      editMode = FALSE;
      leavesr;
   endif;

   if not %open(tppdffld1);
      open tppdffld1;
   endif;

   chain(n) (hfice:hnewfrmtcd) pdffields;

   if %found(tppdffld1);
      ei += 1;
      errs(ei) = 'Format code already exists for fice.';
      editMode = FALSE;
      leavesr;
   endif;

   clear formId;

   // Attmept to find if there is a format of '1' if there is copy that Form ID
   chain(n) (hfice:'1') pdffields;
   if %found(tppdffld1);
      formId = aformid;
   endif;

   clear pdffields;

   afice = hfice;
   aformatcd = hnewfrmtcd;
   atp_orient = hnew_orient;
   adescrp = 'New Format';
   aformid = formId;
   apdf_scale = 0;
   apdf_xoff = 0;
   apdf_yoff = 0;
   aprntscale = 0;
   aprntxoff = 0;
   aprntyoff = 0;
   achguser = '';
   achgdate = 0;
   achgtime = 0;

   if hnew_orient = 'L';
      apdft_hrz = '027';
      apdft_vrt = '513';
      apdft_opc = '0.00';
      apdft_scl = '024';
      apdfb_hrz = '027';
      apdfb_vrt = '027';
      apdfb_opc = '0.00';
      apdfb_scl = '024';
      apdfw_hrz = '279';
      apdfw_vrt = '189';
      apdfw_opc = '0.20';
      apdfw_scl = '000';
      aprntt_hrz = '027';
      aprntt_vrt = '513';
      aprntt_opc = '0.00';
      aprntt_scl = '024';
      aprntb_hrz = '027';
      aprntb_vrt = '027';
      aprntb_opc = '0.00';
      aprntb_scl = '024';
      aprntw_hrz = '279';
      aprntw_vrt = '189';
      aprntw_opc = '0.20';
      aprntw_scl = '000';
   else;
      apdft_hrz = '027';
      apdft_vrt = '693';
      apdft_opc = '0.00';
      apdft_scl = '024';
      apdfb_hrz = '027';
      apdfb_vrt = '027';
      apdfb_opc = '0.00';
      apdfb_scl = '024';
      apdfw_hrz = '189';
      apdfw_vrt = '279';
      apdfw_opc = '0.20';
      apdfw_scl = '000';
      aprntt_hrz = '027';
      aprntt_vrt = '693';
      aprntt_opc = '0.00';
      aprntt_scl = '024';
      aprntb_hrz = '027';
      aprntb_vrt = '027';
      aprntb_opc = '0.00';
      aprntb_scl = '024';
      aprntw_hrz = '189';
      aprntw_vrt = '279';
      aprntw_opc = '0.20';
      aprntw_scl = '000';
   endif;

   write pdffields;

   hformatcd = hnewfrmtcd;
   htp_orient = hnew_orient;

endsr;

// ***************************************************************************************
// addLocation: Add a new location to TPLOC1
// ***************************************************************************************
begsr addLocation;

   if hnewonlncd = *blanks;
      ei += 1;
      errs(ei) = 'You must input an Online Code.';
      editMode = FALSE;
      leavesr;
   endif;

   if locationTot >= locationMax;
      ei += 1;
      errs(ei) = 'Maximum of ' + %char(locationMax) + ' Online Codes allowed per Fice.';
      editMode = FALSE;
      leavesr;
   endif;

   if not %open(tploc1);
      open tploc1;
   endif;

   chain(n) (hfice:hnewonlncd) tplocrec;

   if %found(tploc1);
      ei += 1;
      errs(ei) = 'Location code already exists for fice.';
      editMode = FALSE;
      leavesr;
   endif;

   lfice = hfice;
   ltms_onlin = hnewonlncd;
   lhas_multi = ' ';
   lformatcd = '1';
   ltm_word = 'NEW LOCATION';
   clear ldescrp;
   clear laltdescrp;
   clear ltm_upl_cd;

   write tplocrec;

   hlocationcd = hnewonlncd;

endsr;

// ***************************************************************************************
// chk_pdf: Check for existnce of the PDF files
// ***************************************************************************************
begsr chk_pdf;

   prevEi = 0;
   prevCi = 0;
   pf# = 0;
   clear pdfs;
   for formatIdx = 1 to formatTot;
      imageFile = 'HEADER/H' + ifice + hchkimgtyp + formats(formatIdx).formatcd + '.png';

      if hchkImgTyp = 'A';
         imageOff = formats(formatIdx).noPdfHeader;
      elseif hchkImgTyp = 'P';
         imageOff = formats(formatIdx).noPrtHeader;
      else;
         imageOff = ' ';
      endif;

      if checkFile(ifice:imageFile:hchkImgTyp:imageOff:tempMessage);
         pf# += 1;
         pdfs(pf#) = tempMessage;
      else;
         ei += 1;
         errs(ei) = tempMessage;
      endif;

      imageFile = 'FOOTER/F' + ifice + hchkimgtyp + formats(formatIdx).formatcd + '.png';

      if hchkImgTyp = 'A';
         imageOff = formats(formatIdx).noPdfFooter;
      elseif hchkImgTyp = 'P';
         imageOff = formats(formatIdx).noPrtFooter;
      endif;

      if checkFile(ifice:imageFile:hchkImgTyp:imageOff:tempMessage);
         pf# += 1;
         pdfs(pf#) = tempMessage;
      else;
         ei += 1;
         errs(ei) = tempMessage;
      endif;

      imageFile = 'WATERMARKS/W' + ifice + hchkimgtyp + formats(formatIdx).formatcd + '.gif';

      if hchkImgTyp = 'A';
         imageOff = formats(formatIdx).noPdfWater;
      elseif hchkImgTyp = 'P';
         imageOff = formats(formatIdx).noPrtWater;
      endif;

      if checkFile(ifice:imageFile:hchkImgTyp:imageOff:tempMessage);
         pf# += 1;
         pdfs(pf#) = tempMessage;
      else;
         ei += 1;
         errs(ei) = tempMessage;
      endif;

      imageFile = 'GRADESCALE/G' + ifice + hchkimgtyp + formats(formatIdx).formatcd + '.pdf';

      if hchkImgTyp = 'A';
         imageOff = formats(formatIdx).noPdfGrade;
      else;
         imageOff = ' ';
      endif;

      if checkFile(ifice:imageFile:hchkImgTyp:imageOff:tempMessage);
         pf# += 1;
         pdfs(pf#) = tempMessage;
      else;
         ei += 1;
         errs(ei) = tempMessage;
      endif;

      if prevCi <> pf# and formatIdx <> formatTot;
         prevCi = pf#;
         pdfs(pf#) = %trim(pdfs(pf#));
      endif;

      if prevEi <> ei and formatIdx <> formatTot;
         prevEi = ei;
         errs(ei) = %trim(errs(ei));
      endif;
   endfor;

endsr;

// ***************************************************************************************
// csopt_add: ADD a CICCSOPT2 Database Record
// ***************************************************************************************
begsr csopt_add;

   if not %open(ciccsopt2);
      open ciccsopt2;
   endif;

   if hmnt_grp = '999';
      hseqnce = 0;
   endif;

   chain(n) (hfice:happlid:hgroup_id:hseqnce) ccsopt2rec;
   if %found(ciccsopt2);
      ei += 1;
      errs(ei) = 'Option already exists';
      leavesr;
   endif;

   pfice = hfice;
   papplid = happlid;
   pgroup_id = hgroup_id;
   pseqnce = hseqnce;
   ptitle = htitle;
   ptext = htext;

   ci += 1;
   conf(ci) = '( ' + %editc(pseqnce:'X') + ' - ' + %trim(ptitle) + ' ) has been ADDED.';

   write ccsopt2rec;

   clear htitle;
   clear htext;
   clear hmnt_grp;
   hseqnce = 0;

   if h_action = 'AD2';
      add_mode = TRUE;
   endif;

endsr;

// ***************************************************************************************
// csopt_del: DEL a CICCSOPT2 Database Record
// ***************************************************************************************
begsr csopt_del;

   if not %open(ciccsopt2);
     open ciccsopt2;
   endif;

   chain (hfice:happlid:hgroup_id:%int(hmnt_seq)) ccsopt2rec;
   if not %found(ciccsopt2);
      ei += 1;
      errs(ei) = 'Please Contact IT';
      leavesr;
   endif;

   ci += 1;
   conf(ci) = '( ' + %editc(pseqnce:'X') + ' - ' + %trim(ptitle) + ' ) has been DELETED.';

   delete ccsopt2rec;

   clear h_key;

endsr;

// ***************************************************************************************
// csopt_edt: edt the CICCSOPT2 database
// ***************************************************************************************
begsr csopt_edt;

   if h_action = 'ADD' or h_action = 'AD2';
      if hseqnce = 0 and hmnt_grp <> '999';
         ei += 1;
         errs(ei) = 'Sequence # cannot be zero.';
      endif;
   endif;

   select;
   when htitle = *blanks;
      ei += 1;
      errs(ei) = 'Title cannot be blank.';
   when htext = *blanks and hmnt_grp <> '999';
      ei += 1;
      errs(ei) = 'Text should not be blank.';
   endsl;

   clear statusDs;
   htext = findHtml(htext:statusDs);
   if statusDs.code = ERROR;
      ei += 1;
      errs(ei) = 'Invalid text entered into textarea';
   endif;

endsr;

// ***************************************************************************************
// csopt_upd: UPD a CICCSOPT2 Database Record
// ***************************************************************************************
begsr csopt_upd;

   if not %open(ciccsopt2);
     open ciccsopt2;
   endif;

   chain (hfice:happlid:hgroup_id:%int(hmnt_seq)) ccsopt2rec;
   if not %found(ciccsopt2);
      ei += 1;
      errs(ei) = 'Please contact IT';
      leavesr;
   endif;

   ptitle = htitle;
   ptext = htext;

   ci += 1;
   conf(ci) = '( ' + %editc(pseqnce:'X') + ' - ' + %trim(ptitle) + ' ) has been UPDATED.';

   update ccsopt2rec;

   clear h_key;
   clear htitle;
   clear htext;

endsr;

// ***************************************************************************************
// checksign: Check the SIGNONKEY value vs. the dvclientf1
// ***************************************************************************************
begsr checksign;

   clear dvlogparm;

   if huserid = *blanks;
      condition = 'bad-sign';
      leavesr;
   endif;

   chain huserid dvclientf1;
   if not %found(dvclientf1);
      csignonkey = huserid + '--';
   endif;

   // If they are not the same and the csignonkey is blank, then the user was inactive for more
   // than x minutes so give a different message for this than for a mismatch.
   if hsignonkey <> csignonkey and csignonkey = *blanks;
      ei += 1;
      errs(ei) = '#7924';
      condition = 'bad-sign';
      unlock dvclientf1;
      leavesr;
   endif;

   // If they are not the same and the csignonkey is not blank, then something else is going on.
   // Either the user has backed up into a prior session or someone else is trying to get on.
   if hsignonkey <> csignonkey;
      condition = 'bad-sign';
      unlock dvclientf1;

      ei += 1;
      errs(ei) = '#7815';

      lgprogram = @appl_name;
      lgerrno = '88';
      lguserid = huserid;
      lgrmtaddr = currmtaddr;
      lgemaddr = cemail;
      lgmessag = 'SignKey Failure    HKey=' + %trim(hsignonkey) + '    CKey=' + csignonkey +
                 '    CurRmtAddr=' + currmtaddr;

      dvlogerror(lgprogram:lgerrno:lguserid:lgmessag:lgrmtaddr:lgemaddr);

   else;
      clastactd = cycle_date;
      clastactt = cycle_time;

      update client;

      if not %open(dvclientf2);
         open dvclientf2;
      endif;

      chain (huserid) authority;
      if not %found(dvclientf2);
         clear cau_ccs;
         clear cau_grp_id;
      endif;
   endif;

endsr;

// ***************************************************************************************
// del_pdf: Delete a Transcript Format
// ***************************************************************************************
begsr del_pdf;

   if not %open(tppdffld1);
      open tppdffld1;
   endif;

   chain (hfice:hformatcd) pdffields;

   if %found(tppdffld1);
      delete pdffields;
   endif;

   clear hformatcd;

endsr;

// ***************************************************************************************
// deleteLocation: Delete a transcript location.
// ***************************************************************************************
begsr deleteLocation;

   if not %open(tploc1);
      open tploc1;
   endif;

   chain (hfice:hlocationcd) tplocrec;

   if %found(tploc1);
      delete tplocrec;
   endif;

   clear hlocationcd;

endsr;

// ***************************************************************************************
// edt_fdxrsh: Edit the FedEx and Rush Date-Time fields
// ***************************************************************************************
begsr edt_fdxrsh;

   select;
   when hfdx_dtoff = '99999999' or hfdx_dtoff = '0';
      // Allow thru
   when hfdx_dtoff = *blanks;
      hfdx_dtoff = '0';
   other;
      if %check('0123456789':%trim(hfdx_dtoff)) > 0;
         ei += 1;
         errs(ei) = 'Invalid Date';
         leavesr;
      else;
         test(de) *iso0 hfdx_dtoff;
         if %error();
            ei += 1;
            errs(ei) = 'Invalid Date';
            leavesr;
         endif;
      endif;
   endsl;

   zfdx_dtoff = %int(hfdx_dtoff);

   select;
   when hfdx_tmoff = '0';
      // Allow thru
   when hfdx_tmoff = *blanks;
      hfdx_tmoff = '0';
   other;
      if %check('0123456789':%trim(hfdx_tmoff)) > 0;
         ei += 1;
         errs(ei) = 'Invalid Date';
         leavesr;
      endif;
   endsl;

   zfdx_tmoff = %int(hfdx_tmoff);

   select;
   when hfdx_dton = '99999999' or hfdx_dton = '0';
      // Allow thru
   when hfdx_dton = *blanks;
      hfdx_dton = '0';
   other;
      if %check('0123456789':%trim(hfdx_dton)) > 0;
         ei += 1;
         errs(ei) = 'Invalid Date';
         leavesr;
      else;
         test(de) *iso0 hfdx_dton;
         if %error();
            ei += 1;
            errs(ei) = 'Invalid Date';
            leavesr;
         endif;
      endif;
   endsl;

   zfdx_dton = %int(hfdx_dton);

   if zfdx_dton < zfdx_dtoff;
      ei += 1;
      errs(ei) = 'FedEx Date On cannot be less than FedEx Date Off';
   endif;

   select;
   when hfdx_tmon = '0';
      // Allow thru
   when hfdx_tmon = *blanks;
      hfdx_tmon = '0';
   other;
      if %check('0123456789':%trim(hfdx_tmon)) > 0;
         ei += 1;
         errs(ei) = 'Invalid Date';
         leavesr;
      endif;
   endsl;

   zfdx_tmon = %int(hfdx_tmon);

   select;
   when hrsh_dtoff = '99999999' or hrsh_dtoff = '0';
      // Allow thru
   when hrsh_dtoff = *blanks;
      hrsh_dtoff = '0';
   other;
      if %check('0123456789':%trim(hrsh_dtoff)) > 0;
         ei += 1;
         errs(ei) = 'Invalid Date';
         leavesr;
      else;
         test(de) *iso0 hrsh_dtoff;
         if %error();
            ei += 1;
            errs(ei) = 'Invalid Date';
            leavesr;
         endif;
      endif;
   endsl;

   zrsh_dtoff = %int(hrsh_dtoff);

   select;
   when hrsh_tmoff = '0';
      // Allow thru
   when hrsh_tmoff = *blanks;
      hrsh_tmoff = '0';
   other;
      if %check('0123456789':%trim(hrsh_tmoff)) > 0;
         ei += 1;
         errs(ei) = 'Invalid Date';
         leavesr;
      endif;
   endsl;

   zrsh_tmoff = %int(hrsh_tmoff);

   select;
   when hrsh_dton = '99999999' or hrsh_dton = '0';
      // Allow thru
   when hrsh_dton = *blanks;
      hrsh_dton = '0';
   other;
      if %check('0123456789':%trim(hrsh_dton)) > 0;
         ei += 1;
         errs(ei) = 'Invalid Date';
         leavesr;
      else;
         test(de) *iso0 hrsh_dton;
         if %error();
            ei += 1;
            errs(ei) = 'Invalid Date';
            leavesr;
         endif;
      endif;
   endsl;

   zrsh_dton = %int(hrsh_dton);

   if zrsh_dton < zrsh_dtoff;
      ei += 1;
      errs(ei) = 'Rush Date On cannot be less than Rush Date Off';
   endif;

   select;
   when hrsh_tmon = '0';
      // Allow thru
   when hrsh_tmon = *blanks;
      hrsh_tmon = '0';
   other;
      if %check('0123456789':%trim(hrsh_tmon)) > 0;
         ei += 1;
         errs(ei) = 'Invalid Date';
         leavesr;
      endif;
   endsl;

   zrsh_tmon = %int(hfdx_tmon);

endsr;

// ***************************************************************************************
// edt_tp_num: Edit the TP Numeric Fields
// ***************************************************************************************
begsr edt_tp_num;

   if hrobomaint = *blanks or %check('0123456789. ':hrobomaint) > 0;
      zrobomaint = irobomaint;
   else;
      zrobomaint = %dec(%trim(hrobomaint):7:2);
   endif;

   if het_ibp_rt = *blanks or %check('0123456789. ':het_ibp_rt) > 0;
      zet_ibp_rt = iet_ibp_rt;
   else;
      zet_ibp_rt = %dec(%trim(het_ibp_rt):3:2);
   endif;

   if het_ibf_rt = *blanks or %check('0123456789. ':het_ibf_rt) > 0;
      zet_ibf_rt = iet_ibf_rt;
   else;
      zet_ibf_rt = %dec(%trim(het_ibf_rt):3:2);
   endif;

   if hmemoa_rat = *blanks or %check('0123456789. ':hmemoa_rat) > 0;
      zmemoa_rat = imemoa_rat;
   else;
      zmemoa_rat = %dec(%trim(hmemoa_rat):3:2);
   endif;

   if hmemod_rat = *blanks or %check('0123456789. ':hmemod_rat) > 0;
      zmemod_rat = imemod_rat;
   else;
      zmemod_rat = %dec(%trim(hmemod_rat):3:2);
   endif;

   if hmemoe_rat = *blanks or %check('0123456789. ':hmemoe_rat) > 0;
      zmemoe_rat = imemoe_rat;
   else;
      zmemoe_rat = %dec(%trim(hmemoe_rat):3:2);
   endif;

   if hmemom_rat = *blanks or %check('0123456789. ':hmemom_rat) > 0;
      zmemom_rat = imemom_rat;
   else;
      zmemom_rat = %dec(%trim(hmemom_rat):3:2);
   endif;

   if hmemod_avw = *blanks or %check('0123456789. ':hmemod_avw) > 0;
      zmemod_avw = imemod_avw;
   else;
      zmemod_avw = %dec(%trim(hmemod_avw):3:2);
   endif;

   if hmemo_brib = *blanks or %check('0123456789. ':hmemo_brib) > 0;
      zmemo_brib = imemo_brib;
   else;
      zmemo_brib = %dec(%trim(hmemo_brib):3:2);
   endif;

   if het_minchg = *blanks or %check('0123456789. ':het_minchg) > 0;
      zet_minchg = iet_minchg;
   else;
      zet_minchg = %dec(%trim(het_minchg):7:2);
   endif;

   if hdisc_pdf = *blanks or %check('0123456789-. ':hdisc_pdf) > 0;
      zdisc_pdf = idisc_pdf;
   else;
      zdisc_pdf = %abs(%dec(%trim(hdisc_pdf):5:2)) * -1;
   endif;

   if hdisc_3pdf = *blanks or %check('0123456789-. ':hdisc_3pdf) > 0;
      zdisc_3pdf = idisc_3pdf;
   else;
      zdisc_3pdf = %abs(%dec(%trim(hdisc_3pdf):5:2)) * -1;
   endif;

   if hdisc_elec = *blanks or %check('0123456789-. ':hdisc_elec) > 0;
      zdisc_elec = idisc_elec;
   else;
      zdisc_elec = %abs(%dec(%trim(hdisc_elec):5:2)) * -1;
   endif;

   if hdisc_prsh = *blanks or %check('0123456789-. ':hdisc_prsh) > 0;
      zdisc_prsh = idisc_prsh;
   else;
      zdisc_prsh = %abs(%dec(%trim(hdisc_prsh):5:2)) * -1;
   endif;

   if hdisc_3rsh = *blanks or %check('0123456789-. ':hdisc_3rsh) > 0;
      zdisc_3rsh = idisc_3rsh;
   else;
      zdisc_3rsh = %abs(%dec(%trim(hdisc_3rsh):5:2)) * -1;
   endif;

   if hdisc_ersh = *blanks or %check('0123456789-. ':hdisc_ersh) > 0;
      zdisc_ersh = idisc_ersh;
   else;
      zdisc_ersh = %abs(%dec(%trim(hdisc_ersh):5:2)) * -1;
   endif;

   if hsid_shaln = *blanks or %check('0123456789 -':hsid_shaln) > 0;
      zsid_shaln = isid_shaln;
   else;
      zsid_shaln = %int(hsid_shaln);
   endif;

   if zsid_shaln < -1 or zsid_shaln > 10;
      ei += 1;
      errs(ei) = 'The value of "Length of ID used for SHA calculation" can only range from -1 to 10.
      editMode = FALSE;
   endif;

   if hssn_len <> '4';
      hssn_len = '0';
   endif;

   zssn_len = %int(hssn_len);

   if hkiosk_ip# = *blanks or %check('013 ':hkiosk_ip#) > 0;
      hkiosk_ip# = '0';
   endif;

   zkiosk_ip# = %int(hkiosk_ip#);

endsr;

// ***************************************************************************************
// edt_tp: Edit the TP Options
// ***************************************************************************************
begsr edt_tp;

   if %len(%trim(htp_opsdly)) = 1;
      htp_opsdly = '0' + htp_opsdly;
   endif;

   if %len(%trim(hsid_len)) = 1;
      hsid_len = '0' + hsid_len;
   endif;

   if hssn_cntrl <> ' ' and hssn_cntrl <> 'F' and hssn_cntrl <> 'L' and hssn_cntrl <> 'M';
      hssn_cntrl  = 'M';
   endif;

   if htm_attctl <> ' ' and htm_attctl <> 'A' and htm_attctl <> 'C';
      ei += 1;
      errs(ei) = 'Valid values are blank, A or C';
   endif;

   if htm_attctl = 'C' and %lookup('PC':har_etsend) = 0;
      ei += 1;
      errs(ei) = 'Only Print/Mail school can have Attachment code set to a "C"';
   endif;

   if halwslfatt <> ' ' and halwslfatt <> 'Y';
      ei += 1;
      errs(ei) = 'Valid values are blank or Y';
   endif;

   if htm_1_bas  <> ' ' and htm_1_bas  <> '1' and htm_1_bas  <> 'S';
      ei += 1;
      errs(ei) = 'Valid values are blank, 1 or S';
   endif;

   if hro_ereset <> ' ' and hro_ereset <> 'Y';
      ei += 1;
      errs(ei) = 'Valid values are blank or Y';
   endif;

   if htp_resend <> '0090' and htp_resend <> '0091' and
      htp_resend <> '0092' and htp_resend <> *blanks;

      ei += 1;
      errs(ei) = 'Valid values are blank, 0090, 0091 or 0092';
   endif;

   if %lookup('AL':har_etsend) > 0 or %lookup('AC':har_etsend) > 0 or %lookup('AE':har_etsend) > 0;
      if not %open(tppdffld1);
         open tppdffld1;
      endif;

      chain(n) (hfice:'1') tppdffld1;
      if not %found(tppdffld1);
         ei += 1;
         if ilive_spdf > 0 or ilive_3pdf > 0;
            errs(ei) = '#7527';                            // School already live
         else;
            errs(ei) = '#7526';                            // Attempting to put live
         endif;
      else;
         if atp_orient = ' ';
            ei += 1;
            if ilive_spdf > 0 or ilive_3pdf > 0;
               errs(ei) = '#7507';                         // School already live
            else;
               errs(ei) = '#7506';                         // Attempting to put live
            endif;
         endif;
      endif;
   endif;

   if %lookup('AE':har_etsend) > 0;
      if hlink_3pdf = *blanks;
         ei += 1;
         errs(ei) = '#7525';
      endif;
   endif;

   if hlink_3pdf <> *blanks;
      if %scan('CREDENTIALS-INC.COM':%xlate(xlc:xuc:hlink_3pdf)) > 0 and hfice <> '009998';
         ei += 1;
         errs(ei) = '#7524';
      endif;
   endif;

   hregistrar = %scanrpl('''':'`':hregistrar);

   if hrobo_mntc = *blanks;
      hrobo_cycl = *blanks;
      hrobo_cycm = *blanks;
   else;
      exsr validateBillMonths;

      if monthInvalid;
         ei += 1;
         errs(ei) = '#7528';
      endif;
   endif;

   hasOtherOptions = (hnoreason <> 'N' or iedt_t_adt <> 'N' or itp_nocmts = 'Y' or
                     (itm_flaga <> ' ' and itm_flaga <> '5') or
                     (itm_flagb <> ' ' and itm_flagb <> '5') or
                     (itm_flag1 <> ' ' and itm_flag1 <> '5') or
                     (itm_flag2 <> ' ' and itm_flag2 <> '5') or
                     (itm_flag3 <> ' ' and itm_flag3 <> '5') or
                     (itm_flag4 <> ' ' and itm_flag4 <> '5') or
                     (iedt_t_col <> ' ' and iedt_t_col <> '5'));

   if not hasOtherOptions;
      htb_noothr = 'Y';
   endif;

endsr;

// ***************************************************************************************
// fillSchoolBasics: Fill H-Fields with School Basic Information
// ***************************************************************************************
begsr fillSchoolBasics;

   // Basic Parameters
   hschname = ischname;
   hsch_sname = isch_sname;
   hsortname = isortname;
   haddr1 = iaddr1;
   haddr2 = iaddr2;
   hcity = icity;
   hpostcd = ipostcd;
   hstate = istate;
   hcntry = icntry;
   hteam_id = iteam_id;
   hficegroup = ificegroup;

   if ifdx_dtoff = 0;
      hfdx_dtoff = '0';
   else;
      hfdx_dtoff = %char(ifdx_dtoff);
   endif;

   if ifdx_dton = 0;
      hfdx_dton = '0';
   else;
      hfdx_dton = %char(ifdx_dton);
   endif;

   if ifdx_tmoff = 0;
      hfdx_tmoff = '0';
   else;
      hfdx_tmoff = %editc(ifdx_tmoff:'X');
   endif;

   if ifdx_tmon = 0;
      hfdx_tmon = '0';
   else;
      hfdx_tmon = %editc(ifdx_tmon:'X');
   endif;

   if irsh_dtoff = 0;
      hrsh_dtoff = '0';
   else;
      hrsh_dtoff = %char(irsh_dtoff);
   endif;

   if irsh_dton = 0;
      hrsh_dton = '0';
   else;
      hrsh_dton = %char(irsh_dton);
   endif;

   if irsh_tmoff = 0;
      hrsh_tmoff = '0';
   else;
      hrsh_tmoff = %editc(irsh_tmoff:'X');
   endif;

   if irsh_tmon = 0;
      hrsh_tmon = '0';
   else;
      hrsh_tmon = %editc(irsh_tmon:'X');
   endif;

   zfdx_dtoff = ifdx_dtoff;
   zfdx_tmoff = ifdx_tmoff;
   zfdx_dton = ifdx_dton;
   zfdx_tmon = ifdx_tmon;
   zrsh_dtoff = irsh_dtoff;
   zrsh_tmoff = irsh_tmoff;
   zrsh_dton = irsh_dton;
   zrsh_tmon = irsh_tmon;

   hs_act = is_act;
   hs_atp = is_atp;
   hs_ccd = is_ccd;
   hs_ceebact = is_ceebact;
   hs_esis = is_esis;
   hs_ipeds = is_ipeds;
   hs_liaison = is_liaison;
   hs_nchelp = is_nchelp;
   hs_opeid = is_opeid;
   hs_usis = is_usis;
   hs_spdefic = is_spdefic;

   hs_cruz = %char(icruz_code);

   if ipassmin = *blanks;
      hpassMin = '8';
   else;
      hpassMin = ipassmin;
   endif;

   if ipassmax = *blanks;
      hpassMax = '50';
   else;
      hpassMax = ipassmax;
   endif;

   hchargecrz = ichargecrz;
   hprtnr_req = iprtnr_req;
   hcolor_pri = icolor_pri;
   hcolor_sec = icolor_sec;
   hcolor_txt = icolor_txt;
   hcolor_tph = icolor_tph;

   if icolor_tph = '#FFF' or icolor_tph = '#FFFFFF';       // If white, set to black
      hcolor_tph = '#000000';
   endif;

   hcoloptpri = icoloptpri;
   hcoloptsec = icoloptsec;

endsr;

// ***************************************************************************************
// fill_con: Pre-fill the Contact Data Screen
// ***************************************************************************************
begsr fill_con;

   exsr get_cntct3;

   husrtype = mrecord_id;
   hfrstname = mfrstname;
   hmidlname = mmidlname;
   hlastname = mlastname;
   hnam_title = mtitle;
   hnickname = mnickname;
   hcompany = mcompany;

   if mcompany = *blanks;
      hcompany = yschname;
   endif;

   haddr1 = maddr1;
   haddr2 = maddr2;
   hcity = mcity;
   hstate = mstate;
   hpostcd = mpostcd;
   hcntry = mcntry;

   if maddr1 = *blanks;
      haddr1 = iaddr1;
      haddr2 = iaddr2;
      hcity = icity;
      hstate = istate;
      hpostcd = ipostcd;
      hcntry = icntry;
   endif;

   hsalut = msalut;
   hnam_title = mtitle;
   htel# = %trim(mtelnum) + ' X' + %trim(mtelextn);
   hemail = memail;
   hno_email = mno_email;

endsr;

// ***************************************************************************************
// fill_prt: Fill H-Fields with School TP Options
// ***************************************************************************************
begsr fill_prt;

   // Transcript Options
   het_senda  = iet_senda;
   herm_paper = ierm_paper;
   hcredp_onl = icredp_onl;
   htp#_toprt = %trim(%editc(itp#_toprt:'4'));             // No 0,-, and 1000 notation
   hprint_ab  = iprint_ab;
   hprint_att = iprint_att;
   htp_reml_c = itp_reml_c;
   hcover_tel = icover_tel;
   hcover_msg = icover_msg;

   if htp#_toprt = *blanks;
      htp#_toprt = '0';
   endif;

endsr;

// ***************************************************************************************
// fill_tp: Fill H-Fields with School TP Options
// ***************************************************************************************
begsr fill_tp;

   // Transcript Options
   htp_reml_c = itp_reml_c;
   hssn_len = %char(issn_len);
   hssn_cntrl = issn_cntrl;
   hssn_iptyp = issn_iptyp;
   hteam_id = iteam_id;
   hedt_t_sid = iedt_t_sid;
   hsid_fmt = isid_fmt;
   hsid_char1 = isid_char1;
   hsid_len = istuid_len;
   hsid_shaln = %char(isid_shaln);
   hsha_methd = isha_methd;
   hdis_dob = idis_dob;
   hdis_nam = idis_nam;
   hdis_sid = idis_sid;
   hdis_ssn = idis_ssn;
   hno_phone = ino_phone;
   hprohtrans = iprohtrans;
   htp_on_tp2 = itp_on_tp2;
   het_senda  = iet_senda;
   hforce_ets = iforce_ets;
   hforce_pdf = iforce_pdf;
   hpdfuplmod = ipdfuplmod;
   hprtuplmod = iprtuplmod;
   hvrfy_outb = ivrfy_outb;
   halw_punam = ialw_punam;
   htm_attctl = itm_attctl;
   halwslfatt = ialwslfatt;
   htm_attfrc = itm_attfrc;
   htm_slffrc = itm_slffrc;
   htm_1_bas  = itm_1_bas;
   htm_dftbas = itm_dftbas;
   hdo_ttypes = ido_ttypes;
   htm_dfttty = itm_dfttty;
   htm_dfthld = itm_dfthld;
   htm_dftxtr = itm_dftxtr;
   htm_dftshp = itm_dftshp;
   hro_ereset = iro_ereset;
   htp_resend = itp_resend;
   hrules_sig = irules_sig;
   hdoes_edi = idoes_edi;
   hrobomaint = %char(irobomaint);
   hrobo_cycl = irobo_cycl;
   hrobo_cycm = irobo_cycm;
   hrobo_mntc = irobo_mntc;
   het_ibp_rt = %char(iet_ibp_rt);
   het_ibf_rt = %char(iet_ibf_rt);
   hmemoe_rat = %char(imemoe_rat);
   hmemom_rat = %char(imemom_rat);
   hmemoa_rat = %char(imemoa_rat);
   hmemod_rat = %char(imemod_rat);
   hmemod_avw = %char(imemod_avw);
   hmemo_brib = %char(imemo_brib);
   het_minchg = %char(iet_minchg);
   hdisc_pdf = %char(idisc_pdf);
   hdisc_3pdf = %char(idisc_3pdf);
   hdisc_elec = %char(idisc_elec);
   hdisc_prsh = %char(idisc_prsh);
   hdisc_3rsh = %char(idisc_3rsh);
   hdisc_ersh = %char(idisc_ersh);
   hcunyctl = icunyctl;
   hgenedreq1 = igenedreq1;
   hgenedreq2 = igenedreq2;
   hgenedreq3 = igenedreq3;
   htp_opsdly = itp_opsdly;
   hschmsgctl = ischmsgctl;
   hnoreason = inoreason;
   htb_noothr = itb_noothr;
   hmouse_sig = imouse_sig;
   htp_supcty = itp_supcty;
   htm_year_q = itm_year_q;
   hreasoncds = ireasoncds;
   htp_svycod = itp_svycod;
   htp_svyurl = itp_svyurl;
   htm_kiourl = itm_kiourl;
   hkiosk_ip# = %char(ikiosk_ip#);
   hregistrar = iregistrar;
   hlink_3pdf = ilink_3pdf;
   henty_fice = ienty_fice;
   hpdfscrty = isigner;
   hpdf3_all = ipdf3_all;
   hatt_gened = iatt_gened;

endsr;

// ***************************************************************************************
// get_cntct3: Get the Contact Database Record - by Seq#
// ***************************************************************************************
begsr get_cntct3;

   hfice = %subst(h_key:1:6);
   hseq# = %int(%subst(h_key:7:2));

   if not %open(dvinstitf3);
      open dvinstitf3;
   endif;

   clear schfax_num;
   clear schcnt_nam;
   clear schcnt_tel;
   clear schcnt_eml;

   chain (hfice:hseq#) contact;
   if not %found(dvinstitf3);
      schfax_num = admin_fax;
      schcnt_nam = 'N/A';
      schcnt_tel = 'N/A';
      schcnt_eml = 'N/A';
      leavesr;
   endif;

   schfax_num = mtelnum;
   schcnt_nam = mfrstname + ' ' + mlastname;

   if mtelextn <> *blanks;
      schcnt_tel = %trim(mtelnum) + ' X' + %trim(mtelextn);
   else;
      schcnt_tel = %trim(mtelnum);
   endif;

   schcnt_eml = memail;

endsr;

// ***************************************************************************************
// get_ciopts: Get the CICCSOPT2 Database Record
// ***************************************************************************************
begsr get_ciopts;

   if not %open(ciccsopt2);
      open ciccsopt2;
   endif;

   chain(n) (hfice:happlid:hgroup_id:%int(hmnt_seq)) ccsopt2rec;
   if %found(ciccsopt2) and ei = 0;
      hgroup_id = pgroup_id;
      hseqnce = pseqnce;
      htitle = ptitle;
      htext = ptext;
   endif;

endsr;

// ***************************************************************************************
// get_formats: Get the Formats from TPPDFFLD1
// ***************************************************************************************
begsr get_formats;

   formatIdx = 0;
   clear formats;
   if ficeChange;
      clear hformatcd;
   endif;

   if not %open(tppdffld1);
      open tppdffld1;
   endif;

   setll (hfice) pdffields;
   dow not %eof(tppdffld1);
      reade (hfice) pdffields;

      if %eof(tppdffld1);
         leave;
      endif;

      formatIdx += 1;

      formats(formatIdx).formatcd = aformatcd;
      formats(formatIdx).orientation = atp_orient;
      formats(formatIdx).description = adescrp;
      formats(formatIdx).noPdfHeader = apdfdishdr;
      formats(formatIdx).noPdfFooter = apdfdisftr;
      formats(formatIdx).noPdfWater = apdfdiswtr;
      formats(formatIdx).noPdfGrade = apdfdisgrd;
      formats(formatIdx).noPrtHeader = aprtdishdr;
      formats(formatIdx).noPrtFooter = aprtdisftr;
      formats(formatIdx).noPrtWater = aprtdiswtr;
   enddo;

   formatTot = formatIdx;

   if hformatcd = *blanks and formatTot > 0;
      hformatcd = formats(1).formatcd;
   endif;

endsr;

// ***************************************************************************************
// getPrintRecs: Get the records required for print options
// ***************************************************************************************
begsr getPrintRecs;

   locationDs = tploc_getLocations(hfice:locationTot);
   opcdcnt = locationTot;

   if not %open(formid1c);
      open formid1c;
   endif;

   formcnt = 0;

   setll ('T') formidrec;
   if not %equal(formid1c);
      leavesr;
   endif;

   reade ('T') formidrec;
   dow not %eof(formid1c);
      if mfice <> *blanks;
         if mfice <> GetLiveFice(hfice);
            reade ('T') formidrec;
            iter;
         endif;
      endif;

      formcnt += 1;
      formds(formcnt).id = mformid;
      formds(formcnt).code = mcategry;
      formds(formcnt).desc = mdescrp;

      reade ('T') formidrec;
   enddo;

endsr;

// ***************************************************************************************
// getSchoolDetails : Get the School Name
// ***************************************************************************************
begsr getSchoolDetails;

   // Open the dvinstitf1
   if not %open(dvinstitf1);
      open dvinstitf1;
   endif;

   chain(n) (wrk_fice) instrec;
   if not %found(dvinstitf1);
      clear ithe_featr;
      clear ischname;
      clear imsgprefix;
      clear idetable;
      clear ichargetm;
      institChain = FALSE;
   else;
      institChain = TRUE;
   endif;

   hfice = ifice;

   if ithe_featr = 'T';
      yschname = 'The ' + %trim(ischname);
   else;
      yschname = ischname;
   endif;

   // Set the default decode/encode table name if school's is blank
   if idetable = *blanks;
      idetable = 'TABLE0    ';
   endif;

   if icntry = *blanks;
      icntry = 'US';
   endif;

   clear irobo_au_p;
   if ifice = '006656';
      irobo_au_p = 'Y';
   endif;

   if ifice = '000000' or ilinkimag = *blanks or %subst(ilinkimag:1:16) = '/icon_sch/demos/';
      ilinkimag = '/CIimages/CSemail.gif';
      ilinkhome = 'https://www.credentials-inc.com';
   endif;

endsr;

// ***************************************************************************************
// live_services: Warn CSRs about school live on tod/ess/tp
// ***************************************************************************************
begsr live_services;

   //SG credUser = crmfunc_getUser(iteam_id);

   select;
   when iess_cycl = 'C';
      fi += 1;
      info(fi) = '<h4>This school is a Career Cruising customer.</h4>';
      fi += 1;
      info(fi) = '<h5>Please call: 800-965-8541 <br/>';

   // Not Live on TP, Live TOD customer viewed from Vegas and Northfield
   when ichargetm <> 'Y' and ichargetod = 'Y' and ichargeess <> 'Y' and
        (ccinc_locn = 'N' or ccinc_locn = 'L');

      fi += 1;
      info(fi) = '<h4>School is a ToD customer. Please Transfer:</h4>';
      fi += 1;
      info(fi) = '<h5>Extension: 3805 for ToD/eSS Customer Service<br/>';
      fi += 1;
      info(fi) = 'Extension: ' + credUser.phoneExt + ' for ' + %trim(credUser.name) + '</h5>';

   // Not Live on TP and Live eSS customer viewed from Vegas and Northfield
   // eSS only customer
   when ichargetm <> 'Y' and (ichargeess = 'Y' or ichargeess = 'L') and
        ichargetod <> 'Y' and (ccinc_locn = 'N' or ccinc_locn = 'L');

      fi += 1;
      info(fi) = '<h4>School is an eSS customer.</h4>';

   // Not Live on TP and Live eSS/ToD customer viewed from Vegas and Northfield
   when ichargetm <> 'Y' and ichargeess = 'Y' and ichargetod = 'Y' and
        (ccinc_locn = 'N' or ccinc_locn = 'L');

      fi += 1;
      info(fi) = '<h4>School is an eSS and ToD customer. Please Transfer:</h4>';
      fi += 1;
      info(fi) = '<h5>Extension: 3805 for ToD/eSS Customer Service<br/>';
      fi += 1;
      info(fi) = 'Extension: ' + credUser.phoneExt + ' for ' + %trim(credUser.name) + '</h5>';

   // Live on TP and ToD viewed from OH
   when ichargetm = 'Y' and ichargetod = 'Y' and ichargeess <> 'Y' and ccinc_locn = 'O';
      our_addrs6 = CurRmt8;
      fi += 1;
      info(fi) = '<h4>School is live on both TranscriptsPlus and ToD. If transfer is needed:</h4>';
      fi += 1;
      info(fi) = '<h5>Extension: 3005 for TranscriptsPlus Customer Service<br/>';
      fi += 1;
      info(fi) = 'Extension: ' + credUser.phoneExt + ' for ' + %trim(credUser.name) + '</h5>';

   // Live on TP and eSS viewed from OH
   when ichargetm = 'Y' and ichargetod <> 'Y' and ichargeess = 'Y' and ccinc_locn = 'O';
      fi += 1;
      info(fi) = '<h4>School is live on both TranscriptsPlus and eSS. If transfer is needed:</h4>';
      fi += 1;
      info(fi) = '<h5>Extension: 3005 for TranscriptsPlus Customer Service<br/>';
      fi += 1;
      info(fi) = 'Extension: ' + credUser.phoneExt + ' for ' + %trim(credUser.name) + '</h5>';

   // Live on TP, ToD and eSS viewed from OH
   when ichargetm = 'Y' and ichargetod = 'Y' and ichargeess = 'Y' and ccinc_locn = 'O';
      fi += 1;
      info(fi) = '<h4>School is live on TranscriptsPlus, ToD and eSS. If transfer is needed:</h4>';
      fi += 1;
      info(fi) = '<h5>Extension: 3005 for TranscriptsPlus Customer Service<br/>';
      fi += 1;
      info(fi) = 'Extension: ' + credUser.phoneExt + ' for ' + %trim(credUser.name) + '</h5>';

   endsl;

   if ichargetm = 'Y';
      // Master Print Code banner message
      select;
      when imaster_pc = *blanks;
         //normal status
      when imaster_pc = 'N';
         ei += 1;
         errs(ei) = '<h4>The school has disabled ALL transcript completing.</h4>';
         ei += 1;
         errs(ei) = '<h4>At this time transcript orders are being accepted,'+
                    ' but are NOT being processed by the school.</h4>';
      when imaster_pc = 'M';
         ei += 1;
         errs(ei) = '<h4>The school has disabled RoboRegistrar transcript completing.</h4>';
         ei += 1;
         errs(ei) = '<h4>At this time transcript orders are being accepted,'+
                    ' but only orders for manual completion are being done.</h4>';
      endsl;

      //ROBO status banner message
      if imaster_pc = *blanks;
         if irobo_stac <> 'R' and irobo_stac <> *blanks;
            select;
            when irobo_stac = 'D'; //Down (PC ROBO Shutdown)
               wrIdx += 1;
               warning(wrIdx) = '<h4>RoboRegistrar for this school is down.</h4>';
            when irobo_stac = 'M'; //Maintenance Mode
               wrIdx += 1;
               warning(wrIdx) = '<h4>RoboRegistrar for this school is currently in Maintenance mode.
            when irobo_stac = 'T' or irobo_stac = 'N'; //Temp Down
               wrIdx += 1;
               warning(wrIdx) = '<h4>RoboRegistrar for this school is down temporarily.</h4>';
            when irobo_stac = 'S'; //Scheduled Down
               wrIdx += 1;
               warning(wrIdx) = '<h4>RoboRegistrar for this school is down on schedule.</h4>';
            endsl;

            wrIdx += 1;
            warning(wrIdx) = '<h4>At this time transcript orders are being ' +
                             'accepted, but are NOT being processed by the school.</h4>';

            if irobo_la_d > 0;
               byte10 = %char(%date(irobo_la_d));
            else;
               byte10 = %char(irobo_la_d);
            endif;
            if irobo_la_t > 0;
               byte9 = %char(%time(irobo_la_t):*usa);
            else;
               byte9 = %char(irobo_la_t);
            endif;

            wrIdx += 1;
            warning(wrIdx) = 'The last active Robo Date/Time was: ' + %trim(byte10) + ' at ' + %trim

         else;
            // do nothing, robo either does not exist for the school or
            // there is no problem status to report
         endif;
      endif;

   endif;

endsr;

// ***************************************************************************************
// next_seq#: Determine the next open sequence# for a contact
// ***************************************************************************************
begsr next_seq#;

   // Default the next sequence# - need to read through and see what sequences
   // are already used for this FICE
   if not %open(dvinstitf3);
      open dvinstitf3;
   endif;

   clear ar_seq#;

   setll hfice dvinstitf3;
   reade(n) hfice contact;
   dow not %eof(dvinstitf3);
      ar_seq#(mseq#) = 'X';
      reade(n) hfice contact;
   enddo;

   // Lookup the first blank element in ar_seq#, this is next open slot
   if %lookup(' ':ar_seq#) > 0;
      hseq# = %lookup(' ':ar_seq#);
   endif;

endsr;

// ***************************************************************************************
// subroutine to parse the input buffer into PAR array and then load working "h" variables
// with initial values. Those fields that are processed in Upper Case only are converted
// from lower case to upper case by this routine.
//
// When this routine is called, it is assumed that the input bufr has been moved into
// pip(2)-pip(2048) with a MOVEA op and that pip(1) is blank or doesn't matter.
// This rtn then moves an & into pip(1) so that all field recognition logic is uniform.
// ***************************************************************************************
begsr parseinp;

   clear htmlForm;
   if httpAccept = 'json';                                            //SG01
      // parseJSON will use the ContentType. of text/json             //SG01
       if parseJSON(htmlForm : bufin : bufinLn : MAX_INPUT_DIM) < 0;  //SG01
          // This is an error parsing                                 //SG01
                                                                      //SG01
       endif;                                                         //SG01
   else;                                                              //SG01
      htmlForm = parseForm(bufin:curContentType:TRUE);
   endif;                                                             //SG01

   //-----------------------------------------------------------------
   //  Now format all the working parms
   //-----------------------------------------------------------------
   for pw = 1 to htmlForm.numInputs;
      field_name = htmlForm.input(pw).name;
      field_data = htmlForm.input(pw).data;
      field_data = %scanrpl('"':'':field_data);
      field_len = %len(%trim(field_data));

      select;

      when field_name = *blanks;

      // SignOnKey
      when field_name = 'SK';
         hsignonkey = cleanInptTxt(field_data);

      // FORMID
      when field_name = 'FORMID';
         if field_len = 3;
            hscrn_type = cleanInptTxt(field_data);
         else;
            hscrn_type = 'XXX';
            condition = 'bad-form';
         endif;

      // APPLID
      when field_name = 'APPLID';
         happlid = field_data;

      // ACTION
      when field_name = 'CHOICE' or field_name='ACTION';
         h_action = cleanInptTxt(field_data);

      // FICE
      when field_name = 'FICE';
         hfice = %xlate(xlc:xuc:field_data);

      // NEW_FICE
      when field_name = 'NUFICE';
         hnufice = %xlate(xlc:xuc:field_data);

      // KEY
      when field_name = 'KEY';
         h_key = field_data;

      // SCRTYP
      when field_name = 'SCRTYP';
         hscrn_type = field_data;

      // User ID
      when field_name = 'USERID';
         huserid = %xlate(xlc:xuc:cleanInptTxt(field_data));

      //--------------------------------------------------------------
      //                GA_PARSE OPTIONS
      //--------------------------------------------------------------
      when field_name = 'EDI_V_DEG';
         hedi_v_deg = %xlate(xlc:xuc:cleanInptTxt(field_data));

      //--------------------------------------------------------------
      //                TP_PARSE OPTIONS
      //--------------------------------------------------------------
      when field_name = 'SSN_LEN';
         hssn_len = field_data;

      when field_name = 'SSN_CTL';
         hssn_cntrl = field_data;

      when field_name = 'SID_EDT';
         hedt_t_sid = field_data;

      when field_name = 'SID_LEN';
         hsid_len = field_data;

      when field_name = 'SID_FMT';
         hsid_fmt = field_data;

      when field_name = 'SID_1ST';
         hsid_char1 = field_data;

      when field_name = 'RO_ERESET';
         hro_ereset = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TP_ON_TP2';
         htp_on_tp2 = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'PDFUPL';
         hpdfuplmod = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'PRTUPL';
         hprtuplmod = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'VRFYOUTB';
         hvrfy_outb = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'FORCE_ETS';
         hforce_ets = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'FORCE_PDF';
         hforce_pdf = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TM_ATTCTL';
         htm_attctl = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'ALWSLFATT';
         halwslfatt = %xlate(xlc:xuc:%trim(field_data));

      when field_name = 'ALW_PUNAM';
         halw_punam = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TM_ATTFRC';
         htm_attfrc = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TM_SLFFRC';
         htm_slffrc = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TM_1_BAS';
         htm_1_bas = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'DO_TTYPES';
         hdo_ttypes = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TM_DFTBAS';
         htm_dftbas = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TM_DFTTTY';
         htm_dfttty = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TM_DFTHLD';
         htm_dfthld = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TM_DFTXTR';
         htm_dftxtr = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TM_DFTSHP';
         htm_dftshp = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TP_RESEND';
         htp_resend = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'RULES_SIG';
         hrules_sig = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'DOES_EDI';
         hdoes_edi = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'ROBOMAINT';
         hrobomaint = field_data;

      when field_name = 'ET_IBP_RT';
         het_ibp_rt = field_data;

      when field_name = 'ET_IBF_RT';
         het_ibf_rt = field_data;

      when field_name = 'MEMOA_RAT';
         hmemoa_rat = field_data;

      when field_name = 'MEMOD_RAT';
         hmemod_rat = field_data;

      when field_name = 'MEMOE_RAT';
         hmemoe_rat = field_data;

      when field_name = 'MEMOM_RAT';
         hmemom_rat = field_data;

      when field_name = 'MEMOD_AVW';
         hmemod_avw = field_data;

      when field_name = 'ET_MINCHG';
         het_minchg = field_data;

      when field_name = 'CUNYCTL';
         hcunyctl = field_data;

      when field_name = 'GENEDREQ1';
         hgenedreq1 = field_data;

      when field_name = 'GENEDREQ2';
         hgenedreq2 = field_data;

      when field_name = 'GENEDREQ3';
         hgenedreq3 = field_data;

      when field_name = 'SCHMSGCTL';
         hschmsgctl = field_data;

      when field_name = 'TP_OPSDLY';
         htp_opsdly = field_data;

      when field_name = 'TP_SVYCOD';
         htp_svycod = %xlate(xlc:xuc:cleanInptTxt(field_data));

      when field_name = 'TP_SVYURL';
         htp_svyurl = field_data;

      when field_name = 'TM_KIOURL';
         htm_kiourl = field_data;

      // USRTYPE (for special discounted user types)
      when field_name = 'USRTYPE';
         husrtype = field_data;

      // Sequence
      when field_name = 'SEQNC';
         monitor;
            hseq# = %int(field_data);
         on-error;
         endmon;

      // Name Salutation
      when field_name = 'NSAL';
         hsalut = field_data;

      // First name
      when field_name = 'NF';
         hfrstname = field_data;

      // Middle name
      when field_name = 'NM';
         hmidlname = field_data;

      // Last name
      when field_name = 'NL';
         hlastname = field_data;

      // Nickname
      when field_name = 'NN';
         hnickname = field_data;

      // Title
      when field_name = 'TITLE';
         hnam_title = field_data;

      // Company Name
      when field_name = 'NC';
         hcompany = field_data;

      // Address 1
      when field_name = 'A1';
         haddr1 = field_data;

      // Address 2
      when field_name = 'A2';
         haddr2 = field_data;

      // City
      when field_name = 'CITY';
         hcity = field_data;

      // State
      when field_name = 'STATE';
         hstate = field_data;

      // Postal code
      when field_name  = 'ZIP';
         hpostcd = field_data;

      // Telephone #
      when field_name = 'TEL';
         htel# = field_data;

      // EMail address
      when field_name = 'EMAIL';
         hemail = field_data;

      // 2nd EMail address
      when field_name = 'EMAIL2';
         hemail2 = field_data;

      // AAC
      when field_name = 'AAC';
         h_aac = field_data;

      // CNR
      when field_name = 'CNR';
         h_cnr = field_data;

      // Opt out for EMail notifications
      when field_name = 'NO_EMAIL';
         hno_email = field_data;

      when field_name = 'SSN_IPTYP';
         hssn_iptyp = field_data;

      when field_name = 'SID_SHALN';
         hsid_shaln = field_data;

      when field_name = 'SHA_METHD';
         hsha_methd = field_data;

      when field_name = 'DIS_DOB';
         hdis_dob = field_data;

      when field_name = 'DIS_NAM';
         hdis_nam = field_data;

      when field_name = 'DIS_SID';
         hdis_sid = field_data;

      when field_name = 'DIS_SSN';
         hdis_ssn = field_data;

      when field_name = 'NO_PHONE';
         hno_phone = field_data;

      when field_name = 'PROH_TRANS';
         hprohtrans = field_data;

      when field_name = 'DISC_PDF';
         hdisc_pdf = field_data;

      when field_name = 'DISC_3PDF';
         hdisc_3pdf = field_data;

      when field_name = 'DISC_ELEC';
         hdisc_elec = field_data;

      when field_name = 'DISC_PRSH';
         hdisc_prsh = field_data;

      when field_name = 'DISC_3RSH';
         hdisc_3rsh = field_data;

      when field_name = 'DISC_ERSH';
         hdisc_ersh = field_data;

      when field_name = 'MOUSE_SIG';
         hmouse_sig = field_data;

      when field_name = 'TP_SUPCTY';
         htp_supcty = field_data;

      when field_name = 'TM_YEAR_Q';
         htm_year_q = field_data;

      when field_name = 'SEND_AR';
         het_senda = %trim(het_senda) + %xlate(xlc:xuc:%trim(field_data));

      when field_name = 'NOREASON';
         hnoreason = %trim(field_data);

      when field_name = 'TB_NOOTHR';
         htb_noothr = %trim(field_data);

      when field_name = 'ET_SENDA';
         het_senda = %xlate(xlc:xuc:%trim(field_data));

      when field_name = 'KIOSK_IP';
         hkiosk_ip# = field_data;

      when field_name = 'REGISTRAR';
         hregistrar = field_data;

      when field_name = 'RELATELINK';
         hlink_3pdf = field_data;

      when field_name = 'ROBOBILLC';
         hrobo_cycl = field_data;

      when field_name = 'ROBOBILLM';
         hrobo_cycm = field_data;

      when field_name = 'ROBOCHGCD';
         hrobo_mntc = field_data;

      when field_name = 'PDF3_ALL';
         hpdf3_all = field_data;

      when field_name = 'PDFSCRTY';
         hpdfscrty = field_data;

      when field_name = 'MEMO_BRIB';
         hmemo_brib = field_data;

      when field_name = 'ENTY_FICE';
         henty_fice = field_data;

      when field_name = 'TPOPTS';
         hgroup_id = field_data;

      when field_name = 'MNTSEQ';
         hmnt_seq = field_data;

      when field_name = 'MNTGRP';
         hmnt_grp = field_data;

      when field_name = 'GROUPID';
         if h_action <> 'GET';
            hgroup_id = %xlate(xlc:xuc:field_data);
         endif;

      when field_name = 'SEQNCE';
         if field_data = *blanks;
            hseqnce = 0;
         else;
            hseqnce = %int(field_data);
         endif;

      when field_name = 'TITLEOPT';
         htitle = field_data;

      when field_name = 'TXT';
         htext = field_data;

      // Team Leader ID
      when field_name = 'CRM_ID';
         hteam_id = %xlate(xlc:xuc:field_data);

      // Fice Group
      when field_name = 'FICEGROUP';
         hficegroup = %xlate(xlc:xuc:field_data);

      when field_name = 'TPPRTBTC';
         herm_paper = field_data;

      when field_name = 'TPFORMID';
         hformid = field_data;

      when field_name = 'PRNTSCALE';
         hprntscale = field_data;

      when field_name = 'PDF_SCALE';
         hpdf_scale = field_data;

      when field_name = 'CREDP_ONL';
         hcredp_onl = field_data;

      when field_name = 'COVER_TEL';
         hcover_tel = field_data;

      when field_name = 'COVER_MSG';
         hcover_msg = field_data;

      when field_name = 'TP_TOPRT';
         htp#_toprt = field_data;

      when field_name = 'PRINT_AB';
         hprint_ab = field_data;

      when field_name = 'PRINT_ATT';
         hprint_att = field_data;

      when field_name = 'RESEND_MAX';
         hcs_rsnd_# = %trim(field_data);
         if hcs_rsnd_# = *blanks;
            hcs_rsnd_# = '0';
         endif;

      when field_name = 'CS_RSND_C';
         hcs_rsnd_c = field_data;

      when field_name = 'CS_RSND_W';
         hcs_rsnd_w = %trim(field_data);
         if hcs_rsnd_w = *blanks;
            hcs_rsnd_w = '0';
         endif;

      when field_name = 'TP_REML_C';
         htp_reml_c = field_data;

      when field_name = 'S_SPDEFIC';
         hs_spdefic = field_data;

      when field_name = 'S_CEEBACT';
         hs_ceebact = field_data;

      when field_name = 'S_IPEDS';
         hs_ipeds = field_data;

      when field_name = 'S_LIAISON';
         hs_liaison = field_data;

      when field_name = 'CHARGE_CRUZ';
         hchargecrz = field_data;

      when field_name = 'S_CRUZ';
         hs_cruz = field_data;
         if hs_cruz = *blanks;
            hs_cruz = '0';
         endif;

      when field_name = 'PASSMIN';
         hpassmin = field_data;

      when field_name = 'PASSMAX';
         hpassmax = field_data;

      when field_name = 'S_ACT';
         hs_act = field_data;

      when field_name = 'S_ATP';
         hs_atp = field_data;

      when field_name = 'S_CCD';
         hs_ccd = field_data;

      when field_name = 'S_ESIS';
         hs_esis = field_data;

      when field_name = 'S_NCHELP';
         hs_nchelp = field_data;

      when field_name = 'S_OPEID';
         hs_opeid = field_data;

      when field_name = 'S_USIS';
         hs_usis = field_data;

      when field_name = 'PRTNR_REQ';
         hprtnr_req = field_data;

      when field_name = 'FDXDTOFF';
         hfdx_dtoff = field_data;
         if hfdx_dtoff = *blanks;
            hfdx_dtoff = '0';
         endif;

      when field_name = 'FDXTMOFF';
         hfdx_tmoff = field_data;
         if hfdx_tmoff = *blanks;
            hfdx_tmoff = '0';
         endif;

      when field_name = 'FDXDTON';
         hfdx_dton = field_data;
         if hfdx_dton = *blanks;
            hfdx_dton = '0';
         endif;

      when field_name = 'FDXTMON';
         hfdx_tmon = field_data;
         if hfdx_tmon = *blanks;
            hfdx_tmon = '0';
         endif;

      when field_name = 'RSHDTOFF';
         hrsh_dtoff = field_data;
         if hrsh_dtoff = *blanks;
            hrsh_dtoff = '0';
         endif;

      when field_name = 'RSHTMOFF';
         hrsh_tmoff = field_data;
         if hrsh_tmoff = *blanks;
            hrsh_tmoff = '0';
         endif;

      when field_name = 'RSHDTON';
         hrsh_dton = field_data;
         if hrsh_dton = *blanks;
            hrsh_dton = '0';
         endif;

      when field_name = 'RSHTMON';
         hrsh_tmon = field_data;
         if hrsh_tmon = *blanks;
            hrsh_tmon = '0';
         endif;

      when field_name = 'COLOR_PRI';
         hcolor_pri = field_data;

      when field_name = 'COLOR_SEC';
         hcolor_sec = field_data;

      when field_name = 'COLOPTPRI';
         hcoloptpri = field_data;

      when field_name = 'COLOPTSEC';
         hcoloptsec = field_data;

      when field_name = 'COLOR_TPH';
         hcolor_tph = field_data;

      when field_name = 'COLOR_TXT';
         hcolor_txt = field_data;

      when field_name = 'FORMATCD';
         hformatcd = field_data;

      when field_name = 'NEWFRMTCD';
         hnewfrmtcd = field_data;

      when field_name = 'NEWONLNCD';
         hnewonlncd = field_data;

      when field_name = 'TPORIENT';
         htp_orient = field_data;

      when field_name = 'NEWORIENT';
         hnew_orient = field_data;

      when field_name = 'CHKIMGTYP';
         hchkimgtyp = field_data;

      when field_name = 'LOCATIONCD';
         hlocationcd = field_data;

      when field_name = 'HASMULTI';
         hhas_multi = field_data;

      when field_name = 'ATT_GENED';
         hatt_gened = field_data;

      other;

         // Standard parsing copybook for file maint applications
/copy rpgcopy,parsutfile

      endsl;
   endfor;

endsr;

// ***************************************************************************************
// pp_conadd : Panel Processing to Add a New Contact
// ***************************************************************************************
begsr pp_conadd;

   if not %open(dvinstitf3);
      open dvinstitf3;
   endif;

   mfice = hfice;
   mseq# = hseq#;
   mrecord_id = husrtype;
   msalut = hsalut;
   mfrstname = hfrstname;
   mmidlname = hmidlname;
   mlastname = hlastname;
   mtitle = hnam_title;
   mnickname = hnickname;
   mcompany = hcompany;
   maddr1 = haddr1;
   maddr2 = haddr2;
   mcity = hcity;
   mstate = hstate;
   mpostcd = hpostcd;
   mcntry = hcntry;
   mtelnum = htel#;
   memail = hemail;
   mno_email = hno_email;
   mchguser = huserid;
   mchgdate = cycle_date;

   write(e) contact;

   if %error;
      ei += 1;
      errs(ei) = 'You attempted to add a duplicate contact, please review';
   endif;

endsr;

// ***************************************************************************************
// pp_condel : Panel Processing to Delete a Contact
// ***************************************************************************************
begsr pp_condel;

   clear condition;

   hfice = %subst(h_key:1:6);
   hseq# = %int(%subst(h_key:7:2));

   // Delete the DVINSTITF3 Record
   if not %open(dvinstitf3);
      open dvinstitf3;
   endif;

   chain (hfice:hseq#) contact;
   if %found(dvinstitf3);
      delete contact;
   endif;

endsr;

// ***************************************************************************************
// pp_conedt : Panel Processing to Edit a New Contact
// ***************************************************************************************
begsr pp_conedt;

   clear condition;

   // First and Last Name cannot be blank
   if hfrstname = *blanks or hlastname = *blanks;
      condition = 'parm-bad';
      ei += 1;
      errs(ei) = '#1591';
   endif;

   if haddr1 = *blanks;                                    // Address Line cannot be blank
      condition = 'parm-bad';
      ei += 1;
      errs(ei) = '#1596';
   endif;

   ccs_data = validST('US':hstate:fov:fov_fice);           // valid state
   if %subst(ccs_data:1:5) = 'BADSC';
      condition = 'parm-bad';
      ei += 1;
      errs(ei) = '#1592';
   endif;

   checkzip = validZip(hpostcd:'US');                      // valid zip code

   select;
   when %subst(checkzip:1:2) = 'BZ';
      condition = 'parm-bad';
      ei += 1;
      errs(ei) = '#1593';
   when %subst(checkzip:1:2) = 'OK';
      hpostcd = %subst(checkzip:3:13);
   endsl;

   if htel# <> *blanks;                                    // Valid telephone number
      @result = validTel(htel#:'US':'X');
      if @reslt_RC = 'BT';
         condition = 'parm-bad';
         ei += 1;
         errs(ei) = '#1594';
      else;
         htel# = @reslt_tel;
      endif;
   endif;

   if hemail <> *blanks;                                   // Valid email address
      clear byte2;
      if not valid_email(hemail:statusds) and not validMsg(hemail:husrtype);
         condition = 'parm-bad';
         ei += 1;
         errs(ei) = '#1595';
      endif;
   endif;

   if condition = *blanks;                                 // Check validity of the address
      clear #AV_dqin;
      clear #AV_dqout;

      #AV_func = 'AV';
      #AV_case = ' ';
      #AV_adrl = '35';
      #AV_adr1 = haddr1;
      #AV_city = hcity;
      #AV_stat = hstate;
      #AV_zipc = hpostcd;
      #AV_zip4 = %subst(hpostcd:7:4);

      exsr $get_AV;

      if #AV_status <> 'E';
         haddr1 = #av_adr2_o;
         hpostcd = #AV_zipc_o;
         if #AV_zip4_o <> *blanks;
            hpostcd = %trim(hpostcd) + '-' + #AV_zip4_o;
         endif;
      else;
         // Set error that address is not in postal system
         condition = 'INV ADDRES';
         ei += 1;
         errs(ei) = 'INVALID ADDRESS: ' + #AV_emsg_o;
      endif;
   endif;

endsr;

// ***************************************************************************************
// pp_conupd : Panel Processing to Update a Contact
// ***************************************************************************************
begsr pp_conupd;

   // Retrieve the resident data by key
   if not %open(dvinstitf3);
      open dvinstitf3;
   endif;

   hfice = %subst(h_key:1:6);
   hseq# = %int(%subst(h_key:7:2));

   chain (hfice:hseq#) contact;
   if %found(dvinstitf3);
      mrecord_id = husrtype;
      msalut = hsalut;
      mfrstname = hfrstname;
      mmidlname = hmidlname;
      mlastname = hlastname;
      mtitle = hnam_title;
      mnickname = hnickname;
      mcompany = hcompany;
      maddr1 = haddr1;
      maddr2 = haddr2;
      mcity = hcity;
      mstate = hstate;
      mpostcd = hpostcd;
      mcntry = hcntry;
      mtelnum = htel#;
      memail = hemail;
      mno_email = hno_email;
      mchgdate = cycle_date;
      mchguser = huserid;

      update contact;
   endif;

endsr;

// ***************************************************************************************
// pp_edt_csr: Edit the email addresses
//****************************************************************************************
begsr pp_edt_csr;

   if hemail <> *blanks;
      clear byte2;
      if not valid_email(hemail:statusds);
         ei += 1;
         errs(ei) = '#1280';
         condition = 'parm-bad';
      endif;
   endif;

   if hemail2 <> *blanks;
      clear byte2;
      if not valid_email(hemail2:statusds);
         ei += 1;
         errs(ei) = '#1280';
         condition = 'parm-bad';
      endif;
   endif;

   if %check('0123456789 ':hcs_rsnd_#) > 0 or %check('0123456789 ':hcs_rsnd_w) > 0;
      ei += 1;
      errs(ei) = 'Did not enter numeric data';
      condition = 'parm-bad';
      leavesr;
   else;
      zcs_rsnd_# = %int(%trim(hcs_rsnd_#));
      zcs_rsnd_w = %int(%trim(hcs_rsnd_w));
   endif;

   if zcs_rsnd_w <> 0 and zcs_rsnd_w >= zcs_rsnd_#;
      ei += 1;
      errs(ei) = '#7511';
      condition = 'parm-bad';
   endif;

endsr;

// ***************************************************************************************
// setPanel: Set Panel based on the next screen
// ***************************************************************************************
begsr setPanel;

   select;
   when hscrn_next = 'CSR';
      panel = #DSP_CSR;

   when hscrn_next = 'DBS';
      panel = #DSP_BSC;

   when hscrn_next = 'DCE';
      panel = #CON_EDIT;
      hscrn_next = 'DCT';

   when hscrn_next = 'DCS';
      panel = #DSP_CCS;

   when hscrn_next = 'DCT';
      panel = #DSP_CNT;

   when hscrn_next = 'DGA';
      panel = #DSP_GA;

   when hscrn_next = 'DTP';
      panel = #DSP_TP;

   when hscrn_next = 'EDU';
      panel = #DSP_EDU;

   when hscrn_next = 'ESS';
      panel = #DSP_ESS;

   when hscrn_next = 'LOC';
      panel = #DSP_LOC;

   when hscrn_next = 'MNT';
      if happlid = 'TP' or happlid = 'D2' or happlid = 'DP';
         panel = #EDTMNT;
      endif;

   when hscrn_next = 'OFF';
      panel = '#LOGOFF';

   when hscrn_next = 'PDF';
      panel = #DSP_PDF;

   when hscrn_next = 'POP';
      panel = #POPUP;

   when hscrn_next = 'PRT';
      panel = #DSP_PRNT;

   endsl;

endsr;

// ***************************************************************************************
// upd_bsc: Update the Basic Options
//
//  This routine goes through a number of steps
//  1.)  Edit the H-fields, and make sure data contains no errors
//  2.)  Compare I-fields to H-fields, are any fields different
//  3.)  Move H-fields to I-fields and update record
// ***************************************************************************************
begsr upd_bsc;

   exsr edt_fdxrsh;
   if ei > 0;
      editMode = TRUE;
      leavesr;
   endif;

   exsr validPassLen;
   if ei > 0;
      editMode = TRUE;
      leavesr;
   endif;

   if hteam_id <> iteam_id or hficegroup <> ificegroup or hprtnr_req <> iprtnr_req or
      hcolor_pri <> icolor_pri or hcolor_sec <> icolor_sec or hcolor_txt <> icolor_txt or
      hcolor_tph <> icolor_tph or hcoloptpri <> icoloptpri or hcoloptsec <> icoloptsec or
      hs_act <> is_act or hs_atp <> is_atp or hs_ccd <> is_ccd or hs_ceebact <> is_ceebact or
      hs_esis <> is_esis or hs_liaison <> is_liaison or hs_cruz <> %char(icruz_code) or
      hchargecrz <> ichargecrz or (hpassmin <> ipassmin and %int(hpassmin) >= 8) or
      (hpassmax <> ipassmax and %int(hpassmax) <= 50) or hs_ipeds <> is_ipeds or
      hs_nchelp <> is_nchelp or hs_opeid <> is_opeid or hs_usis <> is_usis or hs_spdefic <> is_spdef
      zfdx_dtoff <> ifdx_dtoff or zfdx_tmoff <> ifdx_tmoff or zfdx_dton <> ifdx_dton or
      zfdx_tmon <> ifdx_tmon or zrsh_dtoff <> irsh_dtoff or zrsh_tmoff <> irsh_tmoff or
      zrsh_dton <> irsh_dton or zrsh_tmon <> irsh_tmon;

      chain (hfice) instrec;
      if %found(dvinstitf1);
         iteam_id = hteam_id;
         ificegroup = hficegroup;
         is_act = hs_act;
         is_atp = hs_atp;
         is_ccd = hs_ccd;
         is_ceebact = hs_ceebact;
         is_esis = hs_esis;
         is_liaison = hs_liaison;
         is_ipeds = hs_ipeds;
         is_nchelp = hs_nchelp;
         is_opeid = hs_opeid;
         is_usis = hs_usis;
         icruz_code = %int(hs_cruz);
         ichargecrz = hchargecrz;

         if %int(hpassmin) >= 8 and %int(hpassmin) <= 50;
            ipassmin = hpassmin;
         endif;

         if %int(hpassmax) <= 50 and %int(hpassmax) >= 10;
            ipassmax = hpassmax;
         endif;

         ifdx_dtoff = zfdx_dtoff;
         ifdx_dton = zfdx_dton;
         ifdx_tmoff = zfdx_tmoff;
         ifdx_tmon = zfdx_tmon;

         irsh_dtoff = %int(hrsh_dtoff);
         irsh_dton = %int(hrsh_dton);
         irsh_tmoff = %int(hrsh_tmoff);
         irsh_tmon = %int(hrsh_tmon);

         icolor_pri = %xlate(xlc:xuc:hcolor_pri);
         icolor_sec = %xlate(xlc:xuc:hcolor_sec);
         icolor_txt = %xlate(xlc:xuc:hcolor_txt);
         icolor_tph = %xlate(xlc:xuc:hcolor_tph);
         icoloptpri = hcoloptpri;
         icoloptsec = hcoloptsec;

         iprtnr_req = hprtnr_req;
         ichgdate = cycle_date;
         ichguser = huserid;

         update instrec;
      endif;
   endif;

endsr;

// ***************************************************************************************
// upd_csopts: Update the CICCSOPT1 database
//
// This routine goes through a number of steps
//  1.)  Edit the H-fields, and make sure data contains no errors
//  2.)  Compare CS-fields to H-fields, are any fields different
//  3.)  Move H-fields to CS-fields and update record
// ***************************************************************************************
begsr upd_csopts;

   if hcs_rsnd_c <> 'N' and hcs_rsnd_c <> ' ' and hcs_rsnd_c <> 'C' and
      (zcs_rsnd_# = 0 or zcs_rsnd_w = 0);

      ei += 1;
      errs(ei) = '#7501';
      leavesr;
   endif;

   if not %open(ciccsopt1);
      open ciccsopt1;
   endif;

   chain hfice ccsopt_rec;
   // Check if a H-fields have changed from file values.
   if %found(ciccsopt1);
      if zcs_rsnd_# <> cs_rsnd_# or zcs_rsnd_w <> cs_rsnd_w or hcs_rsnd_c  <> cs_rsnd_c or
         h_aac <> cs_adrchg or h_cnr <> cs_norcpt or hemail <> cs_reseml or hemail2 <> cs_reseml2;

         cs_rsnd_c = hcs_rsnd_c;
         cs_rsnd_w = zcs_rsnd_w;
         cs_rsnd_# = zcs_rsnd_#;
         cs_adrchg = h_aac;
         cs_norcpt = h_cnr;
         cs_reseml = hemail;
         cs_reseml2 = hemail2;

         if cs_rsnd_c = 'N';
            cs_rsnd_w = 0;
            cs_rsnd_# = 0;
            cs_adrchg = ' ';
            cs_norcpt = ' ';
            ei += 1;
            errs(ei) = '#7509';
         elseif cs_rsnd_c = ' ';
            cs_rsnd_w = 0;
            cs_rsnd_# = 0;
            cs_adrchg = ' ';
            cs_norcpt = ' ';
            ei += 1;
            errs(ei) = '#7529';
         elseif cs_rsnd_c = 'C';
            // Must set both if one is non-zero
            if (cs_rsnd_w = 0 and cs_rsnd_# > 0) or (cs_rsnd_w > 0 and cs_rsnd_# = 0);
               cs_rsnd_w = 0;
               cs_rsnd_# = 0;
               ei += 1;
               errs(ei) = '#7530';
            endif;
         endif;

         update ccsopt_rec;
         editMode = FALSE;
      else;
         unlock ciccsopt1;
      endif;
   else;
      cs_fice = hfice;
      cs_rsnd_c = hcs_rsnd_c;
      cs_rsnd_w = zcs_rsnd_w;
      cs_rsnd_# = zcs_rsnd_#;
      cs_adrchg = h_aac;
      cs_norcpt = h_cnr;
      cs_reseml = hemail;
      cs_reseml2 = hemail2;

      write ccsopt_rec;
   endif;

endsr;

// ***************************************************************************************
// upd_ga: Update the GA Options
//
//  This routine goes through a number of steps
//  1.)  Edit the H-fields, and make sure data contains no errors
//  2.)  Compare I-fields to H-fields, are any fields different
//  3.)  Move H-fields to I-fields and update record
// ***************************************************************************************
begsr upd_ga;

   if hedi_v_deg <> iedi_v_deg;
      chain (hfice) instrec;
      if %found(dvinstitf1);
         iedi_v_deg = hedi_v_deg;
         ichgdate = cycle_date;
         ichguser = huserid;
         update instrec;
      endif;
   endif;

endsr;

// ***************************************************************************************
// upd_prt: Update the PRT Options
//
//  This routine goes through a number of steps
//  1.)  Edit the H-fields, and make sure data contains no errors
//  2.)  Compare I-fields to H-fields, are any fields different
//  3.)  Move H-fields to I-fields and update record
// ***************************************************************************************
begsr upd_prt;

   setOppsite = ' ';
   het_senda = iet_senda;

   select;
   when (htp#_toprt <> 'ALL' and %check('0123456789':%trim(htp#_toprt)) > 0) or htp#_toprt = *blanks
      ei += 1;
      errs(ei) = '#7519';

   when htp#_toprt = 'ALL';
      if ichargetm = 'Y';
         if %lookup('PC':har_etsend) = 0;
            ei += 1;
            errs(ei) = '#7520';
         endif;
      else;
         ei += 1;
         errs(ei) = '#7521';
      endif;

   when %len(%trim(htp#_toprt)) > 2;
      ei += 1;
      errs(ei) = '#7522';
   endsl;

   if hprint_ab = 'Y' and iairbills <> 'F';
      ei += 1;
      errs(ei) = '#7516';
   endif;

   if hcover_tel <> *blanks;                               // Valid telephone number
      @result = validTel(hcover_tel:'US':'X');
      if @reslt_RC = 'BT';
         condition = 'parm-bad';
         ei += 1;
         errs(ei) = '#7523';
      else;
         hcover_tel = @reslt_tel;
      endif;
   endif;

   if hcover_msg <> *blanks and hcover_msg <> 'Y';
      ei += 1;
      errs(ei) = 'Cover Page Message must be "YES" or "NO"';
   endif;

   if ei > 0;
      editMode = TRUE;
      leavesr;
   endif;

   if htp#_toprt <> 'ALL';
      ztp#_toprt = %int(%trim(htp#_toprt));
   else;
      ztp#_toprt = 99;
   endif;

   if herm_paper <> ierm_paper;
      ci += 1;
      conf(ci) = 'Print Batch paper indicator UPDATED';
   endif;

   if hcredp_onl <> icredp_onl;
      ci += 1;
      conf(ci) = 'Online Print Code UPDATED';
   endif;

   if ztp#_toprt <> itp#_toprt;
      ci += 1;
      conf(ci) = 'Convert Completed Transcripts UPDATED';
      select;
      when ztp#_toprt = 99;                                // No need to set the "XX" fice
         setOppsite = ' ';
      when ichargetm = 'Y';                                // Set test fice to a "+" number
         setOppsite = '+';
         wrk_fice = getTestFice(ifice);
      other;                                               // Set live fice to a "-" number
         setOppsite = '-';
         wrk_fice = getLiveFice(ifice);
      endsl;
   endif;
   if hprint_ab <> iprint_ab;
      ci += 1;
      conf(ci) = 'Print Airbills UPDATED';
   endif;
   if hprint_att <> iprint_att;
      ci += 1;
      conf(ci) = 'Print Attachments UPDATED';
   endif;
   if htp_reml_c <> itp_reml_c;
      ci += 1;
      conf(ci) = 'Remail Option UPDATED';
   endif;
   if hcover_tel <> icover_tel;
      ci += 1;
      conf(ci) = 'Cover Page Phone # UPDATED';
   endif;
   if hcover_msg <> icover_msg;
      ci += 1;
      conf(ci) = 'Cover Page Message UPDATED';
   endif;

   if ci > 0;
      if setOppsite <> ' ';
         chain (wrk_fice) instrec;
         if %found(dvinstitf1);
            if itp#_toprt = 99;
               unlock dvinstitf1;
            else;
               if setOppsite = '+';
                  itp#_toprt = %abs(ztp#_toprt);
               else;
                  itp#_toprt = ztp#_toprt * -1;
               endif;
               ichgdate = cycle_date;
               ichguser = huserid;

               update instrec;
            endif;
         endif;
      endif;

      chain (hfice) instrec;
      if %found(dvinstitf1);
         ierm_paper = herm_paper;
         icredp_onl = hcredp_onl;
         itp#_toprt = ztp#_toprt;
         if setOppsite = '+';
            itp#_toprt = ztp#_toprt * -1;
         else;
            itp#_toprt = %abs(ztp#_toprt);
         endif;
         iprint_ab = hprint_ab;
         iprint_att = hprint_att;
         itp_reml_c = htp_reml_c;
         icover_tel = hcover_tel;
         icover_msg = hcover_msg;
         ichgdate = cycle_date;
         ichguser = huserid;

         update instrec;
      endif;

   else;
      ei += 1;
      errs(ei) = '#7517';
      clear ci;
      clear conf;
   endif;

endsr;

// ***************************************************************************************
// upd_tp: Update the TP Options
//
//  This routine goes through a number of steps
//  1.)  Edit the H-fields, and make sure data contains no errors
//  2.)  Compare I-fields to H-fields, are any fields different
//  3.)  Move H-fields to I-fields and update record
// ***************************************************************************************
begsr upd_tp;

   exsr edt_tp;                                            // Edit basic tp fields
   exsr edt_tp_num;                                        // Edit tp numeric fields

   if ei > 0;                                              // Do no updates if invalid data
      leavesr;
   endif;

   // Check if a H-fields have changed from file values.
   if zssn_len   <> issn_len   or
      hssn_cntrl <> issn_cntrl or
      hssn_iptyp <> issn_iptyp or
      hedt_t_sid <> iedt_t_sid or
      hsid_fmt   <> isid_fmt   or
      hsid_char1 <> isid_char1 or
      hsid_len   <> istuid_len or
      zsid_shaln <> isid_shaln or
      hsha_methd <> isha_methd or
      hdis_dob   <> idis_dob   or
      hdis_nam   <> idis_nam   or
      hdis_sid   <> idis_sid   or
      hdis_ssn   <> idis_ssn   or
      het_senda  <> iet_senda  or
      hno_phone  <> ino_phone  or
      hprohtrans <> iprohtrans or
      hforce_ets <> iforce_ets or
      hforce_pdf <> iforce_pdf or
      htm_attctl <> itm_attctl or
      halwslfatt <> ialwslfatt or
      halw_punam <> ialw_punam or
      htm_attfrc <> itm_attfrc or
      htm_slffrc <> itm_slffrc or
      htm_1_bas  <> itm_1_bas  or
      hdo_ttypes <> ido_ttypes or
      htm_dftbas <> itm_dftbas or
      htm_dfttty <> itm_dfttty or
      htm_dfthld <> itm_dfthld or
      htm_dftxtr <> itm_dftxtr or
      htm_dftshp <> itm_dftshp or
      hro_ereset <> iro_ereset or
      htp_resend <> itp_resend or
      hrules_sig <> irules_sig or
      hdoes_edi  <> idoes_edi  or
      zrobomaint <> irobomaint or
      zet_ibp_rt <> iet_ibp_rt or
      zet_ibf_rt <> iet_ibf_rt or
      zmemoa_rat <> imemoa_rat or
      zmemod_rat <> imemod_rat or
      zmemoe_rat <> imemoe_rat or
      zmemom_rat <> imemom_rat or
      zmemod_avw <> imemod_avw or
      zmemo_brib <> imemo_brib or
      zet_minchg <> iet_minchg or
      zdisc_pdf  <> idisc_pdf  or
      zdisc_pdf  <> idisc_pdf  or
      zdisc_3pdf <> idisc_3pdf or
      zdisc_elec <> idisc_elec or
      zdisc_prsh <> idisc_prsh or
      zdisc_3rsh <> idisc_3rsh or
      zdisc_ersh <> idisc_ersh or
      hcunyctl   <> icunyctl   or
      hgenedreq1 <> igenedreq1 or
      hgenedreq2 <> igenedreq2 or
      hgenedreq3 <> igenedreq3 or
      htp_opsdly <> itp_opsdly or
      hschmsgctl <> ischmsgctl or
      hnoreason  <> inoreason  or
      htb_noothr <> itb_noothr or
      htp_on_tp2 <> itp_on_tp2 or
      htp_svycod <> itp_svycod or
      htp_svyurl <> itp_svyurl or
      hpdfuplmod <> ipdfuplmod or
      hprtuplmod <> iprtuplmod or
      hvrfy_outb <> ivrfy_outb or
      htm_kiourl <> itm_kiourl or
      zkiosk_ip# <> ikiosk_ip# or
      hregistrar <> iregistrar or
      hlink_3pdf <> ilink_3pdf or
      henty_fice <> ienty_fice or
      hmouse_sig <> imouse_sig or
      hrobo_cycl <> irobo_cycl or
      hrobo_cycm <> irobo_cycm or
      hrobo_mntc <> irobo_mntc or
      hpdf3_all  <> ipdf3_all  or
      hpdfscrty  <> isigner    or
      htp_supcty <> itp_supcty or
      hatt_gened <> iatt_gened or
      htm_year_q <> itm_year_q;

      chain (hfice) instrec;
      if not %found(dvinstitf1);
         leavesr;
      endif;

      // Move the H-fields from screen to record

      // NO ONE IS TO CHANGE NEXT 6 LINES WITHOUT PRIOR AUTHORIZATION FROM JJG
      if huserid <> 'JJGCCS' and huserid <> 'WGGCCS';
         if hssn_cntrl = 'F';
            hssn_cntrl = issn_cntrl;
         endif;
      endif;

      issn_cntrl = hssn_cntrl;
      issn_len = zssn_len;
      issn_iptyp = hssn_iptyp;
      iedt_t_sid = hedt_t_sid;
      isid_fmt = hsid_fmt;
      isid_char1 = hsid_char1;
      istuid_len = hsid_len;
      isid_shaln = zsid_shaln;
      isha_methd = hsha_methd;
      idis_dob = hdis_dob;
      idis_nam = hdis_nam;
      idis_sid = hdis_sid;
      idis_ssn = hdis_ssn;
      iet_senda = het_senda;
      ino_phone = hno_phone;
      iprohtrans = hprohtrans;
      iforce_ets = hforce_ets;
      iforce_pdf = hforce_pdf;
      ipdfuplmod = hpdfuplmod;
      iprtuplmod = hprtuplmod;
      ivrfy_outb = hvrfy_outb;
      itm_attctl = htm_attctl;
      ialwslfatt = halwslfatt;
      ialw_punam = halw_punam;
      itm_attfrc = htm_attfrc;
      itm_slffrc = htm_slffrc;
      itm_1_bas  = htm_1_bas;
      ido_ttypes = hdo_ttypes;
      itm_dftbas = htm_dftbas;
      itm_dfttty = htm_dfttty;
      itm_dfthld = htm_dfthld;
      itm_dftxtr = htm_dftxtr;
      itm_dftshp = htm_dftshp;
      iro_ereset = hro_ereset;
      itp_resend = htp_resend;
      irules_sig = hrules_sig;
      idoes_edi  = hdoes_edi;
      irobomaint = zrobomaint;
      irobo_cycl = hrobo_cycl;
      irobo_cycm = hrobo_cycm;
      irobo_mntc = hrobo_mntc;
      iet_ibp_rt = zet_ibp_rt;
      iet_ibf_rt = zet_ibf_rt;
      imemoa_rat = zmemoa_rat;
      imemod_rat = zmemod_rat;
      imemoe_rat = zmemoe_rat;
      imemom_rat = zmemom_rat;
      imemod_avw = zmemod_avw;
      imemo_brib = zmemo_brib;
      iet_minchg = zet_minchg;
      idisc_pdf  = zdisc_pdf;
      idisc_3pdf = zdisc_3pdf;
      idisc_elec = zdisc_elec;
      idisc_prsh = zdisc_prsh;
      idisc_3rsh = zdisc_3rsh;
      idisc_ersh = zdisc_ersh;
      icunyctl = hcunyctl;
      igenedreq1 = hgenedreq1;
      igenedreq2 = hgenedreq2;
      igenedreq3 = hgenedreq3;
      itp_opsdly = htp_opsdly;
      ischmsgctl = hschmsgctl;
      itp_svycod = htp_svycod;
      inoreason = hnoreason;
      itb_noothr = htb_noothr;
      itp_svyurl = htp_svyurl;
      itm_kiourl = htm_kiourl;
      ikiosk_ip# = zkiosk_ip#;
      iregistrar = hregistrar;
      ilink_3pdf = hlink_3pdf;
      ienty_fice = henty_fice;
      itp_on_tp2 = htp_on_tp2;
      imouse_sig = hmouse_sig;
      ipdf3_all = hpdf3_all;
      isigner = hpdfscrty;
      itp_supcty = htp_supcty;
      itm_year_q = htm_year_q;
      iatt_gened = hatt_gened;

      if hfice <> '009998' and hfice <> 'T09998' and hfice <> 'SALES1' and %subst(hfice:1:1) <> 'X';
         for a1=1 to %elem(har_etsend);
            if het_senda = *blanks;
               ilive_dir = *blanks;
               ilive_edi = 0;
               ilive_xml = 0;
               ilive_spdf = 0;
               ilive_3pdf = 0;
               ilive_asci = 0;
               leave;
            endif;
            if har_etsend(a1) = *blanks;
               leave;
            endif;

            select;
            when har_etsend(a1) = 'XO' and ilive_xml = 0;
               ilive_xml = cycle_date;
               havexml = TRUE;
            when har_etsend(a1) = 'XO' and ilive_xml <> 0;
               havexml = TRUE;
            when %subst(har_etsend(a1):1:1) = 'E' and ilive_edi = 0;
               ilive_edi = cycle_date;
               haveedi = TRUE;
            when %subst(har_etsend(a1):1:1) = 'E' and ilive_edi <> 0;
               haveedi = TRUE;
            when har_etsend(a1) = 'TX' and ilive_asci = 0;
               ilive_asci = cycle_date;
               haveasci = TRUE;
            when har_etsend(a1) = 'TX' and ilive_asci <> 0;
               haveasci = TRUE;
            when (har_etsend(a1) = 'DU' or har_etsend(a1) = 'FU') and ilive_dir = *blanks;
               ilive_dir = 'CALL';
               havedir = TRUE;
            when (har_etsend(a1) = 'DU' or har_etsend(a1) = 'FU') and ilive_dir <> *blanks;
               havedir = TRUE;
            when har_etsend(a1) = 'AL' and ilive_spdf = 0;
               ilive_spdf = cycle_date;
               havespdf = TRUE;
            when har_etsend(a1) = 'AL' and ilive_spdf <> 0;
               havespdf = TRUE;
            when har_etsend(a1) = 'AC' and ilive_spdf = 0;
               ilive_spdf = cycle_date;
               havespdf = TRUE;
            when har_etsend(a1) = 'AC' and ilive_spdf <> 0;
               havespdf = TRUE;
            when har_etsend(a1) = 'AE' and ilive_3pdf = 0;
               ilive_3pdf = cycle_date;
               have3pdf = TRUE;
            when har_etsend(a1) = 'AE' and ilive_3pdf <> 0;
               have3pdf = TRUE;
            when har_etsend(a1) = 'PC' and ilive_erm = 0;
               ilive_erm = cycle_date;
               haveerm = TRUE;
            when har_etsend(a1) = 'PC' and ilive_erm <> 0;
               haveerm = TRUE;
            endsl;
         endfor;
      endif;

      // Set ilive codes to 0/blanks if flag is false
      if havexml = FALSE;
         ilive_xml = 0;
      endif;
      if haveedi = FALSE;
         ilive_edi = 0;
      endif;
      if havedir = FALSE;
         ilive_dir = *blanks;
      endif;
      if havespdf = FALSE;
         ilive_spdf = 0;
      endif;
      if have3pdf = FALSE;
         ilive_3pdf = 0;
      endif;
      if haveasci = FALSE;
         ilive_asci = 0;
      endif;
      if haveerm = FALSE;
         ilive_erm = 0;
      endif;

      ichgdate = cycle_date;
      ichguser = huserid;
      update instrec;

   endif;

endsr;

// ***************************************************************************************
// validPassLen: Validate the length of the min and max of a password
// ***************************************************************************************
begsr validPassLen;

   if %check('0123456789':%trim(hpassmax)) > 0;
      ei +=1;
      errs(ei) = 'Only numbers are expected as a Max Password';
      hpassmax = '50';

   elseif %int(hpassmax) < 10 or %int(hpassmax) > 50;
      ei +=1;
      errs(ei) = 'Cannot have a max lower than 10 or higher than 50';
      hpassmax = '50';
   endif;

   if %check('0123456789':%trim(hpassmin)) > 0;
      ei +=1;
      errs(ei) = 'Only numbers are expected as a Min Password';
      hpassmin = '08';
   elseif %int(hpassmin) < 8 or %int(hpassmin) > 50;
      ei +=1;
      errs(ei) = 'Cannot have a min lower than 8 or higher than 50';
      hpassmin = '08';
   endif;

endsr;

// ***************************************************************************************
// validateBillMonths: Routine to validate robo bill months
// ***************************************************************************************
begsr validateBillMonths;

   monthInvalid = FALSE;
   monthSize = %len(%trim(hrobo_cycm));

   select;
   when hrobo_cycl = 'M';
      hrobo_cycm = *blanks;
      loopIdx = 0;

   when hrobo_cycl = 'A';
      if monthSize = 2;
         loopIdx = 1;
      else;
         monthInvalid = TRUE;
         leavesr;
      endif;

   when hrobo_cycl = 'S';
      if monthSize = 4;
         loopIdx = 2;
      else;
         monthInvalid  = TRUE;
         leavesr;
      endif;

   when hrobo_cycl = 'Q';
      if monthSize = 8;
         loopIdx = 4;
      else;
         monthInvalid  = TRUE;
         leavesr;
      endif;

   other;
      monthInvalid = TRUE;
      leavesr;
   endsl;

   if loopIdx > 0;
      if hrobo_cycm = *blanks;
         monthInvalid  = TRUE;
         leavesr;
      elseif %check('0123456789':%trim(hrobo_cycm)) > 0;
         monthInvalid  = TRUE;
         leavesr;
      endif;

      for idx = 1 to loopIdx;
         if har_robocm(idx) < '01' or har_robocm(idx) > '12' or har_robocm(idx) = *blanks;
            monthInvalid  = TRUE;
            leavesr;
         endif;
      endfor;
   endif;

endsr;

// ***************************************************************************************
// checkGaProduct: Check to see if the GA product is avalable and sets go_livedt
// ***************************************************************************************
dcl-proc checkGaProduct;
   dcl-pi *n ind;
      $applid like(h_applid);
      $productList likeds(productList);
      @go_livedt like(go_livedt);
   end-pi;

   select;
   when $applid = 'PP' and ($productList.hasPP or (ifice = 'XPHONE'));
      go_livedt = $productList.ppLiveDate;
      return TRUE;

   when $applid = 'CE' and $productList.hasCE;
      go_livedt = $productList.ceLiveDate;
      return TRUE;

   when $applid = 'DP' and ($productList.hasDP or (ifice = 'XPHONE' or ifice = '000000'));
      go_livedt = $productList.dpLiveDate;
      return TRUE;

   other;
      clear glive_appl;
      return FALSE;
   endsl;

end-proc;

// ***************************************************************************************
// checkFile: Check if a File exists
// ***************************************************************************************
dcl-proc checkFile;
   dcl-pi *n ind;
      $fice char(6) const;
      $filePath like(imageFile) const;
      $imgType char(1) const;
      $turnedOff char(1) const;
      @message like(errs);
   end-pi;

   clear @message;
   clear #M2_dqin;
   #M2_func = 'EX';
   #M2_fice = $fice;
   #M2_filenm = '/CIPGM/PDF_IMAGES/' + %trim($filePath);
   exsr $get_M2;

   // File found
   if #M2_status = 'OK';
      // Option turned off, so error to screen
      if ($imgType = 'A' or $imgType = 'P') and $turnedoff = 'Y';
         @message = %trim($filePath);
         return FALSE;
      // else this is good
      else;
         @message = %trim($filePath);
         return TRUE;
      endif;

   // File not found
   else;
      // If option turned off, this is okay that it wasn't found
      if ($imgType = 'A' or $imgType = 'P') and $turnedoff = 'Y';
         @message = %trim($filePath) + ' turned off';
         return TRUE;

      // error to screen that file wasn't found
      else;
         @message = %trim($filePath) + ' NOT loaded';
         return FALSE;
      endif;
   endif;

/copy rpgcopy,$srvrm2_sr
end-proc;

// ***************************************************************************************
// findHtml: Find and sanitize anything that resembles html
// ***************************************************************************************
dcl-proc findHtml;
   dcl-pi *n like(htext) rtnparm;
      $text like(htext) const;
      @msgStatusDs likeds(statusDs);
   end-pi;

   dcl-s p3 packed(3) template;

   dcl-s startTagPos like(p3) inz;
   dcl-s killLoop like(p3) inz;
   dcl-s endTagPos like(p3) inz;
   dcl-s endTagLen like(p3) inz;
   dcl-s tagLen like(p3) inz;

   dcl-s endTag char(12);
   dcl-s foundHtml ind;
   dcl-s returnText like(htext);
   dcl-s sourceString like(htext);
   dcl-s workText like(htext);
   dcl-s foundTag char(8);

   dcl-c FALSE '0';
   dcl-c TRUE '1';

   foundHtml = TRUE;

   startTagPos = 1;
   killLoop = 0;

   returnText = $text;
   workText = %xlate(xlc:xuc:$text);

   dow foundHtml = TRUE;
      killLoop += 1;
      if killLoop >= 100;
         leave;
      endif;

      startTagPos = %scan('<':workText:startTagPos);
      if startTagPos = 0;
         leave;
      endif;

      foundTag = %subst(workText:startTagPos+1:8);
      select;
      when foundTag = 'TEXTAREA';
         endTag = '</TEXTAREA>';
      when %subst(foundTag:1:6) = 'SCRIPT';
         endTag = '</SCRIPT>';
      when %subst(foundTag:1:5) = 'STYLE';
         endTag = '</STYLE>';
      when %subst(foundTag:1:4) = 'FORM';
         endTag = '</FORM>';
      when %check(XUC:%subst(foundTag:1:1)) = 0 or %subst(foundTag:1:1) = '/';
         endTag = '>';
      other;
         startTagPos += 1;
         iter;
      endsl;

      endTagLen = %len(%trim(endTag));

      endTagPos = %scan(%trim(endTag):workText:startTagPos);
      if endTagPos = 0;
         if endTag = '>';
            leave;
         endif;
         endTagPos = %scan('>':workText:startTagPos);
         if endTagPos = 0;
            leave;
         endif;
         endTagLen = 1;
      endif;

      tagLen = (endTagPos+endTagLen) - startTagPos;

      sourceString = %subst(returnText:startTagPos:tagLen);

      if sourceString = '<BR>' or sourceString = '<BR/>' or sourceString = '<BR />';
         startTagPos += 1;
         iter;
      endif;

      @msgStatusDs.code = ERROR;

      returnText = %scanrpl(%trim(sourceString):'':returnText);
      sourceString = %xlate(xlc:xuc:sourceString);
      workText = %scanrpl(%trim(sourceString):'':workText);

   enddo;

   return returnText;
end-proc;

// ***************************************************************************************
// get_csopt: Get the CICCSOPT1 Database Record
// ***************************************************************************************
dcl-proc get_csopt;
   dcl-pi *n;
   end-pi;

   if not %open(ciccsopt1);
      open ciccsopt1;
   endif;

   chain(n) hfice ccsopt_rec;
   if %found(ciccsopt1);
      hcs_rsnd_c = cs_rsnd_c;
      hcs_rsnd_w = %char(cs_rsnd_w);
      hcs_rsnd_# = %char(cs_rsnd_#);
      h_aac = cs_adrchg;
      h_cnr = cs_norcpt;
      hemail = cs_reseml;
      hemail2 = cs_reseml2;
   endif;

   htp_rsnd_# = %char(itp_rsnd_#);
   htp_rsnd_w = %char(itp_rsnd_w);

end-proc;

// ***************************************************************************************
// get_cntct: Get the Contact Database Record
// ***************************************************************************************
dcl-proc get_cntct;
   dcl-pi *n;
   end-pi;

   if not %open(dvinstitl4);
      open dvinstitl4;
   endif;

   select;
   when fileAccess = 'CHAIN';
      clear schfax_num;
      clear schcnt_nam;
      clear schcnt_tel;
      clear schcnt_eml;

      chain (hfice:krec_id) cntct_l4;
      if not %found(dvinstitl4);
         institl4Found = FALSE;
         schfax_num = admin_fax;
         schcnt_nam = 'N/A';
         schcnt_tel = 'N/A';
         schcnt_eml = 'N/A';
         return;
      else;
         institl4Found = TRUE;
      endif;

      schfax_num = mtelnum;
      schcnt_nam = %trim(mfrstname) + ' ' + %trim(mlastname);

      if mtelextn <> *blanks;
         schcnt_tel = %trim(mtelnum) + ' X' + %trim(mtelextn);
      else;
         schcnt_tel = %trim(mtelnum);
      endif;

      schcnt_eml = memail;
   endsl;

end-proc;

// ***************************************************************************************
// getVarValues(): Process html 'VAR', 'PANEL', 'MSG' , 'SELECTED' variables
// ***************************************************************************************
dcl-proc getVarValues;
   dcl-pi *n  like(#wp_out.result);
      varType like(HTML_VAR) const;
      varName like(HTML_PARM) dim(HTML_PARM_DIM) const options(*nopass);
   end-pi;

   // Variables
   dcl-s returnVal like(#wp_out.result);
   dcl-s exists char(1) inz;

   dcl-s variableNonVarChar like(HTML_PARM) inz;
   dcl-s panelscriptFile like(panelFile);
   dcl-s panelstyleFile like(panelFile);

   clear returnVal;

   variableNonVarChar = %trim(varName(1));

   select;

   when varType = 'PANEL';
      if varName(1) = 'SCRIPT';
         panelscriptFile = %scanrpl('.html':'.js':panel);

         exists_ifs(rootfilepath + %trim(panelscriptfile):exists);
         if exists = TRUE;
            web_processFile(%trim(rootFilePath):%trim(panelscriptFile):%paddr('GETVARVALUES'):
                            %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
         endif;

      elseif varName(1) = 'STYLE';
         panelstyleFile = %scanrpl('.html':'.css':panel);

         exists_ifs(rootfilepath + %trim(panelstyleFile):exists);
         if exists = TRUE;
            web_processFile(%trim(rootFilePath):%trim(panelstyleFile):%paddr('GETVARVALUES'):
                            %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
         endif;

      else;
         if panel <> *blanks;
            // if client accepts json, change panelFile to json suffix        //SG01
            if httpAccept = 'json';                                           //SG01
               panel = setPanelToJSON(panel:httpAccept);                      //SG01
            endif;                                                            //SG01
            web_processFile(%trim(rootFilePath):%trim(panel):%paddr('GETVARVALUES'):
                            %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
         endif;
      endif;


      return returnVal;

   when varType = 'MSG';
      select;
      when varName(1) = 'INFO';
         if fi > 0;
            for loopidx = 1 to fi;
               returnVal = %trim(returnVal) + %trim(info(loopidx)) + BREAK;
            endfor;
         else;
            clear returnVal;
         endif;

      when varName(1) = 'WARNING';
         if wrIdx > 0;
            for loopidx = 1 to wrIdx;
               returnVal = %trim(returnVal) + %trim(warning(loopidx)) + BREAK;
            endfor;
         else;
            clear returnVal;
         endif;

      when varName(1) = 'CONF';
         if ci > 0;
            for loopidx = 1 to ci;
               errtext = conf(loopidx);
               select;
               when err_indic = '#';
                  returnVal = %trim(returnVal) + web_getMessage(msg_defalt:err_msg#:'CS') + BREAK;
               other;
                  returnVal = %trim(returnVal) + %trim(conf(loopidx)) + BREAK;
               endsl;
            endfor;
         else;
            clear returnVal;
         endif;

      when varName(1) = 'ERROR';
         if ei > 0;
            for loopidx = 1 to ei;
               errtext = errs(loopidx);
               if err_indic = '#';
                  returnVal = %trim(returnVal) + web_getMessage(msg_defalt:err_msg#:'CS') + BREAK;
               else;
                  returnVal = %trim(returnVal) + %trim(errs(loopidx)) + BREAK;
               endif;
            endfor;
         else;
            clear returnVal;
         endif;

      other;
         returnVal = getMessage(msg_defalt:varName(1):varName(2):varName(3));
      endsl;

      return %trim(returnval);

   when varType = 'VAR';
      select;

      //----------------------------------------------------------------
      // Hidden Header Variables

      when varName(1) = 'FICE';
         return hfice;

      when varName(1) = 'FORMID';
         return hscrn_next;

      when varName(1) = 'APPLID';
         return %trim(happlid);

      when varName(1) = 'ACTION';
         return h_action;

      when varName(1) = 'SIGNONKEY';
         return %trim(hsignonkey);

      when varName(1) = 'USERID';
         return huserid;

      when varName(1) = 'COPYYEAR';
         return %trim(%subst(%char(cycle_date):1:4));

      when varName(1) = 'SCHOOL';
         return %trim(yschname);

      when varName(1) = 'APPLNAME';
         return %trim(formAction);

      when varName(1) = 'CLIENTMANAGER';                   // Insert Team Leader ID
         return %trim(iteam_id);

      when varName(1) = 'PHNUSER';
         return %xlate(' ':'*':huserid);

      when varName(1) = 'PHNAPPLID';
         return phnapplid;

      //----------------------------------------------------------------
      // Basic School Information Panel

      when varName(1) = 'PRIMARYCOLOR';                    // School Primary Colour
         return %trim(icolor_pri);

      when varName(1) = 'SECONDARYCOLOR';                  // School Secondary Colour
         select;
         when hcoloptpri = 'W';
            return 'color:#fff';
         when hcoloptpri = 'B';
            return 'color:#000';
         when hcoloptpri = 'S';
            return 'color:' + %trim(icolor_sec);
         other;
            return 'color:#fff';
         endsl;

      when varName(1) = 'MNTSEQ';
         return %trim(hmnt_seq);

      when varName(1) = 'MNTGRP';
         return %trim(hmnt_grp);

      when varName(1) = 'KEY';
         return %trim(h_key);

      when varName(1) = 'FORMATCD';
         return %trim(hformatcd);

      when varName(1) = 'TPORIENT';
         return %trim(htp_orient);

      when varName(1) = 'LOCATIONCD';
         return %trim(hlocationCD);

      when varName(1) = 'HASMULTI';
         return %trim(hhas_multi);

      when varName(1) = 'SCHOOLWEBLINK';
         return %trim(ilinkhome);

      when varName(1) = 'SCHOOLIMGLINK';
         if ifice = '000000' or ilinkimag = *blanks or %subst(ilinkimag:1:16) = '/icon_sch/demos/';
            ilinkimag = '/CIimages/CSemail.gif';
            ilinkhome = 'https://www.credentials-inc.com';
         endif;
         return %trim(ilinkimag);

      when varName(1) = 'IFICE';
         return %trim(ifice);

      when varName(1) = 'SPEEDEFICE';
         return %trim(hs_spdefic);

      when varName(1) = 'CEEBCODE';
         return %trim(hs_ceebact);

      when varName(1) = 'IPEDSCODE';
         return %trim(hs_ipeds);

      when varName(1) = 'LIAISONCODE';
         return %trim(hs_liaison);

      when varName(1) = 'ACLGETESTCODE';
         return %trim(hs_act);

      when varName(1) = 'ADMISSONTESTCODE';
         return %trim(hs_atp);

      when varName(1) = 'COMMOMCORECODE';
         return %trim(hs_ccd);

      when varName(1) = 'S_ESISCODE';
         return %trim(hs_esis);

      when varName(1) = 'S_NCHELPCODE';
         return %trim(hs_nchelp);

      when varName(1) = 'S_OPEIDCODE';
         return %trim(hs_opeid);

      when varName(1) = 'S_USISCODE';
         return %trim(hs_usis);

      when varName(1) = 'CARRIERTESTCRUZ';
         return %trim(hchargecrz);

      when varName(1) = 'CARRIERCRUZ';
         return %trim(hs_cruz);

      when varName(1) = 'FEDEXDTOFF';
         return %trim(hfdx_dtoff);

      when varName(1) = 'FEDEXTMOFF';
         return %trim(hfdx_tmoff);

      when varName(1) = 'FEDEXDTON';
         return %trim(hfdx_dton);

      when varName(1) = 'FEDEXTMON';
         return %trim(hfdx_tmon);

      when varName(1) = 'RUSHDTOFF';
         return %trim(hrsh_dtoff);

      when varName(1) = 'RUSHTMOFF';
         return %trim(hrsh_tmoff);

      when varName(1) = 'RUSHDTON';
         return %trim(hrsh_dton);

      when varName(1) = 'RUSHTMON';
         return %trim(hrsh_tmon);

      when varName(1) = 'PASSWORDMIN';
         return hpassmin;

      when varName(1) = 'PASSWORDMAX';
         return hpassmax;

      when varName(1) = 'CRMID';
         return %trim(hteam_id);

      when varName(1) = 'FICEGROUP';
         return %trim(hficegroup);

      when varName(1) = 'COLOR_TPH';
         return %trim(hcolor_tph);

      when varName(1) = 'COLOR_TXT';
         return %trim(hcolor_txt);

      when varName(1) = 'COLOR_PRI';
         return %trim(hcolor_pri);

      when varName(1) = 'PRITXTCOL';
         select;
         when hcoloptpri = 'W';
            return 'color:#fff';
         when hcoloptpri = 'B';
            return 'color:#000';
         when hcoloptpri = 'S';
            return 'color:' + %trim(icolor_sec);
         other;
            return 'color:#fff';
         endsl;

      when varName(1) = 'COLOR_SEC';
         return %trim(hcolor_sec);

      when varName(1) = 'SECTXTCOL';
         select;
         when hcoloptsec = 'W';
            return 'color:#fff';
         when hcoloptsec = 'B';
            return 'color:#000';
         when hcoloptsec = 'P';
            return 'color:' + %trim(icolor_pri);
         other;
            return 'color:#fff';
         endsl;

      when varName(1) = 'SORTNAME';                        // Sort Name
         return %trim(hsortname);

      when varName(1) = 'SHORTNAME';                       // Short Name
         return %trim(hsch_sname);

      when varName(1) = 'SCHOOLNAME';                      // School Name
         return %trim(hschname);

      when varName(1) = 'SCHOOLADDR1';                     // School Address 1
         return %trim(haddr1);

      when varName(1) = 'SCHOOLADDR2';                     // School Address 2
         return %trim(haddr2);

      when varName(1) = 'SCHOOLCITY';                      // School City
         return %trim(hcity);

      when varName(1) = 'SCHOOLSTATE';                     // School State
         return %trim(hstate);

      when varName(1) = 'SCHOOLZIP';                       // School Zipcd
         return %trim(hpostcd);

      when varName(1) = 'SCHOOLCOUNTRY';                   // School Country
         return %trim(hcntry);

      when varName(1) = 'BACKOFFICESYS';                   // Back Office System
         return %trim(ibo_system);

      when varName(1) = 'TMSYEAR';                         // TMS year
         return %trim(itms_year);

      when varName(1) = 'ELECTRONICYEAR1';                 // Electronic first year
         return%trim(ifirstyear);

      when varName(1) = 'PDFYEAR1';                        // PDF first year
         return %trim(ipdf_1styr);

      when varName(1) = 'PARTNERREQ';                      // Partner Required
         select;
         when hprtnr_req = 'E';
            return 'Entity-based Accept All Option';
         when hprtnr_req = 'N';
            return 'Not Required';
         other;
            return 'Required';
         endsl;

      when varName(1) = 'MSGPREFIX';                       // MSG Prefix
         return %trim(imsgprefix);

      when varName(1) = 'THEFEATURE';                      // "The" feature
         return %trim(ithe_featr);

      when varName(1) = 'TIMEZONE';                        // School Time zone
         select;
         when itime_zone = 1;
            return 'Eastern (' + %char(itime_zone) + ')';
         when itime_zone = 0;
            return 'Central (' + %char(itime_zone) + ')';
         when itime_zone = -1;
            return 'Mountain (' + %char(itime_zone) + ')';
         when itime_zone = -2;
            return 'Pacific (' + %char(itime_zone) + ')';
         endsl;

      when varName(1) = 'FEDEXOFF';                        // FedEx Date/Time Off
         if zfdx_dtoff > 0 and zfdx_dtoff < 99999999;
            byte50 = %char(%date(zfdx_dtoff):*usa) + ' at';
            if zfdx_tmoff = 0;
               byte50 = %trim(byte50) + ' Midnight';
            else;
               byte6  = hfdx_tmoff + '00';
               byte50 = %trim(byte50) + ' ' + %char(%time(%int(byte6)):*usa);
            endif;
         else;
            byte50 = 'Values Not Set';
         endif;
         return %trim(byte50);

      when varName(1) = 'FEDEXON';                         // FedEx Date/Time On
         if zfdx_dton > 0 and zfdx_dton < 99999999;
            byte50 = %char(%date(zfdx_dton):*usa) + ' at';
            if zfdx_tmon = 0;
               byte50 = %trim(byte50) + ' Midnight';
            else;
               byte6  = hfdx_tmon + '00';
               byte50 = %trim(byte50) + ' ' + %char(%time(%int(byte6)):*usa);
            endif;
         else;
            byte50 = 'Values Not Set';
         endif;
         return %trim(byte50);

      when varName(1) = 'RUSHOFF';                         // Rush Date/Time Off
         if zrsh_dtoff > 0 and zrsh_dtoff < 99999999;
            byte50 = %char(%date(zrsh_dtoff):*usa) + ' at';
            if zrsh_tmoff = 0;
               byte50 = %trim(byte50) + ' Midnight';
            else;
               byte6  = hrsh_tmoff + '00';
               byte50 = %trim(byte50) + ' ' + %char(%time(%int(byte6)):*usa);
            endif;
         else;
            byte50 = 'Values Not Set';
         endif;
         return %trim(byte50);

      when varName(1) = 'RUSHON';                          // Rush Date/Time On
         if zrsh_dton > 0 and zrsh_dton < 99999999;
            byte50 = %char(%date(zrsh_dton):*usa) + ' at';
            if zrsh_tmon = 0;
               byte50 = %trim(byte50) + ' Midnight';
            else;
               byte6  = hrsh_tmon + '00';
               byte50 = %trim(byte50) + ' ' + %char(%time(%int(byte6)):*usa);
            endif;
         else;
            byte50 = 'Values Not Set';
         endif;
         return %trim(byte50);

      when varName(1) = 'FFICE';
         return %trim(ffice);

      when varName(1) = 'FFICEGROUP';
         return %trim(fficegroup);

      when varName(1) = 'FSCHOOLNAME';
         return %trim(fschname);

      when varName(1) = 'PROGRAMNAME';
         if pgm_name = TEST_NAME;
            return PROD_NAME;
         else;
            if web_objectExists(TEST_NAME);
               return TEST_NAME;
            endif;
         endif;

      when varName(1) = 'TESTPRODSITE';
         if pgm_name = TEST_NAME;
            return 'Go To Prod';
         else;
            if web_objectExists(TEST_NAME);
               return 'Go To Test';
            endif;
         endif;

      //----------------------------------------------------------------
      // Institution TP Data Information

      when varName(1) = 'SSNLENGTH';                       // SSN Length
         return %trim(hssn_len);

      when varName(1) = 'SSNCONTROL';                      // SSN Control Code
         return %trim(hssn_cntrl);

      when varName(1) = 'SSNINPTYPE';                      // SSN Input Type
         select;
         when hssn_iptyp = ' ';
            return 'Default - Show SSN as numbers';
         when hssn_iptyp = 'P';
            return 'Show SSN as password field';
         other;
            return ' ';
         endsl;

      when varName(1) = 'SIDEDIT';                         // Student ID Edit Control
         return %trim(hedt_t_sid);

      when varName(1) = 'SIDFORMAT';                       // Student ID Format
         return %trim(hsid_fmt);

      when varName(1) = 'SID1CHARACTER';                   // SID 1st Char
         return %trim(hsid_char1);

      when varName(1) = 'SIDLENGTH';                       // SID Length
         return %trim(hsid_len);

      when varName(1) = 'SIDSHALEN';                       // Length for SHA calculation
         return %trim(hsid_shaln);

      when varName(1) = 'SHAMETHOD';                       // SHA Type
         select;
         when hsha_methd = ' ';
            return 'Default - SHA1';
         when hsha_methd = '2';
            return 'SHA256';
         when hsha_methd = '5';
            return 'MD5';
         when hsha_methd = 'T';
            return 'TOD MD5';
         other;
            return ' ';
         endsl;

      when varName(1) = 'DISABLEDOB';                      // Disable DOB Editing Ability
         select;
         when hdis_dob = ' ';
            return 'No - Do not disable';
         when hdis_dob = 'Y';
            return 'Yes - Disable';
         other;
            return ' ';
         endsl;

      when varName(1) = 'DISABLENAME';                     // Disable Name Editing Ability
         select;
         when hdis_nam = ' ';
            return 'No - Do not disable';
         when hdis_nam = 'Y';
            return 'Yes - Disable';
         other;
            return ' ';
         endsl;

      when varName(1) = 'DISABLESID';                      // Disable SID Editing Ability
         select;
         when hdis_sid = ' ';
            return 'No - Do not disable';
         when hdis_sid = 'Y';
            return 'Yes - Disable';
         other;
            return ' ';
         endsl;

      when varName(1) = 'DISABLESSN';                      // Disable SSN Editing Ability
         select;
         when hdis_ssn = ' ';
            return 'No - Do not disable';
         when hdis_ssn = 'Y';
            return 'Yes - Disable';
         other;
            return ' ';
         endsl;

      when varName(1) = 'NOPHONEORDERS';                   // Prohibit phone orders
         return %trim(hno_phone);

      when varName(1) = 'PROHIBITTRANS';                   // Prohibit Transcript sent to school
         select;
         when hprohtrans = ' ';
            return ' ';
         when hprohtrans = 'A';
            return 'ALL Entities are Prohibited';
         when hprohtrans = 'U';
            return 'Undergraduate only';
         when hprohtrans = 'G';
            return 'Graduate only';
         other;
            return ' ';
         endsl;

      when varName(1) = 'ON2TPAPPL';                       // TP Application
         select;
         when htp_on_tp2 = ' ';
            return 'DVCGITP (Production)';
         when htp_on_tp2 = '5';
            return 'DVCGITP5 (Development)';
         other;
            return ' ';
         endsl;

      when varName(1) = 'PDFSECURITY';                     // Document Security Options
         signerIdx = %lookup(hpdfscrty:pdfSigner);
         if signerIdx > 0;
            return pdfSignerText(signerIdx);
         else;
            return ' ';
         endif;

      when varName(1) = 'SECURITYTEXT';                    // Security Text
         signerIdx = %lookup(ctdataSignerValue:pdfSigner);
         if signerIdx > 0;
            return %trimr(pdfSignerText(signerIdx));
         else;
            return ' ';
         endif;

      when varName(1) = 'ENABLE3PDF';                      // Enable 3 PDF for all Recipients
         return %trim(hpdf3_all);

      when varName(1) = 'VRFYOUTBOUNDTP';                  // Verify OutBound TP
         return %trim(hvrfy_outb);

      when varName(1) = 'MANUALPRTUPLD';                   // Manual PRT upload
         return %trim(hprtuplmod);

      when varName(1) = 'MANUALPDFUPLD';                   // Manual PRT upload
         return %trim(hpdfuplmod);

      when varName(1) = 'FORCEETS';                        // Force Electronics
         return %trim(hforce_ets);

      when varName(1) = 'FORCEPDF';                        // Force PDF
         return %trim(hforce_pdf);

      when varName(1) = 'ATTACHCONTROLCDE';                // Attachment Control Code
         return %trim(htm_attctl);

      when varName(1) = 'ALLOWSELFATTACH';                 // Allow Self Attach
         return %trim(halwslfatt);

      when varName(1) = 'FILTERATTR';                      // Filter Attributes
         select;
         when hatt_gened = 'F';
            return 'Basic Filter';
         when hatt_gened = 'X';
            return 'Basic Filter with Auto Check';
         other;
            return 'No Filter';
         endsl;

      when varName(1) = 'ALLOWPICKUPNAME';                 // Allow PickUp Name
         return %trim(halw_punam);

      when varName(1) = 'ATTACHFORCEBASE';                 // Attach Force Base Code
         return %trim(htm_attfrc);

      when varName(1) = 'SELFRECIPFORCE';                  // Self Recip Force Base Code
         return %trim(htm_slffrc);

      when varName(1) = 'TP1BASEONLY';                     // TP 1 Base Only
         return %trim(htm_1_bas);

      when varName(1) = 'TPDEFAULTBASE';                   // TP Default Base
         return %trim(htm_dftbas);

      when varName(1) = 'DOTRANSTYPES';                    // DO Transcript Types
         return %trim(hdo_ttypes);

      when varName(1) = 'DFLTTRANSTYPE';                   // Default Transcript Type
         return %trim(htm_dfttty);

      when varName(1) = 'TPDEFAULTHOLD';                   // TP Default Hold
         return %trim(htm_dfthld);

      when varName(1) = 'TPDEFAULTXTRA';                   // TP Default Xtra
         return %trim(htm_dftxtr);

      when varName(1) = 'TPDEFAULTSHIP';                   // TP Default Ship
         return %trim(htm_dftshp);

      when varName(1) = 'RESETELIGBLTY';                   // Reset Eligibility
         return %trim(hro_ereset);

      when varName(1) = 'TPRESEND';                        // TP Resend Policy
         return %trim(htp_resend);

      when varName(1) = 'TPAUTHRULES';                     // Omit TP Auth Fields
         return %trim(hrules_sig);

      when varName(1) = 'DOESEDIPRTNR';                    // Does EDI Partner
         return %trim(hdoes_edi);

      when varName(1) = 'ROBOMAINTFEE';                    // Robo Maintenance Fee
         return %trim(hrobomaint);

      when varName(1) = 'ROBOCHNGECODE';                   // Robo Mnt Change Code
         return %trim(hrobo_mntc);

      when varName(1) = 'ROBOBILLCYCLE';                   // Robo Bill Cycle
         return %trim(hrobo_cycl);

      when varName(1) = 'ROBOBILLMONTH';                   // Robo Bill Month
         return %trim(hrobo_cycm);

      when varName(1) = 'PDFCHARGE';                       // I/B PDF Charge
         return %trim(het_ibp_rt);

      when varName(1) = 'FULLIMPCHARGE';                   // I/B Full Import Charge
         return %trim(het_ibf_rt);

      when varName(1) = 'MEMORATE';                        // O/B Memo - PDF
         return %trim(hmemoa_rat);

      when varName(1) = 'MEMO3RDPTYPDF';                   // O/B Memo - 3rd Pty PDF
         return %trim(hmemod_rat);

      when varName(1) = 'MEMOEDIXML';                      // O/B Memo - EDI/XML
         return %trim(hmemoe_rat);

      when varName(1) = 'MEMODAVOWPDF';                    // O/B Memo - AVOW PDF
         return %trim(hmemod_avw);

      when varName(1) = 'MEMOBRIB';                        // O/B Memo - Digitally Signed PDF
         return %trim(hmemo_brib);

      when varName(1) = 'MEMOMRATE';                       // Memo - eRoboMail
         return %trim(hmemom_rat);

      when varName(1) = 'ETMINCHARGE';                     // Elec T+ Minimum Fee
         return %trim(het_minchg);

      when varName(1) = 'DISCOUNTPDF';                     // Discount for PDF
         return %trim(hdisc_pdf);

      when varName(1) = 'DISC3RDPTYPDF';                   // Discount for 3rd Party PDF
         return %trim(hdisc_3pdf);

      when varName(1) = 'DISCOUNTEDIXML';                  // Discount for EDI/XML
         return %trim(hdisc_elec);

      when varName(1) = 'DISCPDFRUSH';                     // Discount for PDF (Rush Service)
         return %trim(hdisc_prsh);

      when varName(1) = 'DISC3RDPTYRUSH';                  // Discount for 3rd Party PDF (Rush Servi
         return %trim(hdisc_3rsh);

      when varName(1) = 'DISCELECRUSH';                    // Discount for EDI/XML (Rush Service)
         return %trim(hdisc_ersh);

      when varName(1) = 'CUNYCONTROL';                     // CUNY - Control
         return %trim(hcunyctl);

      when varName(1) = 'GENEDREQ1';
         return %trim(hgenedreq1);

      when varName(1) = 'GENEDREQ2';
         return %trim(hgenedreq2);

      when varName(1) = 'GENEDREQ3';
         return %trim(hgenedreq3);

      when varName(1) = 'TPOPSDELAYHRS';
         return %trim(htp_opsdly);

      when varName(1) = 'SCHOOLMSGCTL';
         lidx = %lookup(hschmsgctl:schmsgopt);
         if lidx > 0;
            return %trim(schtxtopt(lidx));
         else;
            return %trim(schtxtopt(1));
         endif;

      when varName(1) = 'NOREASON';
         lidx = %lookup(hnoreason:norsnopt);
         if lidx > 0;
            return %trim(norsntxt(lidx));
         else;
            return %trim(norsntxt(1));
         endif;

      when varName(1) = 'TB_NOOTHER';
         lidx = %lookup(htb_noothr:noothopt);
         if lidx > 0;
            return %trim(noothtxt(lidx));
         else;
            return %trim(noothtxt(1));
         endif;

      when varName(1) = 'MOUSESIGN';                       // E-Signature
         select;
         when hmouse_sig = ' ';
            return 'OFF - School does not allow';
         when hmouse_sig = 'Y';
            return 'ON - School allows';
         other;
            return ' ';
         endsl;

      when varName(1) = 'TPSUPPRESS';
         select;
         when htp_supcty = ' ';
            return 'Suppress Nothing';
         when htp_supcty = 'B';
            return 'Suppress Schl Name/City/State';
         when htp_supcty = 'Y';
            return 'Suppress City/State Only';
         other;
            return ' ';
         endsl;

      when varName(1) = 'TPYEARQUAL';
         select;
         when htm_year_q = ' ';
            return 'Use "Attended To" Year';
         when htm_year_q = 'F';
            return 'Use "Attended From" Year';
         other;
            return ' ';
         endsl;

      when varName(1) = 'TPSURVEYCODE';                    // TP Survey Code
         return %trim(htp_svycod);

      when varName(1) = 'TPSURVEYURL';                     // TP Survey URL
         return %trim(htp_svyurl);

      when varName(1) = 'TPKIOSKURL';                      // TP Kiosk URL
         return %trim(htm_kiourl);

      when varName(1) = 'TPKIOSKIP';                       // TP Kiosk IP
         return %trim(hkiosk_ip#);

      when varName(1) = 'REGISTRAR';                       // Registrar
         return %trim(hregistrar);

      when varName(1) = 'PDF3PTYLINK';
         return %trim(hlink_3pdf);

      when varName(1) = 'ENTITYFICE';                      // Entity Fice
         return %trim(henty_fice);

      when varName(1) = 'ET_SEND';
         return %trim(et_send(lp));

      when varName(1) = 'ET_DESCRIPTION';
         return %trim(et_descrpt(lp));

      when varName(1) = 'GENEDTYPE';                       // Select Gened Req Types
         return gened_typ(idx1);

      when varName(1) = 'SCHOOLMSGOPT';
         return schmsgopt(idx1);

      when varName(1) = 'SCHOOLTEXTOPT';
         return %trim(schtxtopt(idx1));

      when varName(1) = 'NOREASONOPT';
         return norsnopt(idx1);

      when varName(1) = 'NOREASONTXT';
         return %trim(norsntxt(idx1));

      when varName(1) = 'NOOTHEROPT';
         return noothopt(idx1);

      when varName(1) = 'NOOTHERTXT';
         return %trim(noothtxt(idx1));

      //----------------------------------------------------------------
      // PDF Transcript Field Setup Panel

      when varName(1) = 'FILE2MAINTAIN';
         web_sendbuffer();
         exsr rtnFileMaint;
         return ' ';

      when varName(1) = 'FORMATONLORT';
         byte20 = formats(formatIdx).formatcd;

         if formats(formatIdx).orientation = 'P';
            return %trim(byte20) + ' - Portrait</td>';
         else;
            return %trim(byte20) + ' - Landscape</td>';
         endif;

      when varName(1) = 'FORMATDESCRP';
         return %trim(formats(formatIdx).description);

      when varName(1) = 'FORMATBUTTON';
         return formats(formatIdx).formatcd;

      //----------------------------------------------------------------
      // eRobo Mail Field Setup Panel

      when varName(1) = 'CREDPONLY';
         lidx = %lookup(hcredp_onl:locationDs(*).ltms_onlin);
         if lidx > 0;
            return locationDs(lidx).ltms_onlin + ' - ' + %trim(locationDs(lidx).ldescrp);
         else;
            return 'No code set or No transcript locations found';
         endif;

      when varName(1) = 'SELECTSIZE';                      // Size of the Select
         return %trim(%char(opcdcnt));

      when varName(1) = 'LOCSONLINE';                      // Location Code
         return locationDs(idx1).ltms_onlin;

      when varName(1) = 'ONLINEDESC';                      // Location Online Description
         return locationDs(idx1).ltms_onlin + ' - ' + %trim(locationDs(idx1).ldescrp);

      when varName(1) = 'TPTOPRINT';                       // TP to print
         if htp#_toprt = '99';
            htp#_toprt = 'ALL';
         endif;
         return %trim(htp#_toprt);

      when varName(1) = 'PRINTAIRBILL';                    // Print Airbill
         if hprint_ab = 'Y';
            return 'YES';
         else;
            return 'NO';
         endif;

      when varName(1) = 'PRINTATTACH';                     // Print Attachment
         if hprint_att = 'Y';
            return 'YES';
         else;
            return 'NO';
         endif;

      when varName(1) = 'TPPRINTBATCH';                    // Print Batch Paper ind.
         if herm_paper = 'Y';
            return 'YES';
         else;
            return 'NO';
         endif;

      when varName(1) = 'TPALWREMAIL';                     // Allow TP Re-email
         select;
         when htp_reml_c = 'Y';
            return 'Yes (FedEx and USPS)';
         when htp_reml_c = 'F';
            return 'FedEx Remails';
         when htp_reml_c = 'N';
            return 'No Remails';
         when htp_reml_c = 'f';
            return 'FedEx Remails (return confirmation)';
         when htp_reml_c = 'n';
            return 'No Remails/Emails';
         other;
            return 'Option Not Chosen';
         endsl;

      when varName(1) = 'COVERTEL#';                       // Cover Page Phone #
         return %trim(hcover_tel);

      when varName(1) = 'COVERMSG';                        // Cover Page Message
         if hcover_msg = 'Y';
            return 'YES';
         else;
            return 'NO';
         endif;

      //----------------------------------------------------------------
      // School Options Maintenance Panel

      when varName(1) = 'MNTGROUPID';                      // Group ID
         return pgroup_id;

      when varName(1) = 'GROUPTITLE';                      // Title
         return %trim(ptitle);

      when varName(1) = 'MNTSEQ#';                         // Sequence#
         return %editc(pseqnce:'X');

      when varName(1) = 'TEXTAREA';                        // Text Area
         return %trim(htext);

      when varName(1) = 'HEADTITLE';
         select;
         when add_mode = TRUE;
            return 'Add Option to ' + %trim(ptitle);
         other;
            return %trim(ptitle);
         endsl;

      when varName(1) = 'GROUPID';
         return %trim(hgroup_id);

      when varName(1) = 'ADDSEQ#';
         return %char(hseqnce);

      when varName(1) = 'EDITSEQ#';
         return %trim(hmnt_seq);

      when varName(1) = 'TITLEOPT';
         return %trim(htitle);

      //----------------------------------------------------------------
      // Display Pop-up variables

      when varName(1) = 'ZTITLE';
         return %trim(ztitle);

      when varName(1) = 'PTITLE';
         return %trim(ptitle);

      when varName(1) = 'PTEXT';
         return %trim(ptext);

      when varName(1) = 'TEXT1';
         return %trim(rowtext1);

      when varName(1) = 'TEXT2';
         return %trim(rowtext2);

      when varName(1) = 'LOCCODE';
         return locationDs(locIdx).ltms_onlin;

      when varName(1) = 'LOCDESCRP';
         return %trim(locationDs(locIdx).ldescrp);

      when varName(1) = 'LOCBUTTON';
         return locationDs(locIdx).ltms_onlin;

      //----------------------------------------------------------------
      // Institute GA Data Panel

      when varName(1) = 'EDIVALIDDEG';                     // EDI Valid Degrees
         return %trim(hedi_v_deg);

      //----------------------------------------------------------------
      // Institute Resend Data Panel

      when varName(1) = 'CS_RESEND_C';
         select;
         when hcs_rsnd_c = 'Y';
            return 'YES';
         when hcs_rsnd_c = 'N';
            return 'NO';
         when hcs_rsnd_c = 'C';
            return 'Case-by-case';
         other;
            return 'Default';
         endsl;

      when varName(1) = 'CS_RESEND_W';
         if hcs_rsnd_c = ' ' and editMode <> TRUE;
            return '(Default) 14';
         else;
            return %trim(hcs_rsnd_w);
         endif;

      when varName(1) = 'CS_RESEND_#';
         return %trim(hcs_rsnd_#);

      when varName(1) = 'ALLOWADDRCHANGE';                 // Allow Address Modification
         select;
         when h_aac = ' ';
            return '(Default) YES';
         when h_aac = 'A';
            return 'Attention Only';
         when h_aac = 'N';
            return 'NO';
         other;
            return 'YES';
         endsl;

      when varName(1) = 'CONFIRMNORECPT';                  // Confirm No Receipt
         select;
         when h_cnr = ' ';
            return '(Default) YES';
         when h_cnr = 'N';
            return 'NO';
         other;
            return '(Default) YES';
         endsl;

      when varName(1) = 'RESENDEMAIL';                     // Resend PDF Email 1
         return %trim(hemail);

      when varName(1) = 'RESENDEMAIL2';                    // Resend PDF Email 2
         return %trim(hemail2);

      when varName(1) = 'TP_RESEND_W';
         return %trim(htp_rsnd_w);

      when varName(1) = 'TP_RESEND_#';
         return %trim(htp_rsnd_#);

      //----------------------------------------------------------------
      // School Contacts Panel and Edit Contacts Panel

      when varName(1) = 'CONFULLNAME';                     // Full Name
         return %trim(wfullname);

      when varName(1) = 'CONTITLE';                        // Title
         return %trim(hnam_title);

      when varName(1) = 'CONCOMPANY';                      // Company
         return %trim(hcompany);

      when varName(1) = 'CONADDR1';                        // Address 1
         return %trim(haddr1);

      when varName(1) = 'CONADDR2';                        // Address 2
         return %trim(haddr2);

      when varName(1) = 'CONCTYSTZIP';                     // City,State and Post Code
         return %trim(hcity) + ', ' + %trim(hstate) + ' ' + hpostcd;

      when varName(1) = 'CONTEL#';                         // Telephone #
         return %trim(htel#);

      when varName(1) = 'CONEMAIL';                        // Contact Email
         return %trim(hemail);

      when varName(1) = 'CONTACTKEY';                      // Contact Key
         return mfice + %editc(mseq#:'X');

      when varName(1) = 'CONTACTDESC';                     // Contact Description
         byte70 = '??????????';
         if %tlookup(mrecord_id:tab_conlet:tab_condes) = *on;
            byte70 = %trim(tab_condes);
         endif;
         return byte70;

      when varName(1) = 'CONFIRSTNAME';                    // First Name
         return %trim(hfrstname);

      when varName(1) = 'CONMIDDLENAME';                   // Middle Name
         return %trim(hmidlname);

      when varName(1) = 'CONLASTNAME';                     // Last Name
         return %trim(hlastname);

      when varName(1) = 'CONNICKNAME';                     // Nick Name
         return %trim(hnickname);

      when varName(1) = 'CONCITY';                         // City
         return %trim(hcity);

      when varName(1) = 'CONSTATE';                        // State
         return %trim(hstate);

      when varName(1) = 'CONZIP';                          // Zip
         return %trim(hpostcd);

      when varName(1) = 'CONSEQUENCE';                     // Sequence Number
         return %editc(hseq#:'X');

      when varName(1) = 'CONUSRTYPE';                      // User Type
         return ar_conlet(idx1);

      when varName(1) = 'CONUSRDESC';                      // User Description
         return %trim(%subst(ar_condes(idx1):2));

      when varName(1) = 'SALUTATION';                      // Salutation
         return %trim(salut(idx1));

      //----------------------------------------------------------------
      // Diploma Customer Service Variables

      when varName(1) = 'THEGARATE';                       // GA Rate
         return %char(the_rate);

      //----------------------------------------------------------------
      // Parking Permit Customer Service Variables

      when varName(1) = 'TPXCODE';
         return tpxcode;

      when varName(1) = 'TPXCODE2';
         return tpxcode2;

      when varName(1) = 'PPGOLIVE';
         h_applid = 'PP';

         if not %open(gamaster1);
            open gamaster1;
         endif;

         chain (hfice:h_applid) ga_master;
         if not %found(gamaster1);
            clear glive_appl;
         else;
            go_livedt = %trim(dspTmStamp(GLIVE_DATE:0:0:'*4YR'));
         endif;
         return %trim(go_livedt);

      when varName(1) = 'GATEXT';
         return %trim(ga_text);

      when varName(1) = 'HELPTBLTEXT';
         return %trim(helpText);

      when varName(1) = 'GARATE';
         return %trim(%editc(ga_rate:'3'));

      when varName(1) = 'RATEHANDLE';
         return %trimr(xrhandle);

      when varName(1) = 'HANDLECODE';
         return %trim(xrhdlcod);

      when varName(1) = 'GATEXT_1';
         return %trim(ga_text_1);

      when varName(1) = 'GAVALIDFROM';
         return %trim(dspTmStamp(ga_validfr:0:0:'*4YR'));

      when varName(1) = 'GAVALIDTO';
         return %trim(dspTmStamp(ga_validto:0:0:'*4YR'));

      when varName(1) = 'GADATETEXT';
         return %trim(byte500);

      //----------------------------------------------------------------
      // D2 Application Customer Service Variables

      when varName(1) = 'D2LIVEDATE';                      // Live Date
         if not %open(d2master1);
            open d2master1;
         endif;

         chain (hfice) d2master;
         if not %found(d2master1);
            go_livedt = *blanks;
         else;
            go_livedt = %trim(dspTmStamp(MLIVE_DATE:0:0:'*4YR'));
         endif;
         return %trim(go_livedt);

      when varName(1) = 'DATALOCATION';                    // Data Location
         if mdata_loc = 'LF';
            return 'Local File';
         elseif mdata_loc = 'RD';
            return 'Robo Data';
         endif;

      when varName(1) = 'DOBLEVEL';                        // Date of birth access level
         if idirdob = 'N';
            return 'Private';
         else;
            return 'Public';
         endif;

      when varName(1) = 'INVOICEPRICE';
         if not %open(d2tiers1);
            open d2tiers1;
         endif;

         for tierIdx = 1 to 3;
            chain (%char(tierIdx)) d2tier;
            d2InvcPrices += %editc(ptier_amt:'1':*CURSYM);
         endfor;

         chain ('C') d2tier;
         d2CcPrices = %trim(%editc(ptier_amt:'1':*CURSYM));
         return %trim(d2InvcPrices);

      when varName(1) = 'CCPRICE';                         // Credit Card Charge
         return %trim(d2CcPrices);

      when varName(1) = 'SCHSURCHARGE';                    // School Surcharge
         return %editc(mamt_schl:'1':*CURSYM);

      when varName(1) = 'TAXSTATE';                        // Tax State
         taxStatesArr = slstx_getSalesTaxStates('D2');
         for taxIdx = 1 to 3;
            d2TaxStates += taxStatesArr(taxidx) + ' ';
         endfor;
         return %trim(d2TaxStates);

      //----------------------------------------------------------------
      // TP Application Customer Service Variables

      when varName(1) = 'TPLIVETIME';                      // Live Time
         return %trim(dspTmStamp(ilive_tp:0:0:'*4YR')) + LINEFEED;

      when varName(1) = 'TPMODE';
         select;
         when ichargetm = 'M'; //Maint
            return ' Maintenance Mode' + LINEFEED;
         when  ichargetm = 'I' or ichargetm = 'S';
            return 'Currently in Simulation' + LINEFEED;
         when ichargetm = 'Y';
            return ' School is live on charging' + LINEFEED;
         endsl;

      when varName(1) = 'CONTACTEMAIL';
         return %trim(schcnt_eml);

      when varName(1) = 'CONTACTNAME';
         return %trim(schcnt_nam);

      when varName(1) = 'CONTACTTEL#';
         select;
         when hsys_type = 'TP';
            krec_id = 'T';
         when hsys_type = 'PP' or hsys_type = 'MS';
            krec_id = 'P';
         when hsys_type = 'DP' or hsys_type = 'CE';
            krec_id = 'K';
         when hsys_type = 'MT' or hsys_type = 'GT';
            krec_id = 'L';
         endsl;

         fileAccess = 'CHAIN';
         get_cntct();
         return %trim(schcnt_tel);

      when varName(1) = 'TPAUTHMETHODS';
         if irobo_au_c <> *blanks;
            byte70 = 'Auto-Authorization<br />';
         endif;
         if irobo_au_p <> *blanks or
            ipin_authr <> *blanks;
            byte70 = %trim(byte70) + 'PIN Accepted<br />';
         endif;
         byte70 = %trim(byte70) + 'Paper Auth Form<br>';
         if imouse_sig = 'Y';
            byte70 = %trim(byte70) + 'Electronic Signatures';
         endif;
         return %trim(byte70);

      when varName(1) = 'TPUPLDFORM';
         if iauth_byci = 'Y';
            return 'YES';
         else;
            return 'NO';
         endif;

      when varName(1) = 'TPFAX#';
         krec_id = '2';
         fileAccess = 'CHAIN';
         get_cntct();
         hfaxnum = %trim(schfax_num);
         return %trim(schfax_num);

      when varName(1) = 'TPFAX#2';
         hfaxnum = %trim(schfax_num);
         return %trim(schfax_num);

      when varName(1) = 'HASROBO';
         if irobo_stac = '';
            return 'NO';
         else;
            return 'YES';
         endif;

      when varName(1) = 'TPCIPT';
         if %lookup('PC':har_etsend) > 0;
            return 'YES - Transcripts printed at Credentials';
         else;
            return 'NO';
         endif;

      when varName(1) = 'TPTMSYEAR1';
         if irobo_stac = '';
            return 'N/A';
         else;
            return %trim(itms_year);
         endif;

      when varName(1) = 'ELECYEAR1';
         if irobo_stac = '';
            return 'N/A';
         else;
            return %trim(ifirstyear);
         endif;

      when varName(1) = 'UNOFFICIALFAX';
         exsr chk_TXs;
         if have_fax = TRUE;
            return '$' + %trim(%EDITC(fax_chrg:'3'));
         else;
            return 'NOT OFFERED';
         endif;

      when varName(1) = 'TPAGREEMENT';
         if icert_auth = 'C';
            return 'YES';
         else;
            return 'NO';
         endif;

      when varName(1) = 'TPREMAILS';                       // School remail type
         select;
         when itp_reml_c = 'Y';
            return 'Yes (FedEx and USPS)';
         when itp_reml_c = 'F';
            return 'FedEx Remails';
         when itp_reml_c = 'N';
            return 'No Remails';
         when itp_reml_c = 'f';
            return 'FedEx Remails (return confirmation)';
         when itp_reml_c = 'n';
            return 'No Remails/Emails';
         other;
            return 'Option Not Chosen';
         endsl;

      when varName(1) = 'TPFREEBIES';                      // If the school does freebies or not
         frebiefice = ifice;
         if idistfice <> *blanks;
            frebiefice = idistfice;
         endif;

         if not %open(tpfrees1);
            open tpfrees1;
         endif;

         setll (frebiefice) freetrack;
         if %equal(tpfrees1);
            haveTpFree = TRUE;
         endif;

         if itm_flagf = 'S' and haveTpFree <> TRUE;        // Selective auto-calc
            return 'NO';
         elseif itm_flagf = 'T';
            return '2 Free - Student must select ';
         elseif itm_flagf = '2';
            return 'Student receives first ' + %char(itpfreemax) + ' automatically';
         elseif itm_flagf <> ' ';
            return 'YES';
         else;
            return 'NO';
         endif;

      when varName(1) = 'TPATTACHMENT';
         if itm_attctl = '';
            byte200 = 'No, except for auto generated by Credentials';
         else;
            byte200 = 'Yes<br>';
            if ialwslfatt = 'Y';
               byte200 = %trim(byte200) + 'Allowed to Self<br>';
            else;
               byte200 = %trim(byte200) + 'Not Allowed to Self<br>';
            endif;

            if %lookup('AL':har_etsend) > 0 or %lookup('AC':har_etsend) > 0 or
               %lookup('AE':har_etsend) > 0 or %lookup('PC':har_etsend) > 0;

               select;
               when itm_attctl = 'A';
                  byte200 = %trim(byte200) + 'Credentials Receives Attachment(s)<br>' +
                           'Student can request school to fill out<br>';
               when itm_attctl = 'C';
                  byte200 = %trim(byte200) + 'Credentials Receives all attachments';
               endsl;
            else;
               byte200 = %trim(byte200) + 'Attachments Sent Directly to School';
            endif;
         endif;
         return %trimr(byte200);

      when varName(1) = 'TPPDFYEAR1';
         if ipdf_1styr = '0000';
            return 'ALL';
         else;
            return %trim(ipdf_1styr);
         endif;

      when varName(1) = 'TPPDFSECURE';
         signerIdx = %lookup(isigner:pdfSigner);
         if signerIdx > 0;
            return pdfSignerText(signerIdx);
         else;
            return '';
         endif;

      when varName(1) = 'TPOFFDATE';
         return %char(%date(tp_dateoff):*usa);

      when varName(1) = 'TPONDATE';
         return %char(%date(tp_dateon):*usa);

      when varName(1) = 'TPOFFTIME';
         return %char(%time(tp_timeoff):*usa);

      when varName(1) = 'TPONTIME';
         return %char(%time(tp_timeon):*usa);

      when varName(1) = 'KIOSKTEXT';
         return %trim(kiosktext);

      when varName(1) = 'TPTEXT';
         return %trim(tp_text);

      when varName(1) = 'TPHELPMSG';
         return %trim(helpText);

      when varName(1) = 'TPRATE';
         return %editc(the_rate:'3');

      when varName(1) = 'STUDHNDLCHRG' or varName(1) = 'APOHNDLCHRG';
         select;
         when varName(1) = 'STUDHNDLCHRG';
            hdlLogic = it_stu_lrh;
            hdlAmount = it_stu_hdl;
         when varName(1) = 'APOHNDLCHRG';
            hdlLogic = it_apo_lrh;
            hdlAmount = it_apo_hdl;
         endsl;

         select;
         when hdlLogic = 'N';
            return '-';
         when hdlLogic = 'O' or hdlLogic = 'T';
            return  %char(hdlAmount);
         when hdlLogic = '2';
            return  '$2.00 to $6.00 <br>(9% if order is $75+)';
         when hdlLogic = 'U';
            return  '$2.25 to $6.25 <br>(9% if order is $75+)';
         when hdlLogic = 'A';                              // Only charge on possible auto_auth
            return  %char(hdlAmount);
         endsl;

      when varName(1) = 'STUPERPRICE' or varName(1) = 'APOPERPRICE';
         select;
         when varName(1) = 'STUPERPRICE';
            hdlLogic = it_stu_lrh;
         when varName(1) = 'APOPERPRICE';
            hdlLogic = it_apo_lrh;
         endsl;

         select;
         when hdlLogic = 'N';
            return 'No Charge';
         when hdlLogic = 'O';
            return 'Per Order';
         when hdlLogic = 'T';
            return 'Per Transcript';
         when hdlLogic = '2' or hdlLogic = 'U';
            return 'Variable';
         when hdlLogic = 'A';
            return 'through Public';
         endsl;

      //----------------------------------------------------------------
      // Common Customer Service Variables

      when varName(1) = 'MSGTEXT';                         // Get message from message file
         clear getMsgDs;
         getMsgDs = getThisMsg#;
         return %trim(getMessage(msg_defalt:getMsg#:getMsgParms:getMsgOvr));

      when varName(1) = 'PDFFILEPATH';                     // File Path
         return '/CIPGM/PDF_IMAGES/' + %trim(pdfs(idx));

      when varName(1) = 'PDFFILENAME';                     // File Name
         return %trim(pdfs(idx));

      // String literals surrounded by ""
      when %len(varName(1)) > 2;
         if %subst(varName(1):1:1) = '"' and %subst(varName(1):%len(varName(1)):1) = '"';
            return %subst(varName(1):2:%len(varName(1))-2);
         endif;

      other;
         clear returnVal;
      endsl;

      return returnval;
   endsl;

   return returnVal;

   //***************************************************************************
   //  rtnFileMaint: routine to determine how to call UTFILEDSP
   //***************************************************************************
   begsr rtnFileMaint;

   select;
   when hscrn_next = 'PDF';
      statusDs = utfile_display('TPPDFFLD1':'SCHMNT':editMode:pgm_name:huserid:cau_grp_id:
                                'T':TEST_NAME:fmFields:hfice:hformatcd);

   when hscrn_next = 'LOC';
      statusDs = utfile_display('TPLOC1':'':editMode:pgm_name:huserid:cau_grp_id:
                                'T':TEST_NAME:fmFields:hfice:hlocationcd);

   when hscrn_next = 'ESS';
      statusDs = utfile_display('DVINSTITF1':'ESS':editMode:pgm_name:huserid:cau_grp_id:
                                'T':TEST_NAME:fmFields:hfice);

   when hscrn_next = 'EDU';
      fileIdx += 1;
      editMode = editModeArray(fileIdx);
      select;
      when fileIdx = 1;
         statusDs = utfile_display('DVINSTITF1':'EDU':editMode:pgm_name:huserid:cau_grp_id:
                                   'T':TEST_NAME:fmFields:hfice);


      when fileIdx = 2;
         statusDs = utfile_display('D2MASTER1':'':editMode:pgm_name:huserid:cau_grp_id:
                                   'T':TEST_NAME:fmFields:hfice);

      when fileIdx = 3;
         statusDs = utfile_display('E2MASTER1':'':editMode:pgm_name:huserid:cau_grp_id:
                                   'T':TEST_NAME:fmFields:hfice);

      endsl;
   endsl;

   endsr;

   // **************************************************************************
   // chk_txs: Check if school offers a fax service in TXs
   // **************************************************************************
   begsr chk_txs;

      if not %open(dvinstit5);
         open dvinstit5;
      endif;

      the_recid = 'TX';
      setll (ifice:the_recid) dvinstit5;
      if %found();
         reade (ifice:the_recid) tmsparms;
         dou %eof(dvinstit5);
            if tp_categry = 'F';
               have_fax = TRUE;
               fax_chrg = tp_q_rate + tp_q_base;
            endif;

            reade (ifice:the_recid) tmsparms;
         enddo;
      endif;

      the_recid = 'TB';

      setll (ifice:the_recid) dvinstit5;
      if %found();
         reade (ifice:the_recid) tmsparms;
         dou %eof(dvinstit5);
            if tp_categry = 'F';
               have_fax = TRUE;
               fax_chrg = tp_q_rate + tp_q_base;
            endif;
            reade (ifice:the_recid) tmsparms;
         enddo;
      endif;

   endsr;

end-proc;

// ***************************************************************************************
// getProductList: Returns the number of products for that FICE
// ***************************************************************************************
dcl-proc getProductList;
   dcl-pi *n likeds(rtnProductList);
      $fice char(6) const;
   end-pi;

   dcl-ds rtnProductList likeds(productList) inz;

   // Check GA Products
   if not %open(gamaster1);
      open gamaster1;
   endif;

   setll (hfice) ga_master;
   if hfice = 'XPHONE';
      clear glive_appl;
      rtnProductList.hasPP = TRUE;
      rtnProductList.hasDP = TRUE;
      rtnProductList.numProducts += 2;
   elseif %found();
      reade (hfice) ga_master;
      dou %eof(gamaster1);
         if glive_appl = 'Y' or glive_appl = 'S';
            select;
            when gapplid = 'PP';
               rtnProductList.hasPP = TRUE;
               rtnProductList.ppLiveDate = %trim(dspTmStamp(GLIVE_DATE:0:0:'*4YR'));
               rtnProductList.numProducts += 1;
            when gapplid = 'CE';
               rtnProductList.hasCE = TRUE;
               rtnProductList.ceLiveDate = %trim(dspTmStamp(GLIVE_DATE:0:0:'*4YR'));
               rtnProductList.numProducts += 1;
            when gapplid = 'DP';
               rtnProductList.hasDP = TRUE;
               rtnProductList.dpLiveDate = %trim(dspTmStamp(GLIVE_DATE:0:0:'*4YR'));
               rtnProductList.numProducts += 1;
            endsl;
         endif;
         reade (hfice) ga_master;
      enddo;
   endif;

   // Check TP
   if (cau_grp_id = 'IT' or cau_grp_id = 'ITS' or cau_grp_id = 'OPS' or cau_grp_id = 'CRM' or
       cau_grp_id = 'DOC' or cau_grp_id = 'ACC') or (ichargetm = 'Y' or ilive_tp > 0 or
       ifice = 'XPHONE' or ifice = '009998');

      rtnProductList.hasTP = TRUE;
      rtnProductList.numProducts += 1;
   endif;

   // Check D2
   if ((cau_grp_id = 'IT' or cau_grp_id = 'ITS' or cau_grp_id = 'OPS' or cau_grp_id = 'CRM' or
       cau_grp_id = 'DOC') and (ifice = '000000' or ifice = 'XPHONE' or ifice = '009998')) or
       icharged2 = 'Y';

       rtnProductList.hasD2 = TRUE;
       rtnProductList.numProducts += 1;
   endif;

   // Check eSS
   if (iss_custyp <> *blanks and ichargetm <> 'Y') or ifice = 'XPHONE';
      rtnProductList.hasESS = TRUE;
      rtnProductList.numProducts += 1;
   endif;

   return rtnProductList;

end-proc;

// ***************************************************************************************
// getMessage
// ***************************************************************************************
dcl-proc getMessage;
   dcl-pi *n like(msg.text);
      $messagePrefix like(HTML_PARM) const;
      $messageNumber like(HTML_PARM) const;
      $messageVars like(HTML_PARM) const;
      $messageOverRide like(HTML_PARM) const;
   end-pi;

   dcl-ds subVars likeds(subVars_t);

   // replaces msg_text and msg_level1
   dcl-ds msg likeds(msgDs_t);
   dcl-s msgOvrPrefix like(msgOvrPrefix_t) inz;

   // replaces msg_num and msg_prefix from messagesds
   dcl-ds msgId likeds(msgId_t);

   // replaces msg_ParmD and msg_ParmL from messagesds
   dcl-s msgParmD like(msgReplaceData_t) inz;
   dcl-s msgParmL like(msgReplaceLen_t) inz;

   // replaces msg_file from messagesds
   dcl-s msgFile like(msgFile_t);

   dcl-s p# packed(3);
   dcl-s #loc packed(3:0);

   clear msg;

   msgId.num = $messageNumber;
   msgId.prefix = $messagePrefix;

   select;
   when $messageOverRide = 'Y';
      msgOvrPrefix = imsgprefix;
      if h_applid = 'PP' or h_applid = 'DP';
         msgfile = 'GAMSGS_ENG*LIBL  ';
      else;
         msgfile = 'T5MESSAGES*LIBL  ';
      endif;
   when $messageOverRide = 'S';
      msgOvrPrefix = imsgprefix;
      msgfile = 'CSMESSAGES*LIBL';
   other;
      msgOvrPrefix = msg_defalt;
      msgfile = 'CSMESSAGES*LIBL';
   endsl;

   subVars = getMessageSubVars($messageVars);

   for p# = 1 to subVars.count;

      select;
      when subVars.parm(p#) = 'A';                         // Log call fields
         byte3 = 'CCS';
         if cau_grp_id = 'IT' or cau_grp_id = 'DOC';
            byte3 = huserid;
         endif;
         clear tpxcode;
         if msg_num = '3036' or msg_num = '3037';
            tpxcode = '5';
         endif;
         if msg_num = '3018';
            tpxcode = gbogutype;
         endif;
         if msg_num = '3019';
            tpxcode = itp_on_tp2;
            tpxcode2 = %trim(itp_on_tp2) + 'T';
         endif;

         #Loc = msgParmL + 1;
         msgParmL += 1;
         %subst(msgParmD:#Loc:1) = tpxcode;

         #Loc = msgParmL + 1;
         msgParmL += 6;
         %subst(msgParmD:#Loc:6) = hfice;

         #Loc = msgParmL + 1;
         msgParmL += 10;
         %subst(msgParmD:#Loc:10) = huserid;

         #Loc = msgParmL + 1;
         msgParmL += 3;
         %subst(msgParmD:#Loc:3) = byte3;

         #Loc = msgParmL + 1;
         msgParmL += 2;
         %subst(msgParmD:#Loc:2) = tpxcode2;

      when subVars.parm(p#) = 'd';
         get_csopt();
         #Loc = msgParmL + 1;
         msgParmL += 100;

         select;
         when cs_rsnd_c = *blanks;
            byte100 = 'Must wait 14 calendar days before requesting.';
         when cs_rsnd_c = 'Y' or (cs_rsnd_c = 'C' and cs_rsnd_w <> 0);
            byte100 = 'Must wait ' + %char(cs_rsnd_w) + ' calendar days before requesting.';
         when cs_rsnd_c = 'C' and cs_rsnd_w = 0;
            byte100='There is no mandatory wait time for a resend request.';
         endsl;
         %subst(msgParmD:#Loc:100) = %trim(byte100);

      when subVars.parm(p#) = 'D';
         get_csopt();
         #Loc = msgParmL + 1;
         msgParmL += 50;

         select;
         when cs_rsnd_c = *blanks or (cs_rsnd_c = 'C' and cs_rsnd_# = 0);
            byte50 = *blanks;
         when cs_rsnd_c = 'Y' or (cs_rsnd_c = 'C' and cs_rsnd_# <> 0);
            byte50 = ' All requests must be made within ' + %char(cs_rsnd_#) + ' calendar days.';
         endsl;
         %subst(msgParmD:#Loc:50) = %trim(byte50);

      endsl;

   endfor;

   msg = web_zGetMessage(msgId:msgFile:msgOvrPrefix:msgParmD:msgParmL);
   if not msg.haveText;
      clear msg.text;
   endif;

   byte4 = msg.level1;
   if byte4 = '*OFF';
      clear msg.text;
   endif;

   return msg.text;

end-proc;

//****************************************************************************************
//  getMessageSubVars -
//****************************************************************************************
dcl-proc getMessageSubVars;
   dcl-pi *n likeds(subVars_t);
      @messageVars like(HTML_PARM) value;
   end-pi;

   dcl-ds @subVars likeds(subVars_t);
   dcl-s colon packed(3) inz;

   clear @subVars;
   if @messageVars <> *blanks;

      // parameters should separated by colon
      // check for more than one parameter
      @subVars.count = 1;
      colon = %scan(':':@messageVars);
      dow colon > 0 and @subVars.count < 5;

         // loop through all parameters but the last and process them
         @subVars.parm(@subVars.count) = %subst(@messageVars:1:colon-1);

         // remove the parameter that was just processed
         @messageVars = %subst(@messageVars:colon+1);

         // find next parameter's end
         colon = %scan(':':@messageVars);
         @subVars.count += 1;
      enddo;

      // process last parameter
      @subVars.parm(@subVars.count) = @messageVars;

   endif;

   return @subVars;

end-proc;

// ***************************************************************************************
// processIf: what to do if the html variable is an "IF"
//            criteria parameter lets the program know what to check
// ***************************************************************************************
dcl-proc processIf;
   dcl-pi *n IND;
      criteria like(HTML_PARM) const;
   end-pi;

   pssrRoutine = 'processIf : ([IF/WHEN/CASE,' + %trim(criteria) + '])';
   if pssrTriggeredVar <> *blanks;
      if pssrTriggeredVar = criteria;
         return FALSE;
      endif;
   endif;

   select;

   when criteria = 'SHOWINFO' and fi > 0;
      return TRUE;

   when criteria = 'SHOWWARNING' and wrIdx > 0;
      return TRUE;

   when criteria = 'SHOWCONF' and ci > 0;
      return TRUE;

   when criteria = 'SHOWERROR' and ei > 0;
      return TRUE;

   when criteria = 'CHECKFILES' and pf# > 0;
      return TRUE;

   when %scan('SELECTED':criteria:1) > 0;
      selected = FALSE;
      checkValue = ' ';
      clear compString;                                    // Comparison String
      clear ctdataSignerValue;

      if %scan('-':criteria:1) > 0;
         checkValue = %subst(criteria:(%scan('-':criteria:1)+1):1);
         compString = %subst(criteria:9:%scan('-':criteria:1)-9);
      else;
         compString = %subst(criteria:9:%len(%trim(criteria))-8);
      endif;

      if %trim(compString) = 'PDFSEC';
         ctdataSignerValue = checkValue;
      endif;

      select;
      when %trim(compString) = 'PTNR' and checkValue = hprtnr_req;        // Partner Required Code
         selected = TRUE;
      when %trim(compString) = 'PRI' and checkValue = hcoloptpri;         // "The" feature
         selected = TRUE;
      when %trim(compString) = 'SEC' and checkValue = hcoloptsec;         // "The" feature
         selected = TRUE;
      when %trim(compString) = 'SSN' and checkValue = hssn_iptyp;
         selected = TRUE;
      when %trim(compString) = 'SHA' and checkValue = hsha_methd;
         selected = TRUE;
      when %trim(compString) = 'DOB' and checkValue = hdis_dob;
         selected = TRUE;
      when %trim(compString) = 'NAM' and checkValue = hdis_nam;
         selected = TRUE;
      when %trim(compString) = 'SID' and checkValue = hdis_sid;
         selected = TRUE;
      when %trim(compString) = 'DISSSN' and checkValue = hdis_ssn;        // Disable SSN Editing
         selected = TRUE;
      when %trim(compString) = 'TRANS' and checkValue = hprohtrans;
         selected = TRUE;
      when %trim(compString) = 'TPVER' and checkValue = htp_on_tp2;       // TP Versions
         selected = TRUE;
      when %trim(compString) = 'PDFSEC' and checkValue = isigner;         // Document Security Code
         selected = TRUE;
      when %trim(compString) = 'FILTER' and checkValue = hatt_gened;      // Filters
         selected = TRUE;
      when %trim(compString) = 'RBOCHG' and checkValue = hrobo_mntc;      // ROBO Charge Code
         selected = TRUE;
      when %trim(compString) = 'RBOBIL' and checkValue = hrobo_cycl;      // ROBO Bill Cycle
         selected = TRUE;
      when %trim(compString) = 'ESIGN' and checkValue = hmouse_sig;       // E-Signature
         selected = TRUE;
      when %trim(compString) = 'TPSUP' and checkValue = htp_supcty;       // Suppress City/State
         selected = TRUE;
      when %trim(compString) = 'YRQUAL' and checkValue = htm_year_q;      // TP Qualifier Year
         selected = TRUE;
      when %trim(compString) = 'FMT' and hformatcd = formats(formatIdx).formatcd;  // Format Row Sel
         selected = TRUE;
      when %trim(compString) = 'LOC' and hlocationcd = locationDs(locIdx).ltms_onlin; //Location sel
         selected = TRUE;
      when %trim(compString) = 'AIR' and checkValue = hprint_ab;          // Airbill
         selected = TRUE;
      when %trim(compString) = 'ATT' and checkValue = hprint_att;         // Attachmentic
         selected = TRUE;
      when %trim(compString) = 'BTC' and checkValue = herm_paper;         // Batch paper
         selected = TRUE;
      when %trim(compString) = 'RML' and checkValue = htp_reml_c;         // Re-emails
         selected = TRUE;
      when %trim(compString) = 'MSG' and checkValue = hcover_msg;         // Cover Message
         selected = TRUE;
      when %trim(compString) = 'RSDC' and checkValue = hcs_rsnd_c;        // Resend Code
         selected = TRUE;
      when %trim(compString) = 'RSDA' and checkValue = h_aac;             // Resend Addr Modificatio
         selected = TRUE;
      when %trim(compString) = 'RSDR' and checkValue = h_cnr;             // Confirm no Receipt
         selected = TRUE;
      when %trim(compString) = 'OPT' and optselected = TRUE;
         optselected = FALSE;
         selected = TRUE;
      endsl;
      if selected = TRUE;
         selected = FALSE;
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'FICECHANGE';                           // Show fice change button
      if editMode = TRUE or %lookup(TRUE:editModeArray) > 0;
         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'DBS_SHOWEDITBTN';                      // Edit Button for Basic School Informati
      select;
      when %scan('U':cau_ccs) = 0 and cau_grp_id <> 'ITS';
         return FALSE;
      when editMode = TRUE;
         return FALSE;
      other;
         return TRUE;
      endsl;

   when criteria = 'EDITMODE' and editMode = TRUE;
      return TRUE;

   when criteria = 'EDITSCHOOLBASICS' and editMode = TRUE;
      return TRUE;

   when criteria = 'DISPLAYSCHOOLBASICS' and editMode = FALSE;
      return TRUE;

   when criteria = 'TESTPRODLINK' and (cau_grp_id = 'IT' or cau_grp_id = 'DOC');
      if pgm_name = TEST_NAME or web_objectExists(TEST_NAME);
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'DTP_SHOWEDITBTN';                      // EDit Button for Institution TP Data
      if editMode = TRUE or (%scan('U':cau_ccs) = 0 and ifice <> '009998') or
         (%scan('U':cau_ccs) = 0 and ifice = '009998' and cau_grp_id <> 'IT');

         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'PDFEDIT';
      if editMode = FALSE or %scan('U':cau_ccs) = 0;
         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'PRINTEDIT';
      if editMode = TRUE or %scan('U':cau_ccs) = 0;
         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'CSR_SHOWEDITBTN';                      // Edit Button for Institution Resend Dat
      if (cau_grp_id <> 'CRM' and cau_grp_id <> 'IT ') or editMode = TRUE;
         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'CSR_UPDCXLBTN';                        // Show Update/Cancel button
      if (cau_grp_id <> 'CRM' and cau_grp_id <> 'IT ') or editMode = FALSE;
         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'DGA_SHOWEDITBTN';                      // Edit Button for Institution GA Data
      if editMode = TRUE or %scan('U':cau_ccs) = 0;
         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'DCT_SHOWEDITBTN' and cau_grp_id <> 'ACC';  // Edit Button for School Contacts
      return TRUE;

   when criteria = 'NOEDIT' and editMode = FALSE;
      return TRUE;

   when criteria = 'NOETSENDA' and haveETsenda = FALSE;
      return TRUE;

   when criteria = 'ETSENDA' and haveETsenda = TRUE;
      return TRUE;

   when criteria = 'NOTALWAYS' and formatTot >= 1;
      return TRUE;

   when criteria = 'NOROWFORMAT';
      if editMode <> TRUE or hformatcd <> formats(formatIdx).formatcd;
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'ROWFORMAT';
      if editMode = TRUE and hformatcd = formats(formatIdx).formatcd;
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'LIVEBATCH' and ierm_paper = 'Y';
      return TRUE;

   when criteria = 'GROUPIDNOT000' and hgroup_id <> '000';
      return TRUE;

   when criteria = 'ITGROUP' and hfice = '000000' and cau_grp_id = 'IT';
      return TRUE;

   when criteria = 'MNTGROUP999' and hmnt_grp = '999';
      return TRUE;

   when criteria = 'DOGROUPLIST' and add_head = TRUE;
      return TRUE;

   when criteria = 'DOSEQUENCELIST' and add_head = FALSE;
      return TRUE;

   when criteria = 'EDITORADDMODE';                        // If Edit/Add chosen in maintenance mode
      if editMode = FALSE and add_mode = FALSE and add_head = FALSE;
         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'NOHEADER' and add_head <> TRUE;
      return TRUE;

   when criteria = 'ADDHEADER' and add_head = TRUE;
      return TRUE;

   when criteria = 'ADDSEQ#' and (add_mode = TRUE or add_head = TRUE);
      return TRUE;

   when criteria = 'ADDMODE' and add_mode = TRUE;
      return TRUE;

   when criteria = 'HAVECCSOPTIONS';
      haveCCSdata = TRUE;
      if not %open(ciccsopt2);
         open ciccsopt2;
      endif;

      sysCmd = 'OVRDBF FILE(CICCSOPTWK) TOFILE(' + PROD_LIBRARY + '/CICCSOPT2) SHARE(*NO)';

      if not %open(ciccsoptwk);
         system(%trim(sysCmd));
         open ciccsoptwk;
      endif;

      setll ('000000':happlid:hgroup_id) wrkccsrec;
      if not %equal(ciccsoptwk);
         haveCCSdata = FALSE;
      endif;

      if haveCCSdata;
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'ZEROSEQUENCE' and zseqnce = 0;
      return TRUE;

   when criteria = 'NOTZEROSEQUENCE' and zseqnce <> 0;
      return TRUE;

   when criteria = 'D2APPLID' and happlid = 'D2';
      return TRUE;

   when criteria = 'PTITLEANDPTEXT' and ptitle <> '' and ptext <> '';
      return TRUE;

   when criteria = 'ZTEXTIS!' and %subst(ztext:1:1) = '!' and iter_ctl <> 'Y';
      return TRUE;

   when criteria = 'ZTEXTISNOT!' and %subst(ztext:1:1) <> '!';
      return TRUE;

   when criteria = 'NOCCSRECORDS';
      setll (ifice:happlid:hgroup_id) ccsopt2rec;
      if not %equal(ciccsopt2);
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'HAVECCSRECORDS';
      setll (ifice:happlid:hgroup_id) ccsopt2rec;
      if %equal(ciccsopt2);
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'LOCTNALWAYS' and locationTot >= 1;
      return TRUE;

   when criteria = 'EDITLOCATION' and (editMode <> TRUE or hlocationcd <> locationDs(locIdx).ltms_on
      return TRUE;

   when criteria = 'NOEDITLOCATION' and (editMode = TRUE and hlocationcd = locationDs(locIdx).ltms_o
      return TRUE;

   when criteria = 'APPLID-TP' and productList.hasTP;
      hsys_type = 'TP';
      phnapplid = 'TP';
      return TRUE;

   when criteria = 'APPLID-D2' and productList.hasD2;
      hsys_type = 'D2';
      phnapplid = 'D2';
      return TRUE;

   when criteria = 'APPLID-ES' and productList.hasESS;
      hsys_type = 'ES';
      phnapplid = 'SS';
      return TRUE;

   when criteria = 'APPLID-PP' or criteria = 'APPLID-MS' or criteria = 'APPLID-CE' or
        criteria = 'APPLID-DP' or criteria = 'APPLID-GT' or criteria = 'APPLID-MT';

      h_applid  = %subst(criteria:(%scan('-':criteria:1)+1):2);
      phnapplid = h_applid;
      skippedAuth = FALSE;
      hsys_type = %subst(criteria:8:2);
      if checkGaProduct(h_applid:productList:go_livedt);
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'NOITSKIPBTN' and cau_grp_id <> 'IT';
      return TRUE;

   when criteria = 'IFITSHOWBTN' and cau_grp_id = 'IT';
      return TRUE;

   when criteria = 'SHOWTITLE' and hnam_title <> *blanks;
      return TRUE;

   when criteria = 'SHOWADDR2' and haddr2 <> *blanks;
      return TRUE;

   when criteria = 'ADDCONTACT' and h_key = *blanks;
      return TRUE;

   when criteria = 'UPDCONTACT' and h_key <> *blanks;
      return TRUE;

   when criteria = 'OPTOUTEMAIL' and hno_email = 'N';
      return TRUE;

   when criteria = 'UPDE2MASTER' and editModeArray(3) = TRUE;
      return TRUE;

   when criteria = 'EDITE2MASTER';
      select;
      when editModeArray(3) or needRecord3 = TRUE;
         return FALSE;
      when cau_grp_id = 'CRM';
         return TRUE;
      when %scan('U':cau_ccs) = 0;
         return FALSE;
      other;
         return TRUE;
      endsl;

   when criteria = 'ADDE2MASTER';
      select;
      when cau_grp_id = 'ACC' or needRecord3 = FALSE;
         return FALSE;
      other;
         return TRUE;
      endsl;

   when criteria = 'UPDD2MASTER' and editModeArray(2) = TRUE;
      return TRUE;

   when criteria = 'EDITD2MASTER';
      select;
      when editModeArray(2) or needRecord2 = TRUE;
         return FALSE;
      when cau_grp_id = 'CRM';
         return TRUE;
      when %scan('U':cau_ccs) = 0;
         return FALSE;
      other;
         return TRUE;
      endsl;

   when criteria = 'EDITEDUBTN';
      select;
      when editModeArray(1);
         return FALSE;
      when cau_grp_id = 'CRM';
         return TRUE;
      when %scan('U':cau_ccs) = 0;
         return FALSE;
      other;
         return TRUE;
      endsl;

   when criteria = 'UPDCXLEDU' and editModeArray(1) = TRUE;
      return TRUE;

   when criteria = 'ADDD2MASTER';
      select;
      when cau_grp_id = 'ACC' or needRecord2 = FALSE;
         return FALSE;
      other;
         return TRUE;
      endsl;

   when criteria = 'ESSEDITBTN';
      select;
      when editMode = TRUE;
         return FALSE;
      when cau_grp_id = 'CRM';
         return TRUE;
      when %scan('U':cau_ccs) = 0;
         return FALSE;
      other;
         return TRUE;
      endsl;

   when criteria = 'ONLYDPPRODUCT' and (productList.hasDP and productList.numProducts = 1);
      return TRUE;

   when criteria = 'MULTIDPPRODUCT' and (productList.hasDP and productList.numProducts > 1);
      return TRUE;

   when criteria = 'NOTADDED' and (the_recid = 'DU' and the_rate <> 0 and not added);
      added = TRUE;
      return TRUE;

   when criteria = 'RECID-GS' and the_recid = 'GS';        // Shipping Records
      return TRUE;

   when criteria = 'ONLYCEPRODUCT' and (productList.hasCE and productList.numProducts = 1);
      return TRUE;

   when criteria = 'MULTICEPRODUCT' and (productList.hasCE and productList.numProducts > 1);
      return TRUE;

   when criteria = 'CEOAUTH' or criteria = 'DPOAUTH';
      clear getThisMsg#;
      if criteria = 'CEOAUTH';
         getThisMsg# = '3026A';
      elseif criteria = 'DPOAUTH';
         getThisMsg# = '3025A';
      endif;

      if cau_grp_id <> 'SAL';
         select;
         when ino_phone = 'Y';
            getThisMsg# = '3034';
            return TRUE;
         when cau_grp_id = 'IT' or cau_grp_id = 'CRM';
            return TRUE;
         when ichargetm = 'Y';
            return TRUE;
         other;
            skippedAuth = TRUE;
            return FALSE;
         endsl;
      else;
         skippedAuth = TRUE;
         return FALSE;
      endif;

   when criteria = 'NOCEOAUTH' or criteria = 'NODPOAUTH' or criteria = 'NOPPAUTH';
      if cau_grp_id <> 'SAL';
         if skippedAuth;
            return TRUE;
            skippedAuth = FALSE;
         else;
            return FALSE;
         endif;
      else;
         return TRUE;
      endif;

   when criteria = 'CEAUTH' or criteria = 'DPAUTH' or criteria = 'PPAUTH';
      if cau_grp_id <> 'SAL';
         select;
         when cau_grp_id = 'IT' or cau_grp_id = 'CRM';
            return TRUE;
         when glive_appl = 'Y';
            return TRUE;
         other;
            skippedAuth = TRUE;
            return FALSE;
         endsl;
      else;
         skippedAuth = TRUE;
         return FALSE;
      endif;

   when criteria = 'MSOAUTH';
      if cau_grp_id <> 'SAL';
         select;
         when cau_grp_id = 'IT' or cau_grp_id = 'CRM';
            return TRUE;
         when ichargetm = 'Y';
            return TRUE;
         other;
            return FALSE;
         endsl;
      else;
         return FALSE;
      endif;

   when criteria = 'MSNOAUTH' and cau_grp_id = 'SAL';
      return TRUE;

   when criteria = 'ONLYPPPRODUCT' and (productList.hasPP and productList.numProducts = 1);
      return TRUE;

   when criteria = 'MULTIPPPRODUCT' and (productList.hasPP and productList.numProducts > 1);
      return TRUE;

   when criteria = 'GBOGUTYPE' and gbogutype <> ' ';
      tpxcode = gbogutype;
      return TRUE;

   when criteria = 'PPLIVE' and glive_appl = 'Y';
      return TRUE;

   when criteria = 'PREFIXNOTJ$$' and imsgprefix <> 'J$$';
      return TRUE;

   when criteria = 'BOGUSER' and (ga_usrtype = gbogutype and gbogutype <> *blanks);
      return TRUE;

   when (criteria = 'GAHEADER' or criteria = 'GAHEADER-H') and ga_hdrsub = 'H';
      return TRUE;

   when criteria = 'GAVALID' and %scan('VALID':%xlate(xlc:xuc:helpText)) > 0;
      return TRUE;

   when criteria = 'GANOTVALID' and %scan('VALID':%xlate(xlc:xuc:helpText)) <= 0;
      return TRUE;

   when criteria = 'GAVALIDISZERO' and (ga_validfr = 0 or ga_validto = 0);
      return TRUE;

   when criteria = 'GAVALIDNOTZERO' and ga_validfr <> 0 and ga_validto <> 0;
      return TRUE;

   when criteria = 'GAUSERTYPE' and GA_USRTYPE = 'B';
      return TRUE;

   when criteria = 'GANOTHEADER' and ga_hdrsub <> 'H';
      return TRUE;

   when criteria = 'ONLYESPRODUCT' and (productList.hasESS and productList.numProducts = 1);
      return TRUE;

   when criteria = 'MULTIESPRODUCT' and (productList.hasESS and productList.numProducts > 1);
      return TRUE;

   when criteria = 'ONLYD2PRODUCT' and (productList.hasD2 and productList.numProducts = 1);
      return TRUE;

   when criteria = 'MULTID2PRODUCT' and (productList.hasD2 and productList.numProducts > 1);
      return TRUE;

   when criteria = 'GROUPID-D2' and (cau_grp_id = 'IT' or cau_grp_id = 'CRM');
      return TRUE;

   when %scan('CONTACTEMAIL':criteria) > 0;
      krec_id = %subst(criteria:(%scan('-':criteria:1)+1):1);
      fileAccess = 'CHAIN';
      get_cntct();
      if schcnt_eml <> *blanks;
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'D2CCSOPT';
      happlid = 'D2';
      hgroup_id = 'MSC';
      return TRUE;

   when criteria = 'ONLYTPPRODUCT' and (productList.hasTP and productList.numProducts = 1);
      return TRUE;

   when criteria = 'MULTITPPRODUCT' and (productList.hasTP and productList.numProducts > 1);
      return TRUE;

   when criteria = 'TPOAUTH';
      clear getThisMsg#;
      getThisMsg# = '3022A';
      if cau_grp_id <> 'SAL';
         select;
         when ino_phone = 'Y';
            getThisMsg# = '3034';
         return TRUE;
         when cau_grp_id = 'IT' or cau_grp_id = 'CRM' or cau_grp_id = 'DOC';
            return TRUE;
         when ichargetm = 'Y' or ifice = '009998';
            return TRUE;
         other;
            return FALSE;
         endsl;
      else;
         return FALSE;
      endif;

   when criteria = 'NOTPAUTH';
      if cau_grp_id = 'CCS' and ifice = 'XPHONE';
         return TRUE;
      elseif cau_grp_id <> 'SAL';
         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'GROUPID-TP' or criteria = 'GROUPID-DP';
      if (cau_grp_id = 'IT' or cau_grp_id = 'CRM') and ifice <> 'XPHONE';
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'TPAUTH';
      clear getThisMsg#;
      getThisMsg# = '3023A';
      if cau_grp_id = 'IT' or cau_grp_id = 'DOC' or cau_grp_id = 'ACC';
         byte10 = 'DVCGITP' + %trim(itp_on_tp2) + 'T';
         if web_objectExists(byte10);
            getThisMsg# = '3019A';
         endif;
      endif;
      if cau_grp_id <> 'SAL';
         select;
         when cau_grp_id = 'IT' or cau_grp_id = 'CRM' or cau_grp_id = 'DOC';
            return TRUE;
         when ichargetm = 'Y' or ifice = '009998';
            return TRUE;
         other;
            return FALSE;
         endsl;
      else;
         return FALSE;
      endif;

   when criteria = 'TSTREM' and (hfice = '009998' or hfice = '000000');
      return TRUE;

   when criteria = 'TPLIVE' and ilive_tp <> 0;
      return TRUE;

   when criteria = 'TPNOTLIVE' and ilive_tp = 0;
      return TRUE;

   when criteria = 'SEECONTACTS-T';
      krec_id = %subst(criteria:(%scan('-':criteria:1)+1):1);
      fileAccess = 'CHAIN';
      get_cntct();

      if %scan('SEE CONTACTS':%xlate(xlc:xuc:schcnt_nam)) > 0;
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'HASTPFAX2';
      krec_id = 'S';
      fileAccess = 'CHAIN';
      get_cntct();

      if institl4Found = FALSE;                            // If not found
         return FALSE;
      else;
         return TRUE;
      endif;

   when criteria = 'TPSENDPDF';
      het_senda = iet_senda;
      if %lookup('AL':har_etsend) > 0 or %lookup('AC':har_etsend) > 0 or %lookup('AE':har_etsend) >
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'ISRESEND0090' and itp_resend = '0090';
      return TRUE;

   when criteria = 'ISRESEND0091' and itp_resend = '0091';
      return TRUE;

   when criteria = 'ISRESEND0092' and itp_resend = '0092';
      return TRUE;

   when criteria = 'NORESENDPLCY' and itp_resend = *blanks;
      return TRUE;

   when criteria = 'BETWEENONOFF' and (cycle_date > tp_dateoff and cycle_date < tp_dateon);
      return TRUE;

   when criteria = 'DATEGTTHANOFF' and (cycle_date > tp_dateoff and tp_dateon < tp_dateoff);
      return TRUE;

   when criteria = 'DATEEQUALOFF' and (cycle_date = tp_dateoff and cycle_time > tp_timeoff);
      return TRUE;

   when criteria = 'DATEEQUALON' and (cycle_date = tp_dateon and cycle_time <= tp_timeon);
      return TRUE;

   when criteria = 'KIOSKITEMS' and haveKioskItems = TRUE;
      return TRUE;

   when criteria = 'ONOFFTEXT' and (tp_dateoff <> 0 or tp_dateon  <> 0);
      return TRUE;

   when criteria = 'NOTXPHONE' and hfice <> 'XPHONE';
      return TRUE;

   when criteria = 'HAVEETPOPT';
      if ilive_edi  > 0 or ilive_xml  > 0 or ilive_asci > 0 or ilive_3pdf > 0 or
         ilive_spdf > 0 or ilive_dir <> *blanks;

         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'TPLOGIC' and it_stu_lrh = 'A';
      return TRUE;

   when criteria = 'TPAPOSTHANDLE' and it_apo_lrh <> '';
      return TRUE;

   when %scan('CCSOPT-':criteria:1) > 0;
      happlid = phnapplid;
      hgroup_id = %subst(criteria:(%scan('-':criteria:1)+1):3);
      return TRUE;

   when %scan('PANEL-':criteria:1) > 0;
      if %subst(criteria:(%scan('-':criteria:1)+1):3) = hscrn_type;
         return TRUE;
      else;
         return FALSE;
      endif;

   when criteria = 'AUTOCOMPLETE' and panel <> #DSP_CCS;
      return TRUE;

   when criteria = 'DSPFICECHANGE' and panel <> #CON_EDIT and panel <> #EDTMNT;
      return TRUE;

   when criteria = 'EDITCONTACT' and panel = #CON_EDIT;
      return TRUE;

   other;
      return FALSE;
   endsl;

end-proc;

// ***************************************************************************************
// processLoop(): Process a html 'LOOP' variable
// ***************************************************************************************
dcl-proc processLoop;
   dcl-pi *n;
      template like(smallBuffer) const;
      criteria like(HTML_PARM) const;
   end-pi;

   dcl-s workbuffer like(smallBuffer);
   dcl-s tempIdx    int(5) inz(0);                                   //SG01

   pssrRoutine = 'processLoop : ([LOOP,' + %trim(criteria) + '])';
   if pssrTriggeredVar <> *blanks;
      if pssrTriggeredVar = criteria;
         return;
       endif;
   endif;

   select;

   when criteria = 'DOFICE';
      if not %open(dvinstitl7);
         open dvinstitl7;
      endif;
      setll *start dvinstitl7;
      read ficegrprec;
      dow not %eof(dvinstitl7);
         if %subst(ffice:1:2) = 'XX' or %subst(ffice:1:2) = 'SI';
            read ficegrprec;
            iter;
         endif;

         tempIdx += 1;
         if httpAccept = 'json' and tempIdx > 1;                    //SG01
            web_addToBuffer(',');                                    //SG01
         endif;                                                      //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
         read ficegrprec;
      enddo;

   when criteria = 'DOCHECKBOX';
      for lp = 1 to ets_size;
         if et_send(lp) = *blanks;
            iter;
         endif;

         if %lookup(et_send(lp):har_etsend) = 0;
            haveETsenda = FALSE;
         elseif %lookup(et_send(lp):har_etsend) > 0;
            haveETsenda = TRUE;
         endif;

         if httpAccept = 'json' and lp > 1;                          //SG01
            web_addToBuffer(',');                                    //SG01
         endif;                                                      //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   when criteria = 'GENEDREQ1' or criteria = 'GENEDREQ2' or criteria = 'GENEDREQ3';
      select;
      when criteria = 'GENEDREQ1';
         hgenedtype = hgenedreq1;
      when criteria = 'GENEDREQ2';
         hgenedtype = hgenedreq2;
      when criteria = 'GENEDREQ3';
         hgenedtype = hgenedreq3;
      endsl;

      optselected = FALSE;

      for idx1=1 to %elem(gened_typ);
         if gened_typ(idx1) = hgenedtype;
            optselected = TRUE;
         endif;

         if httpAccept = 'json' and idx1 > 1;
            web_addToBuffer(',');
         endif;
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   when criteria = 'SCHOOLMSGS';                           // Select Banner Messages
      optselected = FALSE;
      for idx1=1 to 3;
         if schmsgopt(idx1) = ischmsgctl;
            optselected = TRUE;
         endif;

         if httpAccept = 'json' and idx1 > 1;                         //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   when criteria = 'NOREASONS';                            // Select/Ask for NO Reason
      optselected = FALSE;
      for idx1=1 to 2;
         if norsnopt(idx1) = inoreason;
            optselected = TRUE;
         endif;

         if httpAccept = 'json' and idx1 > 1;                         //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   when criteria = 'TPNOOTHER';                            // Select itb_noothr
      optselected = FALSE;
      for idx1=1 to 2;
         if noothopt(idx1) = itb_noothr;
            optselected = TRUE;
         endif;
                                                                      //SG01
         if httpAccept = 'json' and idx1 > 1;                         //SG01
            web_addToBuffer(',');                                     //SG01
         endif;
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   when criteria = 'PDFROWFORMAT';                         // Put out a format table row
      for formatIdx = 1 to formatTot;
         if httpAccept = 'json' and formatIdx > 1;                    //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   when criteria = 'MNT1OPTIONS' or criteria = 'TPOPTIONS';
      optselected = FALSE;
      isEqual = TRUE;

      if criteria = 'TPOPTIONS';
         happlid = 'TP';
      endif;

      if not %open(ciccsopt2);
         open ciccsopt2;
      endif;

      setll ('000000':happlid) ccsopt2rec;
      if not %equal(ciccsopt2);
         isEqual = FALSE;
      endif;

      reade(n) ('000000':happlid) ccsopt2rec;
      dow not %eof(ciccsopt2) and isEqual = TRUE;
         if pseqnce = 0;
            if hgroup_id = pgroup_id;
               optselected = TRUE;
            endif;
            tempIdx += 1;                                             //SG01
            if httpAccept = 'json' and tempIdx > 1;                   //SG01
               web_addToBuffer(',');                                  //SG01
            endif;                                                    //SG01
            web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                                 %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
         endif;

         reade(n) ('000000':happlid) ccsopt2rec;
      enddo;

   when criteria = 'GROUPLIST';                            // List of existing group id's
      isEqual = TRUE;

      setll (hfice:happlid) ccsopt2rec;
      if not %equal(ciccsopt2);
         isEqual = FALSE;
      endif;

      reade(n) (hfice:happlid) ccsopt2rec;
      dow not %eof(ciccsopt2) and isEqual = TRUE;
         if pseqnce = 0;
            tempIdx += 1;                                             //SG01
            if httpAccept = 'json' and tempIdx > 1;                   //SG01
               web_addToBuffer(',');                                  //SG01
            endif;                                                    //SG01
            web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                                 %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
         endif;

         reade(n) (hfice:happlid) ccsopt2rec;
      enddo;

   when criteria = 'SEQLIST';                              // List of sequence #s for a group id
      isEqual = TRUE;

      setll (hfice:happlid:hgroup_id) ccsopt2rec;
      if not %equal(ciccsopt2);
         isEqual = FALSE;
      endif;

      reade(n) (hfice:happlid:hgroup_id) ccsopt2rec;
      dow not %eof(ciccsopt2) and isEqual = TRUE;
         if pseqnce > 0;
            tempIdx += 1;                                             //SG01
            if httpAccept = 'json' and tempIdx > 1;                   //SG01
               web_addToBuffer(',');                                  //SG01
            endif;                                                    //SG01
            web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                                 %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
         endif;

         reade(n) (hfice:happlid:hgroup_id) ccsopt2rec;
      enddo;

   when criteria = 'CCSOPTIONS';                           // Put out CCS options
      reade ('000000':happlid:hgroup_id) wrkccsrec;
      dow not %eof(ciccsoptwk);
         if zseqnce <> 0;
            select;
            when %subst(ztext:1:1) = '!';
               value = %subst(ztext:2);
               rowtext1 = ' ';
               rowtext2 = ' ';
               if iter_ctl = 'Y';
                  reade ('000000':happlid:hgroup_id) wrkccsrec;
                  clear iter_ctl;
                  iter;
               endif;
            other;
               if value <> 'RESEND';
                  rowtext1 = %trim(ztext);
                  rowtext2 = *blanks;
               endif;
            endsl;
         endif;

         tempIdx += 1;                                                //SG01
         if httpAccept = 'json' and tempIdx > 1;                      //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));

         if zseqnce <> 0 and %subst(ztext:1:1) = '!';
            clear ztext;
         endif;

         reade ('000000':happlid:hgroup_id) wrkccsrec;
      enddo;

   when criteria = 'CCSOPT2RECORDS';
      reade(n) (ifice:happlid:hgroup_id) ccsopt2rec;
      dow not %eof(ciccsopt2);
         tempIdx += 1;                                                //SG01
         if httpAccept = 'json' and tempIdx > 1;                      //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));

         reade(n) (ifice:happlid:hgroup_id) ccsopt2rec;
      enddo;

   when criteria = 'LOCATIONCODE';                         // Put out location codes
      locationDs = tploc_getLocations(hfice:locationTot);
      for locIdx = 1 to locationTot;
         if httpAccept = 'json' and locIdx > 1;                       //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   when criteria = 'PRINTLOCATIONS';                       // Print location codes
      optselected = FALSE;
      for idx1=1 to locationTot;
         if hcredp_onl = locationDs(idx1).ltms_onlin;
            optselected = TRUE;
         endif;

         if httpAccept = 'json' and idx1 > 1;                         //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   when criteria = 'CONTACTINFO';                          // Put out contact information
      isContact = TRUE;
      if not %open(dvinstitl4);
         open dvinstitl4;
      endif;

      setll (hfice) cntct_l4;
      if not %equal(dvinstitl4);
         isContact = FALSE;
      endif;

      reade (hfice) cntct_l4;
      dow not %eof(dvinstitl4) and isContact = TRUE;

         hnam_title = mtitle;
         hfrstname = mfrstname;
         hmidlname = mmidlname;
         hlastname = mlastname;

         clear wfullname;
         wfullname = %trim(msalut);
         wfullname = %trim(wfullname) + ' ' + %trim(mfrstname);
         wfullname = %trim(wfullname) + ' ' + %trim(mmidlname);
         wfullname = %trim(wfullname) + ' ' + %trim(mlastname);
         wfullname = %trim(wfullname);

         if mnickname <> mfrstname and mnickname <> *blanks;
            wfullname = %trim(wfullname) + ' (' + %trim(mnickname) + ')';
         endif;

         hcompany = mcompany;
         if mcompany = *blanks;
            hcompany = yschname;
         endif;

         haddr1 = maddr1;
         haddr2 = maddr2;
         hcity = mcity;
         hstate = mstate;
         hpostcd = mpostcd;
         hcntry = mcntry;

         if maddr1 = *blanks;
            haddr1 = iaddr1;
            haddr2 = iaddr2;
            hcity = icity;
            hstate = istate;
            hpostcd = ipostcd;
            hcntry = icntry;
         endif;

         htel# = %trim(mtelnum) + ' X' + %trim(mtelextn);

         if mtelnum = *blanks;
            htel# = 'N/A';
         endif;
         hemail = memail;

         tempIdx += 1;                                                //SG01
         if httpAccept = 'json' and tempIdx > 1;                      //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));

         reade (hfice) cntct_l4;

      enddo;

   when criteria = 'SALUTATIONS';                          // Salutations
      optselected = FALSE;
      for idx1=1 to 5;
         if hsalut = salut(idx1);
            optselected = TRUE;
         endif;

         if httpAccept = 'json' and idx1 > 1;                         //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   when criteria = 'CONUSERS';                             // Contact User Details
      optselected = FALSE;
      for idx1=1 to %elem(tab_conlet);
         if husrtype = ar_conlet(idx1);
            optselected = TRUE;
         endif;

         if httpAccept = 'json' and idx1 > 1;                         //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));

         if ar_conlet(idx1) = *blanks;
            leave;
         endif;

      endfor;

   // GA options for Diploma CCS
   when criteria = 'GVAROPTIONS3-GP' or criteria = 'GVAROPTIONS3-DU' or criteria = 'GVAROPTIONS3-GS'
      the_recid = %subst(criteria:(%scan('-':criteria:1)+1):2);
      h_applid = 'DP';
      haveGAoptions = TRUE;
      if not %open(gaoption1#);
         open gaoption1#;
      endif;

      setll (hfice:h_applid:the_recid) ga_parms;
      if not %equal(gaoption1#);
         haveGAoptions = FALSE;
      endif;

      reade (hfice:h_applid:the_recid) ga_parms;
      dow not %eof(gaoption1#) and haveGAoptions = TRUE;

         // Skip: down options, header rows, and diploma types w/o cost
         if ga_tempdwn = 'Y' or ga_hdrsub = 'H' or (the_recid = 'DU' and ga_rate = 0);
            reade (hfice:h_applid:the_recid) ga_parms;
            iter;
         endif;

         // Pull GAMSGS text for messages found in ga_help
         clear helpText;
         select;
         when '(((MSG))' = %subst(ga_help:1:8);
            getMsgDs = %subst(ga_help:9:13);
            helpText = %trim(getMessage(msg_defalt:getMsg#:getMsgParms:'Y'));

            // Remove links and input sections for certain messages
            select;
            when (ga_fice = '001776' or ga_fice = '001671') and %scan('7010':ga_help) > 0;
               helpText = %subst(helpText:1:%scan('.<p>Destination Country:':helpText));
            when ga_fice = '003644' and %scan('7009':ga_help) > 0;
               helpText = %subst(helpText:1:%scan(' For more information, <a':helpText));
            endsl;
         when ga_help <> *blanks;
            helpText = %trim(ga_help);
         endsl;

         // Setup td_cell1 for the Text column
         the_rate = ga_rate;

         tempIdx += 1;                                                //SG01
         if httpAccept = 'json' and tempIdx > 1;                      //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));

         reade (hfice:h_applid:the_recid) ga_parms;

      enddo;

   // GA options for Parking Permit CCS
   when criteria = 'GVAROPTIONS' or criteria = 'GVAROPTIONS2';
      the_recid = 'GP';
      haveGAoptions = TRUE;

      if not %open(gaoption1#);
         open gaoption1#;
      endif;

      setll (hfice:h_applid:the_recid) ga_parms;
      if not %equal(gaoption1#);
         haveGAoptions = FALSE;
      endif;

      reade (hfice:h_applid:the_recid) ga_parms;
      dow not %eof(gaoption1#) and haveGAoptions = TRUE;

         if criteria = 'GVAROPTIONS';
            select;
            when ga_tempdwn = 'Y';                         // Permit temp down, skip
               reade (hfice:h_applid:the_recid) ga_parms;
               iter;
            when ga_categry = 'R';   // items that only show in RSS
               reade (hfice:h_applid:the_recid) ga_parms;
               iter;
            when ga_ef_datf <> 0 or ga_ef_datt <> 0 or     //Has effective dates or valid dates, che
                 ga_validfr <> 0 or ga_validto <> 0;
               if (cycle_date >= ga_validfr and cycle_date <= ga_validto) or
                  (cycle_date >= ga_ef_datf and cycle_date <= ga_ef_datt);
               else;
                  reade (hfice:h_applid:the_recid) ga_parms;
                  iter;
               endif;
            endsl;
         endif;

         if criteria = 'GVAROPTIONS2';
            // Criterial that will make us skip the record, do not write out permits that should onl
            // seen in RSS or permits that are currently on sale or are old but do not skip
            // Headers for permits which have 0 effective dates
            if ga_categry = 'R' or (ga_ef_datf < cycle_date and ga_ef_datf <> 0);
               reade (hfice:h_applid:the_recid) ga_parms;
               iter;
            endif;
         endif;

         clear helpText;
         select;
         when '(((MSG))' = %subst(ga_help:1:8);
            getMsgDs = %subst(ga_help:9:13);
            helpText = %trim(getMessage(msg_defalt:getMsg#:getMsgParms:'Y'));

         when ga_help <> *blanks;
            if %scan('VALID':%xlate(xlc:xuc:ga_help)) > 0;
               if ga_validfr <> 0 or ga_validto <> 0;
                  helpText = 'Valid from: ' + %trim(dspTmStamp(ga_validfr:0:0:'*4YR')) +' to '+
                              %trim(dspTmStamp(ga_validto:0:0:'*4YR'));
               else;
                  helpText = %trim(ga_help);
               endif;
            endif;
         endsl;

         if ga_hdrsub = 'H';
         else;
            if the_recid = 'GP';                           // Product records
               // If gaoption1 charges not set, use gamaster charges
               if ga_rhandle = 0 and ga_mhandle = 0;
                  wrhandle = g_rhandle;
               else;
                  wrhandle = ga_rhandle;
               endif;

               if ga_rhdlcod = 0 and ga_mhdlcod = 0;
                  wrhdlcod = g_rhdlcod;
               else;
                  wrhdlcod = ga_rhdlcod;
               endif;

               if wrhandle <> 0;
                  xrhandle = ' + $' + %trim(%editc(wrhandle:'3')) + ' (for CC orders)';
               else;
                  xrhandle = *blanks;
               endif;

               if wrhdlcod <> 0;
                  xrhdlcod = '<br /> + $' + %trim(%editc(wrhdlcod:'3')) + ' (for COD orders)';
               else;
                  xrhdlcod = *blanks;
               endif;
            endif;

            clear byte500;
            clear effectiveDate;

            select;
            when criteria = 'GVAROPTIONS';
               effectiveDate = 0;
            when criteria = 'GVAROPTIONS2';
               effectiveDate = cycle_date;
            endsl;

            // Available Dates
            if ga_ef_datf > effectiveDate and ga_ef_datt > effectiveDate;
               byte500 = %trim(byte500) + 'Dates Available for ' + 'Purchase:&nbsp;&nbsp;' +
                         %trim(dspTmStamp(ga_ef_datf:0:0:'*4YR')) + '&nbsp;to&nbsp;' +
                         %trim(dspTmStamp(ga_ef_datt:0:0:'*4YR')) + '<br />';
            endif;

            // Temp permits
            if ga_tempdat > effectiveDate;
               byte500 = %trim(byte500) + 'Temp Permit Available ' + 'Starting:&nbsp;' +
                         %trim(dspTmStamp(ga_tempdat:0:0:'*4YR')) + '<br />';

               if ga_tempdys > 0;
                  byte500 = %trim(byte500) + 'Temp Permit valid for <b>' +
                            %trim(%char(ga_tempdys)) + '</b> days';
               else;
                  byte500 = %trim(byte500) + 'Temp Permit days not set';
               endif;
            else;
               byte500 = %trim(byte500) + 'Temp Permits are not available';
            endif;
         endif;

         tempIdx += 1;                                                //SG01
         if httpAccept = 'json' and tempIdx > 1;                      //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));

         reade (hfice:h_applid:the_recid) ga_parms;

      enddo;
      close gaoption1#;

   // Service options for TP Application
   when criteria = 'BASEOPTIONS-TB' or criteria = 'ETPOPTIONS-TM' or criteria = 'SHIPOPTIONS-TS';
      the_recid = %subst(criteria:(%scan('-':criteria:1)+1):2);
      haveTPoptions = TRUE;

      if not %open(dvinstit5);
         open dvinstit5;
      endif;

      setll (ifice:the_recid) tmsparms;
      if not %equal();
         haveTPoptions = FALSE;
      endif;

      reade (ifice:the_recid) tmsparms;
      dow not %eof(dvinstit5) and haveTPoptions = TRUE;
         if tp_categry = 'R';
            reade (ifice:the_recid) tmsparms;
            iter;
         endif;

         iter_ctl = 'N';
         if tp_dateoff <> 0 or tp_dateon  <> 0;
            select;
            when cycle_date > tp_dateon and tp_dateoff < tp_dateon;
               iter_ctl = 'N';                             // Today is gt ond and offd is 0
            when cycle_date = tp_dateoff and cycle_time <= tp_timeoff;
               iter_ctl = 'N';                             // Today = offd and time <= offtime
            when cycle_date = tp_dateon and cycle_time > tp_timeon;
               iter_ctl = 'N';                             // Today = ond and time > ontime
            endsl;

            if iter_ctl = 'Y';
               reade (ifice:the_recid) tmsparms;
               iter;
            endif;
         endif;

         // Do NOT show for REGINPUT Items
         if tp_categry = 'I';
            reade (ifice:the_recid) tmsparms;
            iter;
         endif;

         // Do NOT show for KIOSK Items
         kiosktext = *blanks;
         haveKioskItems = FALSE;
         if tp_categry  = 'K';
            kiosktext = '*** AVAILABLE ON CAMPUS ONLY ***';
            haveKioskItems = TRUE;
         endif;

         if tp_recid = 'TM';
            select;
            when (tp_value = 'P') or                       // print option
                 (tp_value = 'D' and ilive_3pdf = 0) or    // 3rd party pdf
                 (tp_value = 'A' and ilive_spdf = 0) or    // sch2sch pdf
                 (tp_value = 'E' and (ilive_edi = 0 and ilive_xml = 0 and ilive_asci = 0 and
                  ilive_dir = *blanks));                   // electronic

               reade (ifice:the_recid) tmsparms;
               iter;
            endsl;

            if tp_value = 'E' and (%lookup('DU':har_etsend) > 0 or %lookup('FU':har_etsend) > 0);
               kiosktext = '*** ELECTRONIC DIRECT FROM SCHOOL ***';
               haveKioskItems = TRUE;
            endif;
         endif;

         if '(((MSG))' = %subst(tp_help:1:8);
            getMsgDs = %subst(tp_help:9:13);
            helpText = %trim(getMessage(msg_defalt:getMsg#:getMsgParms:'Y'));
         else;
            helpText = %trim(tp_help);
         endif;

         if the_recid = 'TB' or the_recid = 'TM' or the_recid = 'TS' or the_recid = 'TX';
            the_rate = tp_q_rate + tp_q_base;
         endif;

         tempIdx += 1;                                                //SG01
         if httpAccept = 'json' and tempIdx > 1;                      //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));

         reade (ifice:the_recid) tmsparms;
      enddo;

   // PDF file path and names
   when criteria = 'LOADFILES';
      for idx=1 to pf#;
         if httpAccept = 'json' and idx > 1;                          //SG01
            web_addToBuffer(',');                                     //SG01
         endif;                                                       //SG01
         web_replaceVariables(template:%trim(rootFilePath):%paddr('GETVARVALUES'):
                              %paddr('PROCESSIF'):%paddr('PROCESSLOOP'):%paddr('PROCESSSWITCH'));
      endfor;

   other;

      return;
   endsl;

   return;

end-proc;

// ***************************************************************************************
// processSwitch(): Process a html 'SWITCH' variable
// ***************************************************************************************
dcl-proc processSwitch;
   dcl-pi *n like(HTML_PARM);
      criteria like(HTML_PARM) const;
   end-pi;

   pssrRoutine = 'processSwitch : ([SWITCH,' + %trim(criteria) + '])';
   if pssrTriggeredVar <> *blanks;
      if pssrTriggeredVar = criteria;
         return '';
      endif;
   endif;

   select;

   when criteria = 'PANELTITLE';                           // Panel Title
      select;
      when panel = #DSP_CCS or panel = #EDTMNT;
         return 'SCHOOLOPTIONS';

      when panel = #DSP_CSR;
         return 'RESENDDATA';

      when panel = #DSP_CNT;
         return 'SCHOOLCONTACTS';

      when panel = #DSP_TP or panel = #DSP_ESS or panel = #DSP_EDU or panel = #DSP_LOC;
         return 'TPDATA';

      when panel = #DSP_BSC;
         return 'BASICINFO';

      when panel = #DSP_PRNT;
         return 'ROBOMAIL';

      when panel = #DSP_GA;
         return 'GADATA';

      when panel = #DSP_PDF;
         return 'PDFSETUP';

      when panel = #CON_EDIT;
         return 'CONTACTS';

      other;
         return 'OTHER';
      endsl;

   other;
      return '';

   endsl;

   return '';

end-proc;

// ***************************************************************************************
// validMsg: Check for validity of message number
// ***************************************************************************************
dcl-proc validMsg;
   dcl-pi *n ind;
      $email char(50) const;
      $userType char(1) const;
   end-pi;

   dcl-c validChars '0123456789';

   if %subst(%trim($email):1:8) = '(((MSG))' and %check(validChars:%subst(%trim($email):9:4)) = 0 an
      %len(%trim($email)) = 12 and $userType = 'I';

      return TRUE;
   endif;

   return FALSE;
end-proc;

// ***************************************************************************************
// cleanInptTxt(): Clean input data of any bad data
// ***************************************************************************************
dcl-proc cleanInptTxt;
   dcl-pi *n char(80);
      theText char(80) const;
   end-pi;

   dcl-c numbers const(' 0123456789-.');
   dcl-s validChars char(65);
   dcl-s wrkText varchar(1000);

   validChars = xuc + xlc + numbers;

   wrkText = theText;
   if wrkText <> *blanks;
      if %check(validChars:%trim(wrkText)) = 0 and %scan('..':wrkText) = 0 and %scan('--':wrkText) =
         return wrkText;
      endif;

      wrkText = web_sanitize(wrkText);
   endif;

   return wrkText;

end-proc;
// ********************************************************************* //SG01
// getHttpAccept - gen environment variable Accept                       //SG01
// ********************************************************************* //SG01
dcl-proc getHttpAccept;
dcl-pi *n like(httpAccept);
end-pi;

// Get the Environment variable, REMOTE_ADDR.
clear EnvRec;
EnvName    = 'HTTP_ACCEPT';
EnvNameLen = 11;
callp APIGetEnv(EnvRec:EnvReclen:EnvLen:EnvName:EnvNameLen:QUSEC);
return  %subst(EnvRec:1:EnvLen);

end-proc;

// ********************************************************************* //SG01
// parseJson - Parse JSON body to HTMLForm                               //SG01
//  parms                                                                //SG01
//    htmlForm - the Form array of Key/value pairs. repurposed
//    Buffer   - the input Buffer containing valid json
//    BufferLen - Buffer length
//  returns number of elements extracted or -1 for error
// *********************************************************************
dcl-proc parseJSON;
dcl-pi *n like(maxParms);
   json  likeds(htmlForm);
   inBuffer like(Bufin);
   inBufferLen  like(bufInLn) const;
   maxParms int(10) const;
end-pi;

// yajl variables
/include yajl/QRPGLESRC,yajl_h

dcl-s yajlErrMsg varchar(500) inz('');
dcl-s docNode like(yajl_val);
dcl-s iYajl   int(10);
dcl-s key     varchar(50);
dcl-s val     like(yajl_val);

json.numInputs = 0;

docNode = yajl_buf_load_tree(
   %addr(inBuffer) : inbufferLen : yajlErrMsg );

if yajlErrMsg <> '';

   json.input(1).data = yajlErrMsg;  // handle error
   return -1;
endif;

iYajl = 0;
dow YAJL_OBJECT_LOOP( docNode: iYajl: key: val);
  if iYajl > maxParms;
     leave;
  endif;
  // Put Key / Val in Html arrays
  json.input(iYajl).name = key;
  json.input(iYajl).data = yajl_get_string(val);
enddo;

json.numInputs = iYajl;

return iYajl;

end-proc;

// ********************************************************************* //SG01
// setPanelToJSON - set/switch file extension to JSON                    //SG01
// ********************************************************************* //SG01
dcl-proc setPanelToJSON;
dcl-pi *n like(panelFile);
   currentPanel like(panelFile) const;
   newExtension like(httpAccept) const;
end-pi;
dcl-s newPanel  like(panelFile);
dcl-s p int(5);

// The panel File default file extension is .html
// and will only be used to change to .json
// This code will scan for a 'dot' in the filename and
// replace or add the newExtension

p = %SCANR('/' : currentPanel);
if p = 0;
   p = 1; // filename starts at the beginning
endif;
p = %SCANR('.' : currentPanel : p);
if p = 0;
   // if no dot found just append the newExtension
   newPanel = currentPanel + '.' + newExtension;
else;
   newPanel = %SUBST(currentPanel : 1 : p) + newExtension;
endif;
return  newPanel;

end-proc;

// ********************************************************************* //SG01
// sanitizeJSONResp: Escape special characters in JSON response          //SG01
// ********************************************************************* //SG01
dcl-proc sanitizeJSONResp;
   dcl-pi *n like(#wp_out.result);
      inReturnVal like(#wp_out.result);
   end-pi;


   inReturnVal = %scanrpl('\':'\\':inReturnVal);    //Escape Back Slash
   inReturnVal = %scanrpl('"':'\"':inReturnVal);    //Escape Double Quotes
   inReturnVal = %scanrpl('/':'\/':inReturnVal);    //Escape Forward Slash
   inReturnVal = %scanrpl(x'16':'\b':inReturnVal);  //Escape Backspace
   inReturnVal = %scanrpl(x'0C':'\f':inReturnVal);  //Escape Form Feed
   inReturnVal = %scanrpl(x'15':'\n':inReturnVal);  //Escape New Line
   inReturnVal = %scanrpl(x'0D':'\r':inReturnVal);  //Escape Carriage Return
   inReturnVal = %scanrpl(x'05':'\t':inReturnVal);  //Escape Tab

   return inReturnVal;

end-proc;

// ***************************************************************************************
// parseForm()
// ***************************************************************************************
/copy rpgcopy,parsinp_sp

/eject

// ***************************************************************************************
// Compile-time array follows:
// ***************************************************************************************
/copy rpgcopy,parsetbl
**    salut    CTDATA
    MR. MRS.MS. DR.
**   GENED_TYP CTDATA

CUNY
SUNY
UCAL
CSU
UNCC
UNCW
**   SCHMSGOPT/SCHTXTOPT CTDATA
  Message Files - Credentials edit
T Text Based - School Edit
C Converting - Show both
**   NORSNOPT/NORSNTXT CTDATA
N No, Do not ask for reason
  Yes, Ask for reason
**   NOOTHOPT/NOOTHTXT CTDATA
  ON
Y OFF
**   tab_conlet ======================================================
A Admissions and Records
B Business Officer
C Contact for Fax/Mail of C.O.D. Transcript Orders
H HR Manager
I Diploma Address/Fax number for Authorizations
K Diploma Re-Order Contact
L Meeting Contact
M Registrar
O Over the Counter Permit Mailing Address
P Police Chief (address is return address for permits)
R Registrar
S Transcript Authorization Fax - SCHOOL
T Daily TP Contact
X Secondary TP Contact
1 DV Authorization Fax
2 Transcript Authorization Fax
3 eRoboMail Contact/Mailing Address
4 registrar management notifications
8 Transcript confidential fax + Attn:
** CTDATA ET_Send/ET_descrpt - used for description and code of et_send text
EC EC - EDI Credentials Network
ES ES - EDI SPEEDE
XS XS - XML SPEEDE
XO XO - XML OBOR
TX TX - TXT eTranCA
AL AL - PDF TranscriptsNetwork via eSS
AC AC - PDF TranscriptsNetwork
AE AE - PDF Third Party
DU DU - School Direct
FU FU - School Direct (Faster)
MU MU - School Direct (Manual)
PC PC - eRoboMail
** CTDATA pdfSigner/pdfSignerText - used for description and code of et_send text
  Printing = Yes, Screen Readers = Yes
P Printing = Yes, Screen Readers = No
A Printing = No, Screen Readers = Yes
L Printing = No, Screen Readers = No
S Signed, Printing = Yes, Screen Readers = Yes
R Signed, Printing = Yes, Screen Readers = No
B Signed, Printing = No, Screen Readers = Yes
N Signed, Printing = No, Screen Readers = No
