// RESIDENCES
cd "C:\Users\K\Documents\S2022\CSDS 341\Final Project\Data"
clear

// Create the total number of students
set obs 1000
set seed 98034

// Generate Sid
gen sid = _n

// Random residence number generator
gen rnum = floor(500*runiform() + 1000)

// residence halls and street names based on modulo of rnum
gen street = "clarke tower" if mod(rnum, 8) == 0
replace street = " random rd." if mod(rnum, 8) == 1
replace street = " overlook rd." if mod(rnum, 8) == 2
replace street = " euclid ave." if mod(rnum, 8) == 3
replace street = " hessler rd." if mod(rnum, 8) == 4
replace street = "kusch hall" if mod(rnum, 8) == 5
replace street = " e. 115th st." if mod(rnum, 8) == 6
replace street = " mayfield rd." if mod(rnum, 8) == 7

tostring rnum, replace

// combine street names and address numbers
gen residence = rnum + street if street != "clarke tower" && street != "kusch hall"
replace residence = street if residence == ""

// remove preresidence variables
drop rnum
drop street
drop sid
duplicates drop

// export 
export delimited "residences.csv", replace
