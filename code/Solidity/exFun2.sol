pragma solidity 0.5.0;

contract exFun2 {
   /*function getSum(uint a, uint b) public pure returns(uint){      
      return a + b;
   }
   function getSum(uint a, uint b, uint c) public pure returns(uint){      
      return a + b + c;
   }
   function callSumWithTwoArguments() public pure returns(uint){
      return getSum(1,2);
   }
   function callSumWithThreeArguments() public pure returns(uint){
      return getSum(1,2,3);
   }
   */
   function getSHA256( ) public pure returns (bytes32){
       return sha256( "Nielit ");
   }
     
}