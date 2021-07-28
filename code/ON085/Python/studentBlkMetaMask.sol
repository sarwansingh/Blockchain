pragma solidity ^0.4.0;
contract Courses {
    
    struct Student {
        string studentName;
        string studentEmail;
        string studentCourseName;
    }
    Student stu ;
    function setStudent( string _studentName, string _studentEmail,
        string _studentCourseName) public {
        stu.studentName  = _studentName;
        stu.studentEmail = _studentEmail; 
        stu.studentCourseName = _studentCourseName;
    }
     
    function getInstructor() view public returns (string, string, string) {
        return (stu.studentName, stu.studentEmail , stu.studentCourseName);
    }
}
