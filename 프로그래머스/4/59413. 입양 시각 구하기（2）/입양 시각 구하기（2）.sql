with recursive rc as (
    select 0 as hour
    union all
    select hour+1 from rc where hour<23
)
SELECT rc.HOUR HOUR, COUNT(ANIMAL_ID) COUNT
FROM ANIMAL_OUTS
RIGHT JOIN rc ON rc.hour = HOUR(DATETIME)
GROUP BY rc.HOUR
ORDER BY rc.HOUR
