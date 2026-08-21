The "tidy data" framework (Hadley Wickham) defines three rules:

1. Each variable forms a column
2. Each observation forms a row
3. Each type of observational unit forms a table

Wide format violates rule 1: "subject" is a variable, but its values (math, english, science) are spread across column names instead of being stored in a column. Melting converts to tidy format by making "subject" an explicit column.