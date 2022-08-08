# HANG-HANGMAN

Hang-Hangman is a word guessing game .
The user will be given the game rules , a level choice to play the game at Easy , Medium or Hard.
The user can try to guess the word by inputting letters, if the letter is wrong a visual of the traditional hangman man will start to appear, if the letter is in the word the letter is shown and another guess can be made. Until either all lives are used or the game is won.
The aim is to supply a fun word guessing game to the user.

![amiresponsive](./assest/readmeimages/hangman-amiresponsive.png)

# Planning Of Hang-Hangman

* When Planning what I thought about and wanted in the game.

  + The user to see and be able to do .
  + The user not to be able to see but the program to do .
  + The game to be easy to use have easy to folow instructions with a logical flow to the  game.
  + I wanted the game to give feed back to the user if the instructions where not followed correctly or if incorrect information was input by accident.
  + I wanted the game to have a bit of color to it to give it a more fun look and to show with the colours instuctions , correct input and incorrect input.

* For the User

  + A nice Introduction
  + Easy to Follow Instructions
  + Clear information to make choices
  + Levels in the Game to keep it Interesting
  + Fun to Play  

# Flowchart

* The logical flow of how I was going to implement the coding of the game

  + Where to use inputs & check inputs.  
  + Where to give user feed back.
  + Where to give choices and direct of game from those choices.
  + Check the logic of the game lay out in order to code accordingly.
 * Note : The flow chart was rough and for me to work from and does not show all the code but assisted me in how I needed to start to code and how the code should flow

![hangman-flowchart](./assest/readmeimages/hangman-flowchart.png)

# Features

  * Current Features

   * Terminal Pages in Order of game Flow

      + Heading Log
      + Welcome
      + User Name Request
      + Input Space shown

  ![1stTerminalpg](./assest/readmeimages/hangman-1stterminalpg.png)

  * Note once the User Enters user name it triggers the option menu to be shown 

      + Users Name Entered
      + Hello "Users Name"
      + Options Menu shown
      + Input Space shown

  ![2ndTerminalpg](./assest/readmeimages/hangman-2ndterminalpg.png) 

  * Note on option selection it will trigger the selection to start 
    * Option 1 = Default Game Level to start   

      + 1 Input by user 
      + Game Deault level starts Lives shown
      + The word to Guess 
      + Guess a letter
      + Input Space Shown

  ![options1](./assest/readmeimages/hangman-options1.png) 
  
  * Note on option selection it will trigger the selection Game Level option & clear the terminal screen
    * Option 2 = Game Level to options Seelction

      + 2 Input by user 
      + Screen clears & Game Level option shows .
      + Input Space Shown
      + Note on selection of any of the 3 options game will start at that level

  ![options2](./assest/readmeimages/hangman-options2.png)

* Note on option selection it will trigger the selection to Game Rules 
    * Option 3 = Game Rules   

      + 3 Input by user 
      + Game Rules shown below 
      + Pressing enter will return to the Options Menu on a cleared terminal
      
  ![options1](./assest/readmeimages/hangman-options3.png)

# Game in play

  * Note that on selction of either options 1 or any off the leves in Options 2 the Game will start .
      + Is letter in word check and result of letter not in word 
      + Is letter in word check and result of letter in word
      + Input of more than 1 letter check and result / just pressing enter 
      + Input of not a letter check and result 
      + Input of a letter already used and result
  * Note Hangman visuals begins to build on letter not in word as life is lost level drops
  * Note User is informed and directed during game play screen is cleared of messages as game progresses    

![gameinplay1](./assest/readmeimages/hangman-gameinplay1.png)
![gameinplay2](./assest/readmeimages/hangman-gameinplay2.png)
![gameinplay3](./assest/readmeimages/hangman-gameinplay3.png)
![gameinplay4](./assest/readmeimages/hangman-gameinplay4.png)
![gameinplay5](./assest/readmeimages/hangman-gameinplay5.png)
![gameinplay6](./assest/readmeimages/hangman-gameinplay6.png)

# Game Won & Game Lost

* Game Won
  + Won message 
  + Option to either play again Y / N will appear

![gamewon](./assest/readmeimages/hangman-youwon.png)

* Game Lost
  + You Lose Message
  + Option to either play again Y/ N will appear

![gamelost](./assest/readmeimages/hangman-gamelost.png)

# Play again Y/N Choice

  * Yes option 
    + User Input Y 
    + Main Options Menu 
    + Input Space Shown

  * On selection of option screen will clear and run the selected option

![playagainy](./assest/readmeimages/hangman-playagainy.png)  

 * No option 
    + User Input N 
    + Game Heading Logo ,Welcome & User name request  
    + Input Space Shown

  * Game is back at the beginning

![playagainn](./assest/readmeimages/hangman-playagainn.png)  


# Technologies  / Support Used

* Below is a list of Technologies / Support I have used to build my site.

    + Code Institute lessons and the Love Sandwiches in assisting with how to start and construct my project.
    + Code Institute Supplied the template inorder to display Python in a Visual formed Terminal
    + GitHub for my repository 
    + Git used to code within and provided backups of all my code.
    + Hourokapp for project deployment https://dashboard.heroku.com/apps
    + Patorjik.com for the Game Logo https://patorjk.com/software/taag/#p=display&f=Letters&t=HANG%20-%0AHANGMAN
    + Lucidchart for my Flowchart which helped with the logic & flow of my code https://www.lucidchart.com/
    
# Testing
* Testing During development of the project was done through out the project to see how the project looked and felt within the Git Terminal using python3 run.py to assertain if the code was working and if any errors "Bugs" occured PEP8 was also used throught the project.

  * Manual Testing

| Feature           |  Expect              |  Action |  Result                 |
|-------------------|----------------------|---------|-------------------------|
|                   |                      |         |                         |
|                   |                      |         |                         |
|                   |                      |         |                         | 

* User Testing

    + Expectations
      As a user I wanted the project to 
      1. Understand the purpose of the site, 
      2. Be able to navigate easily through the site,
      3. Have clear instructions
      4. 
    + Result
      As a user I was able to  
      1. 
      2. 
      3. 
      4. 

# Bugs 



# Validator testing
  * PEP8 
    * No errors were returned from 

# Deployment of Project

  * Deployment was made possible by GitHub
    + Initiated a repository in git via template supplied by codeinstute : 
    + Created all folders and files and code project
    
  
# Credits

   * Code Institute without who I would have had no base to begin a project & Readme.md Template .https://codeinstitute.net/ie/
   * Reuben Ferrante my mentor without all his great guidance I would be lost. A Huge Thanks. https://github.com/arex18
   * Youtube video tutorial to base my game on. https://www.youtube.com/watch?v=m4nEnsavl6w
   * The Slack community - for someone always been there no matter the time and with advice or direction. https://slack.com
   * StackOverflow for all the information to assit with my project . https://stackoverflow.com
   * I am Responsive for a fantastic spot to see a visual of responsiveness. https://ui.dev/amiresponsive?msclkid=400b1adabe5b11ecbc48938198bb87b4
   * 

  