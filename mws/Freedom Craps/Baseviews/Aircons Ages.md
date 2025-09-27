# Age of the Air Conditioners

These R their ages.

> Only viewable in Obsidian
> 
> [Something interesting else to see](Aircons%20GS%20Identities.md)

```dataview
TABLE 
dob as "Date of Birth", 
durationformat(dur(date(today) - dob), "y'y' M'm' d'd'") AS 
"Age (YYYY-MM-DD)"
FROM #airconditioner AND -"_Templates"
SORT (dob = NULL) ASC, dob ASC
```

Ignore those at the bottom. They are just description and templates
