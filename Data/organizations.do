// Organizations
cd "C:\Users\K\Documents\S2022\CSDS 341\Final Project\Data"
clear

// Create the total number of orgs
set obs 50
set seed 98034

// Generate orgid
gen orgid = _n + 49

// export
export delimited "organizations.csv", replace
