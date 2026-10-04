      *****************************************************************
     h copyright('(C) Copyright 1996 - 2008 King III Solutions, Inc.  +
     h Rel 5.00 2008-01-01       Program Property of King III Solutions, Inc. +
     h All rights reserved              +
     h K3S_Replenish (R) is a Registered Trade Mark of King III Solutions Inc.')

      *****************************************************************
      **
      **   K3S-Replenish (R) - Inventory REPLENISHment System
      **   Copyright (C) 1996-2008 by King III Solutions, Inc.
      **   Program property of King III Solutions, Inc.
      **   All rights reserved.
      **   K3S_Replenish (R) is a Registered Trade Mark of
      **   King III Solutions Inc.
      **
      *****************************************************************
      **
      **   Name: K3S_M120
      **   Type: ILE RPG Program
      **   Desc: Retrieve user specified date and time from timestamp
      **
      *****************************************************************
      **  Maintenance Log.
      **  Programmer. David Meyer.
      **  Date. 05/23/2014.
      **  Remarks. Converted this code from a stand-alone program to
      **           an exportable free-format RPGLE subprocedure. Added
      **           this subprocedure to service program DATEPROCS.
      **           Also, reduced the amount of code needed to get the
      **           date and time by utilizing RPG IV built-in
      **           functions such as %hours, %time, and %date.
      *****************************************************************
     h NOMAIN
     h OPTION(*NODEBUGIO)
      * --------------------------------------------- Parameters passed
      /copy qprotosrc
      *****************************************************************
     p K3S_M120        B                   EXPORT
      *procedure interface
     d                 PI
     d  date_fmt                      4    Const
     d  time_fmt                      4    Const
     d  time_adj                      3  0 Const
     d  date_char                    10
     d  time_char                     8
      * --------------------------------------------------- Timestamp fields
     d time_stamp      s               z   inz
     d time            s               t   timfmt(*iso)
     d time_work       s              8    inz(*blanks)
     d date            s               d   datfmt(*iso)
     d date_work       s             10    inz(*blanks)

     d not_six         s              1p 0 inz(0)
      * ----------------------------------------------- Format date and time
      /free
       //call subprocedure to retrieve timestamp
       callp K3S_M090(time_stamp);
       //user preferred time adjustment
       time_stamp += %hours(time_adj);
       //time = %time(%char(time_stamp):*iso);
       time = %time(%subst(%char(time_stamp):12:8):*iso);
       date = %date(%subst(%char(time_stamp):1:10):*ISO);

       //call subprocedure to convert *iso date to user specified format
       callp K3S_M100(date:date_fmt:not_six:date_work);
       date_char = %triml(date_work);

       //call subprocedure to convert *iso time to user specified format
       callp K3S_M110(time:time_fmt:time_work);

       time_char = %triml(time_work);

       return;
      /end-free
     p K3S_M120        e
