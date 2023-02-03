DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  country TEXT NOT NULL,
  place TEXT NOT NULL,
  date TEXT NOT NULL,
  title TEXT NOT NULL,
  company TEXT NOT NULL,
  summary TEXT NOT NULL,
  description TEXT NOT NULL,
  logo TEXT NOT NULL,
  link TEXT NOT NULL
);