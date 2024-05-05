SELECT 
	[ProductKey]
      ,[OrderDateKey]
      ,[DueDateKey]
      ,[ShipDateKey]
      ,[CustomerKey]
      --,[PromotionKey]
      --,[CurrencyKey]
      --,[SalesTerritoryKey]
      ,[SalesOrderNumber]
      --,[SalesOrderLineNumber]
      --,[RevisionNumber]
      --,[OrderQuantity]
      --,[UnitPrice]
     -- ,[ExtendedAmount]
      --,[UnitPriceDiscountPct]
      --,[DiscountAmount]
      --,[ProductStandardCost]
      --,[TotalProductCost]
      ,[SalesAmount]
     -- ,[TaxAmt]
      --,[Freight]
      --,[CarrierTrackingNumber]
      --,[CustomerPONumber]
      --,[OrderDate]
     -- ,[DueDate]
      --,[ShipDate]
  FROM
  [dbo].[FactInternetSales]
  WHERE 
  CAST(LEFT(OrderDateKey, 4) AS INT) <= 2019 -- ensure we always only bring of date from extration
  ORDER BY 
  OrderDateKey desc
