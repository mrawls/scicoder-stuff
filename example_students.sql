CREATE TABLE "City" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "label" TEXT);
CREATE TABLE "Club" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "label" TEXT);
CREATE TABLE "Status" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "label" TEXT);
CREATE TABLE "Student" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "first_name" TEXT, "last_name" TEXT, "city_id" INTEGER, "status_id" INTEGER);
CREATE TABLE "Student_to_Club" ("student_id" INTEGER NOT NULL , "club_id" INTEGER NOT NULL , PRIMARY KEY ("student_id", "club_id"));
CREATE TABLE "Student_to_Supervisor" ("student_id" INTEGER NOT NULL , "supervisor_id" INTEGER NOT NULL , PRIMARY KEY ("student_id", "supervisor_id"));
CREATE TABLE "Supervisor" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , "first_name" TEXT, "last_name" TEXT, "room_number" TEXT);