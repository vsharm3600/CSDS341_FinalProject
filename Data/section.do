// SECTION
cd "C:\Users\K\Documents\S2022\CSDS 341\Data"
clear

// Create the total number of sections
set obs 300
set seed 98034

// Generate Cid
gen cid = _n + 99

// Generate in person
gen in_person = runiform() > 0.2

// export
export delimited "section.csv", replace
