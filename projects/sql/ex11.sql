insert into person (id, first_name, last_name, age)
    values (0, 'Frank', 'Smith', 100);

insert or replace into person (id, first_name,last_name, age)
    values (0, 'Frank', 'Smith', 100);

select * from person;

replace into person (id, first_name, last_name, age)
    values (0, 'Zed', 'Shaw', 37);

select * from person;
