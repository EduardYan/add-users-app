-- This is the model for the database
BEGIN TRANSACTION;
DROP TABLE IF EXISTS "users";
CREATE TABLE IF NOT EXISTS "users" (
	"id"	integer,
	"name"	varchar(100),
	"age"	integer NOT NULL,
	"description"	text NOT NULL,
	PRIMARY KEY("id")
);
INSERT INTO "users" VALUES (1,'Daniel',12,'This is other user');
COMMIT;
