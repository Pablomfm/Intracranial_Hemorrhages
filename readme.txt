
## PROJECT INFORMATION
-------------------

Author: Pablo Menéndez Fernández-Miranda MD, PhD (pablomenendezfernandezmiranda@gmail.com).



	* WARNING - GitHub does not render all HTML content, to view all representations copy and paste Notebook links on https://nbviewer.org.



1. ABSTRACT
-----------

	* THIS PROJECT IS STILL ONGOING!!!!

The aim of this project is to find new prognostic factors of ICH and develop a risk stratification tool, with the premise of being easy-to-implement and use. For that purpose data from more than 160 variables belonging to 300 patients were collected. The results showed that glucose levels, prothrombin activity, hours from the clinical onset, Glasgow Coma Scale, and the comorbidity associated, were prognosis factors for survival. The models with highest performance (c-index) were those based on Cox regression, with up to 0.84 95% CI (0.75,0.90). There, a Cox model based on five clinical variables is proposed as a potential tool to aid in decision making for patients with ICH, although further clinical validation studies is required.


2. PROJECT WORKFLOW SUMMARY
---------------------------

	2.1 (Anonymization, Cleaning and Curation)
	------------------------------------------

	'ICH_database_complete.xlsx' (not available in this repository due to privacy issues) -->
 	
	--(...)--> 'ICH_database_pseudoanonymized_nonredudant.csv' (not available) ------------->

	--(1. Anonymization 2 (R))--------------> 'ICH_database_anonymized.csv' ---------------->

	--(2. Cleaning & Curation (R))----------> 'ICH_database.csv'/'ICH_database.rds' & 
	                                          'ICH_database_metadata.csv'------------------->

	--(3. Save the dataset in Python-HDF5)--> 'ICH_database.hdf5' -------------------------->

	--> ...


	2.2 (Data Loading, Statistical Analysis and Machine Learning Modeling)
	----------------------------------------------------------------------
	
	Data Loading

	--(A. Loading the dataset in python)-----------------------> Options to load the dataset in R.
	--(B. Loading the dataset in R)----------------------------> Options to load the dataset in python.

	
	Statistical Analysis

	--(4.1 EDA & Descriptive Statistics of Outcomes)-----------> EDA & Descriptive Statistics of outcomes.
	--(4.2 EDA & Descriptive Statistics of Predictors)---------> EDA & Descriptive Statistics of predictors.
	--(4.3 EDA & Descriptive Statistics of Dates (R))----------> EDA & Descriptive Statistics of dates.
	--(5.1 Inferential Statistics - Hypothesis Contrasts (R))--> Hypothesis contrasts.
	--(5.2 Inferential Statistics - Survival Analysis)---------> Survival analysis.

	
	Machine Learning Modeling

	--(6. Dimensionality reduction - PCAs & FA)----------------> PCAs & FA.
	--(7. Kernel Methods - SVM & SSVM)-------------------------> SVM & SSVM.
	--(8. RSF, GB model and AFT models)------------------------> Random Survival Forest, Gradient Boosted & Accelerated Failure Time models.



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


    	· '4.3 EDA & Descriptive Statistics of Dates (R)': this Notebook analyzes the relevant dates, which have been deleted in the databases shared in the repository for anonymization purposes.

		1. Load data
		2. Change dates into Date types
		3. Descriptive statistics


    	· '5.1 Inferential Statistics - Hypothesis Contrasts (R)': this Notebook is designed to do an statistical analysis following the standards of biostatistics for multiple variables (False Discovery Rate - FDR correction of p-values was included):

		1. Load dataset and metadata.
		2. Assumption of normality.
		3. Correlation analysis.
		4. Statistical tests: hypothesis contrasts.


	· '5.2 Inferential Statistics - Survival Analysis': this Notebook conducts a survival analysis of patients who have suffered an intracranial hemorrhage. Survival is defined as survival to hospitalization discharge. Different biostatiscal techniques are used for that purpose, including the well-known Kaplain-Meier estimator, Mantel-Cox (log-rank) test, and the state-of-the-art method for survival prediction until the last adaptations of machine learning algorithms for survival analysis, Cox Proportional Hazards regression.

		1. Load dataset
		2. Define survival variables
		3. Survival functions
		4. Cox Proportional Hazards regression


	· '6. Dimensionality reduction - PCAs & FA': this Notebook explores some dimensionality reduction techniques, including Principal Component Analysis (PCA) and Factorial Analysis (FA). PCA is more appropriate for quantitative data, nevertheless, FA allows to analyze a dataset with numerical and categorical variables.

		1. Load dataset
		2. Principal Component Analysis (PCAs)
		3. Factorial Analysis (FA)


	· '7. Kernel Methods - SVM & SSVM': kernel methods are a type of Machine Learning algorithms used to map input data into a different multidimensional space in which data classes can be easily sepparated. Therefore, this methods are very used to solve classifcation and regression problems. A very well-knowned algorithm of this group is Support Vector Machine (SVM), which has been adapted for solving survival prediction in the named Survival Support Vector Machine (SSVM).

		1. Load dataset
		2. Support Vector Machine (SVM)
		3. Survival Support Vector Machine (SSVM)


	· '8. RSF, GB model and AFT models': This Notebook explores models based on Random Survival Forest and Gradient Boosted techniques, including a parametric approach for survival function estimation, the well-known Accelerated Failure Time approach.

		1. Load dataset
		2. Random Survival Forests
		3. Gradient Boosted Model
		4. Accelerated Failure Time Model

	-----------------------------------------------------------------------------------------------------

