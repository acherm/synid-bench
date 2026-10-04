     *** TIMESTMP - Module to produce an *ISO time-stamp and return it as a character string.
     *** Users of this module should prototype it as follows:
     *** D TIMESTMP        PR             26Z
     *** or, as well
     *** D TIMESTMP        PR             26A
     *** depending on the type of variable they want to load it on.
     *** It will return a time-stamp with microsecond precision.  Pay attention to the <precisionIndicator> field of the
     *** API call.  This function, will internally obtain first a time-stamp value with no separator characters at all.
     *** It will then build a standard *ISO time-stamp just as the %TIMESTAMP built-in function does, with the
     *** benefit of having full-microsecond precision.  %TIMESTAMP by default will return a millisecond precision, with 
     *** only three (left-most) significant digits padded with three (right-most) zeros.
     *** Compile this as module using the CRTRPGMOD command.  Then, if you want, may use it as a bound module or may
     *** create a service program.  The former is recommended as this code is very light and does not justify the cost of
     *** loading it as a service program.
     *** Copyright Javier Sanchez 2020.
     *** Licensed under GNU GPL 3.0.
     ***
     H NOMAIN
     ***
     D QWCCVTDT        PR                  EXTPGM('QWCCVTDT')
     D  inputFormat                  10A   CONST
     D  inputVariable             32767A   OPTIONS(*VARSIZE) CONST
     D  outputFormat                 10A   CONST
     D  outPutVariable...
     D                            32767A   OPTIONS(*VARSIZE)
     D  errorCode                 32767A   OPTIONS(*VARSIZE)
     D** Optional parameter group 1.
     D  inputTimeZone                10A   CONST
     D  outPutTimeZone...
     D                               10A   CONST
     D  timeZoneInfo                       LIKEDS(Qwc_Time_Zone_Info_t)
     D  timeZoneInfoLen...
     D                               10I 0 CONST
     D  precisionIndicator...
     D                                1A   CONST
     ***
     D ErrorCode       DS                  QUALIFIED
     D  bytes_provided...
     D                               10I 0
     D  bytes_available...
     D                               10I 0
     D  exception_id                  7A
     D  reserved1                     1A
     ***
     D Qwc_Time_Zone_Info_t...
     D                 DS                  QUALIFIED TEMPLATE
     D bytes_returned                10I 0
     D bytes_available...
     D                               10I 0
     D time_zone_name                10A
     D reserved01                     1A
     D current_dst_indicator...
     D                                1A
     D current_utc_offset...
     D                               10I 0
     D current_full_time_zone_name...
     D                               50A
     D current_abbr_time_zone_name...
     D                               10A
     D current_Time_Zone_Msg_ID...
     D                                7A
     D current_Time_Zone_Msg_File...
     D                               10A
     D current_Time_Zone_Msg_File_Lib...
     D                               10A
     D reserved02                     1A
     D yearOffset                    10I 0
     ***
     D dsts20          DS                  QUALIFIED INZ
     D  year                   1      4
     D  month                  5      6
     D  day                    7      8
     D  hour                   9     10
     D  minute                11     12
     D  second                13     14
     D  microsecond           15     20
     ***
     P TIMESTMP        B                   EXPORT
     D TIMESTMP        PI            26
     **
     D timeZoneInfo    DS                  LIKEDS(Qwc_Time_Zone_Info_t) INZ
     D retVal          S             26    INZ
     **
       CLEAR errorCode;
       errorCode.bytes_provided = %SIZE(errorCode);
       QWCCVTDT('*CURRENT  ':
                *BLANKS:
                '*YYMD     ':
                dsts20:
                errorCode:
                '*SYS      ':
                '*SYS      ':
                timeZoneInfo:
                %SIZE(timeZoneInfo):
                '1');
       retVal = dsts20.year + '-' +
                dsts20.month + '-' +
                dsts20.day  + '-' +
                dsts20.hour    + '.' +
                dsts20.minute  + '.' +
                dsts20.second  + '.' +
                dsts20.microsecond;
       RETURN retVal;
     P TIMESTMP        E
