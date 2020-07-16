pragma solidity ^0.5.0;

contract cBase { 
    uint public pubData = 50;
    uint private priData = 50;
    uint internal iData = 70;
    
    constructor () public{
        pubData=20;
    }
    
     //private function
   function increment(uint a) private pure returns(uint) { return a + 1; }
   
   //public function
   function updatepriData(uint a) public { priData = a; }
   function getpriData() public view returns(uint) { return priData; }
   function compute(uint a, uint b) internal pure returns (uint) { return a + b; }
    
}

contract call_cBase{
    
    function readData() public returns(uint) {
      cBase cb = new cBase();
      cb.updatepriData (17);         
      return cb.getpriData();
   }
 
}
// Inheritance 
contract derived is cBase{
    uint private result;
    cBase private c;
   
   constructor() public {
      c = new cBase();
   }  
   function getComputedResult() public {      
      result = compute(3, 5); 
   }
   function getResult() public view returns(uint) { return result; }
   function getpubData() public view returns(uint) { return c.pubData(); }
}
