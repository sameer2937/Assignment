problem #3:

1. Alter boolian operator at line no. 12:
	In previous code, developer compare existing event's end time and new events start time, if it is overlapping return True.
	But we are expecting that if it is overlapping it should return False and do not insert event

2. Replace operator '<=' with '<' at line no. 09:
	In previous code, developer combine both of the situation for one result only(events are overlapping and events are between
	between two events there is not time.) But we are expection that even if there is no time difference in the starting time of
	new event and end time of previous event it should return True and insert event as well.

3. Remove one step intendetion of line no. 12:
	In previous code, There were two separate return statment which was throwing error unneccessorily. We are expecting that at
	any situation if two events are overlapping it should return False.
