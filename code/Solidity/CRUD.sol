pragma solidity ^0.5.0;

contract Crud {
  struct User {
    uint id;
    string name;
  }
  User[] public users;
  uint public nextId = 1;

  function create(string memory name) public {
    users.push(User(nextId, name));
    nextId++;
  }
function read(uint id) view public 
	returns(uint, string memory) 
{
    uint j;
    for(uint i = 0; i < users.length; i++) {
      if(users[i].id == id) {
        j = i;
      }
    }
    if(j == 0) {
      revert('User does not exist!');
    }
    return(users[j].id, users[j].name);
}



}
