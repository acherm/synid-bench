      *****************************************************************
     h copyright('(C) Copyright 1996 - 2005 King III Solutions, Inc.  +
     h Rel 4.36 2005-07-01       Program Property of King III Solutions, Inc. +
     h All rights reserved              +
     h K3S_Replenish (R) is a Registered Trade Mark of King III Solutions Inc.')

     h FIXNBR(*ZONED) AUT(*ALL)
     h OPTION(*NODEBUGIO)
     h BNDDIR('K3S_BNDDIR')
      *****************************************************************
      **
      **   K3S-Replenish (R) - Inventory REPLENISHment System
      **   Copyright (C) 1996-2005 by King III Solutions, Inc.
      **   Program property of King III Solutions, Inc.
      **   All rights reserved.
      **   K3S_Replenish (R) is a Registered Trade Mark of
      **   King III Solutions Inc.
      **
      *****************************************************************
      **
      **   Name: K3S_9100
      **   Type: ILE RPG Program
      **   Desc: Convert alternate source entries to K_INTALTR
      **
      *****************************************************************
      **
      **  This program will read the alternate source entries from 15
      **  different files, edit them, and place transactions into 1 file.
      **
      **  This program will also write records to k_logaltr file.
      **
      *****************************************************************

     fk_altsrc01ip   f   80        disk
      * alternate source entries for k_altsrc01

     fk_altsrc02is   f   80        disk
      * alternate source entries for k_altsrc02

     fk_altsrc03is   f   80        disk
      * alternate source entries for k_altsrc03

     fk_altsrc04is   f   80        disk
      * alternate source entries for k_altsrc04

     fk_altsrc05is   f   80        disk
      * alternate source entries for k_altsrc05

     fk_altsrc06is   f   80        disk
      * alternate source entries for k_altsrc06

     fk_altsrc07is   f   80        disk
      * alternate source entries for k_altsrc07

     fk_altsrc08is   f   80        disk
      * alternate source entries for k_altsrc08

     fk_altsrc09is   f   80        disk
      * alternate source entries for k_altsrc09

     fk_altsrc10is   f   80        disk
      * alternate source entries for k_altsrc10

     fk_altsrc11is   f   80        disk
      * alternate source entries for k_altsrc11

     fk_altsrc12is   f   80        disk
      * alternate source entries for k_altsrc12

     fk_altsrc13is   f   80        disk
      * alternate source entries for k_altsrc13

     fk_altsrc14is   f   80        disk
      * alternate source entries for k_altsrc14

     fk_altsrc15is   f   80        disk
      * alternate source entries for k_altsrc15

     fk_companyaif   e           k disk
      * companys by company id

     fk_suplierbif   e           k disk
      * suppliers by locn, supl

     fk_supliercif   e           k disk    rename(rk_suplier:rx_suplier)        suppliers
      * suppliers by supl

     fk_locatnsaif   e           k disk
      * locations by locn

     fk_producteif   e           k disk
      * products by locn, ndc_upc

     fk_productcif   e           k disk    rename(rk_product:r1_product)
      * products by locn, product

     fk_productgif   e           k disk    rename(rk_product:r2_product)
      * products by product,locn

      **NDC_UPC start
     fk_producthif   e           k disk    rename(rk_product:r3_product)
      * products by product,locn

      **NDC_UPC end
     fk_intaltreuf a e           k disk
      * alternate source entries by locn, suplalt, suplals, prod

     fk_prodrstaif   e           k disk
      * products with a restricted quantity by locn, product

     fk_dealperbif   e           k disk
      * Permanent deals file

     fk_logaltr o    e             disk
      * alternate source entries into weekly offerings file

     fk_suplrej o    e             disk
      * alternate source entries rejected summary file

     fk3s_p9100 o    e             printer oflind(over_flow)
      * printer file

      * ----------------------------------------------------- get time stamp
     d upc#            s             13                                         user date format
     d lda_usrdat      s              4                                         user date format
     d lda_usrtim      s              4                                         user time format
     d lda_usradj      s              3p 0                                      user time adj. hours

      * --------------------------------------------------------- Workfields
     d time_stamp      s               z   inz                                  time stamp
     d time            s               t                                        time
     d date            s               d                                        date
     d x               s              3p 0                                      # valid locations
     d y               s              3p 0                                      step through locns
     d i               s              3p 0                                      step through locns
     d first_page      s              1                                         first page printed
     d last_supl       s                   like(altsrc)                         last supplier read
      * Permenant Deal fields
     d disc_each       s             11  4                                      Discount value each
     d trlocn          s                   like(pr_locn)                        last supplier read
     d trsuplorg       s                   like(pr_suplorg)                     last supplier read
     d trsuplors       s                   like(pr_suplors)                     last supplier read
     d trprod          s                   like(pr_prod)                        last supplier read
     d file            s             10
     d libr            s             10
     d prmdeal         s              1
      * End Permenant Deal fields
     d first_cycl      s              1                                         first cycle
     d first_try       s              5p 0                                      first try ndc check
     d ndc_valid       s              1                                         ndc valid flag
     d ndc_used        s                   like(pr_ndc_upc)                     last supplier read
     d restricted      s              1                                         restricted product
     d block_prod      s              1                                         product blocked
     d block_locn      s              1                                         location blocked
     d block_supl      s              1                                         supplier blocked
     d cash_disc       s              3p 1                                      reg supl cash disc
     d supl_rebat      s              3p 1                                      reg supl rebate
     d alts_rebat      s              3p 1                                      alt supl rebate
     d run_day         s              3p 0                                      day program runs
     d once_only       s              1                                         day program runs

      * ------------------------------------------- Product rejected reasons
     d reason_1        c                   'Not found in NDC/UPC link file'     reason 5
     d reason_2        c                   'Invalid available quantity    '     reason 1
     d reason_3        c                   'Invalid price offered         '     reason 2

      * --------------------------------------------------- Named indicators
     d over_flow       s               n                                        print overflow
      * ----------------------------------- parameter passed to subr $_write
     d altsrc          s             10                                         alternate supplier
     d*ndc_upc         s             15                                         ndc or upc code
     d ndcupc11_0      s             11  0                                      ndc or upc code
     d descript        s             30                                         product description
     d qty_avl         s              7  0                                      quantity available
     d cost_each       s             11  4                                      cost
     d cost            s             11  4                                      cost
     d cost_div        s              5  0                                      cost divisor
     d zz_percnt       s              9  4                                      errors detected ?
     d dealwindow      s                   like(pr_dealbeg)
      * ------------------------------ work fields passed to module K3S_M070
     d vldatng         s              3  3                                      value dating %
     d mode            s              1  0                                      Mode=1 from K3S_1500
     d disc_accum      s             11  4                                      accum disc eaches
     d off_invce       s             11  4                                      Off invoice
     d net_cost        s             11  4                                      net cost
     d deal_days       s              3  0                                      deal days
     d off_reg         s             11  4                                      Off invoice

      * ---------------------------------------------------- valid locations
     d locn            s              5    dim(999)                             valid locations

      * -------------------------------------- Program Status Data Structure
     d*copy k3s_c040
      *****************************************************************
      **
      **   K3S-Replenish - Inventory REPLENISHment System
      **   Copyright (c) 1996-1997 by King III Solutions, Inc.
      **   All rights reserved.
      **
      *****************************************************************
      **
      **   Name: K3S_C040
      **   Type: ILE /COPY member
      **   Desc: *PROC Program Status Data Structure fields
      **
      *****************************************************************

     d                sds
     d psds_progm        *proc                                                  program name
     d psds_error             90    170                                         error
     d psds_user             254    263                                         user ID
     d*
      * --------------------------------------------------- parameter passed prototype
     d/copy k3s_proto
      * --------------------------------------------------- procedure interface
     d K3S_9100        PI
     d  comp                          1
      * -------------------------------------- Likerec Statements
     d intaltre_key    DS                  likerec(rk_intaltr:*key)
     d dealperb_key    DS                  likerec(rk_dealper:*key)
      * ----------------------------------------------------------- Supreme
     Ik_altsrc01ns  01
     I                                  9   19  ndc_upc_01                      ndc or upc code
     I                                 21   51  descrip_01                      product description
     I                                 53   57 0qty_avl_01                      quantity available
     I                                 61   63 0cost_dl_01                      cost - whole dollars
     I                                 65   66 2cost_cn_01                      cost - cents

      * ------------------------------------------------------ Quality King
     Ik_altsrc02ns  02
     I                                  9   19  ndc_upc_02                      ndc or upc code
     I                                 21   51  descrip_02                      product description
     I                                 53   57 0qty_avl_02                      quantity available
     I                                 61   63 0cost_dl_02                      cost - whole dollars
     I                                 65   66 2cost_cn_02                      cost - cents

      * ---------------------------------------------------------- available
     Ik_altsrc03ns  03
     I                                  9   19  ndc_upc_03                      ndc or upc code
     I                                 21   51  descrip_03                      product description
     I                                 53   57 0qty_avl_03                      quantity available
     I                                 61   63 0cost_dl_03                      cost - whole dollars
     I                                 65   66 2cost_cn_03                      cost - cents

      * -------------------------------------------------- Victory Wholesale
     Ik_altsrc04ns  04
     I                                  9   19  ndc_upc_04                      ndc or upc code
     I                                 21   51  descrip_04                      product description
     I                                 53   57 0qty_avl_04                      quantity available
     I                                 61   63 0cost_dl_04                      cost - whole dollars
     I                                 65   66 2cost_cn_04                      cost - cents

      * --------------------------------------------------- Purity Wholesale
     Ik_altsrc05ns  05
     I                                  9   19  ndc_upc_05                      ndc or upc code
     I                                 21   51  descrip_05                      product description
     I                                 53   57 0qty_avl_05                      quantity available
     I                                 61   63 0cost_dl_05                      cost - whole dollars
     I                                 65   66 2cost_cn_05                      cost - cents

      * -------------------------------------------------------- R & S Sales
     Ik_altsrc06ns  06
     I                                  5   15  ndc_upc_06                      ndc or upc code
     I                                 24   53  descrip_06                      product description
     I                                 54   58 0qty_avl_06                      quantity available
     I                                 60   63 0cost_dl_06                      cost - whole dollars
     I                                 64   65 2cost_cn_06                      cost - cents

      * ----------------------------------------------------------- Stanford
     Ik_altsrc07ns  07
     I                                  1   11  ndc_upc_07                      ndc or upc code
     I                                 24   53  descrip_07                      product description
     I                                 53   57 0qty_avl_07                      quantity available
     I                                 60   62 0cost_dl_07                      cost - whole dollars
     I                                 63   64 2cost_cn_07                      cost - cents

      * --------------------------------------------------------- Supreme
     Ik_altsrc08ns  08
     I                                  1   11  ndc_upc_08                      ndc or upc code
     I                                 24   53  descrip_08                      product description
     I                                 54   58 0qty_avl_08                      quantity available
     I                                 60   63 0cost_dl_08                      cost - whole dollars
     I                                 64   65 2cost_cn_08                      cost - cents

      * -------------------------------------------------------- available
     Ik_altsrc09ns  09
     I                                  2   11  ndc_upc_09                      ndc or upc code
     I                                 24   53  descrip_09                      product description
     I                                 54   58 0qty_avl_09                      quantity available
     I                                 60   63 0cost_dl_09                      cost - whole dollars
     I                                 64   65 2cost_cn_09                      cost - cents

      * ------------------------------------------------------------- United
     Ik_altsrc10ns  10
     I                                  5   15  ndc_upc_10                      ndc or upc code
     I                                 24   53  descrip_10                      product description
     I                                 54   58 0qty_avl_10                      quantity available
     I                                 60   63 0cost_dl_10                      cost - whole dollars
     I                                 64   65 2cost_cn_10                      cost - cents

      * ----------------------------------------------------------- Value Rx
     Ik_altsrc11ns  11
     I                                  1   11  ndc_upc_11                      ndc or upc code
     I                                 23   52  descrip_11                      product description
     I                                 54   58 0qty_avl_11                      quantity available
     I                                 60   63 0cost_dl_11                      cost - whole dollars
     I                                 64   65 2cost_cn_11                      cost - cents

      * --------------------------------------------------- S & S Medical
     Ik_altsrc12ns  12
     I                                  1   11  ndc_upc_12                      ndc or upc code
     I                                 24   53  descrip_12                      product description
     I                                 54   58 0qty_avl_12                      quantity available
     I                                 60   63 0cost_dl_12                      cost - whole dollars
     I                                 64   65 2cost_cn_12                      cost - cents

      * --------------------------------------------------- Michigan Rx
     Ik_altsrc13ns  13
     I                                  5   15  ndc_upc_13                      ndc or upc code
     I                                 24   53  descrip_13                      product description
     I                                 54   58 0qty_avl_13                      quantity available
     I                                 60   63 0cost_dl_13                      cost - whole dollars
     I                                 64   65 2cost_cn_13                      cost - cents

      * --------------------------------------------------- Bindley Trading
     Ik_altsrc14ns  14
     I                                  1   11  ndc_upc_14                      ndc or upc code
     I                                 24   53  descrip_14                      product description
     I                                 54   58 0qty_avl_14                      quantity available
     I                                 60   63 0cost_dl_14                      cost - whole dollars
     I                                 64   65 2cost_cn_14                      cost - cents

      * --------------------------------------------------- available to use
     Ik_altsrc15ns  15
     I                                  5   15  ndc_upc_15                      ndc or upc code
     I                                 24   53  descrip_15                      product description
     I                                 54   58 0qty_avl_15                      quantity available
     I                                 60   63 0cost_dl_15                      cost - whole dollars
     I                                 64   65 2cost_cn_15                      cost - cents
      /free
       //----------------------------------------------------- once routine

       if        first_cycl <> *on;
                 first_cycl =  *on;
                 first_page =  *off;
       endif;

       //---------------------------------------------------------- Supreme

       //Alternate source entries for Supreme

       if        *in01;

       // prime fields for subroutine $_write
                 altsrc     = '41330  ';
                 upc#       = *all'0';
                 upc#       = %replace(ndc_upc_01:upc#:3:%len(ndc_upc_01));
                 ndc_upc = upc#;
                 descript   = descrip_01;
                 qty_avl    = qty_avl_01;
                 cost_each  = cost_dl_01 + cost_cn_01;
                 cost       = cost_dl_01 + cost_cn_01;
                 cost_div   = 1;

                 exsr       $_write;

       endif;

       //------------------------------------------------------ Quality King

       //Alternate source entries for Quality King

       if        *in02;

       // prime fields for subroutine $_write
                 altsrc     = '39990  ';
                 upc#       = *all'0';
                 upc#       = %replace(ndc_upc_02:upc#:3:%len(ndc_upc_02));
                 ndc_upc    = upc#;
                 descript   = descrip_02;
                 qty_avl    = qty_avl_02;
                 cost_each  = cost_dl_02 + cost_cn_02;
                 cost       = cost_dl_02 + cost_cn_02;
                 cost_div   = 1;

                 exsr       $_write;

       endif;

       //------------------------------------------------ Newport Wholesaler

       //Alternate source entries for Newport Wholesalers

       if        *in03;

       // prime fields for subroutine $_write
                 altsrc     = '37011  ';
                 upc#       = *all'0';
                 upc#       = %replace(ndc_upc_03:upc#:3:%len(ndc_upc_03));
                 ndc_upc    = upc#;
                 descript   = descrip_03;
                 qty_avl    = qty_avl_03;
                 cost_each  = cost_dl_03 + cost_cn_03;
                 cost       = cost_dl_03 + cost_cn_03;
                 cost_div   = 1;

                 exsr       $_write;

       endif;

       //------------------------------------------------- Victory Wholesale

       //Alternate source entries for Victory wholesale


       if        *in04;

       // prime fields for subroutine $_write
                 altsrc     = '61455  ';
                 upc#       = *all'0';
                 upc#       = %replace(ndc_upc_04:upc#:3:%len(ndc_upc_04));
                 ndc_upc    = upc#;
                 descript   = descrip_04;
                 qty_avl    = qty_avl_04;
                 cost_each  = cost_dl_04 + cost_cn_04;
                 cost       = cost_dl_04 + cost_cn_04;
                 cost_div   = 1;

                 exsr      $_write;

       endif;

       //-------------------------------------------------- Purity Wholesale

       //Alternate source entries for Purity Wholesale


       if        *in05;

       // prime fields for subroutine $_write
                 altsrc     = '15730  ';
                 upc#       = *all'0';
                 upc#       = %replace(ndc_upc_05:upc#:3:%len(ndc_upc_05));
                 ndc_upc    = upc#;
                 descript   = descrip_05;
                 qty_avl    = qty_avl_05;
                 cost_each  = cost_dl_05 + cost_cn_05;
                 cost       = cost_dl_05 + cost_cn_05;
                 cost_div   = 1;

                 exsr      $_write;

       endif;

       //------------------------------------------------------- R & S Sales

       //Alternate source entries for R & S Sales

       if        *in06;

       // prime fields for subroutine $_write
                 altsrc     = '7217   ';
                 ndc_upc    = ndc_upc_06;
                 descript   = descrip_06;
                 qty_avl    = qty_avl_06;
                 cost_each  = cost_dl_06 + cost_cn_06;
                 cost       = cost_dl_06 + cost_cn_06;
                 cost_div   = 1;

                 exsr      $_write;

       endif;

       //---------------------------------------------------------- Stanford

       //Alternate source entries for Stanford

       if        *in07;

       // prime fields for subroutine $_write
                 altsrc     = '8006   ';
                 ndc_upc    = ndc_upc_07;
                 descript   = descrip_07;
                 qty_avl    = qty_avl_07;
                 cost_each  = cost_dl_07 + cost_cn_07;
                 cost       = cost_dl_07 + cost_cn_07;
                 cost_div   = 1;

                 exsr      $_write;

       endif;

       //-------------------------------------------------------- Supreme

       if        *in08;

       //Alternate source entries for Supreme
       // prime fields for subroutine $_write
                 altsrc     = '8202   ';
                 ndc_upc    = ndc_upc_08;
                 descript   = descrip_08;
                 qty_avl    = qty_avl_08;
                 cost_each  = cost_dl_08 + cost_cn_08;
                 cost       = cost_dl_08 + cost_cn_08;
                 cost_div   = 1;

                 exsr       $_write;

       endif;


       //------------------------------------------------------- available

       //Alternate source entries for available

       if        *in09;

       // prime fields for subroutine $_write
                 altsrc     = '62870  ';
                 ndc_upc    = ndc_upc_09;
                 descript   = descrip_09;
                 qty_avl    = qty_avl_09;
                 cost_each  = cost_dl_09 + cost_cn_09;
                 cost       = cost_dl_09 + cost_cn_09;
                 cost_div   = 1;

                 exsr      $_write;

       endif;

       //------------------------------------------------------------ United

       //Alternate source entries for United

       if        *in10;

       // prime fields for subroutine $_write
                 altsrc     = '8875   ';
                 ndc_upc    = ndc_upc_10;
                 descript   = descrip_10;
                 qty_avl    = qty_avl_10;
                 cost_each  = cost_dl_10 + cost_cn_10;
                 cost       = cost_dl_10 + cost_cn_10;
                 cost_div   = 1;

                 exsr       $_write;

       endif;

       //---------------------------------------------------------- Value Rx

       //Alternate source entries for Value Rx

       if        *in11;

       // prime fields for subroutine $_write
                 altsrc     = '9148   ';
                 ndc_upc    = ndc_upc_11;
                 descript   = descrip_11;
                 qty_avl    = qty_avl_11;
                 cost_each  = cost_dl_11 + cost_cn_11;
                 cost       = cost_dl_11 + cost_cn_11;
                 cost_div   = 1;

                 exsr       $_write;

       endif;

       //-------------------------------------------------- S & S Medical

       //Alternate source entries for S & S Medical

       if        *in12;

       // prime fields for subroutine $_write
                 altsrc     = '7736   ';
                 ndc_upc    = ndc_upc_12;
                 descript   = descrip_12;
                 qty_avl    = qty_avl_12;
                 cost_each  = cost_dl_12 + cost_cn_12;
                 cost       = cost_dl_12 + cost_cn_12;
                 cost_div   = 1;

                 exsr       $_write;

       endif;

       //-------------------------------------------------- Michigan Rx

       //Alternate source entries for Michigan Rx

       if        *in13;

       // prime fields for subroutine $_write
                 altsrc     = '5145   ';
                 ndc_upc    = ndc_upc_13;
                 descript   = descrip_13;
                 qty_avl    = qty_avl_13;
                 cost_each  = cost_dl_13 + cost_cn_13;
                 cost       = cost_dl_13 + cost_cn_13;
                 cost_div   = 1;

                 exsr       $_write;

       endif;

       //-------------------------------------------------- Bindley Trading

       //Alternate source entries for Bindley Trading Company

       if        *in14;

       // prime fields for subroutine $_write
                 altsrc     = '9110   ';
                 ndc_upc    = ndc_upc_14;
                 descript   = descrip_14;
                 qty_avl    = qty_avl_14;
                 cost_each  = cost_dl_14 + cost_cn_14;
                 cost       = cost_dl_14 + cost_cn_14;
                 cost_div   = 1;

                 exsr       $_write;

       endif;

       //-------------------------------------------------- available to use

       //Alternate source entries for


       if        *in15;

       // prime fields for subroutine $_write
                 altsrc     = '41330  ';
                 ndc_upc    = ndc_upc_15;
                 descript   = descrip_15;
                 qty_avl    = qty_avl_15;
                 cost_each  = cost_dl_15 + cost_cn_15;
                 cost       = cost_dl_15 + cost_cn_15;
                 cost_div   = 1;

                 exsr       $_write;

       endif;

       //Calculate rejected percent, and print total line
       if *inlr = *on;
          clear reject_pct;
          if tot_record > 0 and
             tot_record > tot_reject;
                eval(h) reject_pct = tot_reject/tot_record * 100;
          endif;
          write     k3s_r03;

       //  save summary information to supplier rejected summary file
          exsr $_rejected;

       //logic to disconnect check program
          if cm_exitchk = 1;
             c#program  = psds_progm;
             c#ndc_upc  = *zeros;
             c#item     = *zeros;
             c#function = 'EXIT';
             callp NDCCHKRR(c#parms);
          endif;
       endif;

       /////////////////////////////////////////////////// write transaction

       begsr $_write;

       //if alternate source supplier break, and first page header has been
       //printed, then print totals
       if last_supl <> altsrc and
          first_page = *on;
          exsr $_break;
       endif;

       //print header only for first alternate source supplier
       if first_page = *off;
          exsr $_print;
       endif;

       //count total records
       tot_record += 1;

       //initialize ndc valid switch
       ndc_valid = *off;

       //initialize ndc value to be used for chain purposes
       ndc_used = ndc_upc;

       //keep track of first try for ndc_upc check
       first_try  = 1;

       //set off once_only flag
       once_only = *off;

       //begin edits
       select;

       //invalid quantity offered
          when qty_avl <= 0;
             tot_reject += 1;
             reason = reason_2;
             exsr $_print;

       //invalid price offered
          when cost <= 0 or cost_each <= 0;
             tot_reject += 1;
             reason = reason_3;
             exsr $_print;

       //quantity and price are ok, so test for ndc/upc
          other;

       //perform do group for each location
             for y = 1 to x;        //increment 1 is assumed

       //only perform the do group logic under the following 2 conditions:
       //     1) this is first location being tested, so we must go see if
       //             the ndc is valid. we know out of this first try if
       //             the ndc is valid, and therefore could continue trying
       //             other locations for this product
       //     2) we know from the first try that the ndc was valid for this
       //             product.
                if first_try = 1 or
                   first_try > 1 and
                   ndc_valid = *on;

                   pr_comp    = comp;
                   pr_locn    = locn(y);
                   pr_ndc_upc = ndc_used;

       //see if product exists for this location
                   chain (pr_comp:pr_locn:pr_ndc_upc) k_producte;

       //if this is the first try with this ndc, see if it is valid
                   if first_try = 1;

       //NDC_UPC start
       //if no hit using location try with ndc, see if it is valid
                      if not %found(k_producte);
                         chain (pr_comp:pr_ndc_upc) k_producth;
                      endif;

       //NDC_UPC end
       //logic to test if product ndc_upc in different format
                      if not %found;
                         c#program  = psds_progm;
                         ndcupc11_0 = %dec(ndc_upc:11:0);
                         c#ndc_upc  = ndcupc11_0;
                         c#item     = *zeros;
                         c#function = *blanks;

       //attempt to get ndc_upc in another format
                         if cm_exitchk = 1;
                            callp NDCCHKRR(c#parms);
                         endif;

       //did find match on ndc_upc
                         if c#item > 0;
                            pr_prod = %editc(c#item:'X');
                            ndc_valid = *on;

       // find product to get our version of ndc_upc code
                            chain (pr_comp:pr_prod) k_productg;
                            ndc_used = pr_ndc_upc;

       // see if product at this location
       // ensure that chain above didn't change location
                            pr_locn    = locn(y);
                            chain (pr_comp:pr_locn:pr_prod) k_productc;

                         else;
                            ndc_valid = *off;
                            tot_reject += 1;
                            reason = reason_1;
                            exsr $_print;
                         endif;

       //if *in98 = *on
                      else;
                         ndc_valid = *on;
                      endif;

       //if first_try = 1
                   endif;

       //if product exists
                   if %found;

       //----------------------------------------------- test block criteria
       //initialize block fields
                      block_prod = *off;
                      block_locn = *off;
                      block_supl = *off;

       //see if product is blocked for this location
                      if pr_procalt = 0;
                         block_prod = *on;

                      else;

       //see if this location is blocked
                         lc_comp = comp;
                         lc_locn = pr_locn;
                         chain (lc_comp:lc_locn) k_locatnsa;
                         if lc_procalt = 0;
                            block_locn = *on;

                         else;

       //see if regular supplier is blocked
                            sp_comp    = comp;
                            sp_locn    = locn(y);
                            sp_supl    = pr_supl;

                            chain (sp_comp:sp_locn:sp_supl) k_suplierb;
                            if sp_procalt = 0;
                               block_supl = *on;

                            endif;
                         endif;
                      endif;
       //----------------------------------------------- end block criteria

       //save values from regular supplier
                      cash_disc  = sp_cashdsc;
                      supl_rebat = sp_rebate;

                      sp_comp    = comp;
                      sp_locn    = locn(y);
                      sp_supl    = altsrc;

       //get alternate source buy group and preference sequence #
                      chain (sp_comp:sp_locn:sp_supl) k_suplierb;
                      if %found(k_suplierb);

       //save values from alternate source supplier
                         alts_rebat = sp_rebate;

       //write record
                         ia_comp    = comp;
                         ia_locn    = pr_locn;
                         ia_birth   = %date(%subst(%char(time_stamp):1:10):
                                      *iso);
                         ia_buyr    = pr_buyr;
                         ia_supl    = pr_supl;
                         ia_suplsub = pr_suplsub;
                         ia_buyralt = sp_buyr;
                         ia_suplalt = sp_supl;
                         ia_suplals = sp_suplsub;
                         ia_prod    = pr_prod;
                         ia_qtyavil = qty_avl;
                         ia_costdiv = cost_div;
                         ia_cost    = cost;
                         ia_costeac = cost_each;
                         ia_costreg = pr_costeac;
                         ia_deal    = pr_deal;
                         ia_prefseq = sp_prefseq;
                         ia_supldsc = cash_disc;
                         ia_suplreb = supl_rebat;
                         ia_supldtg = *zeros;
                         ia_prodreb = pr_rebate;
                         ia_altrreb = alts_rebat;

       // determine load code value, and get discount value if deal exists
                         exsr $_loadcode;

                         ia_dealeac = disc_accum;

       //only write a record once for this location
                         intaltre_key.ia_comp    = comp;
                         intaltre_key.ia_locn    = pr_locn;
                         intaltre_key.ia_suplalt = sp_supl;
                         intaltre_key.ia_suplals = sp_suplsub;
                         intaltre_key.ia_prod    = pr_prod;
                         chain %kds(intaltre_key) k_intaltre;
                         if not %found(k_intaltre);
                            write     rk_intaltr;

       //only write a record to the weekly offerings file once per
       //     alternate source/product. (not once per location)
       //     we are basically capturing what was sent on the tapes
       //**                 if        first_try = 1
                            if once_only  = *off;
                               once_only  = *on;
                               la_comp    = comp;
                               la_birth   = %date(%subst(%char(time_stamp):
                                            1:10):*iso);
                               la_supl    = pr_supl;
                               la_suplsub = pr_suplsub;
                               la_suplalt = sp_supl;
                               la_suplals = sp_suplsub;
                               la_prod    = pr_prod;
                               la_qtyavil = qty_avl;
                               la_costdiv = cost_div;
                               la_cost    = cost;
                               la_costeac = cost_each;
                               la_costreg = pr_costeac;
                               la_deal    = pr_deal;
                               la_dealeac = disc_accum;
                               write rk_logaltr;
                            endif;

                         endif;
                      endif;
                   endif;
                endif;

       //increment # of tries
                first_try += 1;
             endfor;

       endsl;

       endsr;

       //////////////////////////////////////////////////////////// One time

       begsr *inzsr;

       //get all locations for this company into locn array
       lc_comp = comp;
       lc_locn = *blanks;

       setll (lc_comp:lc_locn) k_locatnsa;
       read k_locatnsa;

       dou (lc_comp <> comp) or %eof(k_locatnsa);
           x += 1;
           locn(x) = lc_locn;
           read k_locatnsa;
       enddo;

       //get company code
       cm_comp = comp;
       chain (cm_comp) k_companya;

       //determine run day for restricted products logic
       run_day = %subdt(cm_sysdate:*days);

       //prime program id
       zz_program = psds_progm;

       //prime company code
       zz_compcod = cm_compcod;

       // prime user id
       zz_user = psds_user;

       //report title
       zz_title  = 'Alternate source entries';
       zz_title2 = 'Products rejected report';

       //------------------------------------------------------ get timestamp
       // call module to retrieve timestamp
       callp K3S_Retrieve_Timestamp(time_stamp);
       //------------------------------------------------- get time formated
       lda_usrdat = cm_reptdat;
       lda_usrtim = cm_repttim;
       lda_usradj = 0;
       //get time formatted
       exsr $_get_time;

       setll *hival k_dealperb;
       setll (comp) k_dealperb;
       reade (comp) k_dealperb;
       if not %eof(k_dealperb);
          file = 'IN USE    ';
       else;
          file = '          ';
       endif;

       endsr;

       ///////////////////////////////////////////////// determine load code

       begsr $_loadcode;

       //initialize restriced product information
       restricted = *off;
       px_restqty = 0;
       ia_restric = 0;

       //initialize load code to 0
       ia_loadcod = 0;

       // initialize zz_percnt to 0
       zz_percnt = 0;

       // initialize disc_accum to 0
       disc_accum = 0;

       // prime net cost with regular product cost
       net_cost   = pr_costeac;

       //----
       if pr_deal <> *blanks;
          dealwindow = lc_sysdate + %days(lc_dwindow);
          vldatng = lc_vldatng * .01;
          mode = 2;
          deal_days = 0;
          disc_accum = 0;
          off_invce = 0;
          off_reg = 0;
       // call to module that calculates forward buy extra days
          callp K3S_M070(mode:
                        pr_comp:
                        pr_locn:
                        pr_deal:
                        pr_prod:
                        pr_costeac:
                        lc_sysdate:
                        dealwindow:
                        lc_vldisct:
                        lc_vlpincr:
                        vldatng:
                        deal_days:
                        disc_accum:
                        off_invce:
                        pr_costreg:
                        off_reg);
          net_cost = net_cost - disc_accum;
       endif;

       // check for supplier permanent deals
       prmdeal = *blanks;
       if file = 'IN USE    ';
          exsr $_prm_deal;
       endif;

       // go ahead and calculate percent off, if alternate source cost is
       // less than net cost, and net cost > 0
       if ia_costeac < net_cost and
          net_cost > 0;
          eval(h)   zz_percnt = 1 - (ia_costeac/net_cost)
                                  - (cash_disc  * .01)
                                  - (supl_rebat * .01)
                                  - (pr_rebate  * .01)
                                  + (alts_rebat * .01);
       endif;

       // go ahead and check for restricted product information
       px_comp    = comp;
       px_locn    = pr_locn;
       px_prod    = pr_prod;
       chain (px_comp:px_locn:px_prod) k_prodrsta;

       //restricted product
       if %found(k_prodrsta);
          restricted = *on;

       //remove negative quantities
          if px_restqty < 0;
             px_restqty = 0;
          endif;

       //only available during first week of month
          if run_day > 7;
             px_restqty = 0;
          endif;

       endif;

       //------------------------------------- perform load code value tests
       // perform tests for load code value
       select;

       // alternate source advantage over maximum % considered valid
       // price 'too good to be true'
          when zz_percnt > lc_altmaxp * .01;
               ia_loadcod = 1;
       // Supplier or Product Permanent deal exists
               if prmdeal = 'Y';
                  ia_loadcod = 11;
               endif;


       // alternate source cost greater than or equal to net cost
          when ia_costeac >= net_cost;
               ia_loadcod = 4;
       // Supplier or Product Permanent deal exists
               if prmdeal = 'Y';
                  ia_loadcod = 11;
               endif;


       // alternate source advantage less than minimum allowable %
          when zz_percnt < lc_altadv * .01;
               if pr_deal = *blanks;
                  ia_loadcod = 2;
               else;
                  ia_loadcod = 3;
               endif;
       // Supplier or Product Permanent deal exists
               if prmdeal = 'Y';
                  ia_loadcod = 11;
               endif;


       // restricted product
       //    if restricted product has a quantity, then this is the quantity
       //    to be purchased.
          when restricted = *on;
             if px_restqty = 0;
                ia_loadcod = 5;
             else;
                ia_restric = px_restqty;
             endif;
       // Supplier or Product Permanent deal exists
             if prmdeal = 'Y';
                ia_loadcod = 11;
             endif;


       // product is overstocked within the company
          when pr_overflg = 1;
             ia_loadcod = 6;
       // Supplier or Product Permanent deal exists
             if prmdeal = 'Y';
                ia_loadcod = 11;
             endif;


       //product annual usage too low
       ///////*          when      (pr_forcast * pr_forcint) < lc_altmaxd
          when (pr_forcast * pr_forcint) < lc_altminq;
             ia_loadcod = 7;
       // Supplier or Product Permanent deal exists
             if prmdeal = 'Y';
                ia_loadcod = 11;
             endif;


       //product has been blocked
          when block_prod = *on;
             ia_loadcod = 8;
       // Supplier or Product Permanent deal exists
             if prmdeal = 'Y';
                ia_loadcod = 11;
             endif;


       // regular supplier has been blocked
          when block_supl = *on;
             ia_loadcod = 9;
       // Supplier or Product Permanent deal exists
             if prmdeal = 'Y';
                ia_loadcod = 11;
             endif;


       // entire location has been blocked
          when block_locn = *on;
             ia_loadcod = 10;
       // Supplier or Product Permanent deal exists
             if prmdeal = 'Y';
                ia_loadcod = 11;
             endif;


       endsl;

       endsr;

       /////////////////////////////////////////////////////////////// Print

       begsr $_print;

       //print header if first page, or overflow
       if first_page = *off  or
          over_flow = *on or
          last_supl <> altsrc;

          over_flow = *off;

       //  get alternate source name
          sp_comp    = comp;
          sp_supl    = altsrc;
          chain (sp_comp:sp_supl) k_suplierc;
          if not %found(k_suplierc);
             sp_name = '*** supplier name missing';
          endif;

          write     k3s_r01;
       endif;

       //save last supplier
       last_supl = altsrc;

       // print detail line
       if first_page = *on;
          write     k3s_r02;
       endif;

       //first page now passed
       first_page = *on;

       endsr;

       /////////////////////////////////////////////////////////////// Break

       begsr $_break;

       //print header if overflow, or supplier break
       if over_flow = *on or
          last_supl <> altsrc;

       //---------------------------------------------------- supplier break
       //Supplier break (not first page), so print totals
          if last_supl <> altsrc and
             first_page = *on;

       //   calculate rejected percent, and print total line
             clear reject_pct;
             if tot_record > 0 and
                tot_record > tot_reject;
                eval(h) reject_pct = tot_reject/tot_record * 100;
             endif;

       //  print totals
              write     k3s_r03;

       //save summary information to supplier rejected summary file
              exsr $_rejected;

       //reset count of records
              tot_record = 0;
              tot_reject = 0;

          endif;
       //-------------------------------------------------------------------

       //first page now passed
          first_page = *on;

          over_flow = *off;

       //get alternate source name
          sp_comp    = comp;
          sp_supl    = altsrc;
          chain (sp_comp:sp_supl) k_suplierc;
          if not %found(k_suplierc);
             sp_name = '*** supplier name missing';
          endif;

          write     k3s_r01;
       endif;

       //save last supplier
       last_supl = altsrc;

       endsr;

       //////////////////////////////////////////////////////////// Rejected

       begsr $_rejected;

       //save summary of rejected records to file

       sr_comp    = comp;
       sr_supl    = last_supl;
       sr_birth = %date(%subst(%char(time_stamp):1:10):*iso);
       sr_procesd = tot_record;
       sr_rejectd = tot_reject;
       write rk_suplrej;

       endsr;

       //----------------------------------------get time subroutine
       //copy k3s_c180
       //*****************************************************************
       //**
       //**   K3S-Replenish - Inventory REPLENISHment System
       //**   Copyright (c) 1996-1997 by King III Solutions, Inc.
       //**   All rights reserved.
       //**
       //*****************************************************************
       //**
       //**   Name: K3S_C180
       //**   Type: ILE /COPY member
       //**   Desc: Get system date and time formated       'C' specs only
       //**
       //**************************************************************

       ///////////////////////////////////////// Get date and time formated

       begsr $_get_time;

       //------------------------------------------- Retrieve date and time
       //call module to retrieve user formated date and time
       callp K3S_Retrieve_Date_Time(lda_usrdat:
                                    lda_usrtim:
                                    lda_usradj:
                                    zz_usrdate:
                                    zz_usrtime);

       endsr;

       ////////////////////////////////////////////////////// Get prm deals

       begsr $_prm_deal;

       //          select type of L1
       trlocn                  = pr_locn;
       trsuplorg               = *blanks;
       trsuplors               = *blanks;
       trprod                  = *blanks;
       dealperb_key.dr_comp    = pr_comp;
       dealperb_key.dr_locn    = trlocn;
       dealperb_key.dr_supl    = trsuplorg;
       dealperb_key.dr_suplsub = trsuplors;
       dealperb_key.dr_prod    = trprod;
       setll *hival k_dealperb;
       setll %kds(dealperb_key) k_dealperb;
       reade %kds(dealperb_key) k_dealperb;
       dow not %eof(k_dealperb);
           exsr $_cal_deal;
           reade %kds(dealperb_key) k_dealperb;
       enddo;

       //        select type of P1
       trlocn = *blanks;
       trsuplorg = pr_suplorg;
       trsuplors = pr_suplors;
       trprod = pr_prod;
       dealperb_key.dr_comp    = pr_comp;
       dealperb_key.dr_locn    = trlocn;
       dealperb_key.dr_supl    = trsuplorg;
       dealperb_key.dr_suplsub = trsuplors;
       dealperb_key.dr_prod    = trprod;
       setll *hival k_dealperb;
       setll %kds(dealperb_key) k_dealperb;
       reade %kds(dealperb_key) k_dealperb;
       dow not %eof(k_dealperb);
          exsr $_cal_deal;
          reade %kds(dealperb_key) k_dealperb;
       enddo;

       //        select type of P2
       trlocn = pr_locn;
       trsuplorg = pr_suplorg;
       trsuplors = pr_suplors;
       trprod = pr_prod;
       dealperb_key.dr_comp    = pr_comp;
       dealperb_key.dr_locn    = trlocn;
       dealperb_key.dr_supl    = trsuplorg;
       dealperb_key.dr_suplsub = trsuplors;
       dealperb_key.dr_prod    = trprod;
       setll *hival k_dealperb;
       setll %kds(dealperb_key) k_dealperb;
       reade %kds(dealperb_key) k_dealperb;
       dow not %eof(k_dealperb);
          exsr $_cal_deal;
          reade %kds(dealperb_key) k_dealperb;
       enddo;

       //        select type of S1
       trlocn = *blanks;
       trsuplorg = pr_suplorg;
       trsuplors = pr_suplors;
       trprod = *blanks;
       dealperb_key.dr_comp    = pr_comp;
       dealperb_key.dr_locn    = trlocn;
       dealperb_key.dr_supl    = trsuplorg;
       dealperb_key.dr_suplsub = trsuplors;
       dealperb_key.dr_prod    = trprod;
       setll *hival k_dealperb;
       setll %kds(dealperb_key) k_dealperb;
       reade %kds(dealperb_key) k_dealperb;
       dow not %eof(k_dealperb);
          exsr $_cal_deal;
          reade %kds(dealperb_key) k_dealperb;
       enddo;

       //        select type of S2
       trlocn = pr_locn;
       trsuplorg = pr_suplorg;
       trsuplors = pr_suplors;
       trprod = *blanks;
       dealperb_key.dr_comp    = pr_comp;
       dealperb_key.dr_locn    = trlocn;
       dealperb_key.dr_supl    = trsuplorg;
       dealperb_key.dr_suplsub = trsuplors;
       dealperb_key.dr_prod    = trprod;
       setll *hival k_dealperb;
       setll %kds(dealperb_key) k_dealperb;
       reade %kds(dealperb_key) k_dealperb;
       dow not %eof(k_dealperb);
          exsr $_cal_deal;
          reade %kds(dealperb_key) k_dealperb;
       enddo;

       endsr;

       //////////////////////////////////////////////// Calculate prm deals

       begsr $_cal_deal;
       //--------------------------------------------------------- discounts
       //discounts

       prmdeal = 'Y';
       //        select type of discount
       select;

       //   *****************************
       //   percent discount
       when dr_facttyp = '%';
          eval(h) disc_each = pr_costeac * dr_factval / 100;
          net_cost          = net_cost - disc_each;

       //   *****************************
       //   actual dollar value
       when dr_facttyp = '$';
          net_cost = (dr_factval/dr_unit);

       //   *****************************
       //   dollar difference
       when dr_facttyp = 'D';

          if (dr_factval/dr_unit) < pr_costeac;
             eval(h) disc_each = dr_factval / dr_unit;
             net_cost          = net_cost - disc_each;
          endif;

       endsl;

       endsr;


