-- list all cities contained in database 'hbtn_0d_usa'
SELECT `hbtn_0d_usa.cities.id`, `hbtn_0d_usa.cities.name`, `hbtn_0d_usa.states.name`
FROM `hbtn_0d_usa.cities` NATURAL JOIN `hbtn_0d_usa.states`
