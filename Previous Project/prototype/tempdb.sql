CREATE DATABASE tempdb;
\c tempdb

CREATE TABLE homeownerapp(
	appid numeric PRIMARY KEY NOT NULL, -- application id
	
	-- q7
	city TEXT NOT NULL,									-- city name 
	
	-- q10
	rent_range_start numeric NOT NULL,
	rent_range_end numeric NOT NULL,
	
	-- q13
	have_children boolean NOT NULL,			-- whether the tenant has children or not 
	children_text TEXT DEFAULT 'N/A'	-- text for q13
	children_num numeric DEFAULT -1,		-- number of children
	
	-- q14	
	live_with_children boolean NOT NULL,-- whether tenant is open with living with someone who has 	children or not

	-- q15
	pets_binary boolean NOT NULL,				-- whether tenant has pets or not
	pets_text TEXT DEFAULT 'N/A',				-- text for q15
	pets_num numeric DEFAULT -1,				-- number of pets
	
	-- q16
	live_with_pets boolean NOT NULL, 	-- whether tenant is open to living with someone who has pets or not
	pets_okay TEXT DEFAULT 'N/A',				-- type of pets tenant is okay with living with
	
	-- q17
	move_date_start DATE NOT NULL,			-- soonest date tenant is okay with moving in
	move_date_end DATE NOT NULL,				-- latest date tenant is okay with moving in
	
	-- q12
	month_or_lease TEXT NOT NULL,				-- whether tenant wants to pay month to month or lease
	lease_length numeric,								-- lease length
	
	-- q8
	neighborhood TEXT,									-- neighborhood name
);


create table tenantapp(
	
	appid numeric PRIMARY KEY NOT NULL, 
	city TEXT NOT NULL, 
	neighborhood TEXT, 
	rent_range_start numeric NOT NULL, 
	rent_range_end numeric NOT NULL

);

create table homeownerapp(
	
	appid numeric PRIMARY KEY NOT NULL, 
	city TEXT NOT NULL, 
	neighborhood TEXT, 
	rent_range_start numeric NOT NULL, 
	rent_range_end numeric NOT NULL

);


SELECT *
FROM homeownerapp
where city=(
	SELECT city 
	FROM tenantapp 
	where appid=1) 

SELECT * 
FROM homeownerapp 
where neighborhood=(
	SELECT neighborhood 
	from tenantapp 
	where appid=1);
	
SELECT * 
FROM homeownerapp 
where rent_range_start<=(
	SELECT rent_range_end 
	FROM tenantapp 
	where appid=1) 
AND rent_range_end>(
	SELECT rent_range_start 
	FROM tenantapp 
	where appid=1) 
			
SELECT * 
FROM homeownerapp 
where rent_range_start<=(
	SELECT rent_range_end 
	FROM tenantapp 
	where appid=10) 
AND rent_range_end>(
	SELECT rent_range_start 
	FROM tenantapp 
	where appid=10) 
AND city=(
	SELECT city 
	FROM tenantapp 
	where appid=10) 
AND neighborhood=(
	SELECT neighborhood 
	FROM tenantapp 
	where appid=10);
