// ENROLLED
cd "C:\Users\K\Documents\S2022\CSDS 341\Final Project\Data"
clear

// Create the total number of students
set obs 3002
set seed 98034

// Generate Sid
gen sid = mod(_n,1001)

// drop extra mods
drop if sid==0

// generate cids
gen cid = floor(100*runiform() + 100) if _n < 1001
replace cid = floor(100*runiform() + 200) if (_n > 1000) & (_n < 2001)
replace cid = floor(100*runiform() + 300) if _n > 2000

// export
export delimited "enrolled.csv", replace
