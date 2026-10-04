      /if defined(QSYUSRIN_H)
      /eof
      /endif
      /define QSYUSRIN_H

     D QSYRUSRI        pr                  extpgm('QSYRUSRI')
     D  RecVar                    65535a   options(*varsize)
     D  RecVarLen                    10i 0 const
     D  Format                        8a   const
     D  User                         10a   const
     D  Qusec                              likeds(QUsec_t)

     D CHGP0100_t      ds                  based(template) qualified
     D  ExitPointName                20a
     D  ExitPointFmt                  8a
     D  UserProfile                  10a

     D USRI0200_t      ds                  based(template) qualified
     D  BytesRet                     10i 0
     D  BytesAva                     10i 0
     D  UserProfile                  10a
     D  UserClass                    10a
     D  SpcAuth                      15a
     D  GrpName                      10a
     D  Owner                        10a
     D  GrpAuth                      10a
     D  LmtCap                       10a

     D Qsy_RUAI0100_t  ds                  qualified template
     D  EntLen                       10i 0
     D  AppInfoId                   200a
     D  AppInfoDisp                  10i 0
     D  AppInfoLen                   10i 0
     D  AppInfoCCSID                 10i 0
     D  MinRls                        6a
     D  AppInfo                    1700a

     D Qsy_RUAI_Feedback_Info_t...
     D                 ds                  qualified template
     D  BytesRtn                     10i 0
     D  BytesAvail                   10i 0
     D  Count                        10i 0

     D QsyUpdateUserApplicationInfo...
     D                 pr                  extproc('QsyUpdate+
     D                                     UserApplicationInfo')
     D  UsrPrf                       10a   const
     D  AppInfoId                   200a   const options(*varsize)
     D  AppInfoIdLen                 10i 0 const
     D  AppInfo                    1700a   const options(*varsize)
     D  AppInfoLen                   10i 0 const
     D  MinRls                        6a   const
     D  ErrorCode                 32767a   options(*varsize)

     D QsyRemoveUserApplicationInfo...
     D                 pr                  extproc('QsyRemove+
     D                                     UserApplicationInfo')
     D  UsrPrf                       10a   const
     D  AppInfoId                   200a   const options(*varsize)
     D  AppInfoIdLen                 10i 0 const
     D  ErrorCode                 32767a   options(*varsize)

     D QsyRetrieveUserApplicationInfo...
     D                 pr                  extproc('QsyRetrieve+
     D                                     UserApplicationInfo')
     D  RcvVar                    65535a   options(*varsize)
     D  RcvVarLen                    10i 0 const
     D  FeedBack                           likeds(Qsy_RUAI_FeedBack_Info_t)
     D  Format                        8a   const
     D  UsrPrf                       10a   const
     D  AppInfoId                   200a   const options(*varsize)
     D  AppInfoIdLen                 10i 0 const
     D  ErrorCode                 32767a   options(*varsize)

