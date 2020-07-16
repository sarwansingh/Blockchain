pragma solidity 0.5.0;
contract exFun1 {
  function show() public pure  returns(uint res){
      uint a = 10; 
      uint b = 25;
      uint result = a + b;
      return sumOfDigits(result); 
   }
  function sumOfDigits(uint _no) internal pure  returns (uint sum) {
	// write the logic to calculate sum of digits in _no
	// and return the calculated sum 
	 uint tot= _no;
		return tot; 
   }
  function showMultipleReturn() public pure  returns(uint sum, uint product ){
      uint a = 10; 
      uint b = 25;
      sum = a+b;
      product = a*b;
      //return (a+b, a*b); 
   }
}