DROP TABLE IF EXISTS jobs;

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