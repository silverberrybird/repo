<?php
$a= $_GET['n1'];
$b=$_GET['user'];
$c=$_GET['n2'];
$d=$_GET['n3'];

// Create connection
 $con=mysqli_connect("localhost","root","","student");

 // Check connection
if (!$con)
 {
   die("Connection failed: " . mysqli_connect_error());
 }

// Insert Query

 $sql = "insert into student values($a,'$b','$c',$d)";

     if (mysqli_query($con, $sql)) 
     {
           echo "New record inserted successfully";
     }
    else 
     {
         echo "Error: " . $sql . "<br>" . mysqli_error($conn);
     }

//Select query
  $rs=mysqli_query($con,"select * from student");

//Display student data in table format
echo "<table border=1><tr><th>Rollno</th><th>Name</th><th>Email</th><th>Mobno</th></tr>";
while($row1=mysqli_fetch_assoc($rs))
{
   echo"<tr>";
   echo "<br><td>".$row1["Rollno"]."</td>";
   echo "<td>".$row1['Name']."</td>";
   echo "<td>".$row1['Email']."</td>";
   echo "<td>".$row1['Mobno']."</td>";
   echo"</tr>";
}

// close the connection 
mysqli_close($con);
?>