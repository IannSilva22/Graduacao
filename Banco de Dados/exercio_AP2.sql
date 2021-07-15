CREATE TABLE Localization(
                          LOCATION_ID INTEGER NOT NULL,
                          STREET_ADDRESS VARCHAR (40),
                          POSTAL_CODE VARCHAR (12),
                          CITY VARCHAR(30),
                          STATE_PROVINCE VARCHAR (25),         
                          COUNTRY_ID VARCHAR (2)
                         );
DESCRIBE  Localization;                          
ALTER TABLE Localization ADD region_id INT NOT NULL; 
                        
                