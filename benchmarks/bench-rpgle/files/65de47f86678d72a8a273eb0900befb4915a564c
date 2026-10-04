<%@ language="RPGLE" %>
<%
D startRow        C                   1
D maxRows         C                   9999
D SqlCmd          S           8192    varying

/free

SetContentType('application/json; charset=utf-8');

sqlCmd = ('                                  +
  SELECT book_id, book_title,                +
    author_last, author_first, author_middle +
    FROM books                               +
    JOIN book_authors USING(book_id)         +
    JOIN authors USING(author_id)            +
    FOR READ ONLY                            +
');

SQL_Execute(
	I_EXTJSMETA:
		sqlcmd:
		maxRows:
		startRow
);

*INLR = *ON;
return;
%>