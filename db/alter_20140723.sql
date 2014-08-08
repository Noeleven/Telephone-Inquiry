use Phone_NUM;
alter table Inquiry_DB add COLUMN position VARCHAR(20) DEFAULT NULL;
alter table Inquiry_DB add COLUMN flag int DEFAULT 1;
