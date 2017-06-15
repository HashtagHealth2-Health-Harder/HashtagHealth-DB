CREATE TABLE IF NOT EXISTS main (
  id               INTEGER      PRIMARY KEY,
  Location         INT          NOT NULL,
  Time             INT          NOT NULL,
  Profile_location INT,
  Full_Tweet       VARCHAR(400) NOT NULL,
  Hashtags         TEXT,
  Mentions         TEXT,
  BuzzWords        TEXT
);