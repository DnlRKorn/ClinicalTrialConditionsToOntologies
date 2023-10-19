SELECT COUNT(nct_id), downcase_name 
FROM ctgov.conditions
/*where downcase_name='metastatic breast cancer'*/
group by downcase_name
limit 500;

/*id, nct_id, name, */
