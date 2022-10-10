# CS3052 - Computer Security

## Program Security and Vulnerabilities
Continuous assessment - Protection of information based on sensitivity and privilege levelsAssignment

The data of each user is stored in a CSV file named ‘user_data.csv’. This file contains userID, 
username, password, and role.
There are 5 roles.
1. Patient
2. Hospital Assistant
3. Pharmacist
4. Lab assistant
5. Doctor

Read-only and Write operations are used to manipulate the data based on the privilege level.
Doctor: 
- Doctor can view all the data of the patients. Such as sickness, personal details, drug 
prescription, and lab report
- Doctor can edit the sickness details and drug prescription details
- Doctor cannot edit the lab report details, he can only view that.

Lab Assistant:
- Lab assistants can read the report of the patient and write the report.
- Lab assistant cannot modify or view other feaures

Pharmacist:
- Pharmacists can only view the patient drug prescription.
- He cannot view or edit other features
- Based on the sensitivity level he cannot access the details

Hospital Assistant
- Hospital assistant can only view the sickness details and sickness details
- Only he can add users to the system

Patient:
- Patients can view all the data according to his/her id
- Patients cannot modify anything on the system

Only hash passwords are stored in the database. The python ‘hashlib’ library is used to hash 
the password by ‘utf-8’
