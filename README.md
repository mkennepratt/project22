# project22

This project aims to pull shipping information from OCR text from digitized New-York Herald newspapers from 1842-1852. The Herald would publish a list of ships (Ship Type, Ship Name, Port, Master/Owner, separated by commas, with ships delimited by semicolons or colons) that departed New York Harbor in the "Maritime Herald" (later renamed the "Maritime Intelligence") column between the subheaders "Cleared" and "Arrived" This project aims to iterate through OCR text files from the LOC Chonicling America using regex to extract the text into new text files, combine extracted text into a csv using the Pandas module. 

Bulk download of New-York Herald OCR was done with Chronam by Andrew Pyle https://github.com/andrew-pyle/chronam


