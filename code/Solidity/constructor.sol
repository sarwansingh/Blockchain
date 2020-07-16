pragma solidity 0.5.0 ;
contract Base {
   uint data;
   constructor(uint _data) public {
      data = _data;   
   }
}
// calling constructor directly
contract Derived is Base (5) {
   constructor() public {}
}

//calling constructor indirectly 
contract Derived1 is Base {
   constructor(uint _info) Base(_info * _info) public {}
}
