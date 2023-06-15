
DATABASES INFO
--------------


1. WORKFLOW
------------

	'ICH_database_complete.xlsx' ---->
	 ----> 'ICH_database_complete_pseudoanonymized.xlsx'/ICH_database_complete_pseudoanonymized.csv ---->
	 ----> 'ICH_database_pseudoanonymized_nonredudant.csv' ---->
	 ----> 'ICH_database_anonymized.csv' ---->
	 ----> 'ICH_database.csv'/'ICH_database.rds'/'ICH_database.hdf5'.

	

	'ICH_database_anonymized_metadata.xls'/'ICH_database_anonymized_metadata.csv' ---->
	 ----> 'ICH_database_metadata.csv'



2. DATABASES
-------------

	· 'ICH_database_complete.xlsx': complete database.

	· 'ICH_database_complete_pseudoanonymized.xlsx': database without patients identifiers (NHC, ID, Hospital...) in .xlsx.

	· 'ICH_database_complete_pseudoanonymized.csv': database without patients identifiers (NHC, ID, Hospital...) in .csv.

        · 'ICH_database_nonredudant_pseudoanonymized.csv': 'ICH_database_complete_pseudoanonymized.csv' without some redundant or non-useful columns.

        · 'ICH_database_anonymized.csv': 'ICH_database_nonredudant_pseudoanonymized.csv' fully anonymized by the:
		- Anonymization of: Fecha de ingreso, Fecha de alta, Fecha de TC, Fecha análisis de sangre, Fecha nacimiento, Fecha mortalidad.
		- Incorporation of: Time between blood analysis and head CT scan, Age at the hospital admission date, Survival days after admission.

        · 'ICH_database.csv': 'ICH_database_anonymized.csv' cleaned (assignation of variable datatypes, correction of incorrect data values, rename variables with the variable labels, and elimination of variables with only one different value or with redundant information and dates which only contain the value "anonymized").

        · 'ICH_database.rds': 'ICH_database.csv' saved as R object in .rds to preserve variable datatypes.

	· 'ICH_database.hdf5': 'ICH_database.csv' saved as hdf5 file to preserve variable datatypes.

	· 'ICH_database_anonymized_metadata.csv': file with information about the variables of 'ICH_database_nonredudant_pseudoanonymized.csv' and 'ICH_database_anonymized.csv'. This file contains the following variables:
       		- Variable_Name: name of the variable (spanish).
       	 	- Variable_R_Name: name of the variable given by R.
		- Variable_Label: recommended name of the variable for further database analysis.
      		- Variable_Definition: definition of the variable.
       		- R_Datatype: recommended R datatype for the variable.
       		- Python_Datatype: recommended Python datatype for the variable.
		- Pandas_Datatype: recommended Pandas datatype for the variable.
       		- Values: values that the variable can have.
       		- Maximum_Number_of_Different_Values_in_the_Dataset: maximum number of possible different values in the dataset.
       		- Comment: comments about the variable.
       		- Type_of_Variable: if variable is a priori an outcome (dependent) or a predictor (independent), or if the variable just contains additional information about the dataset (auxiliary).

	· 'ICH_database_anonymized_metadata.xls': same as 'ICH_database_anonymized_metadata.csv' but in .xls.

	· 'ICH_database_metadata.csv': file with information about the variables of 'ICH_database.csv'. This file contains the following variables:
		- Variable_Name: name of the variable (spanish).
		- Variable_Label: name of the variable in the database.
      		- Variable_Definition: definition of the variable.
       		- R_Datatype: R datatype.
       		- Python_Datatype: Python datatype.
		- Pandas_Datatype: Pandas datatype.
       		- Values: values that the variable can have.
       		- Maximum_Number_of_Different_Values_in_the_Dataset: maximum number of possible different values in the dataset.
       		- Comment: comments about the variable.
       		- Type_of_Variable: if variable is a priori an outcome (dependent) or a predictor (independent), or if the variable just contains additional information about the dataset (auxiliary).



3. MAIN DATABASE CONTENT (ICH_database)
---------------------------------------

	The cleanest version of ICH database is 'ICH_database', which is available in three formats (.csv, .rds, .hdf5). This database is accompanied by another file ('ICH_database_metadata') having all the relevant database metadata, including the definition of all variables. These variables, group by categories are the following:

	
	IDENTIFIERS
		· patient


	DEMOGRAPHICS
		· sex
		· age
		· hospital


	OUTCOMES
		· follow_up
		· final_outcome
		· survival_discharge
		· survival_3d
		· survival_6d
		· survival_9d
		· survival_12d
		· survival_15d
		· survival_1m
		· survival_3m
		· survival_1y
		· survival_5y
		· survive
		· survival_days

		· neurosurg (detailed also below in treatment of the ICH)
		· interprocedures (detailed also below in treatment of the ICH)

	OUTCOMES/PREDICTORS
		· hospitalizations_1y
		· hospitalizations_3y
		· hospitalizations_5y
		· hospitalization_icu_days
		· hospitalization_days


	PAST MEDICAL HISTORY

		FAMILY DISEASES
		· nfamily_medhist

		DRUG USE
		· tobacco
		· n_tobacco
		· drugs
		· alcohol
		· g_alcohol

		PAST MEDICAL HISTORY
		· ht
		· dmellitus
		· dyslipidemia
		· previous_ich
		· cv_diseases
		· carrhythmias
		· structural_heart_disease
		· vascular_diseases
		· neurological_diseases
		· dementia
		· depression
		· psychiatric_diseases
		· cancerous_autoimmune_diseases
		· cancerous_diseases
		· autoimmune_diseases
		· hyper_hypo_thyroidism
		· haematological_disorders
		· other_diseases
		
		REGULAR MEDICATIONS
		· antihypertensives
		· antidiabetics
		· hypolipidemics
		· anticoagulants
		· antiplatelets
		· chemotherapeutics
		· digoxin
		· n_other_medications
		· aceis
		· arbs
		· ccbs
		· bblockers
		· ablockers
		· ablockers1
		· ablockers2
		· diuretics
		· other_antihypertensives
		· biguanides
		· sulfonylureas
		· glinides
		· glp1a
		· dpp4i
		· agi
		· insulin
		· statins
		· aspirin
		· p2y12b
		· gIIbIIIai
		· cumarinics
		· noac
		· dabigatran
		· rivaroxaban
		· other_medications


	SYMPTOMS / ANAMNESIS AT THE EMERGENCY DEPARTMENT
		· onset_h
		· headache
		· emesis
		· visual_disturbances
		· seizures
		· mh_trauma
		· mh_le_trauma
		· mh_he_trauma
		· other_symptoms


	PHYSICAL EXAMINATION AT THE EMERGENCY DEPARTMENT
		· sbp
		· dbp
		· spo2
		· temperature
		· bpm
		· rr
		· neurol_signs
		· diplopia
		· anisocoria
		· aphasia
		· dysarthria
		· altered_consciousness
		· nuchal_rigidity
		· rfacial_palsy
		· lfacial_palsy
		· ruplimb_mimpairment
		· luplimb_mimpairment
		· rlwlimb_mimpairment
		· llwlimb_mimpairment
		· balance_impairment
		· tgcs


	ICH CAUSES
		· primary_ich
		· vascular_ich
		· traumatic_ich
		· ht_ich
		· amyloidangiopathy_ich
		· aneurysmal_ich
		· avm_ich
		· hti_ich
		· other_ich


	TREATMENT OF THE ICH
		· neurosurg
		· interprocedures


	BLOOD ANALYSIS
		BLOOD ANALYSIS AT THE EMERGENCY DEPARTMENT
		· glucose
		· urea
		· creatinine
		· sodium
		· potasium
		· egfr
		· prothrombin_activity
		· leukocytes
		· erythrocytes
		· hemoglobin
		· hematocrit
		· platelets
		· mcv
		· rdw
		· mchc
		· mpv
		· mch
		· inr
		· fibrinogen
		
		OTHER BLOOD ANALYSIS VARIABLES
		· maxfibrinogen
		· time_between_CT_bloodanalysis







