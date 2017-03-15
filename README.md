# hashmap-python
A hashmap implemented in Python without using a hashmap primitive.

## Requirements
* Python (2.7.10-2.7.13)
* Xcode developer Tools
* Homebrew


## Setup

1. Open up Your Command Line Application
2. Make sure you have Installed Xcode Developer Tools with:

 `$ xcode-select --install`
  
3. Install Homebrew with:

 `$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
 
4. Install Python with:

 `$ brew install python` 
 
5. Check the version of Python:

 `$ python --version`
 
 
6. If version is not 2.7.1X then run:

 `$ brew upgrade python`
 
7. Clone the Code to Your Local:

 `$ git clone https://github.com/acucciniello/hashmap-python.git'`
 
## Test

1. Enter the Directory:

 `$ cd hashmap-python`
  
2. Run the Tests:

 `$ python test.py`

## Design and Analysis

This is a Hashmap that is designed to be a list where each element of the list is a LinkedList.  Each element in the Hashmap has a key, which takes you to a specific Linked List.  There you have access to the first element of the list. Here is a picture  of how the Hashmap would look like:

![Hashmap_Image](https://github.com/acucciniello/hashmap-python/blob/master/images/HashmapChaining.png)

The Hashmap was designed this way in order to utilize the chaining method of resolving collisions.  When two elements are supposed to be inserted to the same key, instead of having to calculate a new location (in a basic Hashmap without Linked Lists), we just add them both to the Linked List.  

Average case scenario, the runtime for an insertion or removal of an element in the Hashmap would be `O(1)` (constant time).  In the worst case, where all elements that are placed in the Hashmap all hash to the same key, then the runtime of an insertion or removal is `O(n)` where `n` is all elements that are hashed to that location (in the Linked List for that key).

## License

MIT