DROP TABLE IF EXISTS jobs;
DROP TABLE IF EXISTS contact;

CREATE TABLE jobs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  country TEXT,
  place TEXT,
  date TEXT,
  title TEXT,
  company TEXT,
  summary TEXT,
  description TEXT,
  logo TEXT,
  link TEXT
);

CREATE TABLE contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);