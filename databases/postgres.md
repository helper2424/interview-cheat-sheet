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


