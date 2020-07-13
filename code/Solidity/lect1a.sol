pragma solidity ^0.5.1;
contract SolidityTest {
   
   function getResult() public  view  returns(uint){
      uint a = 1;
      uint b = 2;
      uint result = a + b;
      return result;
   }
  
}