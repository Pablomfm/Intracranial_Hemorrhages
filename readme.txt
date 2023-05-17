
PROJECT INFORMATION
-------------------

Author: Pablo Menéndez Fernández-Miranda MD, PhD (pablomenendezfernandezmiranda@gmail.com).



1. ABSTRACT
-----------

	* THIS PROJECT IS STILL ONGOING!!!!


2. PROJECT WORKFLOW SUMMARY
---------------------------

	2.1 (Anonymization, Cleaning and Curation)
	------------------------------------------

	'ICH_database_complete.xlsx' (not available in this repository due to privacy issues) --> 	
	--(...)--> 'ICH_database_pseudoanonymized_nonredudant.csv' (not available in this repository due to privacy issues) -->

	--(1. Anonymization 2 (R))--------------> 'ICH_database_anonymized.csv' -------------------------------------->
	--(2. Cleaning & Curation (R))----------> 'ICH_database.csv'/'ICH_database_metadata.csv'/'ICH_database.rds' -->
	--(3. Save the dataset in Python-HDF5)--> 'ICH_database.hdf5' ------------------------------------------------>
	--> ...


	2.2 (Data Loading, Analysis and Modeling)
	-----------------------------------------

	--(A. Loading the dataset in python)-----------------------> Options to load the dataset in R.
	--(B. Loading the dataset in R)----------------------------> Options to load the dataset in python.

	--(4.1. EDA & Descriptive Statistics of Outcomes)----------> EDA & Descriptive Statistics of outcomes
	--(4.2. EDA & Descriptive Statistics of Predictors)--------> EDA & Descriptive Statistics of predictors
	--(5.1. Inferential Statistics - Hypothesis Contrasts (R))--> Hypothesis contrasts
	--(5.2. Inferential Statistics - Survival Analysis (R))-----> Survival analysis

	--(6. PCAs & SVM)------------------------------------------> PCAs-SVM model
	--(7. Kernel Regressions)----------------------------------> Kernel Regressions models	
	--(8. K-Nearest Neighbors)---------------------------------> KNN models
	--(9. Association Algorithms)------------------------------> APPROACH and Eclat results.
	--(10. Decision Trees & Random Forest)---------------------> Decision Trees and Random Forest models.
	--(11. Bayesian Networks)----------------------------------> Bayesian models.
	--(12. Deep Neural Networks)-------------------------------> Deep neural networks models.



3. MATERIALS AND METHODS
------------------------

	3.1 Available Databases
	-----------------------

		(not available databases are not described here, they are in Databases/readme_databases.txt)

		3.1.1 Datasets
		--------------

        	· 'ICH_database_anonymized.csv': data collected from 300 patients with Intracranial Hemorrhages (ICH) fully anonymized by removing patient identifiers and relevant dates (ex. birth or death date).

        	· 'ICH_database.csv': 'ICH_database_anonymized.csv' cleaned after the following steps:
			-- Assignation of variable datatypes.
			-- Correction of incorrect data values.
			-- Rename variables with variable labels.
			-- Elimination of variables with only one different value.
			-- Elimination of variables with redundant information.
			-- Elimination of dates which only contain the value "anonymized".

        	· 'ICH_database.rds': 'ICH_database.csv' saved as R object in .rds to preserve variable datatypes.

		· 'ICH_database.hdf5': 'ICH_database.csv' saved as hdf5 file to preserve variable datatypes.
		
		
		3.1.2 Metadata
		--------------

		· 'ICH_database_anonymized_metadata.csv': file with information about the variables in 'ICH_database_anonymized.csv':
       			-- Variable_Name: name of the variable (spanish).
       	 		-- Variable_R_Name: name of the variable given by R.
			-- Variable_Label: recommended name of the variable for further database analysis.
      			-- Variable_Definition: definition of the variable.
       			-- R_Datatype: recommended R datatype for the variable.
       			-- Python_Datatype: recommended Python datatype for the variable.
			-- Pandas_Datatype: recommended Pandas datatype for the variable.
       			-- Values: values that the variable can have.
       			-- Maximum_Number_of_Different_Values_in_the_Dataset: maximum number of possible different values in the dataset.
       			-- Comment: comments about the variable.
       			-- Type_of_Variable: if variable is a priori an outcome (dependent), predictor (independent), or if it just contains additional information about the dataset (auxiliary).

		· 'ICH_database_anonymized_metadata.xls': same as 'ICH_database_anonymized_metadata.csv' but in .xls.

		· 'ICH_database_metadata.csv': file with information about the variables in 'ICH_database.csv':
       			-- Variable_Name: name of the variable (spanish).
			-- Variable_Label: name of the variable in the database.
      			-- Variable_Definition: definition of the variable.
       			-- R_Datatype: R datatype.
       			-- Python_Datatype: Python datatype.
			-- Pandas_Datatype: Pandas datatype.
       			-- Values: values that the variable can have.
       			-- Maximum_Number_of_Different_Values_in_the_Dataset: maximum number of possible different values in the dataset.
       			-- Comment: comments about the variable.
       			-- Type_of_Variable: if variable is a priori an outcome (dependent) or a predictor (independent), or if the variable just contains additional information about the dataset (auxiliary).


	3.2. Notebooks
	--------------

	· 'A. Loading the dataset in python': describe the best options to load the dataset in python.

	· 'B. Loading the dataset in R': describe the best options to load the dataset in R.

    	· '1. Anonymization 2 (R)': load 'ICH_database_nonredudant_pseudoanonymized.csv' and generate 'ICH_database_anonymized.csv'. In a first step, all patient identifiers (IDs,...) were removed. Now this Notebook conducts a second anonymization step, that consists in the anonymization of the dates. This kind of data may contain information which can help to identify patients, so it will be safer to anonymize all variables containing dates. However, to avoid the loss of information three new variables will be generated and added to the database: Time between head CT scan and blood analysis (days), Age at the hospital admission date (years), Survival days after admission (days). This Notebook will conduct this second anonymization step including the following sub-steps:

		1. Load data
		2. Change the dates into Date types
		3. Generate the new variables
		4. Anonymize the dates and save the anonymized database.


    	· '2. Cleaning & Curation (R)': load 'ICH_database_anonymized.csv' & 'ICH_database_anonymized_metadata.csv' and generate 'ICH_database.csv' & 'ICH_database_metadata.csv' after the following steps.
		
		1. Load the database
		2. Check variables: datatypes and values
		3. Change datatypes when appropriate
		4. Change values when appropriate
		5. Delete non-useful variables
		6. Change column names and re-adapt metadata_database
		8. Save the cured database and the metadata database.

	· '3. Save the dataset in Python-HDF5': save the dataset in a HDF5 file to easier further usage in Python. This Notebooks includes the following steps:

		1. Load dataset metadata and extract an array with categorical columns index.
		2. Load the dataset: all variables with NaN will be float64 and all variables without NaN int64.
		3. Change to categories when appropriate.
		4. Check datatypes and save in a hdf5 file.

    	· '4.1 EDA & Descriptive Statistics of Outcomes': exploring data analysis and descriptive statistics of the priori outcome variables contained in 'ICH_cured.csv'. This Notebook contains the following steps:

		1. Define some useful functions for further analysis.
		2. Load data and metadata.
		3. Check the pandas datatype and the a priori variable type of the dataset variables.
		4. Exploring and making a statistical description of the a priori outcome variables.


    	· '4.2 EDA & Descriptive Statistics of Predictors': exploring data analysis and descriptive statistics of the a priori predictor variables contained in 'ICH_cured.csv'. This Notebook contains the following steps:
		1. Load data and metadata.
		2. Check the pandas datatype and the a priori variable type of the dataset variables.
		3. Exploring and making a statistical description of the a priori predictor variables.




