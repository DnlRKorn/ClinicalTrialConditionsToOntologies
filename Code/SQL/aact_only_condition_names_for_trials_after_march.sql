select distinct(ctgov.conditions.downcase_name), (SELECT COUNT(c.nct_id) from ctgov.conditions c where ctgov.conditions.downcase_name=c.downcase_name)
from ctgov.conditions, ctgov.outcome_analyses, ctgov.studies
where ctgov.studies.results_first_posted_date_type='Actual'
and ctgov.studies.results_first_posted_date>'2023-02-28'
and ctgov.studies.results_first_posted_date<'2023-08-12'
and ctgov.studies.nct_id=ctgov.outcome_analyses.nct_id 
and ctgov.studies.nct_id=ctgov.conditions.nct_id;
