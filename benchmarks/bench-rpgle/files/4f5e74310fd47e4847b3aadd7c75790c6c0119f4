**FREE
//_________________________________________________________________
// template:
// create table
//_______________________________________________

//Compiler Option
CTL-OPT Option(*NODEBUGIO:*srcstmt:*nounref) DFTACTGRP(*NO) BNDDIR('KAPSBNDDIR');

/define jrnTables
/define Tool
/include QRPGLESRC,PRPROTOTYP
/undefine Tool
/undefine jrnTables
/copy QRPGLESRC,DCCONST

DCL-S TableExists ind;

//_______________________________________
// *ENTRY
DCL-PI *N;
END-PI;

// SQL Optionen
exec sql set option commit = *NONE, CLOSQLCSR = *ENDMOD;

/////////////////////////////////////////////////////////////////////////
//  MAIN

// schema
Library = yta105_bib();
exec sql set schema = :Library;

Table = 'YMUST';

// enabling leave and iter
FOR x to 1;

EXEC SQL
SELECT '1' INTO :TableExists FROM QSYS2.SYSTableS
WHERE Table_SCHEMA = :Library AND Table_NAME = :Table;

//_________________________
IF not TableExists;

  sqlCmd =
  'create Table '+%TRIM(Table)+' +
  ( ID INTEGER NOT NULL generated always as IDENTITY (start with 1 increment by 1) +
  , NAME   CHAR(10) NOT NULL WITH DEFAULT +
  , PRIMARY KEY (ID) +
  )';
  EXEC SQL EXECUTE IMMEDIATE :SQLCMD;

  IF SQLCODE < 0;
  snd_sqlMSG_User(SQLCODE);
  LEAVE;
  ENDIF;

  sqlCmd =
  'LABEL ON Table '+%TRIM(Table)+' +
   is ''Table template''';
  EXEC SQL EXECUTE IMMEDIATE :SQLCMD;

  Column_Label();

  // Journal create
  jrnTabs('KAPSJRN': 'KAPSRCV': Library: Table);
ENDIF;

IF Alter_Table_Patch01(Table:Library) = error;
LEAVE;
ENDIF;

ENDFOR;

*INLR = true;
return;
//
/////////////////////////////////////////////////////////////////////////

DCL-PROC Column_Label;
  sqlCmd =
  'LABEL ON COLUMN '+%TRIM(Table)+' +
  ( ID   TEXT IS ''ID''   +
  , NAME TEXT IS ''Name'' +
  )';
  EXEC SQL EXECUTE IMMEDIATE :SQLCMD;
END-PROC;

/////////////////////////////////////////////////////////////////////////
// add columns to table
// 1. check if the column was already added to the table
// 2. add the column
// 3. Error handling => Send Msg to User
DCL-PROC Alter_Table_Patch01;
DCL-S ColumnExists ind;
DCL-S ColumnLastAdded CHAR(10);

DCL-PI *N IND;
  iTable           like(Table);
  iLibrary         like(Library);
END-PI;

ColumnLastAdded = 'DESC';
exec sql
select '1'
  into :ColumnExists
  from qsys2.syscolumns
 where Table_Name   = :Table
   and Table_schema = :Library
   and Column_name  = :ColumnLastAdded
;

IF NOT ColumnExists;
sqlCmd =
'+
ALTER TABLE '+%TRIM(Table)+' +
ADD COLUMN ARTIKLE CHAR(10) +
ADD COLUMN STATUS CHAR(1) +
ADD COLUMN '+%TRIM(ColumnLastAdded)+' CHAR(80) +
';
EXEC SQL EXECUTE IMMEDIATE :SQLCMD;
ENDIF;

IF SQLCODE <> 0;
snd_sqlMSG_User(SQLCODE);
return error;
ENDIF;

return valid;
END-PROC;
