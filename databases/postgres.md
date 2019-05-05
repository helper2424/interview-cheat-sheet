0) What is postgresl?

postgresl - is a ORDBMS - object-relational database management system

1) What is postgresql functions?

Functions written in PL/psql, or other PL which could be run in PS request and work efficintly. 

2) Write an exmaple of function:

```
CREATE FUNCTION test(p1 integer, p2 integer) 
	RETURNS integer AS $$
BEGIN
		RETURN p1 + p2;
END; $$
LANGUAGE plpgsql;
```

example with python

```
CREATE FUNCTION test_python(p1 integer, p2 integer)
	RETURNS integer AS $$
	p1 ** p2
	$$
LANGUAGE plpythonu;
```

3) Main features
- object relational db
- custom languange
- wal
- mvcc

4) What is 'select ||/ 27'
the result is 3 , cubic root

5) What is mvcc?

Multiversion concurrency control. The technique which allows users of database accessing to records for reading and writing concurrently wothout locks. Realized through several versions of the same data. DBS saves several versions of records with additional flags (Xmin, Xmax, Cmin, CMax). When transactions are processing they work with their own versions of data. So, If we read and update (delete(mark as invalid) and insert) simulteniously, reader sees his version of data and updateer works with his version. Readers never block writers, writers never block readers.
http://momjian.us/main/writings/pgsql/mvcc.pdf - and amazine description

DBS adds several fields to every record version
xmin - transaction id which create record
xmax - transaction id which deleted (marked as invalid) the record

cmin, cmax - the same in context of one transaction.

6) What is ACID?
This is an abbreviation of
Atomicity

Consistency - a transaction swtich system state from one consistent state to another

Isolation - the result of parallel execution of transactions is equvivalent to sequential execution order

Durability - if transaction is commited, DBS gurantee that we don't lose this data

7) What isolation levels exist in postgres? (See this for details https://habr.com/ru/company/postgrespro/blog/442804/, an amazing article)

Read commited
repeatable read
serializable

8) What is a problem (main requirment) of serializable isolation level?
The system should be able to repeat tranaction failed because of serializable error. This error means that transaction can't be committed because of inconsistency. Usually it could be repeated later without any issues.

9) Could you tell about different kind phenomenas on different levels of isolation?

dirty read - when you read uncommitted data from another transaction
phantom read - read an object which was created by another transaction, on first read it didn't exist
nonrepearable read - reread data in transaction and find that it was changed by another
serialization anomanly - 

10) List of postgresql features:

Object-relational database
Support and Extensibility for SQL
flexible API and Database validation
MVCC and Procedural languages
WAL and Client server

extensions
user defined functions
user defined indexes
user defined rules
views 
inheritance

11) Administration tools for pgsql

psql
pgadmin
phppgadmin

12) What is ctid?

One of the system properties of a record. Shows physical location of row. Is being change when row updated/vacuumed ...

13) What is Vacuum Analyze?

It's a simple vacuum commmand (free space used for different versions of rows after transactions processing, deleted rows, etc.) and rebuild statistics for planner. In the next time planner will do quesries more efficient.

14) What is WAL?

Write-Ahead Log. The journal of actions which are writing before applying to db. It's required to restore db if something it's crashed from some point.

15) What is Cube Root Operator (||/) in PostgreSQL?

Cube root - select ||/ 16;

16) What is TOAST?

TOAST (The Oversized-Attribute Storage Technique) is used to transparently store large table attributes (such as big MIME attachments or XML messages) in a separate area, with automatic compression. It creates an additional table where put sliced data or compress it

17) When were released 10 and 11 versions?:

2017, 2018

18) What is command enable-debug?

The command enable-debug is used to enable the compilation of all the applications and libraries. The execution of this procedure usually impedes the system, but it also amplifies the binary file size. Debugging symbols which are present generally assist the developers in spotting the bugs and other problems which may arise associated with their script.

19) Explain About Tokens?

Tokens are also known to contain several special character symbols. It can be considered as keyword, constant, identifier and quoted identifier. Keywords include pre defined SQL meanings and SQL commands. Variable names such as tables, columns, etc are represented by identifiers.


20) Question 28. How Do I Tell What Postgresql Version I Am Running?

Run this query: SELECT version();

21) How Does Postgresql Compare To Mysql?

This is a topic that can start several hours of discussion. As a quick summary, MySQL is the “easy-to-use, web developer” database, and PostgreSQL is the “feature-rich, standards-compliant” database. PostgreSQL is liberally licensed and owned by its community; MySQL is GPL-licensed and owned by Oracle. Beyond that, each database user should make his own evaluation; open source software makes doing comparisons very easy.

22) What standarts does support postgres?

 SQL-92, SQL-98, SQL-2003 and SQL-2011 is coming

23) An amaizing article from Uber about the main issues in Postgres and switching from Mysql -> Postgres -> Mysql