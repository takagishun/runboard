begin;

create temp table owner_profile_seed as
select id as val_id, handle as display_name
from vals;

create table vals_next (
  id integer primary key,
  code text not null
);

insert into vals_next (id, code)
select id, code
from vals;

drop table vals;

alter table vals_next rename to vals;

create table owner_profiles (
  val_id integer primary key references vals(id),
  display_name text not null
);

insert into owner_profiles (val_id, display_name)
select val_id, display_name
from owner_profile_seed;

drop table owner_profile_seed;

commit;
