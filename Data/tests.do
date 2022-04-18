// TESTS
cd "C:\Users\K\Documents\S2022\CSDS 341\Final Project\Data"
clear

// Create the total number of students
set obs 1000
set seed 98034

// Generate Sid
gen sid = _n

//generate random number
generate rand = runiform()

// generate positivity
gen has_covid = rand < 0.2

//generate date
gen year = floor(3*runiform() + 2020)
tostring year, replace

gen month = floor(12*runiform() + 1)
tostring month, replace

gen day = floor(28*runiform() + 1)
tostring day, replace

gen positive_date = month + "-" + day + "-" + year if has_covid > 0

drop rand year month day

export delimited "tests.csv", replace
