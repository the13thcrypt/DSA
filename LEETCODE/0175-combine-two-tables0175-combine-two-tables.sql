# Write your MySQL query statement below
Select firstname , lastname , city , state from Person
left outer join Address
    on Person.personId=Address.personId
