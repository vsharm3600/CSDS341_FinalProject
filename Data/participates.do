// Participates
cd "C:\Users\K\Documents\S2022\CSDS 341\Final Project\Data"
clear

// Create the total number of students
set obs 1000
set seed 98034

// Generate Sid
gen sid = _n

// generate orgids
gen orgid = floor(50*runiform() + 50)

// export
export delimited "participates.csv", replace
