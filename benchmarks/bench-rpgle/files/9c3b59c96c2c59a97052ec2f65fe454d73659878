      *  This code uses service program JDBCR4 referenced in binding directory JDBC
      *
      *  To Compile:
      *     CRTBNDRPG JDBCTEST3 DBGVIEW(*LIST)
      *
     H DFTACTGRP(*NO) BNDDIR('JDBC')

     FQSYSPRT   O    F  132        PRINTER

      /copy qrpglesrc,jdbc_h

     D JDBCTEST3       PR                  extpgm('JDBCTEST3')
     D    driver                    128A   const
     D    url                       128A   const
     D    database                   30A   const
     D    userid                     15A   const
     D    passwrd                    15A   const
     D    sql                       256A   const
     D JDBCTEST3       PI
     D    driver                    128A   const
      *               SQL Server 2005 example 'com.microsoft.sqlserver.jdbc.SQLServerDriver'
      *               SQL Server 2000 example 'com.microsoft.jdbc.sqlserver.SQLServerDriver'
      *               AS400 example 'com.ibm.as400.access.AS400JDBCDriver'
     D    url                       128A   const
      *               SQL Server 2005 example 'jdbc:sqlserver://hostname:1433'
      *               SQL Server 2000 example 'jdbc:microsoft:sqlserver://hostname:1433;DatabaseName
      *               AS400 example 'jdbc:as400://S102LKZM:446/S102LKZM'
     D    database                   30A   const
      *               SQL Server 2005 example 'fcdorderentry'
     D    userid                     15A   const
     D    passwrd                    15A   const
     D    sql                       256A   const
      *               SQL Server 2000 example 'select ssn_ein_id, last_name, first_name, birth_date'
      *                                       'from dbo.person'
      *               AS400 example 'select * from library.file'

     D conn            s                   like(Connection)
     D ErrMsg          s             50A
     D wait            s              1A
     D idx             s             10I 0
     D colcnt          s             10I 0
     D rs              s                   like(ResultSet)
     D rsmd            s                   like(ResultSetMetaData)
     D Row1            s            132A
     D prop            s                   like(Properties)


      /free
         *inlr = *on;

         prop = JDBC_Properties();
         JDBC_setProp(prop: 'User'    : %trim(userid));
         JDBC_setProp(prop: 'Password': %trim(passwrd));
         JDBC_setProp(prop: 'DatabaseName': %trim(database));
         // JDBC_setProp(prop: 'prompt'  : 'false');
         // JDBC_setProp(prop: 'errors'  : 'full');
         // 'sql' naming looks like library.table
         // 'system' naming looks like library/table
         // JDBC_setProp(prop: 'naming'  : 'sql');

         // conn = JDBC_Connect( %trim(driver)
         //                    : %trim(url)
         //                    : %trim(userid)
         //                    : %trim(passwrd));

         conn = JDBC_ConnProp( %trim(driver)
                             : %trim(url)
                             : prop );
         JDBC_freeProp(prop);

         if (conn = *NULL);
             return;
         endif;

         // Query the database

         rs = jdbc_ExecQry( conn
                          : %trim(sql)
                          );
         rsmd = jdbc_GetMetaData(rs);
         colcnt = jdbc_GetColCount(rsmd);

         // Get column names
         idx = 1;
         Row1 = jdbc_getColName(rsmd: idx)
              + ' '
              + jdbc_getColTypName(rsmd: idx)
              + '('
              + %trim(%editc(jdbc_getColDspSize(rsmd: idx):'Z'))
              + ')';
         dow (idx < colcnt);
             idx = idx + 1;
             Row1 = %trim(Row1)
                  + ', '
                  + jdbc_getColName(rsmd: idx)
                  + ' '
                  + jdbc_getColTypName(rsmd: idx)
                  + '('
                  + %trim(%editc(jdbc_getColDspSize(rsmd: idx):'Z'))
                  + ')';
         enddo;
         except;

         // Get rows from table
         dow (jdbc_nextRow(rs));
             idx = 1;
             Row1 = jdbc_getCol(rs: idx);
             dow (idx < colcnt);
                 idx = idx + 1;
                 Row1 = %trim(Row1)
                      + ', '
                      + jdbc_getCol(rs: idx);
             enddo;
             except;
         enddo;

         jdbc_freeResult(rs);

         jdbc_close(conn);
         return;
      /end-free

     OQSYSPRT   E
     O                       Row1               132
