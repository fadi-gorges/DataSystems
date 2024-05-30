create table if not exists
  custom (
    custom_id bigint primary key generated always as identity,
    doors text,
    seats text,
    extColour text,
    intColour text
  );

insert into
  custom (doors, seats, extColour, intColour)
select
  doors,
  seats,
  "extColour",
  "intColour"
from
  "CarSales";

create table if not exists
  model (
    model_id bigint primary key generated always as identity,
    year int4,
    transmission text
  );

insert into
  model (year, transmission)
select
  "year",
  "transmission"
from
  "CarSales";

create table if not exists
  line (
    line_id bigint primary key generated always as identity,
    model text,
    engine numeric,
    driveType text,
    fuelType text,
    fuelConsumption	numeric,
    cylindersInEngine numeric,
    bodyType text
  );

insert into
  line (engine, model, driveType, fuelType, fuelConsumption, cylindersInEngine, bodyType)
select
  "engine", "model", "driveType", "fuelType", "fuelConsumption", "cylindersInEngine", "bodyType" 
from
  "CarSales";

create table if not exists
  cars (
    car_id bigint primary key generated always as identity,
    usedOrNew text,
    kilometres int4,
    price int4
  );

insert into
  cars (usedOrNew, kilometres, price)
select
  "usedOrNew",
  "kilometres",
  "price"
from
  "CarSales";