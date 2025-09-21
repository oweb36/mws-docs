```dataview
TABLE 
dob as "Date of Birth", 
durationformat(dur(date(today) - dob), "y'y' M'm' d'd'") AS 
"Age (YYYY-MM-DD)"
FROM #airconditioner
WHERE dob
SORT dob ASC
```
