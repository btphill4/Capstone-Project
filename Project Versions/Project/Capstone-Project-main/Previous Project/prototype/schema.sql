CREATE TABLE homeownerapp(
  appid numeric PRIMARY KEY NOT NULL, -- application id

-- MOST IMPORTANT QUESTIONS

  -- q1
  full_name TEXT NOT NULL,

  -- q2
  phone_number TEXT NOT NULL,

  -- q3
  email TEXT NOT NULL,

  -- q4
  age numeric NOT NULL,

  -- q5 
  what_do_you_do TEXT NOT NULL,
  
  -- q6 hours to work each week (need to ask Aisha for this question)

  -- q7
  city TEXT NOT NULL,

  -- q8 
  preferred_neighborhood TEXT NOT NULL,

  -- q9
  max_house_mates numeric NOT NULL,

  -- q10
	rent_range_start numeric NOT NULL,
	rent_range_end numeric NOT NULL,

  -- q11
  age_range TEXT NOT NULL,

  -- q12
  lease_or_rent TEXT NOT NULL,
  lease_length TEXT,

  -- q13
  has_children boolean NOT NULL, 
  children_ages TEXT, -- should maybe be a separate table in real database

  -- q14
  live_with_children boolean NOT NULL,

  -- q15
  personal_pets_bool boolean NOT NULL,
  personal_pets_text TEXT,

  -- q16
  live_with_pets_bool boolean NOT NULL,
  live_with_pets_text TEXT,

  -- q17
  move_in_date date NOT NULL,

  -- q18 personality
  q18_1 boolean NOT NULL, -- carefree
  q18_2 boolean NOT NULL, -- outgoing
  q18_3 boolean NOT NULL, -- laid back
  q18_4 TEXT, -- other (please specify)

  -- q19
  environment_type TEXT NOT NULL,

  -- q20 
  q20_1 numeric NOT NULL, -- furnished room
  q20_2 numeric NOT NULL, -- parking
  q20_3 numeric NOT NULL, -- gym
  q20_4 numeric NOT NULL, -- personal bathroom
  q20_5 numeric NOT NULL, -- personal kitchen

  -- q21 ideal friday night
  q21_1 boolean NOT NULL, -- movie night with friends/housemates
  q21_2 boolean NOT NULL, -- night out
  q21_3 boolean NOT NULL, -- bar hopping
  q21_4 boolean NOT NULL, -- self care night to wind down
  q21_5 boolean NOT NULL, -- netflix
  q21_6 TEXT, -- other (please specify)

  -- q22 which of the following motivates you to participate in co-living
  q22_1 boolean,  -- you'd like to have company at home
  q22_2 boolean,  -- it is a more feasible option
  q22_3 boolean,  -- the added safety of not living alone
  q22_4 boolean,  -- belonging to a community of fun, supportive women
  q22_5 TEXT,

  -- q23 what do you want to see to ensure your privaty is protected
  privacy_needs TEXT NOT NULL,

  -- q24 personal 
  q24_1 numeric NOT NULL, -- kitchen use
  q24_2 numeric NOT NULL, -- neatness
  q24_3 numeric NOT NULL, -- kitchen cleanliness
  q24_4 numeric NOT NULL, -- guests often visit
  q24_5 numeric NOT NULL, -- household cleanliness
  q24_6 numeric NOT NULL, -- recreational cannabis
  q24_7 numeric NOT NULL, -- smoking

  -- q25 events that you'd like to see
  future_events TEXT,

  -- q26 housemate
  q26_1 numeric NOT NULL, -- kitchen use
  q26_2 numeric NOT NULL, -- neatness
  q26_3 numeric NOT NULL, -- kitchen cleanliness
  q26_4 numeric NOT NULL, -- guests often visit
  q26_5 numeric NOT NULL, -- household cleanliness
  q26_6 numeric NOT NULL, -- recreational cannabis
  q26_7 numeric NOT NULL, -- smoking

  -- q27 favorite hobbies/what do you do on days off for enjoyment
  hobbies_text TEXT NOT NULL,

  -- q28
  additional_info TEXT

);