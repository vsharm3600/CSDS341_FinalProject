// Organizations
cd "C:\Users\K\Documents\S2022\CSDS 341\Data"
clear

// Create the total number of orgs
set obs 50
//original seed +1
set seed 98035

// Generate orgid
gen orgid = _n + 49

// Generate in-person
gen in_person = runiform() > 0.2

// Last meeting date
//generate date
gen year = floor(3*runiform() + 2020)
tostring year, replace

gen month = floor(12*runiform() + 1)
tostring month, replace

gen day = floor(28*runiform() + 1)
tostring day, replace

gen last_meeting_day = year + "-" + month + "-" + day if in_person == 1

drop year month day

// export
export delimited "organizations.csv", replace
