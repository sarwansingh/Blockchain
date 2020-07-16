 pragma solidity 0.5.1;

contract StudentMgt {
    uint256 studentCount = 0;
    
    address owner;

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
    
    constructor() public {
        owner = msg.sender;
    }

    struct Student {
        uint _rollno;
        string _name;
        string _courseName;
        uint256 _coureStartDate;
    }

    mapping(uint => Student) public enrolledStudents;
    
    function enrollStudent(uint _rollno, string memory _name, string memory _courseName, 
        uint256   _coureStartDate) public   onlyOwner   {
        studentCount +=1 ;
        enrolledStudents[studentCount] = Student(_rollno,_name, _courseName, _coureStartDate);
    }
}

