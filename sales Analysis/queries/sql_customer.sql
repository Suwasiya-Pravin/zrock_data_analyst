SELECT 
   c.CustomerKey AS CustomerKey 
      --,[GeographyKey]
     -- ,[CustomerAlternateKey]
     -- ,[Title]
      ,
	  c.FirstName AS [First Name]
      --,[MiddleName]
      , c.LastName AS [Last Name],
	  c.FirstName + '' + c.LastName As [Full Name]
     -- ,[NameStyle]
     -- ,[BirthDate]
     -- ,[MaritalStatus]
      --,[Suffix]
      ,CASE c.Gender when 'M' then 'Male' when 'F' then 'Female' END AS Gender
     -- ,[EmailAddress]
     -- ,[YearlyIncome]
      --,[TotalChildren]
     -- ,[NumberChildrenAtHome]
     -- ,[EnglishEducation]
     -- ,[SpanishEducation]
     -- ,[FrenchEducation]
     -- ,[EnglishOccupation]
     -- ,[SpanishOccupation]
     -- ,[FrenchOccupation]
     -- ,[HouseOwnerFlag]
     -- ,[NumberCarsOwned]
      --,[AddressLine1]
      --,[AddressLine2]
      --,[Phone]
      ,c.DateFirstPurchase AS DateFirstPurchase,
	  g.City as [Customer City]
      --,[CommuteDistance]
  FROM dbo.DimCustomer as c LEFT JOIN dbo.DimGeography as g ON g.GeographyKey = c.GeographyKey
  ORDER BY 
  CustomerKey ASC  --- order accending 
