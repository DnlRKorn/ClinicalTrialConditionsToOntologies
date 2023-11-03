SELECT distinct ctgov.interventions.nct_id, ctgov.conditions.downcase_name 
FROM ctgov.interventions, ctgov.studies, ctgov.conditions 
WHERE ctgov.interventions.intervention_type='Drug' 
AND ctgov.interventions.nct_id=ctgov.studies.nct_id
AND ctgov.interventions.nct_id=ctgov.conditions.nct_id
AND ctgov.studies.phase<>'Not Applicable'
AND ctgov.studies.phase is not NULL;
