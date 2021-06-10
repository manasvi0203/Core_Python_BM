MySQL Shell 8.0.25

Copyright (c) 2016, 2021, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
Other names may be trademarks of their respective owners.

Type '\help' or '\?' for help; '\quit' to exit.
MySQL  JS> ]sqk
SyntaxError: Unexpected token ']'
MySQL  JS> ]sql
SyntaxError: Unexpected token ']'
MySQL  JS> \sql
Switching to SQL mode... Commands end with ;
MySQL  SQL> \connect root@localhost;
Creating a session to 'root@localhost;'
Please provide the password for 'root@localhost;': *********
MySQL Error 2005: No such host is known 'localhost;'
MySQL  SQL> \connect root@localhost
Creating a session to 'root@localhost'
Fetching schema names for autocompletion... Press ^C to stop.
Your MySQL connection id is 17 (X protocol)
Server version: 8.0.25 MySQL Community Server - GPL
No default schema selected; type \use <schema> to set one.
MySQL  localhost:33060+ ssl  SQL > create database school;
ERROR: 1007: Can't create database 'school'; database exists
MySQL  localhost:33060+ ssl  SQL > use school;
Default schema set to `school`.
Fetching table and column names from `school` for auto-completion... Press ^C to stop.
MySQL  localhost:33060+ ssl  school  SQL > show tables;
+------------------+
| Tables_in_school |
+------------------+
| marks            |
| result           |
| student          |
| student_info     |
+------------------+
4 rows in set (0.0020 sec)
MySQL  localhost:33060+ ssl  school  SQL > describe marks;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| name  | varchar(10) | YES  |     | NULL    |       |
| marks | int         | YES  |     | NULL    |       |
| roll  | int         | NO   | PRI | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.0068 sec)
MySQL  localhost:33060+ ssl  school  SQL > describe result;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| roll  | int         | NO   | PRI | NULL    |       |
| name  | char(20)    | YES  | MUL | NULL    |       |
| res   | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.0023 sec)
MySQL  localhost:33060+ ssl  school  SQL > drop database school;
Query OK, 4 rows affected (0.1217 sec)
MySQL  localhost:33060+ ssl  school  SQL > use school;
MySQL Error 1049: Unknown database 'school'
MySQL  localhost:33060+ ssl  school  SQL > create database school;
Query OK, 1 row affected (0.0130 sec)
MySQL  localhost:33060+ ssl  school  SQL > use school;
Default schema set to `school`.
Fetching table and column names from `school` for auto-completion... Press ^C to stop.
MySQL  localhost:33060+ ssl  school  SQL > show tables;
Empty set (0.0023 sec)
MySQL  localhost:33060+ ssl  school  SQL > create table (roll int, name varchar(10), class int, adm char(4));
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(roll int, name varchar(10), class int, adm char(4))' at line 1
MySQL  localhost:33060+ ssl  school  SQL > create table (roll int, name varchar (10), class int, adm char(4));
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(roll int, name varchar (10), class int, admchar(4))' at line 1
MySQL  localhost:33060+ ssl  school  SQL > create table student (roll int, name varchar(10), class int, adm char(4));
Query OK, 0 rows affected (0.0553 sec)
MySQL  localhost:33060+ ssl  school  SQL > show tables;
+------------------+
| Tables_in_school |
+------------------+
| student          |
+------------------+
1 row in set (0.0108 sec)
MySQL  localhost:33060+ ssl  school  SQL > show students
                                         -> ;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'students' at line 1
MySQL  localhost:33060+ ssl  school  SQL > select * from student;
Empty set (0.0108 sec)
MySQL  localhost:33060+ ssl  school  SQL > describe student;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| roll  | int         | YES  |     | NULL    |       |
| name  | varchar(10) | YES  |     | NULL    |       |
| class | int         | YES  |     | NULL    |       |
| adm   | char(4)     | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
4 rows in set (0.0071 sec)
MySQL  localhost:33060+ ssl  school  SQL > insert into students values(1001, "Brain Mentors", 5, "1234");
ERROR: 1146: Table 'school.students' doesn't exist
MySQL  localhost:33060+ ssl  school  SQL > insert into student values(1001, "Brain Mentors", 5, "1234");
ERROR: 1406: Data too long for column 'name' at row 1
MySQL  localhost:33060+ ssl  school  SQL > insert into student values(1001, "Brain", 5, "1234");
Query OK, 1 row affected (0.0490 sec)
MySQL  localhost:33060+ ssl  school  SQL > insert into student(roll, adm, class, name) values(1001, "1245", 5, "Brain");
Query OK, 1 row affected (0.0106 sec)
MySQL  localhost:33060+ ssl  school  SQL > insert into student(roll, adm, class) values(1001, "1245", 5);
Query OK, 1 row affected (0.0106 sec)
MySQL  localhost:33060+ ssl  school  SQL > select * from student;
+------+-------+-------+------+
| roll | name  | class | adm  |
+------+-------+-------+------+
| 1001 | Brain |     5 | 1234 |
| 1001 | Brain |     5 | 1245 |
| 1001 | NULL  |     5 | 1245 |
+------+-------+-------+------+
3 rows in set (0.0008 sec)
MySQL  localhost:33060+ ssl  school  SQL > select roll from student;
+------+
| roll |
+------+
| 1001 |
| 1001 |
| 1001 |
+------+
3 rows in set (0.0007 sec)
MySQL  localhost:33060+ ssl  school  SQL > select roll,name from student;
+------+-------+
| roll | name  |
+------+-------+
| 1001 | Brain |
| 1001 | Brain |
| 1001 | NULL  |
+------+-------+
3 rows in set (0.0007 sec)
MySQL  localhost:33060+ ssl  school  SQL > select * from student where name=="Brain";
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '=="Brain"' at line 1
MySQL  localhost:33060+ ssl  school  SQL > select * from student where name="Brain";
+------+-------+-------+------+
| roll | name  | class | adm  |
+------+-------+-------+------+
| 1001 | Brain |     5 | 1234 |
| 1001 | Brain |     5 | 1245 |
+------+-------+-------+------+
2 rows in set (0.0010 sec)
MySQL  localhost:33060+ ssl  school  SQL > select * from student where class=5;
+------+-------+-------+------+
| roll | name  | class | adm  |
+------+-------+-------+------+
| 1001 | Brain |     5 | 1234 |
| 1001 | Brain |     5 | 1245 |
| 1001 | NULL  |     5 | 1245 |
+------+-------+-------+------+
3 rows in set (0.0007 sec)
MySQL  localhost:33060+ ssl  school  SQL > insert into student values(1002, "Mentors", NULL, "R234");
Query OK, 1 row affected (0.0097 sec)
MySQL  localhost:33060+ ssl  school  SQL > select * from student;
+------+---------+-------+------+
| roll | name    | class | adm  |
+------+---------+-------+------+
| 1001 | Brain   |     5 | 1234 |
| 1001 | Brain   |     5 | 1245 |
| 1001 | NULL    |     5 | 1245 |
| 1002 | Mentors |  NULL | R234 |
+------+---------+-------+------+
4 rows in set (0.0057 sec)
MySQL  localhost:33060+ ssl  school  SQL > insert into student values(1002, "Mentors", "R234");
ERROR: 1136: Column count doesn't match value count at row 1
MySQL  localhost:33060+ ssl  school  SQL > insert into student (roll, name, class, adm) values (1004,"Gautam", 10, "kjhg"), (1005, "Ram", 12, "jhgjk);
                                         "> ;
                                         "> ";
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 3
 MySQL  localhost:33060+ ssl  school  SQL > insert into student (roll, name, class, adm) values (1004,"Gautam", 10, "kjhg"), (1005, "Ram", 12, "jinsert into student (roll, name, class, adm) values (1004,"Gautam", 10, "kjhg"), (1005, "Ram", 12, "jinsert into student (roll, name, class, adm) values (1004,"Gautam", 10, "kjhg"), (1005, "Ram", 12, "jinsert into student (roll, name, class, adm) values (1004,"Gautam", 10, "kjhg"), (1005, "Ram", 12, "jinsert into student (roll, name, class, adm) values (1004,"Gautam", 10, "kjhg"), (1005, "Ram", 12, "jinsert into student (roll, name, class, adm) values (1004,"Gautam", 10, "kjhg"), (1005, "Ram", 12, "jhgjk); ; ";
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
MySQL  localhost:33060+ ssl  school  SQL > insert into student (roll, name, class, adm) values (1004,"Gautam", 10, "kjhg"), (1005, "Ram", 12, "jhgjk");
ERROR: 1406: Data too long for column 'adm' at row 2
MySQL  localhost:33060+ ssl  school  SQL > insert into student (roll, name, class, adm) values (1004,"Gautam", 10, "kjhg"), (1005, "Ram", 12, "jhgj");
Query OK, 2 rows affected (0.0130 sec)

Records: 2  Duplicates: 0  Warnings: 0
MySQL  localhost:33060+ ssl  school  SQL > select * from students;
ERROR: 1146: Table 'school.students' doesn't exist
MySQL  localhost:33060+ ssl  school  SQL > select * from student;
+------+---------+-------+------+
| roll | name    | class | adm  |
+------+---------+-------+------+
| 1001 | Brain   |     5 | 1234 |
| 1001 | Brain   |     5 | 1245 |
| 1001 | NULL    |     5 | 1245 |
| 1002 | Mentors |  NULL | R234 |
| 1004 | Gautam  |    10 | kjhg |
| 1005 | Ram     |    12 | jhgj |
+------+---------+-------+------+
6 rows in set (0.0008 sec)
MySQL  localhost:33060+ ssl  school  SQL >
