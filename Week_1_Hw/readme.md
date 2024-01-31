## Questions

### Question 1: Which tag has the following text? - Automatically remove the container when it exits

- --delete
- --rc
- --rmc
- --rm

#Answer :- rm 

### Question 2: What is version of the package wheel ?

- 0.42.0
- 1.0.0
- 23.0.1
- 58.1.0

  #Answer :- 0.42.0

### Question 3: Count records
How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18.

Remember that lpep_pickup_datetime and lpep_dropoff_datetime columns are in the format timestamp (date and hour+min+sec) and not in date.

- 15767
- 15612
- 15859
- 89009

### Question 4: Largest trip for each day

Which was the pick up day with the largest trip distance Use the pick up time for your calculations.

- 2019-09-18
- 2019-09-16
- 2019-09-26
- 2019-09-21

### Question 5: Three biggest pickups

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

- "Brooklyn" "Manhattan" "Queens"
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens"
- "Brooklyn" "Queens" "Staten Island"

### Question 6: Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

Note: it's not a typo, it's tip , not trip

- Central Park
- Jamaica
- JFK Airport
- Long Island City/Queens Plaza

## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```
Answer 

```
Terraform used the selected providers to generate the following execution plan. 
Resource actions are indicated with the following symbols: 
... and much more 
```
