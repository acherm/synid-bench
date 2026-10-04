      *****************************************************************
     h copyright('(C) Copyright 1996 - 2014 King III Solutions, Inc.  +
     h Rel 5.1  2014-01-01       Program Property of King III Solutions, Inc. +
     h All rights reserved              +
     h K3S_Replenish (R) is a Registered Trade Mark of King III Solutions Inc.')

     h DFTACTGRP(*NO) ACTGRP('K3S_ACTG_5') OPTION(*NODEBUGIO)
     h BNDDIR('K3S_BNDDIR')
      *****************************************************************
      **
      **   K3S-Replenish (R) - Inventory REPLENISHment System
      **   Copyright (C) 1996-2014 by King III Solutions, Inc.
      **   Program property of King III Solutions, Inc.
      **   All rights reserved.
      **   K3S_Replenish (R) is a Registered Trade Mark of
      **   King III Solutions Inc.
      **
      *****************************************************************
      **
      **   Name: K3S_9010
      **   Type: ILE RPG Program
      **   Desc: Update database from external source
      **
      *****************************************************************
      **
      **  This program is used to update the database from an external
      **  source. Typically, this program would run once each night,
      **  and contain one record for each product to be updated.
      **
      **  This program will determine a change in forecasting period,
      **  and will automatically set on the forecasting module based
      **  upon this knowledge.
      **
      **  This program reads products from file k_intprod that were
      **  assembled using OPNQRYF. This OPNQRYF set should only contain
      **  data for one company at a time. Multiple locations can be
      **  processed during the same batch. For performance, make sure
      **  sequence is in company, location, supplier, sub supplier.
      **
      *****************************************************************
      **
      **  The file K_LOGPROD contains transactions that audit changes to
      **  products in the K3S-Replenish system. Most of these transactions
      **  will be created within this program. However, program K3S_1500
      **  is responsible for generating types 3 and 4.
      **
      **     The types are:  1  New product
      **                     2  Products changing supplier
      **                     3  No interface records passed
      **                     4  Products deleted from file
      **                     5  Supplier passed does not exist
      **                     6  Location passed does not exist
      **                     7  Products being re-instated
      **                     8  First time 'D' make 'M'
      **                     9  Probation period expired
      **
      **                     A  Forecast going negative
      **                     B  Deviation going negative
      **                     C  Invalid T/S generated
      **                     D  Negative sales passed
      **                     E  Negative outs passed
      **                     F  Negative on hand passed
      **                     G  Negative on order passed
      **                     H  Negative back orders passed
      **                     I  Negative purchase price passed
      **                     J  Negative sales price passed
      **                     K  Product missing description
      **                     L  Purchase price divisor < 1
      **                     M  Buy multiple passed < 1
      **                     N  Minimum quantity passed < 1
      **                     O  Negative purhase increment
      **                     Q  Negative convenience pack
      **                     R  Negative weight passed
      **                     S  Weight divisor less than 1
      **                     T  Negative volume passed
      **                     U  Volume divisor less than 1
      **                     V  Status passed not 'R' or 'D'
      **                     W  Forecast cycle code not 1,2,3
      **                     X  Invalid flag alt srce process
      **                     Y  Sales price < cost
      **                     Z  Negative rebate passed
      **
      **                     a  Conv Pack less than Buy Mult
      **                     b  Conv Pack not a true multiple
      **                     c  Cost sent across as $0
      **
      *****************************************************************
      **
      **  There are 3 supplier fields in the K3S-Replenish database
      **
      **      supl    - is used to build orders
      **
      **      suplorg - is used to go after history. since alternate source
      **                orders will have products under 'supl', the
      **                'suplorg' field directs us to the original
      **                supplier to know where the history records are.
      **
      **      suplusr - can be used to pass back orders for super
      **                suppliers. It should contain the supplier that
      **                the product exists under in the user's host
      **                system, and is sent across in k_intprod.
      **                Transfer supplier logic would change the ip_supl
      **                field, but not the ip_suplusr. the ip_suplusr
      **                is to carry throughout the entire system via
      **                pr_suplusr.

      *****************************************************************

     fk_intprod if   e             disk
      * products

     fk_productauf a e           k disk
      * products  (locn,supl,suplsub,prod)

     fk_productcif   e           k disk    rename(rk_product:xk_product)
      * products  (locn,prod)

     fk_suplieraif   e           k disk
      * suppliers (locn,supl,sub)

     fk_locatnsaif   e           k disk
      * locations

     fk_logprod o  a e             disk
      * log product transactions

     fk_tablcodaif   e           k disk                                         table codes
      * table file

     fk_prodlogauf a e           k disk                                         deal summary info
      * product changes log

     fk_companyauf   e           k disk                                         table codes
      * company file

     fk_transplaif   e           k disk                                         transfer suppliers
      * transfer system regular supplier link

     fk_tranprdaif   e           k disk                                         transfer products
      * transfer system product link

     fk_prodltmauf a e           k disk                                         deal summary info
      * product lead time transactions

     fk_prodforauf a e           k disk                                         forcast change log
      * forcast change log

      * -------------------------------------- LDA D specs
     d/COPY K3S_C035

      * ----------------------------------------- Supplier for Control Break
     d                 ds
     d supl                          25
     d  ip_locn                            overlay(supl:1)
     d  ip_supl                            overlay(supl:6)
     d  ip_suplsub                         overlay(supl:16)
     d suplsaved       s                   like(supl)

      * --------------------------------------------------------- Workfields
     d #once           s              1  0
     d #notfirst       s              1
     d exist_here      s              1
     d exist_othr      s              1
     d locn            s                   like(pr_locn)
     d forcper         s                   like(pr_forcper)
     d error_type      s              1
     d histype         s              1  0
     d demlo           s                   like(lc_demlo)
     d seas_factr      s              5  2                                      Seasonal factor
     d days_perd       s                   like(pr_daysout)
     d lost_perct      s              3  2
     d bad_suplr       s              1
     d bad_suplrd      s             25    inz('Supplier not in database')
     d bad_locn        s              1
     d bad_locnd       s             25    inz('Location not in database')
     d time_stamp      s               z   inz
     d block_alts      s              1  0                                      block alt source
     d new_slow        s              1  0                                      new to slow status
     d new_usedft      s              1  0                                      new use deflt avg?
     d new_avgdft      s              7  2                                      new default average
     d cost_0          s              1  0                                      cost sent as $0?
     d cost_fill       s              1  0                                      cost to be filled?
     d cost_value      s              7  2                                      cost default value
     d night           s              1                                         parm for K3S_5056
     d delay_days      s              1  0                                      delay days flg 1=yes
     d delay_diff      s              5  0                                      delay birth differnc
     d delayuntil      s                   like(pr_excuntl)                     delay until date
     d delay_test      s                   like(pr_birth)                       delay until date
     d Ninety_Out      s                   like(pr_excuntl)                     delay until date
     d copy_deals      s              1  0                                      copy deals flg 1=yes
     d trans_prod      s              1  0                                      trans prod flg 1=yes
     d no_deal_06      s              1  0                                      bw no deal '06'1=yes
     d min_season      s              7  2
     d min_used        s              1  0
     d clr_record      s              1  0                                      clear PR_EXCUNTL
     d clr_promo       s              1  0                                      clear 3 promo fields
     d not_0001        s               d   inz(d'0001-01-01') datfmt(*iso)
     d back_order      s              1  0                                      include back order
     d lost_sales      s              1  0                                      include lost sales
     d continue        s              1  0                                      continue with logic
     d lstrcvd         s              1  0                                      last receive date
     d days_10out      s                   like(pl_ordrecv)                     10 days out
     d corp_prof       s              1  0                                      use corporate prof?
     d CorpProfID      s                   like(pr_seasonl)                     default corp profile
     d NewBirth        s              1  0                                      Birth for new prods
     d car_update      s              1  0                                      Car Count update
     d PE1_FLTR_1      s              1  0                                      PE1 filtering
     d pe_snpshot      s              1  0                                      PE snapshots
     d first_shot      s              1  0                                      once routine
     d not_recvd       s               d   inz(d'0001-01-01') datfmt(*iso)
     d ref_birth       s              1  0                                      ref birth logic

      * ---------------------------------------- period end processing logic
     d total_12        s             15  0                                      total for perd 12
     d total_13        s             15  0                                      total for perd 13
     d total_52        s             15  0                                      total for perd 52
     d rolled_12       s             15  0                                      total rolled perd 12
     d rolled_13       s             15  0                                      total rolled perd 13
     d rolled_52       s             15  0                                      total rolled perd 52
     d ye_for_12       s              1
     d ye_for_13       s              1
     d ye_for_52       s              1

     d px_comp         s                   like(pr_comp)
     d px_locn         s                   like(pr_locn)
     d px_prod         s                   like(pr_prod)
     d px_supl         s                   like(pr_supl)
     d px_suplsub      s                   like(pr_suplsub)

     d sx_comp         s                   like(sp_comp)
     d sx_locn         s                   like(sp_locn)
     d sx_supl         s                   like(sp_supl)
     d sx_suplsub      s                   like(sp_suplsub)
     d saved_name      s                   like(sp_name)
     d saved_buyr      s                   like(sp_buyr)
     d saved_lt        s                   like(sp_leadtmo)
     d saved_ltv       s                   like(sp_leadtmv)

      * ------------------------------ work fields passed to module K3S_M080
     d fordevp         s              3  3                                      DEV %
     d nodevp          s              3  3                                      default DEV %
     d accdem          s                   like(pr_accdem)                      accumulated demand
     d forcast         s                   like(pr_forcast)                     forecast, average
     d forserr         s                   like(pr_forserr)                     smoothed error
     d forserr_AV      s                   like(pr_forserr)                     absolute value smoot

     d time_stam1      s               z   inz
     d time            s               t   timfmt(*iso)
     d date            s               d   datfmt(*iso)

     d convpkw1        s                   like(pr_qtyohnd)
     d convpkw2        s                   like(pr_qtyohnd)
      * -------------------------------------- Likerec Statements
     d producta_key    DS                  likerec(rk_product:*key)
     d prodltma_key    DS                  likerec(rk_prodltm:*key)
     d prodloga_key    DS                  likerec(rk_prodlog:*key)
     d prodfora_key    DS                  likerec(rk_prodfor:*key)
      * -------------------------------------------------- parameter passed prototype
     d/copy k3s_proto
      * -------------------------------------------------- procedure interface
     d K3S_9010        PI
     d  per_end_12                    1                                         period end parm 12
     d  per_end_13                    1                                         period end parm 13
     d  per_end_52                    1                                         period end parm 52
     d  supl_chg                      1                                         supplier has changed
     d  today_str                    26                                         start timestamp
     d  today_end                    26                                         end timestamp
     d  get_log_5                     1                                         get logtype '5' data
     d  first_time                    1                                         1st time 'D' make 'M
     d  yearend_12                    1
     d  yearend_13                    1
     d  yearend_52                    1


      /free
       // retrieve local data area *lda
       in *dtaara;

       // clear fields to total number of records processed for each log type
       clear lda_recprc;
       clear lda_rctyp1;
       clear lda_rctyp2;
       clear lda_rctyp3;
       clear lda_rctyp4;
       clear lda_rctyp5;
       clear lda_rctyp6;
       clear lda_rctyp7;
       clear lda_rctyp8;
       clear lda_rctyp9;
       clear lda_rctypx;

       // Read Products and increment counter for total # of records processed

       read k_intprod;

       // ---------------------------------------------------------- Main Loop
       // main loop
       dou %eof(k_intprod);
           lda_recprc += 1;

       //------------------------------------------------------ Once Routine

       // once routine
           if #once <> 1;
              #once = 1;

       // call module to retrieve timestamp
              callp K3S_Retrieve_Timestamp(time_stamp);
              today_str = %char(time_stamp);

       // prime key lists
       //    company
              cm_comp = ip_comp;
              lc_comp = ip_comp;
              sp_comp = ip_comp;
              sx_comp = ip_comp;
              producta_key.pr_comp = ip_comp;

              chain (cm_comp) k_companya;
              update rk_company;

       // develop future date 90 days out
              Ninety_Out = cm_sysdate + %days(90);

       // save alternate source blocking method
       //      block_alts = 1 means that user will maintain blocking via
       //                     Product maintenance K3S_3000
       //      block_alts = 0 means that user will maintain blocking via
       //                     interface file K_INTPROD
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  BLOCK_ALTS';
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda);
                 block_alts = ta_flag1;
              else;
                 block_alts = 0;
              endif;



       // New to Slow for system status during product add
       //      new_slow = 1 means that this product will automatically
       //                   have system status changed from 'N' to 'S'
       //                   (New to Slow) during add to system
       //      new_slow = 0 no automatic change made to system status
       //                   when New product added to system
       //        new_usedft = 1 means that this product should use a default
       //                     average stored in field Number 2
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  NEW_SLOW  ';
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda);
                 new_slow = ta_flag1;
                 new_usedft = ta_flag2;
                 new_avgdft = ta_number2;
              else;
                 new_slow = 0;
                 new_usedft = 0;
                 new_avgdft = 0;
              endif;

       // delay days processing logic
       //      delay_days = 1 means that logic should be used
       //      delay_days = 0 means not using this logic
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'DELAY_DAYSPROCESSING';
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda);
                 delay_days = ta_flag1;
                 delay_diff = ta_number1;
              else;
                 delay_days = 0;
                 delay_diff = 0;
              endif;

       // new product automatic deal copy logic
       //      copy_deals = 1 means that logic should be used
       //      copy_deals = 0 means not using this logic
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_5056  PROCESSING';
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda);
                 copy_deals = ta_flag1;
              else;
                 copy_deals = 0;
              endif;

       // clear PR_EXCUNTL after expiration
       //      clr_record = 1 means that PR_EXCUNTL should be cleared
       //      clr_record = 0 means to not execute logic
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'EXCL_BUY  CLR_RECORD';
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda);
                 clr_record = ta_flag1;
              else;
                 clr_record = 0;
              endif;

       // clear PR_PROMQTY, PR_PROMBEG, PR_PROMEND after expiration
       //      clr_promo  = 1 means that 3 fields should be cleared
       //      clr_promo  = 0 means to not execute logic
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  CLR_PROMO ';
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda);
                 clr_promo  = ta_flag1;
              else;
                 clr_promo  = 0;
              endif;

       // include back orders in 'count days out' logic?
       //      back_order = 1 means to include back orders in logic
       //      back_order = 0 means to not include back orders in logic
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  DAYS_OUT  ';
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda);
                 back_order = ta_flag1;
              else;
                 back_order = 0;
              endif;

       // include lost sales in 'count days out' logic?
       //      lost_sales = 1 means to include lost sales in logic
       //      lost_sales = 0 means to not include lost sales in logic
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  DAYS_OUT_2';
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda);
                 lost_sales = ta_flag1;
              else;
                 lost_sales = 0;
              endif;

       // new products at Bindley, no deal copy for Location 06
       //      no_deal_06 = 1 means this is Bindley Western, perform test
       //      no_deal_06 = 0 means this is NOT Bindley Western
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'BINDLEY   NO_DEAL_06';
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda);
                 no_deal_06 = ta_flag1;
              else;
                 no_deal_06 = 0;
              endif;

       // look for Minimum Seasonal Factor being used
       //    must be reasonable value between .01 and .50
       //    or special logic will not be used
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_M080  MIN_SEASON';
              min_used   = 0;
              min_season = 0;
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda) AND ta_flag1 = 1;
                 min_season = ta_number2;
                 if min_season < 0 or min_season > .50;
                    min_season = 0;
                 endif;
              else;
                 min_season = 0;
              endif;
              if min_season > 0;
                 min_used   = 1;
              endif;

       // determine if customer wants 'cost sent as $0' logged
       //   into K_LOGPROD file as type 'c'. If the answer is yes,
       //   then see if the customer wants to use a default value
       //   for cost, stored in Number2 field.
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  COST_0    ';
              cost_0     = 0;
              cost_fill  = 0;
              cost_value = 0;
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda) AND ta_flag1 = 1;
                 cost_0     = 1;
                 if ta_flag2   = 1 AND ta_number2 > 0;
                    cost_fill  = 1;
                    cost_value = ta_number2;
                 endif;
              endif;

       //  determine if customer wants field PR_LSTRCVD updated
       //    daily in this program, which will be used in program K3S_3600
       //    to filter any products not received yet from Overstock Report
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  PR_LSTRCVD';
              lstrcvd    = 0;
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda) AND ta_flag1 = 1;
                 lstrcvd    = 1;
                 days_10out = cm_sysdate + %days(10);
              endif;

       // determine if customer wants field PR_RFBIRTH updated
       //   daily in this program, which will be used in program K3S_3600
       //   to filter any products with Reference Birth logic in play
       //      ***  notice that flag 2 is used to control the population
       //      ***  of PR_RFBIRTH
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_3600  PR_RFBIRTH';
              ref_birth  = 0;
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda) AND ta_flag2 = 1;
                 ref_birth  = 1;
              endif;

       // determine if customer wants field PR_BIRTH populated
       //   using IP_BIRTH for new products.
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  PR_BIRTH  ';
              NewBirth   = 0;
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda) AND ta_flag1 = 1;
                    NewBirth   = 1;
              endif;

       // for customers who use Corporate Profiles
       //   corp_prof = 1 means customer does use Corporate Profiles
       //   corp_prof = 0 means customer does not use Corporate Profiles
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  CORP_PROF ';
              corp_prof  = 0;
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda) AND ta_flag1 = 1;
                 corp_prof  = 1;
                 CorpProfID = ta_codeds3;
              endif;

       // will Car Count be updated from interface
       //   car_update = 1 means car count updated from interface file
       //   car_update = 0 means car count not updated from interface
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_1500  CAR_COUNT ';
              car_update = 0;
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda) and ta_flag2 = 1;
                 car_update = 1;
              endif;

       // PE1 filtering in play?
       //   PE1_FLTR_1 = 1 means we do want to filter PE1 when Demand <= Man Min Unit
       //   PE1_FLTR_1 = 0 means we do not want to filter PE1 checks
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  PE1_FLTR_1';
              PE1_FLTR_1 = 0;
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda) AND ta_flag1 = 1;
                 PE1_FLTR_1 = 1;
              endif;

       // PE snapshots in play?
       //   pe_snpshot = 1 means we do want to collect period ending snapshots
       //   pe_snpshot = 0 means we do not want to collect pe snapshots
              ta_comp    = ip_comp;
              ta_codetyp = 'APP';
              ta_codeval = 'K3S_9010  PE_SNPSHOT';
              pe_snpshot = 0;
              chain (ta_comp:ta_codetyp:ta_codeval) k_tablcoda;
              if %found(k_tablcoda) AND ta_flag1 = 1;
                 pe_snpshot = 1;
              endif;

       // the purpose of this section is to read the very first
       //   location record, to ensure that the field lc_buyrbad is available
       //   to be used if a lg_logtype of '6' is generated for
       //   an invalid location being passed.
              lc_locn = *blanks;
              setll (lc_comp:lc_locn) k_locatnsa;
              read k_locatnsa;

           endif;

       // ----------------------------------------------------- Location break

       //  change in location
           if ip_locn <> locn;
              locn    = ip_locn;

              lc_locn = ip_locn;

       //  get location
              chain (lc_comp:lc_locn) k_locatnsa;

       //    test if location set up in database
              if %found(k_locatnsa);
                 bad_locn  = *off;

       //      make demand filter low limit a negative value
                 demlo = lc_demlo * -1;

       //       save answer for later testing in Delay Days processing
                 if delay_days = 1;
                    delay_test = lc_sysdate - %days(delay_diff);
                 endif;

              else;
                 bad_locn  = *on;

              endif;

           endif;

       // ----------------------------------------------------- Supplier break

       // change in supplier ID
           if supl <> suplsaved;

       // save new supplier ID
              suplsaved = supl;

       // prime key list for supplier
              sp_locn    = ip_locn;
              sp_supl    = ip_supl;
              sp_suplsub = ip_suplsub;

       // get supplier record
              chain (sp_comp:sp_locn:sp_supl:sp_suplsub) k_supliera;

       //     test if supplier set up in database
              if %found(k_supliera);
                 bad_suplr  = *off;
                 saved_name = sp_name;
                 saved_buyr = sp_buyr;
                 saved_lt   = sp_leadtmo;
                 saved_ltv  = sp_leadtmv;
              else;
                 bad_suplr = *on;
              endif;

           endif;

       // ---------------------------------- Process product interface records

       // process product interface records

       //     always start Log Type as blank, no carry over from
       //     previous product
           lg_logtype = ' ';

       // If location no good, then log error, and by-pass the rest of tests
           if bad_locn  = *on;
              lg_logtype = '6';
              lg_prvsupl = *blanks;
              lg_prvsub  = *blanks;
              lg_prvsplu = *blanks;
              lg_prvname = *blanks;
           // sp_buyr    = 'ZZZ';
              sp_buyr    = lc_buyrbad;
              sp_name    = bad_locnd;
              exsr $_log_prod;

       // Location is fine, so continue
           else;

       // If supplier no good, then log error, and by-pass the rest of tests
              if bad_suplr = *on;
                 lg_logtype = '5';
                 lg_prvsupl = *blanks;
                 lg_prvsub  = *blanks;
                 lg_prvsplu = *blanks;
                 lg_prvname = *blanks;
                 sp_buyr    = lc_buyrbad;
                 sp_name    = bad_suplrd;
                 exsr $_log_prod;

       // Supplier is fine, so continue
              else;

       // This next set of tests will determine if product is already in
       //   the database, and can simply be updated with new information.
       //   The product may exist under a different supplier id. Depending
       //   on the type of industry being processed, a decission is made to
       //   either create a new product record, or simply to copy existing
       //   product information that exists under a different supplier to
       //   the new supplier.

                 exist_here = *off;
                 exist_othr = *off;

       //   prime key list
                 producta_key.pr_locn    = ip_locn;
                 producta_key.pr_supl    = ip_supl;
                 producta_key.pr_suplsub = ip_suplsub;
                 producta_key.pr_prod    = ip_prod;

       //   determine if product exists at this supplier

       //   get product record (locn,supl,suplsub,prod)
                 chain %kds(producta_key) k_producta;
       //      product does exist at this supplier
                 if %found(k_producta);
                    exist_here = *on;

       //      if product had been in delete count mode, then it is
       //         being re-instated, so send a record to the log file
                    if pr_deltcnt > 0;
                       lg_logtype = '7';
                       lg_prvsupl = *blanks;
                       lg_prvsub  = *blanks;
                       lg_prvsplu = *blanks;
                       lg_prvname = *blanks;

                       exsr $_log_prod;
                    endif;
                 else;

       //   look for product record at this location
                       px_comp    = ip_comp;
                       px_locn    = ip_locn;
                       px_prod    = ip_prod;

       //      does product exist at another supplier ?
                       setll (px_comp:px_locn:px_prod) k_productc;

       //      if yes, then see if it is regular source product
                       if %equal(k_productc);
                          read k_productc;

                          dow not %eof(k_productc);

                             if not %eof(k_productc)    AND
                                pr_comp    = ip_comp    AND
                                pr_locn    = ip_locn    AND
                                pr_prod    = ip_prod    AND
                                pr_altsrce = 0;

                                exist_othr = *on;
                                px_supl    = pr_supl;
                                px_suplsub = pr_suplsub;
                                leave;
                             endif;

                             if not %eof(k_productc);
                                read k_productc;
                             endif;

                             if not %eof(k_productc);
                                if pr_comp   <> ip_comp    OR
                                   pr_locn   <> ip_locn    OR
                                   pr_prod   <> ip_prod;

                                   leave;
                                endif;
                             endif;

                          enddo;
                       endif;

                 endif;

       //   product is allowed to be switched to another supplier
                 if lc_swallow = 1;

                    select;

       //   product does exist at this supplier, so just update
                       when exist_here = *on;
                            exsr   $_update;
                            update rk_product;

       //   product does exist at another supplier, and supplier switching
       //       allowed, so move it.
                       when exist_othr = *on;
                            exsr $_switch;

       //   product does not exist at another supplier, so add it
                       when exist_othr = *off;
                            exsr  $_newprod;
                            exsr  $_update;
                            write rk_product;

                            exsr  $_prodlog;

       //   go check for deals
                            if copy_deals = 1;
       //   but make sure new product NOT under Hub Transfer Supplier
                               trans_prod = 0;
                               exsr $_transfer;
                               if trans_prod = 0;
       //   if Bindley, make sure its not location 06
                                  if no_deal_06 = 0 OR
                                    (no_deal_06 = 1 AND pr_locn <> '06');
                                    night = 'Y';
                                    callp K3S_5056(pr_comp:
                                                   pr_locn:
                                                   pr_prod:
                                                   pr_supl:
                                                   pr_suplsub:
                                                   night);
                                  endif;
                               endif;
                            endif;

                    endsl;

       //   product is not allowed to be switched to another supplier
                 else;

                    select;

       //   product does exist at this supplier, so just update
                       when exist_here = *on;
                            exsr   $_update;
                            update rk_product;

       //   product does not exist at this supplier, so add it
                       when exist_here = *off;
                            exsr   $_newprod;
                            exsr   $_update;
                            write  rk_product;

                            exsr   $_prodlog;

       //   go check for deals
                            if copy_deals = 1;
       //   but make sure new product NOT under Hub Transfer Supplier
                               trans_prod = 0;
                               exsr $_transfer;
                               if trans_prod = 0;
       //   if Bindley, make sure its not location 06
                                  if no_deal_06 = 0 OR
                                     (no_deal_06 = 1 AND pr_locn <> '06');
                                      night = 'Y';
                                      callp K3S_5056(pr_comp:
                                                     pr_locn:
                                                     pr_prod:
                                                     pr_supl:
                                                     pr_suplsub:
                                                     night);
                                  endif;
                               endif;
                            endif;

                    endsl;

       //   lc_swallow
                 endif;

       //   bad_suplr
              endif;

       //   bad_locn
           endif;

       // read next product interface record
           read k_intprod;

       // read product interface records end of loop
       enddo;

       // --------------------------------------------------- End of Main Loop

       // --------------------------------- determine if period end took place
       //     periodicity 12
       if total_12 > 0 and
          rolled_12 / total_12 > .50;

          per_end_12 = '1';
          if ye_for_12  = '1';
             yearend_12 = '1';
          endif;
       endif;

       //     periodicity 13
       if total_13 > 0 and
          rolled_13 / total_13 > .50;

          per_end_13 = '1';
          if ye_for_13  = '1';
             yearend_13 = '1';
          endif;
       endif;

       //     periodicity 52
       if total_52 > 0 and
          rolled_52 / total_52 > .50;

          per_end_52 = '1';
          if ye_for_52  = '1';
             yearend_52 = '1';
          endif;
       endif;

       //       update local data area *lda
       out *dtaara;

       // call module to retrieve timestamp
       callp K3S_Retrieve_Timestamp(time_stamp);
       today_end = %char(time_stamp);

       // finished, set on LR
       *inlr = *on;

       //***************************************************** End of program

       /////////////////////////////////////////////////////// Update product

       // update product fields from interface

       begsr $_update;

       //  initialize fields
       clear pr_soqnite;
       clear pr_qtybaln;
       clear pr_overflg;
       clear pr_overunt;
       clear pr_overcst;
       clear pr_overcur;
       clear pr_overmax;
       clear pr_qtypend;

       //  update buy group since this product could have switched buyers
       pr_buyr    = saved_buyr;

       //  keep original supplier up to date
       pr_suplorg = ip_supl;
       pr_suplors = ip_suplsub;

       pr_suplusr = ip_suplusr;
       pr_suplusb = ip_suplusb;

       //  last interface date
       pr_lstintr = lc_sysdate;

       // last update date
       pr_lastupd = lc_sysdate;

       //  region update
       pr_regn    = sp_regn;

       //  manufactor out flag
       pr_mfgout  = ip_mfgout;

       //  product sequence
       pr_prodseq = ip_prodseq;

       //  product description information

       //      product must have first description
       if ip_desc1 = *blanks;
          lg_logtype = 'K';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
          ip_desc1   = *blanks;
          ip_desc1   = '** Missing description **';
          exsr $_log_prod;
       endif;
       pr_desc1   = ip_desc1;

       //     only update description 2 if data passed from host system
       if ip_desc2 <> *blanks;
          pr_desc2 = ip_desc2;
       endif;

       //     only update manufactor if data passed from host system
       if ip_mfg <> *blanks;
          pr_mfg = ip_mfg;
       endif;

       //      default catalog with ndc/upc code
       pr_catalog = ip_ndc_upc;

       //      only update ndc/upc code if data passed from host system
       if ip_ndc_upc <> *blanks;
          pr_ndc_upc = ip_ndc_upc;
       endif;

       //      only update unit of measure if data passed from host system
       if ip_uom <> *blanks;
          pr_uom = ip_uom;
       endif;

       //      only update pack size if data passed from host system
       if ip_packsiz <> *blanks;
          pr_packsiz = ip_packsiz;
       endif;

       //      only update ti/hi if data passed from host system
       if ip_tihi <> *blanks;
          pr_tihi = ip_tihi;
       endif;

       //      only update warehouse location if data passed from host system
       if ip_whslocn <> *blanks;
          pr_whslocn = ip_whslocn;
       endif;

       //  product status
       //      product status passed must be an 'R' or 'D'
       //        if not, then an 'R' is assumed
       if ip_status <> 'R' AND ip_status <> 'D';
          lg_logtype = 'V';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // if ip_status <> *blanks;
       //    ip_desc1 = 'Invalid status passed as ' +
       //               ip_status;
       // else;
       //    ip_desc1 = 'Invalid status passed as blank';
       // endif;
          exsr $_log_prod;
          ip_status = 'R';
       endif;

       //      if discontinued status passed, and product currently not
       //      set as discontinued, then change to discontinued status
       if ip_status  = 'D' AND pr_sysstat <> 'D';
          pr_sysstat = 'D';

       //          if the first time flag is on, then this customer wants
       //          any products going to 'D' for the first time, to
       //          automatically be changed to user status 'M'
       //            log these as type '8'
       //            clear any 'F' Freeze or 'P' Probation dates
          if first_time = '1';
             pr_usrstat = 'M';
             clear pr_forfrez;
             clear pr_probdat;
             lg_logtype = '8';
             lg_prvsupl = *blanks;
             lg_prvsub  = *blanks;
             lg_prvsplu = *blanks;
             lg_prvname = *blanks;
             sp_name    = saved_name;
             sp_buyr    = saved_buyr;
             exsr       $_log_prod;
          endif;

       endif;

       //      if regular status passed, and product currently set as
       //      discontinued status, then re-instate product back to
       //      either 'R', 'L', or 'S'
       if ip_status  = 'R' AND pr_sysstat = 'D';
       //      first you must force system status to an 'R' for k3s_c160
          pr_sysstat = 'R';
       //------------------------------------------------ update system status
      /copy k3s_c160
       endif;

       //  group 1 logic
       pr_group1  = ip_group1;

       if exist_here = *off;
          pr_group1o = *blanks;
          pr_group2o = *blanks;
          pr_group3o = *blanks;
          pr_group4o = *blanks;
          pr_group5o = *blanks;
       endif;

       if pr_group1o <> *blanks and
          lc_prdgrp1 = 0 and
          exist_here = *on;

          pr_group1o = *blanks;
       endif;

       if pr_group1o <> *blanks;
          pr_group1  = pr_group1o;
       endif;

       //  group 2 logic
       pr_group2  = ip_group2;

       if pr_group2o <> *blanks and
          lc_prdgrp2 = 0 and
          exist_here = *on;

          pr_group2o = *blanks;
       endif;

       if pr_group2o <> *blanks;
          pr_group2  = pr_group2o;
       endif;


       //  group 3 logic
       pr_group3  = ip_group3;

       if pr_group3o <> *blanks and
          lc_prdgrp3 = 0 and
          exist_here = *on;

          pr_group3o = *blanks;
       endif;

       if pr_group3o <> *blanks;
          pr_group3  = pr_group3o;
       endif;


       //  group 4 logic
       pr_group4  = ip_group4;

       if pr_group4o <> *blanks and
          lc_prdgrp4 = 0 and
          exist_here = *on;

          pr_group4o = *blanks;
       endif;

       if pr_group4o <> *blanks;
          pr_group4  = pr_group4o;
       endif;


       //  group 5 logic
       pr_group5  = ip_group5;

       if pr_group5o <> *blanks and
          lc_prdgrp5 = 0 and
          exist_here = *on;

          pr_group5o = *blanks;
       endif;

       if pr_group5o <> *blanks;
          pr_group5  = pr_group5o;
       endif;

       //  pricing logic

       //      don't allow purchase price divisor to be less than 1
       if ip_costdiv < 1;
          lg_logtype = 'L';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Purchase price divisor ------>';
       // ip_costdiv = ip_costdiv * -1;
       // evalr ip_desc1 = %editc(ip_costdiv:'X');
          exsr $_log_prod;
          ip_costdiv = 1;
       endif;

       //      don't allow purchase price to be negative
       if ip_costreg < 0;
          lg_logtype = 'I';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Negative purchase price of--->';
       // evalr ip_desc1 = %editc(ip_costreg:'X');
       // ip_costreg = ip_costreg * -1;
          exsr $_log_prod;
          ip_costreg = 0;
       endif;

       //      Log if purchase price comes across as $0?
       //        Optionally determine if a default value to be used.
       //        If used it will be placed into purchase AND sales price.
       if ip_costreg = 0 and cost_0 = 1;
          lg_logtype = 'c';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
          if cost_fill  = 1;
             ip_costreg = cost_value;
             ip_sales   = cost_value;
          endif;
          exsr $_log_prod;
       endif;

       //      don't allow sales price to be negative
       if ip_sales   < 0;
          lg_logtype = 'J';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Negative sales price of ----->';
       // ip_sales   = ip_sales   * -1;
       // move      ip_sales      ip_desc1
          exsr $_log_prod;
          ip_sales   = 0;
       endif;

       //      don't allow sales price to be < cost
       if ip_sales   < ip_costreg / ip_costdiv;
          lg_logtype = 'Y';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks
       // ip_desc1   = 'Sales price < cost ---------->';
          ip_sales   = ip_costreg / ip_costdiv;
       // move      ip_sales      ip_desc1
          exsr $_log_prod;
       endif;

       //    save cost changes
       if exist_here = *off;
          pr_ovrcreg = 0;
          pr_ovrcdiv = 1;
       endif;

       if pr_ovrcreg > 0 and
          lc_overcst = 0 and
          exist_here = *on;

          pr_ovrcreg = 0;
          pr_ovrcdiv = 1;
       endif;

       if pr_ovrcreg > 0 and
          lc_overcst = 1 and
          exist_here = *on;

          ip_costreg = pr_ovrcreg;
          ip_costdiv = pr_ovrcdiv;
       endif;

       if pr_costreg <> ip_costreg;
          pr_costlst = pr_costreg;
          pr_costldt = lc_sysdate;
       endif;

       //    make sure over-ride cost divisor is at least 1
       if pr_ovrcdiv < 1;
          pr_ovrcdiv = 1;
       endif;

       //    update costs
       pr_costreg = ip_costreg;
       pr_costdiv = ip_costdiv;
       pr_costeac = ip_costreg / ip_costdiv;

       //    update sales price
       pr_sales   = ip_sales;

       //    quantity logic

       //    on hand section
       if ip_qtyohnd < 0;
          lg_logtype = 'F';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks
       // ip_desc1   = 'Negative on hand of --->';
       // ip_qtyohnd = ip_qtyohnd * -1;
       // move      ip_qtyohnd    ip_desc1
          exsr $_log_prod;
          clear ip_qtyohnd;
       endif;

       //      is delay days logic being used ?
       //        if so, then test if yesterday's onhand has gone to 0,
       //        because of daily sales
       if delay_days = 1;
          if pr_sysstat <> 'D' AND
             pr_usrstat <> 'M' AND
             pr_ansaleu  > 0;

             if pr_qtyohnd > 0 AND
                ip_qtyohnd = 0 AND
                pr_birth   < delay_test AND
                ip_dlysale > 0;

                clear delayuntil;
                callp K3S_3860(ip_comp:
                               ip_locn:
                               ip_supl:
                               ip_suplsub:
                               sp_buyr:
                               pr_ansaleu:
                               lc_sysdate:
                               delayuntil);

                if delayuntil  > pr_excuntl;
                   pr_excuntl  = delayuntil;
                endif;
             endif;
          endif;
       endif;

       pr_qtyohnd = ip_qtyohnd;

       //     on order section
       if ip_qtyoord < 0;
          lg_logtype = 'G';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Negative on order of --->';
       // ip_qtyoord = ip_qtyoord * -1;
       // move      ip_qtyoord    ip_desc1
          exsr $_log_prod;
          clear ip_qtyoord;
       endif;
       pr_qtyoord = ip_qtyoord;

       //     back order section
       if ip_qtyback < 0;
          lg_logtype = 'H';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;

          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
        //ip_desc1   = *blanks
        //ip_desc1   = 'Negative back orders of --->'
        //ip_qtyback = ip_qtyback * -1;
        //move      ip_qtyback    ip_desc1
          exsr $_log_prod;
          clear ip_qtyback;
       endif;
       pr_qtyback = ip_qtyback;

       //  buying multiple
       //      is buying multiple being passed less than 1?
       if ip_buymult < 1;
          lg_logtype = 'M';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Invalid buying multiple passed';
          exsr $_log_prod;
          ip_buymult = 1;
       endif;
       pr_buymuli = ip_buymult;
       pr_buymult = ip_buymult;
       if pr_buymulo <> *zeros;
          pr_buymult = pr_buymulo;
       endif;

       //  minimum quantity
       //      is minimum quantity being passed less than 1?
       if ip_minqty < 1;
          lg_logtype = 'N';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Invalid min. quantity passed';
          exsr $_log_prod;
          ip_minqty  = 1;
       endif;
       pr_minqty  = ip_minqty;
       if pr_minqtyo <> *zeros;
          pr_minqty  = pr_minqtyo;
       endif;

       //  purchase increment
       //      is purchase increment being passed less than 0?
       if ip_purincr < 0;
          lg_logtype = 'O';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Negative purchase increment';
          exsr $_log_prod;
          ip_purincr = 0;
       endif;
       pr_purincr = ip_purincr;
       if pr_purinco <> *zeros;
          pr_purincr = pr_purinco;
       endif;

       //  Unit 6 bracket
       //      is unit 6 bracket value being passed less than 0?
       if ip_disothr < 0;
          lg_logtype = 'd';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
          exsr $_log_prod;
          ip_disothr = 0;
       endif;
       pr_disothr = ip_disothr;
       if pr_disotho <> *zeros;
          pr_disothr = pr_disotho;
       endif;

       //  Unit 7 bracket
       //      is unit 7 bracket value being passed less than 0?
       if ip_disunt7 < 0;
          lg_logtype = 'e';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
          exsr $_log_prod;
          ip_disunt7 = 0;
       endif;
       pr_disunt7 = ip_disunt7;
       if pr_disun7o <> *zeros;
          pr_disunt7 = pr_disun7o;
       endif;

       //  Unit 8 bracket
       //      is unit 8 bracket value being passed less than 0?
       if ip_disunt8 < 0;
          lg_logtype = 'f';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
          exsr $_log_prod;
          ip_disunt8 = 0;
       endif;
       pr_disunt8 = ip_disunt8;
       if pr_disun8o <> *zeros;
          pr_disunt8 = pr_disun8o;
       endif;

       //  Unit 9 bracket
       //      is unit 9 bracket value being passed less than 0?
       if ip_disunt9 < 0;
          lg_logtype = 'g';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
          exsr $_log_prod;
          ip_disunt9 = 0;
       endif;
       pr_disunt9 = ip_disunt9;
       if pr_disun9o <> *zeros;
          pr_disunt9 = pr_disun9o;
       endif;

       //  product rebate
       //      is rebate being passed less than 0?
       if ip_rebate  < 0;
       // lg_logtype = 'P';
          lg_logtype = 'Z';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Negative rebate passed';
          exsr $_log_prod;
          ip_rebate  = 0;
       endif;
       pr_rebate  = ip_rebate;

       //  convenience pack
       //      is convenience pack being passed less than 0?
       if ip_convpak  < 0;
          lg_logtype = 'Q';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks
       // ip_desc1   = 'Neg. convenience pack passed';
          exsr $_log_prod;
          ip_convpak = 0;
       endif;
       pr_convpak = ip_convpak;
       if pr_convpko <> *zeros;
          pr_convpak = pr_convpko;
       endif;

       //  convenience pack less than buy multiple
       //      is convenience pack being used, and if so is it less
       //      than the buy multiple used to build orders?
       if (pr_convpak > 0 AND
          pr_convpak < pr_buymult);

          lg_logtype = 'a';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Conv Pack less than Buy Mult';
          exsr $_log_prod;
       endif;

       //  convenience pack not a true multiple
       //      is convenience pack being used, and if so is it evenly
       //      divisible by the buy multiple?
       //      no need to log this if previous test above failed - 'a'
       if pr_convpak > 0 AND pr_buymult > 0
                         AND lg_logtype <> 'a';

          convpkw1 = pr_convpak/pr_buymult;
          convpkw2 = %rem(pr_convpak:pr_buymult);
          if convpkw2 <> 0;
             lg_logtype = 'b';
             lg_prvsupl = *blanks;
             lg_prvsub  = *blanks;
             lg_prvsplu = *blanks;
             lg_prvname = *blanks;
             sp_name    = saved_name;
             sp_buyr    = saved_buyr;
       //    ip_desc1   = *blanks;
       //    ip_desc1   = 'Conv Pack not a true multiple';
             exsr $_log_prod;
          endif;
       endif;

       //  weight logic
       //      don't allow weight divisor to be less than 1
       if ip_weightd  < 1;
          lg_logtype = 'S';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Weight divisor less than 1';
          exsr $_log_prod;
          ip_weightd = 1;
       endif;

       //      is weight being passed less than 0?
       if ip_weight  < 0;
          lg_logtype = 'R';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Negative weight being passed';
          exsr $_log_prod;
          ip_weight  = 0;
       endif;

       pr_weight  = ip_weight;
       pr_weightd = ip_weightd;

       if pr_weighto <> *zeros;
          pr_weight  = pr_weighto;
       endif;

       if pr_weighdo <> *zeros;
          pr_weightd = pr_weighdo;
       endif;

       //  volume logic
       //      don't allow volume divisor to be less than 1
       if ip_volumed  < 1;
          lg_logtype = 'U';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Volume divisor less than 1';
          exsr $_log_prod;
          ip_volumed = 1;
       endif;

       //    is volume being passed less than 0?
       if ip_volume  < 0;
          lg_logtype = 'T';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Negative volume being passed';
          exsr $_log_prod;
          ip_volume  = 0;
       endif;

       pr_volume  = ip_volume;
       pr_volumed = ip_volumed;

       if pr_volumeo <> *zeros;
          pr_volume  = pr_volumeo;
       endif;

       if pr_volumdo <> *zeros;
          pr_volumed = pr_volumdo;
       endif;

       //  accumulated demand information

       //      is data valid (negative sales being passed?)
       if ip_dlysale < 0;
          lg_logtype = 'D';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Negative sales of --->';
       // ip_dlysale = ip_dlysale * -1;
       // move      ip_dlysale    ip_desc1
          exsr $_log_prod;
          clear ip_dlysale;
       endif;

       //      is data valid (negative outs being passed?)
       if ip_dlyouts < 0;
          lg_logtype = 'E';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Negative outs of --->';
       // ip_dlyouts = ip_dlyouts * -1;
       // move      ip_dlyouts    ip_desc1
          exsr $_log_prod ;
          clear ip_dlyouts;
       endif;

       //      if daily demand not sent in interface, then period-to-date
       //      demand is being passed, so clear accumulated fields
       if lc_daily = 0;
          clear pr_accsale;
          clear pr_accouts;
       endif;

       //      add daily sales
       pr_accsale += ip_dlysale;
       //      add daily lost sales
       pr_accouts += ip_dlyouts;
       //      demand for period
       pr_accdem  = pr_accsale + pr_accouts;

       //  do not include products excluded from 'count days' logic
       if pr_daysunt <> 999;

       //  do not include products not yet received
          if pr_lstrcvd <> not_recvd;

       //  determine if lost sales are used with 'count days out' logic
       //    and if any lost sales exist.
             if lost_sales = 1;
                if (pr_sysstat <> 'N') and
                   (pr_forcast > *zeros) and
                   (ip_dlyouts > *zeros);

                   pr_daysout += 1;
                endif;

             else;

       //  determine if back orders are used with 'count days out' logic
       //    and if any back orders exist.
                continue = 1;
                if back_order = 1 and pr_qtyback = 0;
                   continue = 0;
                endif;

       //  days out logic
                if (ip_qtyohnd <= pr_daysunt) and
                   (pr_sysstat <> 'N') and
                   (pr_forcast > *zeros) and
                   continue = 1;

                   pr_daysout += 1;
                endif;
       //     end of 'else' for lost_sales = 1
             endif;

       //     end for pr_lstrcvd <> not_recvd
          endif;

       //     end for pr_daysunt <> 999
       endif;

       //  clear delete count
       pr_deltcnt = 0;

       //  temporary split code
       pr_splttmp = 1;

       //  contract existance
       pr_contflg = ip_contflg;

       //  car count flag (must be 0=no or 1=yes)
       if car_update = 1;
          pr_carcoun = ip_carcoun;
          if pr_carcoun <> 0 and
             pr_carcoun <> 1;
             pr_carcoun =  0;
          endif;
       endif;

       //  transfer on order
       pr_trnoord = ip_trnoord;

       //  alternate source on order
       pr_altoord = ip_altoord;

       //  update alternate source process flag
       //     has updating of field been blocked? 0=No
       if block_alts = 0;
       //     if value passed not a 0 or 1, then set to 0
          if ip_procalt <> 0 AND ip_procalt <> 1;
             lg_logtype = 'X';
             lg_prvsupl = *blanks;
             lg_prvsub  = *blanks;
             lg_prvsplu = *blanks;
             lg_prvname = *blanks;
             sp_name    = saved_name;
             sp_buyr    = saved_buyr;
       //    ip_desc1   = *blanks;
       //    ip_desc1   = 'Invalid flag alt srce process';
             ip_procalt = 0;
             exsr $_log_prod;
          endif;
          pr_procalt = ip_procalt;
       endif;

       //  clear exclude buying until after expiration?
       if clr_record = 1 AND
          pr_excuntl < lc_sysdate;

          clear pr_excuntl;
       endif;

       //  clear 3 promo fields after expiration?
       if clr_promo  = 1 AND
          pr_promend <> not_0001 and
          pr_promend < lc_sysdate;

          clear pr_promqty;
          clear pr_prombeg;
          clear pr_promend;
       endif;

       // --------------------------------------------------------- deal logic

       //  if a deal exists for the product being updated, and
       //     we have passed deal end date, then remove deal ID from product
       //     record, and determine if another deal exists that starts after
       //     the deal ID being removed.

       if pr_deal <> *blanks AND
          lc_sysdate > pr_dealend;

       //     go check for another deal
          pr_deal = *blanks;
          pr_dealbeg = pr_dealend;
          callp K3S_5120(ip_comp:
                         ip_locn:
                         ip_supl:
                         ip_suplsub:
                         ip_prod:
                         pr_deal:
                         pr_dealbeg:
                         pr_dealend:
                         pr_dealalw:
                         pr_dealuse);

       //     if another upcoming deal does not exist for this product,
       //        then clear fields in product record.
          if pr_deal = *blanks;
             clear pr_dealbeg;
             clear pr_dealend;
             clear pr_dealalw;
             clear pr_dealuse;
          endif;

       endif;

       // ----------------------------------------------------- end of period?

       //  if period has changed, then save history and update forecast
       //     also, total up the number of products processed by periodicity
       select;

       //       weekly forecasting
          when pr_forcint =  52;
               forcper = lc_perd52;
               total_52 += 1;

       //       monthly forecasting
          when pr_forcint =  12;
               forcper = lc_perd12;
               total_12 += 1;

       //       thirteen four-weekly forecasting
          when pr_forcint =  13;
               forcper = lc_perd13;
               total_13 += 1;

       endsl;

       //       period in product file different from location file, end perd
       if pr_forcper <> forcper;
          exsr $_end_perd;

       else;
       //   'Not end of period' processing

       //        if product is coded as Frozen,
       //        then check Today's date is greater than Frozen date
       //        clear frozen information
          if pr_usrstat = 'F';
             if lc_sysdate >  pr_forfrez;
                clear pr_usrstat;
                clear pr_forfrez;
             endif;
          endif;

       endif;

       //   If product is coded as Probation,
       //      then check Today's date is greater than Probation date
       //           clear probation information and log
       if pr_usrstat = 'P';
          if lc_sysdate >  pr_probdat;
             clear pr_usrstat;
             clear pr_probdat;
       //    lg_logtype = 'P';
             lg_logtype = '9';
             lg_prvsupl = *blanks;
             lg_prvsub  = *blanks;
             lg_prvsplu = *blanks;
             lg_prvname = *blanks;
             sp_name    = saved_name;
             sp_buyr    = saved_buyr;
             exsr $_log_prod;
          endif;
       endif;

       //       annual sales dollars and units
       pr_ansaleu = pr_forcast * pr_forcint;
       eval(h)   pr_ansale$ = pr_ansaleu * pr_sales;

       //    is customer updating PR_LSTRCVD 'last received date' daily?
       if lstrcvd = 1;
           prodltma_key.pl_comp = pr_comp;
           prodltma_key.pl_locn = pr_locn;
           prodltma_key.pl_supl = pr_supl;
           prodltma_key.pl_suplsub = pr_suplsub;
           prodltma_key.pl_prod = pr_prod;
           setll %kds(prodltma_key:5) k_prodltma;
           reade(n) %kds(prodltma_key:5) k_prodltma;
           if not %eof(k_prodltma)    AND
              pl_ordrecv < days_10out AND
              pl_ordrecv > pr_lstrcvd;

              pr_lstrcvd = pl_ordrecv;
           endif;
       endif;

       //    is customer updating PR_RFBIRTH 'Reference Birth' daily?
       if ref_birth = 1;
          if pr_rfbirth = not_recvd  AND
             pr_qtyohnd > 0;

             pr_rfbirth = lc_sysdate;
          endif;
       endif;

       endsr;

       // /////////////////////////////////////////////////// Switch suppliers

       //  switch product to another supplier

       begsr $_switch;

       // pass flag back to night job to control process of changing
       // supplier ID's for alt source orders that have been saved during
       // the week.
       supl_chg = '1';

       // force getting supplier again on next product transaction input recd
       suplsaved  = *blanks;

       // prime key list for previous supplier information
       sx_locn    = px_locn;
       sx_supl    = px_supl;
       sx_suplsub = px_suplsub;
       chain (sx_comp:sx_locn:sx_supl:sx_suplsub) k_supliera;

       // put entry into log file for supplier change to product
       lg_logtype = '2';
       lg_prvsupl = sp_supl;
       lg_prvsub  = sp_suplsub;
       lg_prvsplu = sp_supl;
       lg_prvname = sp_name;
       sp_name    = saved_name;
       sp_buyr    = saved_buyr;
       exsr $_log_prod;

       //  change product's history file records to reflect new supplier

       if pr_forcint = 12 OR pr_forcint = 13;

       //     monthly and 13-four weekly products
          callp K3S_3510(ip_comp:
                         ip_locn:
                         px_supl:
                         px_suplsub:
                         ip_prod:
                         lc_sysdate:
                         ip_supl:
                         ip_suplsub:
                         ip_suplusr:
                         ip_suplusb);

       else;

       //     weekly products
          callp K3S_3511(ip_comp:
                         ip_locn:
                         px_supl:
                         px_suplsub:
                         ip_prod:
                         lc_sysdate:
                         ip_supl:
                         ip_suplsub:
                         ip_suplusr:
                         ip_suplusb);

       endif;

       //  change supplier information
       pr_supl    = ip_supl;
       pr_suplsub = ip_suplsub;
       pr_suplusr = ip_suplusr;
       pr_suplusb = ip_suplusb;
       pr_suplorg = ip_supl;
       pr_suplors = ip_suplsub;
       pr_buyr    = saved_buyr;

       //  use new supplier's lead time information
       pr_leadtm  = saved_lt;
       pr_leadtmv = saved_ltv;
       clear pr_leadtms;

       //  clear deal ID fields
       clear pr_deal;
       clear pr_dealbeg;
       clear pr_dealend;
       clear pr_dealalw;
       clear pr_dealuse;

       //write new product information
       exsr $_update;
       write rk_product;


       //   go check for deals
       if copy_deals = 1;
       //   but make sure new product NOT under Hub Transfer Supplier
          trans_prod = 0;
          exsr $_transfer;
          if trans_prod = 0;
       //   if Bindley, make sure its not location 06
             if no_deal_06 = 0 OR
                (no_deal_06 = 1 AND pr_locn <> '06');

                night = 'Y';
                callp K3S_5056(pr_comp:
                               pr_locn:
                               pr_prod:
                               pr_supl:
                               pr_suplsub:
                               night);
             endif;
          endif;
       endif;

       //  prime key list for removal of product record that was copied
       producta_key.pr_locn = px_locn;
       producta_key.pr_supl = px_supl;
       producta_key.pr_suplsub = px_suplsub;
       producta_key.pr_prod = px_prod;
       //  get product record (locn,suplusr,prod) to be removed
       chain %kds(producta_key) k_producta;
       if %found(k_producta);
          delete rk_product;
       endif;

       endsr;

       ////////////////////////////////////////////////////////// New product

       //  add new product to database

       begsr $_newprod;


       // key information
       pr_comp    = ip_comp;
       pr_locn    = ip_locn;
       pr_supl    = ip_supl;
       pr_suplsub = ip_suplsub;
       pr_suplusr = ip_suplusr;
       pr_suplusb = ip_suplusb;
       pr_suplorg = ip_supl;
       //pr_suplors = *blanks;
       pr_suplors = ip_suplsub;
       pr_prod    = ip_prod;

       //  default buyer from supplier
       pr_buyr    = sp_buyr;

       //  birth date from location file
       pr_birth   = lc_sysdate;
       //    or from IP_BIRTH based upon APP 'K3S_9010  PR_BIRTH' setting
       if NewBirth = 1;
          pr_birth   = ip_birth;
       endif;

       //  lead time from supplier file
       pr_leadtm  = sp_leadtmo;
       pr_leadtmv = sp_leadtmv;

       //  system status as NEW
       pr_sysstat = 'N';

       //  automatic change of system status from 'N' to 'S'?
       if new_slow = 1;
          pr_sysstat = 'S';
       //         default average for new products
          if new_usedft = 1 and
             new_avgdft > 0;

             pr_forcast = new_avgdft;
          endif;
       endif;

       //  long term trend rate to 1.00

       pr_longtrm = 1.00;

       //  line cost from location file
       pr_linecst = sp_linecst;

       //  convenience pack % from location file
       pr_convpkp = sp_convpkp;

       //  ranking information
       pr_rnkbuy$ = 0;
       pr_rnkbuyu = 0;
       pr_rnkloc$ = 0;
       pr_rnklocu = 0;
       pr_rnkcom$ = 0;
       pr_rnkcomu = 0;
       pr_rnksup$ = 0;
       pr_rnksupu = 0;
       pr_rnkdate = lc_sysdate;

       //  purchase order quantity divisor to 1
       pr_poqtydv = 1;

       //  dev% value from location file
       pr_fordevp = lc_fordevp;

       //  previous dev% value from location file
       //    this would be helpful if previous averages need to be
       //    restored, and there are new products that had no prv value
       pr_prvdevp = lc_fordevp;

       //  investment method from company file
       pr_invmeth = cm_invmeth;

       //  forecast method from company file
       pr_formeth = cm_formeth;

       //  forecast interval

       //      is forecast interval code being passed a valid one?
       //      if not, default to 2 for monthly
       //         should be:  1 = weekly
       //                     2 = monthly
       //                     3 = 13 four-weekly
       if ip_forctyp < 1 OR ip_forctyp > 3;
          lg_logtype = 'W';
          lg_prvsupl = *blanks;
          lg_prvsub  = *blanks;
          lg_prvsplu = *blanks;
          lg_prvname = *blanks;
          sp_name    = saved_name;
          sp_buyr    = saved_buyr;
       // ip_desc1   = *blanks;
       // ip_desc1   = 'Invalid forecast cycle code';
          ip_forctyp = 2;
          exsr $_log_prod;
       endif;

       select;

       //       weekly forecasting
          when ip_forctyp = 1;
               pr_forcint = 52;
               pr_forcper = lc_perd52;
               pr_forcyr  = lc_year52;

       //       monthly forecasting
          when ip_forctyp = 2;
               pr_forcint = 12;
               pr_forcper = lc_perd12;
               pr_forcyr  = lc_year12;

       //       thirteen four-weekly forecasting
          when ip_forctyp = 3;
               pr_forcint = 13;
               pr_forcper = lc_perd13;
               pr_forcyr  = lc_year13;

       endsl;

       //  permanent split code to 1
       pr_spltprm = 1;

       //  initialize last cost to 0, so update routine will save last date
       pr_costlst = 0;

       //  use supplier service level target as default for new product
       pr_service = sp_service;

       //  check to see if history already exists for this product
       callp K3S_3037(pr_comp:
                      pr_locn:
                      pr_suplusr:
                      pr_suplusb:
                      pr_prod:
                      pr_forcint:
                      pr_fstslyr:
                      pr_fstslpr);

       //  create a new product history record, if no previous history exists
       //    or if first sales year is not this current year, then go see if
       //    a new history record for this year is needed
       if pr_fstslyr = 0 or
          pr_fstslyr <> pr_forcyr;

          exsr $_add_hist;
       endif;

       //       put entry into log file for addition of new product
       lg_logtype = '1';
       lg_prvsupl = *blanks;
       lg_prvsub  = *blanks;
       lg_prvname = *blanks;
       exsr $_log_prod;

       //       maximum forward buy days
       pr_maxdays = sp_maxdays;

       //       always assume new products can be purchased from diverter,
       //       regardless of what the APP record 'K3S_9010  BLOCK_ALTS' says,
       //       since buyer can then change setting in K3S_3000 '1 of 5'
       pr_procalt = 1;

       //    Assignment of Corporate Profiles
       if corp_prof = 1;
          pr_seasonl = CorpProfID;
          pr_seassrc = 'S';
          pr_seasact = lc_sysdate;
       endif;

       endsr;

       ////////////////////////////////////////////////////////// End period

       //  end of period

       begsr $_end_perd;

       // save off 'before picture' for PE snapshot capture
       if pe_snpshot = 1;
          pf_comp    = pr_comp;
          pf_locn    = pr_locn;
          pf_supl    = pr_supl;
          pf_suplsub = pr_suplsub;
          pf_prod    = pr_prod;

          prodfora_key.pf_comp = pr_comp;
          prodfora_key.pf_locn = pr_locn;
          prodfora_key.pf_supl = pr_supl;
          prodfora_key.pf_suplsub = pr_suplsub;
          prodfora_key.pf_prod = pr_prod;

          if first_shot = 0;
             first_shot = 1;

             callp K3S_Retrieve_Timestamp(time_stamp);

             pf_birth =  %date(%subst(%char(time_stamp):1:10):*ISO);
             prodfora_key.pf_birth = %date(%subst(%char(time_stamp):1:10):*ISO);

             pf_birthtm = %time(%subst(%char(time_stamp):12:8):*iso);
             prodfora_key.pf_birthtm = %time(%subst(%char(time_stamp):12:8):
                                       *iso);

             pf_chgtype = 'G';
             pf_chgdesc = 'Period End snapshots';
             pf_user    = 'K3S Night';
             pf_workstn = 'Batch job';
             pf_program = 'K3S_9010  ';
          endif;
          pf_seasbef = pr_seasonl;
          pf_seasaft = pr_seasonl;
          pf_avgbef  = pr_forcast;
          pf_devpbef = pr_fordevp;
          pf_statbef = pr_usrstat;
          pf_stataft = pr_usrstat;
       endif;

       //------------------------------------ retrieve seasonal profile factor
       //  retrieve seasoal profile factor for one period only
       //    (default value to 1.00 if not seasonal)

       if pr_seasonl <> *blanks;

       // call module to retrieve the seasonal profile factor for one period
          callp K3S_M051(pr_comp:
                         pr_seasonl:
                         pr_forcper:
                         seas_factr);

       //    default value to 1.00 if not seasonal
       else;
          seas_factr = 1.00;

       endif;

       //--------------------------------------- days out logic for lost sales
       //  calculate lost sales based upon days out of stock
       //    (product uses either accumulated PTD outs, or days out, but
       //     not both!)

       //  is days out logic being used?
       if lc_daysusd = 1;

          pr_accouts = 0;

          select;

       //       monthly forecasting
             when pr_forcint = 12;
                  days_perd  = lc_daysp12;

       //       thirteen four-weekly forecasting
             when pr_forcint = 13;
                  days_perd  = lc_daysp13;

       //       weekly forecasting
             when pr_forcint = 52;
                  days_perd  = lc_daysp52;

          endsl;

       //   days out can't be greater than days in period
          if pr_daysout > days_perd;
             pr_daysout = days_perd;
          endif;

       //   calculate lost percent
          if days_perd > 0;
             eval(h)   lost_perct = pr_daysout / days_perd;
          endif;

       //   calculate lost sales
          if pr_daysunt <> 999;
             eval(h)   pr_accouts = pr_forcast * lost_perct *
                                    seas_factr;
          endif;

       //   re-calculate accumulated demand
          pr_accdem  = pr_accouts + pr_accsale;

       endif;

       //------------------------------------------------- save demand history
       //  save accumulated demand into product history file, and determine
       //       if this is the first sale ever for this product
       if pr_accdem > 0;
          clear histype;

       // call program to save accumulated demand into product history file
          if pr_forcint = 12 OR pr_forcint = 13;

       //      monthly or 13 four-weekly products
             callp K3S_3500(pr_comp:
                            pr_locn:
                            pr_supl:
                            pr_suplsub:
                            pr_suplusr:
                            pr_suplusb:
                            pr_prod:
                            pr_forcyr:
                            pr_forcint:
                            histype:
                            pr_forcper:
                            pr_accdem:
                            lc_sysdate);

          else;

       //     weekly products
             callp K3S_3501(pr_comp:
                            pr_locn:
                            pr_supl:
                            pr_suplsub:
                            pr_suplusr:
                            pr_suplusb:
                            pr_prod:
                            pr_forcyr:
                            pr_forcint:
                            histype:
                            pr_forcper:
                            pr_accdem:
                            lc_sysdate);

          endif;

          if pr_fstslyr = 0;
             pr_fstslyr = pr_forcyr;
             pr_fstslpr = pr_forcper;
          endif;

       endif;

       //---------------------------- save previous period forecast components
       //  save previous period forecast components

       //  ensure no negative values get saved for Previous fields
       if pr_accsale < 0 OR
          pr_accouts < 0 OR
          pr_accdem  < 0;

          pr_accsale = 0;
          pr_accouts = 0;
          pr_accdem  = 0;
       endif;

       pr_prvdemd = pr_accdem;
       pr_prvfore = pr_forcast;
       pr_prvdevp = pr_fordevp;
       pr_prvserr = pr_forserr;
       // pr_prvts   = pr_prvserr /
       //              (pr_prvdevp * .01);
       pr_prvlost = pr_accouts * pr_sales;
       pr_prvsale = pr_accsale * pr_sales;
       pr_prvexpt = pr_prvfore * pr_sales *
                    seas_factr;

       //----------------------------------------------------- update forecast
       //  update forcast components

       clear error_type;

       //  check if forecast has been frozen until today?
       if lc_sysdate >= pr_forfrez;

       // any products that had been frozen are cleared
          if pr_usrstat = 'F';
             clear pr_usrstat;
             clear pr_forfrez;
          endif;

       // convert values to be passed from 3.1 to 3.3 fields
          fordevp = pr_fordevp * .01;
          nodevp  = lc_nodevp  * .01;

          accdem  = pr_accdem;
          forcast = pr_forcast;
          forserr = pr_forserr;

       //   don't allow demand to be negative when passed to K3S_M080
          if accdem  < 0;
             accdem  = 0;
          endif;

       //  By-pass forecast routine when Minimum Seasonal Factor logic
       //     being used, and this period is low
          if (min_used = 1 AND
             seas_factr >= min_season) OR
             min_used = 0;

       // call module to update forcast components
             callp K3S_M080(seas_factr:
                            accdem:
                            forcast:
                            fordevp:
                            forserr:
                            pr_longtrm:
                            lc_demhi:
                            demlo:
                            lc_smfactr:
                            lc_tslimit:
                            nodevp:
                            error_type:
                            lc_avgzero);
          endif;

       //         calculate absolute value of smoothed error to be used below
       //         for tests
          if forserr < 0;
             forserr_AV = forserr * -1;
          else;
             forserr_AV = forserr;
          endif;

       // If forecast is negative, or deviation is negative, or
       //    absolute value of smoothed error is greater than deviation %,
       //    then don't update product values, but log problem.
       //      change on 1/25/99 now self cleanses T/S problem

          if forcast < 0 or
             fordevp < 0 or
             forserr_AV >= fordevp;

       // If forecast going negative, log problem
             if forcast < 0;
                lg_logtype = 'A';
                lg_prvsupl = *blanks;
                lg_prvsub  = *blanks;
                lg_prvsplu = *blanks;
                lg_prvname = *blanks;
                exsr $_log_prod;
             endif;

       // If deviation going negative, log problem
             if fordevp < 0;
                lg_logtype = 'B';
                lg_prvsupl = *blanks;
                lg_prvsub  = *blanks;
                lg_prvsplu = *blanks;
                lg_prvname = *blanks;
                exsr $_log_prod;
             endif;

       //  If absolute value of smoothed error is greater than devaition %
             if forserr_AV >= fordevp;
                lg_logtype = 'C';
                lg_prvsupl = *blanks;
                lg_prvsub  = *blanks;
                lg_prvsplu = *blanks;
                lg_prvname = *blanks;
       //       exsr $_log_prod;
                pr_forserr = 0;
             endif;

          else;

       //  update product values
             pr_forcast = forcast;
             pr_fordevp = fordevp * 100;
             pr_forserr = forserr;
          endif;

       //  check if forecast has been frozen
       endif;

       //------------------------------- save previous period service acheived
       //  save previous period service level acheived

       if pr_accdem > 0 AND pr_accdem >= pr_accsale;
          pr_svceprv = (pr_accsale/pr_accdem) * 100;
       else;
          clear pr_svceprv;
       endif;

       //  If there was no demand in previous period then make previous service
       //  level 100%
       if pr_accdem = 0;
          pr_svceprv = 100;
       endif;

       //---------------------------------------------- update period and year
       //  period has changed, so save correct current period and year
       //         also, total up the number of products that have rolled
       //         by periodicity

       select;

       //      weekly forecasting
          when pr_forcint = 52;

       //          if this is year end, then create a new history record
               if pr_forcyr <> lc_year52;
                  pr_forcyr  = lc_year52;
                  exsr $_add_hist;
                  ye_for_52  = '1';
               endif;

               pr_forcyr  = lc_year52;
               pr_forcper = lc_perd52;
               rolled_52 += 1;

       //       monthly forecasting
          when pr_forcint = 12;

       //          if this is year end, then create a new history record
               if pr_forcyr <> lc_year12;
                  pr_forcyr  = lc_year12;
                  exsr $_add_hist;
                  ye_for_12  = '1';
               endif;

               pr_forcyr  = lc_year12;
               pr_forcper = lc_perd12;
               rolled_12 += 1;

       //       thirteen four-weekly forecasting
          when pr_forcint = 13;

       //          if this is year end, then create a new history record
               if pr_forcyr <> lc_year13;
                  pr_forcyr  = lc_year13;
                  exsr $_add_hist;
                  ye_for_13  = '1';
               endif;

               pr_forcyr  = lc_year13;
               pr_forcper = lc_perd13;
               rolled_13 += 1;

       endsl;

       //------------------------------------------------ update system status
      /copy k3s_c160

       //-------------------------------------------------- end of period code
       //  end of period code

       //     clear end of period code
       pr_endper = *blanks;

       //     only regular, lumpy, or slow products into 1st five categories
       //       1=DF high, 2=DF low, 3=TS high, 4=TS low, 5=Service
       //       then discontinued or new products are tested
       //          6=New, 7=Discontinued

       if (pr_sysstat = 'R') or
          (pr_sysstat = 'L') or
          (pr_sysstat = 'S');

          select;

       //     demand filter high
             when error_type = '1';
                  pr_endper  = '1';

       //     demand filter low
             when error_type = '2';
                  pr_endper  = '2';

       //     tracking signal high trending up
             when error_type = '3';
                  pr_endper  = '3';

       //     tracking signal low  trending down
             when error_type = '4';
                  pr_endper  = '4';

       //     service level check
             other;

                  if pr_accdem > 0 AND
                     pr_svceprv < pr_service;

                     pr_endper  = '5';
                  endif;

          endsl;

       //     if Exclude Buying Until in effect and more than 90 days out,
       //        and this product had fallen into PE1 through PE5,
       //        then buyer does not need to see this as PE check for now
          if pr_excuntl > Ninety_Out and
             pr_endper <> *blanks;

             clear pr_endper;
          endif;

       else;
       //   test for new and discontinued products
       //   new products
          if pr_sysstat = 'N';
             pr_endper  = '7';
          endif;

       //     discontinued products
          if pr_sysstat = 'D';
             pr_endper  = '9';
          endif;

       endif;

       //     un-conditionally make watch products category 6
       if pr_usrstat = 'W';
          pr_endper  = '6';
       endif;

       //     un-conditionally make manual products category 8
       if pr_usrstat = 'M';
          pr_endper  = '8';
       endif;

       //     save end of period code
       pr_endpers = pr_endper;

       //     Filter PE1 checks?
       if PE1_FLTR_1 =  1  and
          pr_endper  = '1' and
          pr_maminiu >  0  and
          pr_prvdemd <= pr_maminiu;

          pr_endper = *blanks;
       endif;

       //     save transfers period-to-date into last period transfers
       pr_tranlst = pr_tranptd;
       clear pr_tranptd;

       //     save previous period days out
       pr_daysprv = pr_daysout;

       //-------------------------------------------------- clear accumulators
       //  clear accumulators
       clear pr_accsale;
       clear pr_accouts;
       clear pr_accdem;
       clear pr_daysout;

       // save off 'after picture' for PE snapshot capture
       if pe_snpshot = 1;
          pf_sysstat = pr_sysstat;
          pf_devpaft = pr_fordevp;
          pf_avgaft  = pr_forcast;
          pf_avgdiff = pf_avgaft - pf_avgbef;
          chain %kds(prodfora_key) k_prodfora;
          if not %found(k_prodfora);
             write rk_prodfor;
          endif;
       endif;

       endsr;

       ///////////////////////////////////////////// Log Product Transactions

       //  Log of Product Transactions

       begsr $_log_prod;

       select;

          when lg_logtype = '1';
               lda_rctyp1 += 1;

          when lg_logtype = '2';
               lda_rctyp2 += 1;

          when lg_logtype = '5';
               lda_rctyp5 += 1;

          when lg_logtype = '6';
               lda_rctyp6 += 1;

          when lg_logtype = '7';
               lda_rctyp7 += 1;

          when lg_logtype = '8';
               lda_rctyp8 += 1;

          when lg_logtype = '9';
               lda_rctyp9 += 1;

          other;
               lda_rctypx += 1;

       endsl;

       lg_comp    = ip_comp;
       lg_locn    = ip_locn;
       lg_buyr    = sp_buyr;
       lg_supl    = ip_supl;
       lg_suplsub = ip_suplsub;
       lg_suplusr = ip_suplusr;
       lg_suplusb = ip_suplusb;
       lg_suplnam = sp_name;
       lg_prod    = ip_prod;
       lg_desc1   = ip_desc1;
       lg_deltcnt = pr_deltcnt;

       // call module to retrieve timestamp
       callp K3S_Retrieve_Timestamp(time_stamp);
       lg_timestp = time_stamp;

       // if customer has a method to get supplier name and buyer id for
       //    log type '5' records, then exist to customer's system to get
       //    data.
       if get_log_5 = '1' AND lg_logtype = '5';
          callp K3S_9010X1(ip_comp:
                           ip_locn:
                           ip_suplusr:
                           ip_suplusb:
                           ip_prod:
                           lg_buyr:
                           lg_suplnam);
                         endif;

       write rk_logprod;

       endsr;

       ///////////////////////////////////////////////// Add Product History

       //  Add product history record

       begsr $_add_hist;

       clear histype;

       // call program to create a new product history record
       if pr_forcint = 12 OR pr_forcint = 13;

       //     monthly and 13-four weekly products
          callp K3S_3505(pr_comp:
                         pr_locn:
                         pr_suplusr:
                         pr_suplusb:
                         pr_prod:
                         pr_forcyr:
                         pr_forcint:
                         histype:
                         lc_sysdate:
                         pr_supl:
                         pr_suplsub);

       else;

       //     weekly products
          callp K3S_3506(pr_comp:
                         pr_locn:
                         pr_suplusr:
                         pr_suplusb:
                         pr_prod:
                         pr_forcyr:
                         pr_forcint:
                         histype:
                         lc_sysdate:
                         pr_supl:
                         pr_suplsub);

       endif;

       endsr;

       ////////////////////////////////////////////////////// Trans supplier?

       begsr $_transfer;

       // test for supplier record

       chain (pr_comp:pr_locn:pr_suplusr:pr_suplusb) k_transpla;
       if %found(k_transpla);
          trans_prod = 1;
       endif;
       if not %found(k_transpla);

       // test for product record
          chain (pr_comp:pr_locn:pr_prod) k_tranprda;
          if %found(k_tranprda);
             trans_prod = 1;
          endif;

       endif;

       endsr;
       /////////////////////////////////////////////////////// write prodlog

       begsr $_prodlog;


       if pr_altsrce = 0 and
          pr_deltcnt = 0 and
          pr_tempory = 0;

          callp K3S_Retrieve_Timestamp(time_stam1);
          date = %date(%subst(%char(time_stam1):1:10):*ISO);
          time = %time(%subst(%char(time_stam1):12:8):*iso);

          p0_comp    = pr_comp;
          p0_locn    = pr_locn;
          p0_supl    = pr_supl;
          p0_suplsub = pr_suplsub;
          p0_prod    = pr_prod;
          p0_repcary = pr_repcary;
          p0_prombeg = pr_prombeg;
          p0_promend = pr_promend;
          p0_forfrez = pr_forfrez;
          p0_probdat = pr_probdat;
          p0_excuntl = pr_excuntl;
          p0_prodseq = pr_prodseq;
          p0_desc2   = pr_desc2;
          p0_ndc_upc = pr_ndc_upc;
          p0_group1o = pr_group1o;
          p0_group2o = pr_group2o;
          p0_group3o = pr_group3o;
          p0_group4o = pr_group4o;
          p0_group5o = pr_group5o;
          p0_mfg     = pr_mfg;
          p0_maminid = pr_maminid;
          p0_maminiu = pr_maminiu;
          p0_mamaxid = pr_mamaxid;
          p0_mamaxiu = pr_mamaxiu;
          p0_catalog = pr_catalog;
          p0_uom     = pr_uom;
          p0_packsiz = pr_packsiz;
          p0_tihi    = pr_tihi;
          p0_leadtm  = pr_leadtm;
          p0_leadtmv = pr_leadtmv;
          p0_whslocn = pr_whslocn;
          p0_linecst = pr_linecst;
          p0_ovrcreg = pr_ovrcreg;
          p0_ovrcdiv = pr_ovrcdiv;
          p0_promqty = pr_promqty;
          p0_minqtyo = pr_minqtyo;
          p0_buymulo = pr_buymulo;
          p0_convpko = pr_convpko;
          p0_convpkp = pr_convpkp;
          p0_daysunt = pr_daysunt;
          p0_maxdays = pr_maxdays;
          p0_add_day = pr_add_day;
          p0_weighto = pr_weighto;
          p0_volumeo = pr_volumeo;
          p0_weighdo = pr_weighdo;
          p0_volumdo = pr_volumdo;
          p0_purinco = pr_purinco;
          p0_disothr = pr_disothr;
          p0_service = pr_service;
          p0_spltprm = pr_spltprm;
          p0_poqtydv = pr_poqtydv;
          p0_poqtyum = pr_poqtyum;
          p0_procalt = pr_procalt;
          p0_exclead = pr_exclead;
          p0_formeth = pr_formeth;
          p0_invmeth = pr_invmeth;
          p0_rebate  = pr_rebate;
          p0_birth = date;
          p0_birthtm = time;
          p0_chgtype = 'A';
          evalr p0_user = 'K3S_NIGHT ';
          evalr p0_workstn = 'K3S_NIGHT ';
          evalr p0_program = 'K3S_9010  ';

          prodloga_key.p0_comp = pr_comp;
          prodloga_key.p0_locn = pr_locn;
          prodloga_key.p0_supl = pr_supl;
          prodloga_key.p0_suplsub = pr_suplsub;
          prodloga_key.p0_prod = pr_prod;
          prodloga_key.p0_birth = date;
          prodloga_key.p0_birthtm = time;
          chain %kds(prodloga_key) k_prodloga;
          if not %found(k_prodloga);
             write rk_prodlog;
          endif;

       endif;

       endsr;
      /end-free

