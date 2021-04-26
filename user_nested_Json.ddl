CREATE EXTERNAL TABLE IF NOT EXISTS nestedJsondb.user_table(
    firstName string,
    lastName string,
    gender string,
    age int,
    address struct<streetAddress:string,city:string,state:string>,
    phoneNumbers array<struct<type:string,number:string>>)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://myfirstjsonbuckettoquery/';