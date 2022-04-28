// VACCINATION
cd "C:\Users\K\Documents\S2022\CSDS 341\Data"
clear

// Create the total number of students
set obs 1000
set seed 98034

// Generate Sid
gen sid = _n

//generate random number
generate rand = runiform()
generate rand2 = runiform()

// generate number of doses
gen num_doses = 0
replace num_doses = 1 if rand > 0.3
replace num_doses = 2 if rand > 0.7

//generate date
gen year = "2021"

gen month = floor(12*runiform() + 1)
tostring month, replace

gen day = floor(28*runiform() + 1)
tostring day, replace

gen last_dose_date = year + "-" + month + "-" + day if num_doses > 0
replace last_dose_date = "0001-01-01" if num_doses == 0
// dose-type
gen dose_type = "johnson" if num_doses > 0
replace dose_type = "moderna" if (num_doses > 0) & (rand2 > 0.2)
replace dose_type = "pfizer" if (num_doses > 0) & (rand2 > 0.6)
replace dose_type = "none" if dose_type == ""

drop rand rand2 year month day

export delimited "vaccination.csv", replace
