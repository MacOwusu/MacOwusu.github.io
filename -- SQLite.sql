--SQLite

SELECT fpl as PovertyStatus, SWB_1 as LifeSatisfactionRate FROM NFWBS where SWB_1 >= 1 and SWB_1 <= 7 limit 400; 
--Analyzing the correlation between the Life Satisfaction Rate and Poverty Status
--Higher satisfaction if individual is less poor
--fpl(Poverty Status): 1 = < 100%, 2 = 100-199%, 3 = 200%
--SWB_1(Life Satisfaction Rate): 1-7; strongly disagree-strongly agree

SELECT PPETHM as Race, PPEDUC as Education, fpl as PovertyRate from NFWBS  limit 400; 
--PPETHM(Race): 1=White, 2=Black, 3=Other, 4=Hispanic
--PPEDUC(Education): 1=Less than high school, 2=HighSchool/GED, 3=Some College, 4=Bachelors degree, 5=Graduate Professional Degree
--Individuals who have a higher level of education are typically less poor
--Black people who get a higher level of education are typically less poor
--Black people with atleast a 3 or higher are generally not poor stay in the 2&3s category with a few outliers

SELECT FWBscore, KH7correct  from NFWBS where FWBscore < 54 and KH7correct = 0; 
--KH7correct(Correct answer for understand of credit card minimum): 0=no, 1=yes
--FWBscore(Financial Well-Being Score): Scale of 0-100
--1758 for FWB score > 54 and KH7correct=1
--1735 for FWB score > 54 and KH7correct=0
--973 for FWB score < 54 and KH7correct=1
--1741 for FWB score < 54 and KH7correct=0
--More people with a score higher than average(54) got the minimum credit card knowledge correct 
--More people with a score lower than average(54) got it incorrect

SELECT generation, LIFEEXPECT from NFWBS where LIFEEXPECT >= 0 and generation = 4;
--1=Pre-Boomer, 2=Boomer, 3=Gen X, 4=Millenial
--Life Expectancy scale from 0-100
--Pre-Boomers were super confident majority of answer were above 50% LOL
--Numbers decreased as it went to boomers more in the 50-80% range
--Dropped alot more for Gen X, fluctuated alot in terms of high and low numbers
--Millenials were confident too, more higher numbers than lower

SELECT FWBscore, PPEDUC FROM NFWBS WHERE FWBscore > 54 LIMIT 400;
--This query shows that individuals with higher education also have a higher FWBscore
