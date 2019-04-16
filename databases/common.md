1) Does Postgresql support unsigned ints, show example.

CREATE DOMAIN uint2 AS int4
   CHECK(VALUE >= 0 AND VALUE < 65536);

1)What is the difference between the WHERE and HAVING clauses?

Where caluse check condition for every row (or part if we use indexes). Having clauses used for aggregated records.

2) What is the difference between the RANK() and DENSE_RANK() functions? Provide an example.

The only difference between the RANK() and DENSE_RANK() functions is in cases where there is a “tie”; i.e., in cases where multiple values in a set have the same ranking. In such cases, RANK() will assign non-consecutive “ranks” to the values in the set (resulting in gaps between the integer ranking values when there is a tie), whereas DENSE_RANK() will assign consecutive ranks to the values in the set (so there will be no gaps between the integer ranking values in the case of a tie).

Dense rank not skip values

3) What are the NVL and the NVL2 functions in SQL? How do they differ?

Both the NVL(exp1, exp2) and NVL2(exp1, exp2, exp3) functions check the value exp1 to see if it is null.

With the NVL(exp1, exp2) function, if exp1 is not null, then the value of exp1 is returned; otherwise, the value of exp2 is returned, but case to the same data type as that of exp1.

With the NVL2(exp1, exp2, exp3) function, if exp1 is not null, then exp2 is returned; otherwise, the value of exp3 is returned.

4) How can you select all the even number records from a table? All the odd number records?

select id from users where id % 2 = 0;
select id from users where id % 2 != 0;

without id  !!

select sub_query.id, sub_query.new_id from (select *, row_number() over (order by (select 1)) as new_id from users) as sub_query where new_id % 2  = 0;

5) Given a table dbo.users where the column user_id is a unique identifier, how can you efficiently select the first 100 odd user_id values from the table?

(Assume the table contains well over 100 records with odd user_id values.)

6) What is a key difference between Truncate and Delete?

TRUNCATE quickly removes all rows from a set of tables. It has the same effect as an unqualified DELETE on each table, but since it does not actually scan the tables it is faster. Furthermore, it reclaims disk space immediately, rather than requiring a subsequent VACUUM operation. This is most useful on large tables.

7) List and explain each of the ACID properties that collectively guarantee that database transactions are processed reliably.

ACID (Atomicity, Consistency, Isolation, Durability) is a set of properties that guarantee that database transactions are processed reliably. They are defined as follows:

Atomicity. Atomicity requires that each transaction be “all or nothing”: if one part of the transaction fails, the entire transaction fails, and the database state is left unchanged. An atomic system must guarantee atomicity in each and every situation, including power failures, errors, and crashes.
Consistency. The consistency property ensures that any transaction will bring the database from one valid state to another. Any data written to the database must be valid according to all defined rules, including constraints, cascades, triggers, and any combination thereof.
Isolation. The isolation property ensures that the concurrent execution of transactions results in a system state that would be obtained if transactions were executed serially, i.e., one after the other. Providing isolation is the main goal of concurrency control. Depending on concurrency control method (i.e. if it uses strict - as opposed to relaxed - serializability), the effects of an incomplete transaction might not even be visible to another transaction.
Durability. Durability means that once a transaction has been committed, it will remain so, even in the event of power loss, crashes, or errors. In a relational database, for instance, once a group of SQL statements execute, the results need to be stored permanently (even if the database crashes immediately thereafter). To defend against power loss, transactions (or their effects) must be recorded in a non-volatile memory.

8) What is an execution plan? When would you use it? How would you view the execution plan?
 This probably came from a query that's hard to optimize:

SELECT * FROM mytable WHERE a=X OR b=Y
This query is hard to optimize with simple B-tree indexing. Does the engine search an index on column a? Or on column b? Either way, searching the other term requires a table-scan.

Hence the trick of using UNION to separate into two queries for one term each. Each subquery can use the best index for each search term. Then combine the results using UNION.

But the two subsets may overlap, because some rows where b=Y may also have a=X in which case such rows occur in both subsets. Therefore you have to do duplicate elimination, or else see some rows twice in the final result.

SELECT * FROM mytable WHERE a=X 
UNION DISTINCT
SELECT * FROM mytable WHERE b=Y
UNION DISTINCT is expensive because typical implementations sort the rows to find duplicates. Just like if you use SELECT DISTINCT ....

We also have a perception that it's even more "wasted" work if the two subset of rows you are unioning have a lot of rows occurring in both subsets. It's a lot of rows to eliminate.

But there's no need to eliminate duplicates if you can guarantee that the two sets of rows are already distinct. That is, if you guarantee there is no overlap. If you can rely on that, then it would always be a no-op to eliminate duplicates, and therefore the query can skip that step, and therefore skip the costly sorting.

If you change the queries so that they are guaranteed to select non-overlapping subsets of rows, that's a win.

SELECT * FROM mytable WHERE a=X 
UNION ALL 
SELECT * FROM mytable WHERE b=Y AND a!=X
These two sets are guaranteed to have no overlap. If the first set has rows where a=X and the second set has rows where a!=X then there can be no row that is in both sets.

The second query therefore only catches some of the rows where b=Y, but any row where a=X AND b=Y is already included in the first set.

So the query achieves an optimized search for two OR terms, without producing duplicates, and requiring no UNION DISTINCT operation.

9)Write a SQL query to find the 10th highest employee salary from an Employee table. Explain your answer.

SELECT Salary FROM
(
    SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 10
) AS Emp ORDER BY Salary LIMIT 1;

9) Given a table TBL with a field Nmbr that has rows with the following values:

1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1

Write a query to add 2 where Nmbr is 0 and add 3 where Nmbr is 1.

UPDATE TBL SET Nmbr = (Nmbr - 1)  * -2 + Nmbr * 3 + Nmbr;

10) Write a query to fetch values in table test_a that are and not in test_b without using the NOT keyword.

Use except;

11) What is mysql strict mode?

Constraints to insert/update operations.

12) What is difference in the next queries:
select count(*) from users;
select count(name) from users;

id name
1	test
2 	test
3 	test3
4 	NULL

4
3

13) Write exampels of all joins:

select * from table1 inner join table2 on table1.id = table.id


14) pgBouncer - что такое?

Дело в том, что postgres для каждого соединения создает новый процесс. Чтобы «удешевить» соединение с БД, современные библиотеки используют пул соединений. То есть, они один раз соединяются с БД, а потом многократно используют это соединение. Если в библиотеке работы с БД нет возможности «пулить» соединения, то здесь приходит на помощь PgBouncer. Вместо того, чтобы каждый раз создавать дорогое соединение с postgres, создается легкое соединение с PgBouncer, который пользуется уже существующим соединением с БД.