# project22

This project aims to pull shipping information from OCR text from digitized New-York Herald newspapers from 1842-1852. The Herald would publish a list of ships (Ship Type, Ship Name, Port, Master/Owner, separated by commas, with ships delimited by semicolons or colons) that departed New York Harbor in the "Maritime Herald" (later renamed the "Maritime Intelligence") column between the subheaders "Cleared" and "Arrived" This project aims to iterate through OCR text files from the LOC Chonicling America using python and regex to extract the text into new text files, combine extracted text into a csv using the Pandas module. 

Due to the errors found within some of the OCR data, as a subsquent step a script will be written using Levenshtein distance to "clean" at least the mistranscriptions of "Cleared" and "Arrived" as those terms are flags for the intial regex. Depending on the success of that script, I could write another script to clean mistranscribed Shipt Types as they are commonly repeated. 

Bulk download of New-York Herald OCR was done with Chronam by Andrew Pyle https://github.com/andrew-pyle/chronam


