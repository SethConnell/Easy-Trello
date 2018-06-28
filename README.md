# Simple Trello API Wrapper.
This is a short Python 2.7 wrapper for Trello’s API — In fact, most Trello API features aren’t even supported.

I created this wrapper so that programmers could launch Trello projects quickly without having to worry about so many details (i.e. what color should your Trello board be?). I did this by spending extra time building a clear structure, leaving documentation, and making certain API settings preset on the developer’s behalf - which can be changed.

## Usage Example:
Assuming you have your environment variables set correctly, you should be able to create a Trello board using the following code:

`Trello(key, token).createBoard("Strategy")`

## Supported Trello API requests:
* createBoard

## Required Python Modules:
* json
* requests
