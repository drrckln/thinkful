create table species (
    name text
);

create table breed (
    name text,
    species int
);

create table pet (
    name text,
    dead integer,
    breed int,
    adopted integer
);

create table person (
    first_name text,
    last_name text,
    age integer,
    email text,
    phone text
);
