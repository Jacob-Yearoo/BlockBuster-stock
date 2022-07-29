# Jacob Yearoo - BlockBuster Stockroom

Project three - BlockBuster stock program

I have made a very simple program, for the use of store managers or people that work in stock management, to effectively manage stock at any given point, without much hassle.

The Value that I will get out of this website is:

- Valuable experience learning Python
- Provide a service to people that don't want to update a spreadsheet every time their stock changes or moves around.

The Value that users of this program will get from this site are:

- A more streamlined way to update and manage stock without having to edit the associated spreadsheet manually, further increasing business productivity.


## Demo

[Live Demo](https://blockbuster-stock.herokuapp.com/)

[App page](https://dashboard.heroku.com/apps/blockbuster-stock/deploy/github)

[Google Sheet](https://docs.google.com/spreadsheets/d/1k80r0xOf3o-7jrTcCOIUANmJ7GQEn5IP8BvDORFdCuA/edit#gid=0)


## User Experience

### The Strategy
The idea was to provide an efficient program for employees to use to manage stock,
### The Scope
I wanted to make the program uncomplicated, it's very simple, provides feedback on correct and incorrect user inputs. 
### The Structure
The whole program is only one level deep, so once you give an input it's designed to return to the main screen so everything can be done quickly and without the need for extensive menus and submenus.
### The Skeleton

![Main Structure Wireframe](https://i.imgur.com/yQpwT7g.png)


### The Surface

The terminal was built with UX in mind so all writing is spaced out and easy to read.
## Features

- An option to check current stock for each film and the week.

![Current stock feature](https://i.imgur.com/Y56jjNS.png)
- An option to add stock to two different sheets with a table to show you what it looked like before and after your input.

![Add stock feature](https://i.imgur.com/9eaoE8Y.png)
- An option to add together the bottom row of two sheets and place it into a 3rd sheet to act as a "Total" numbers sheet.

![Total feature](https://i.imgur.com/1eCyIjd.png)

![Total feature - spreadsheet](https://i.imgur.com/fNDemun.png)
- An exit function to break out of the program

![Exit feature](https://i.imgur.com/k2OaKfO.png)
- Input validation to make sure that the user is inputing correct data - this includes an upper limit to what can be added as well.

## Features I'd Like to Implement

- I'd like to include an option to remove stock rather than just add.
- I would like to add a function that calculates the week at the side of the sheet rather than it having to be manually entered - so when you input new stock it tells you exactly what date it's gone in, rather than just the next row.

## Tech

**Python:** Used to write out all of the functions that allow the program to work.

**Google Cloud:** Supplied the APIs and keys needed for Python to communicate with Google Sheets.

**Google Sheets:** Used for the sheet that has all the stock information.

**Pandas:** To receive data from the external Google Sheet into a DataFrame.

**Tabulate:** to render pandas DataFrames.

## Testing

The Program does achieve my desired outcome of making stock management a more efficient process without the need for manually editing a Spreadsheet.

My code has passed through code linters such as Pep8 Online without any issues or errors.

## Bugs

| Bug     | Expected Outcome | What was the Issue | Fixed/Not Fixed |
|:--------|:-----------------|:-------------------|:----------------|
| Error message when entering invalid input was printing twice | The Error message is supposed to show once when only one error has been made | The validate_data function was being called twice before the Main function would continue | Fixed |
| Error trying to convert a list of strings to an integer | need the values as integers to be able to compare them to an integer which would then throw an error if not matching | Instead of trying to change the whole list, I iterated through the list and individually changed each item to an integer | Fixed |

## Deployment

This site is hosted using Heroku, To set up Heroku you must;


The requirements.txt file in the IDE must be updated to package all dependencies. To do this:

1. Enter the following into the terminal: 'pip3 freeze > requirements.txt'
2. Commit the changes and push to GitHub
3. Next, follow the steps below:
4. Login to Heroku, create an account if necessary
5. Once at your Dashboard, click 'Create New App'
6. Enter a name for your application, this must be unique, and select a region
7. Click 'Create App'
8. At the Application Configuration page, apply the following to the Settings and Deploy sections:
9. Within 'Settings', scroll down to the Config Vars section to apply the credentials being used by the application. In the Reveal Config Vars enter 'CREDS' for the Key field and paste the all the contents from the creds.json file into the Value field
10. Click 'Add'
11. Add another Config Var with the Key of 'PORT' and the Value of '8000'
12. Within Settings, scroll down to the Buildpacks sections, click to Add a Buildpack
13. Select Python from the pop-up window and Save
14. Add the Node.js Buildpack using the same method
15. Navigate to the Deploy section, select Github as the deployment method, and connect to GitHub when prompted
16. Use your GitHub repository name created for this project
17. Finally, scroll down to and select to deploy 'Automatically' as this will ensure each time you push code in GitHub, the pages through Heroku are updated
18. Your application can be run from the Application Configuration section, click 'Open App'


## GitPod Commits
The deployed site will update automatically upon new commits to the master branch.

## Credits

### Acknowledgements
I would like to credit [RickofManc](https://github.com/RickofManc/vv-pizzas) for his excellent README, I have used his instructions for deployment on Heroku, and for [this snippet of code](https://i.imgur.com/34eV4I4.png) as he was the one to make it, I utilised it to print off my panda DataFrames in a more presentable way.

This project was inspired by the walkthrough project at Code institute. [this is a link to the source code.](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1) the overall layout of my project was inspired by this program.

Special thanks to the Tutors at Code Institute for the support they've given.

