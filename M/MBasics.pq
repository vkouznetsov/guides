// M Documentation - https://docs.microsoft.com/en-us/powerquery-m/

let  
   VariableName = expression,  
   #"Variable Name" = expression2  
in   
   VariableName;

/*////////////////////////////////////////////////////////////////////////
//
//     Evaluation Model
//

M evaluation is based on dependency model.

List, Record, and Table member expressions, as well as let expressions (See Expressions, values, and let expression),
are evaluated using lazy evaluation: they are evaluated when needed. All other expressions are evaluated using eager
evaluation: they are evaluated immediately, when encountered during the evaluation process. 

*/


/*////////////////////////////////////////////////////////////////////////
//
//     Primitive Values
//

Type	        Example value
Binary	        00 00 00 02 // number of points (2)
Date	        5/23/2015
DateTime	    5/23/2015 12:00:00 AM
DateTimeZone	5/23/2015 12:00:00 AM -08:00
Duration	    15:35:00
Logical	        true and false
Null	        null
Number	        0, 1, -1, 1.5, and 2.3e-5
Text	        "abc"
Time	        12:34:12 PM

*/

/*////////////////////////////////////////////////////////////////////////
//
//     List
//

A List is a zero-based ordered sequence of values enclosed in curly brace characters { }. The curly
brace characters { } are also used to retrieve an item from a List by index position.


Value	                        Type

{123, true, "A"}	            List containing a number, a logical, and text.

{1, 2, 3}	                    List of numbers

{
{1, 2, 3},
{4, 5, 6}
}	                            List of List of numbers

{
[CustomerID = 1, Name = "Bob", Phone = "123-4567"],
[CustomerID = 2, Name = "Jim", Phone = "987-6543"]
}	                            List of Records

{123, true, "A"}{0}	            Get the value of the first item in a List. This expression returns the value 123.

{
{1, 2, 3},
{4, 5, 6}
}{0}{1}                         Get the value of the second item from the first List element. This expression returns the value 2.

*/


/*////////////////////////////////////////////////////////////////////////
//
//     Record
//

A Record is a set of fields. A field is a name/value pair where the name is a text value that is unique within
the field’s record. The syntax for record values allows the names to be written without quotes, a form also
referred to as identifiers. An identifier can take the following two forms:

- identifier_name such as OrderID.
- #"identifier name" such as #"Today's data is: ".

*/

let 
    Source =   
        [  
              OrderID = 1,   
              CustomerID = 1,   
              Item = "Fishing rod",   
              Price = 100.00  
        ]  
in 
    Source

let 
    Source =   
    [  
          OrderID = 1,   
          CustomerID = 1,   
          Item = "Fishing rod",   
          Price = 100.00  
    ]  
in 
    Source[Item] //equals "Fishing rod"


/*////////////////////////////////////////////////////////////////////////
//
//     Table
//

A Table is a set of values organized into named columns and rows. The column type can be implicit or explicit.
You can use #table to create a list of column names and list of rows. A Table of values is a List in a List.
The curly brace characters { } are also used to retrieve a row from a Table by index position

*/

let  
  Source = #table(   
    {"OrderID", "CustomerID", "Item", "Price"},   
      {   
          {1, 1, "Fishing rod", 100.00},   
          {2, 1, "1 lb. worms", 5.00}   
      })  
in  
    Source

// Create a table with explicit column types
let  
    Source = #table(  
    type table [OrderID = number, CustomerID = number, Item = text, Price = number],   
        {   
            {1, 1, "Fishing rod", 100.00},   
            {2, 1, "1 lb. worms", 5.00}   
        }  
    )  
in  
    Source

let  
    Source = #table(  
    type table [OrderID = number, CustomerID = number, Item = text, Price = number],   
        {   
            {1, 1, "Fishing rod", 100.00},   
            {2, 1, "1 lb. worms", 5.00}   
        }  
    )  
in  
    Source{1}   // Get a row from a table by index position


/*////////////////////////////////////////////////////////////////////////
//
//     Conditional Expression
/*/

if 2 > 1 then  
    2 + 2   
else   
    1 + 1


/*//////////////////////////////////////////////////////////////////////
//
//     Functions
/*/

// Definition
let  
    MyFunction = (parameter1, parameter2) => (parameter1 + parameter2) / 2  
in  
    MyFunction  
  
// Calling the MyFunction() returns the result:  
  
let  
    Source = MyFunction(2, 4)  
in  
    Source

