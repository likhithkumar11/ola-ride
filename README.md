OVERALL RIDE PERFORMANCE – SQL
-- Total Rides
SELECT COUNT(Booking_ID) AS Total_Rides
FROM July;

-- Successful Rides
SELECT COUNT(Booking_ID) AS Successful_Rides
FROM July
WHERE Booking_Status = 'Success';

-- Total Revenue
SELECT SUM(Booking_Value) AS Total_Revenue
FROM July;

BOOKING STATUS DISTRIBUTION – SQL
SELECT Booking_Status,
       COUNT(Booking_ID) AS Total_Bookings
FROM July
GROUP BY Booking_Status;

VEHICLE ANALYSIS – SQL
SELECT Vehicle_Type,
       SUM(Ride_Distance) AS Total_Ride_Distance
FROM July
GROUP BY Vehicle_Type
ORDER BY Total_Ride_Distance DESC
LIMIT 5;

CANCELLATION ANALYSIS – SQL
SELECT Canceled_Rides_by_Driver,
       COUNT(Booking_ID) AS Cancel_Count
FROM July
WHERE Booking_Status = 'Canceled by Driver'
GROUP BY Canceled_Rides_by_Driver;

Customer Cancellation Reasons
SELECT Canceled_Rides_by_Customer,
       COUNT(Booking_ID) AS Cancel_Count
FROM July
WHERE Booking_Status = 'Canceled by Customer'
GROUP BY Canceled_Rides_by_Customer;

RATINGS ANALYSIS – SQL
-- Average Customer Rating
SELECT AVG(Customer_Rating) AS Avg_Customer_Rating
FROM July;

-- Average Driver Rating
SELECT AVG(Driver_Ratings) AS Avg_Driver_Rating
FROM July;

REVENUE ANALYSIS – SQL
SELECT Payment_Method,
       SUM(Booking_Value) AS Revenue
FROM July
GROUP BY Payment_Method;

Revenue Trend by Year
SELECT YEAR(Date) AS Year,
       SUM(Booking_Value) AS Revenue
FROM July
GROUP BY YEAR(Date);

