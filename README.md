# The Review page

![The Review page Mockup Images]()

[View the live project here](https://github.com/LySeriuos/MS-3-book-review)

## Table of contents
1. [`Introduction`](#introduction)
2. [`UX`](#ux)    
    1. [`Design`](#design)
3. [`Features`](#features)
4. [`Issues and Bugs`](#issues-and-bugs)
5. [`Technologies Used`](#technologies-Used)
     1. [`Main Languages Used`](#main-languages-used)    
     2. [`Frameworks, Libraries & Programs Used`](#frameworks,-libraries-&-programs-Used)
6. [`Testing`](#automated-testing)
7. [`Further testing`](#further-testing)    
8. [`Deployment`](#deployment)    
9. [`Credits`](#credits)
     1. [`Audio`](#audio)
10. [`Acknowledgements`](#acknowledgements)
[`Back to top ⇧`](#the-review-page)

***
## Introduction
---
* **The Review page** is book lovers place to share their minds with other readers or just to find good professionals reviews to help find The Book. The The Review page fits all ages from arround 13 years old to let's say 99! The main goal is to give best expierence and easy to use web page. 

* The Review page is my third Milestone project and this is 3nd of 4 projects during the Software Developer Program at The Code institute.

[`Back to top ⇧`](#the-review-page)

### Requirements
---
1. HTML, CSS, JavaScript, Python+Flask, MongoDB
Additional libraries and external APIs.
2. Users make use of the site to share their own data with the community, and benefit from
having convenient access to the data provided by all other members.
The site owner advances their own goals by providing this functionality, potentially by being
a regular user themselves. The site owner might also benefit from the collection of the
dataset as a whole.
3. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
4. Version Control: Use Git & GitHub for version control.
5. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
6. Deployment: Deploy the final version of your code to a hosting platform such as GitHub Pages.
7. Build a book review and recommendation site.
8. Find books they would like to read.
9. Earn money on each book purchased via a link from the site.

[`Back to top ⇧`](#the-review-page)

### UX
---

The potential user of this The Review page:
* All ages from 2 years old.

What players are willing to find:

* Fun game, easy to understandt.
* To Load and Play.
* To be able to save scores.
* To compete with friends.
* To change difficulty levels.

[`Back to top ⇧`](#the-review-page)

## Skeleton 
---
Wireframe mockups were created in a [Figma Workspace](https://www.figma.com/file/7fXyHSsH2WbTadTaDyaUsC/The-Review?node-id=0%3A1) for the positive expierence:

Index Page:
![Index Page Wireframe](assets/read.me/The Review page MS2.png"Index Page Wireframe")

### Design
---
* The main idea was to create a stylish page with simple design to be easy understanble and not crowded with function that users do'nt need. The main font is ["Lora"](https://fonts.google.com/?query=lora). As a back up font going to be "Sans Serif". 
* THe review page meets user with the image wich tells directly what about this page is. 
* Buttons has slightly different colours: black and white. to bee easy readible. 
* The main color of the page is white, because it is very importnat to have eyes friendly environment in the page.
* Middle of the page I gave to the main purpose of the page. To introduce newest books!

[`Back to top ⇧`](#the-review-page)

### Features
---
* The The Review page developed as responsive. It can be shown on mobile phones, tablet computers and on big screens.
* User can register, log in and logout.
* User can leave their reviews to the each book separatly.
* All the reviews and user information is saved in the mongo db cloud database.
* User is able to see his created reviews and member profile page.
* User can add, delete or edit their reviews.
* User can search for the books by authos, book name, genre and years.


  [`Back to top ⇧`](#the-review-page)  

## Further Testing 
## Code


* The The Review page was tested on Google Chrome, Opera, Mozilla Firefox, Microsoft Edge and Safari, mobile Safari, mobile Chrome browsers.
* The The Review page was viewed on a variety of devices such as Desktop, Laptop, Android phones, iPhone7, iPhone 8 & iPhone13.
* Friends and family members were asked to review the game and documentation to point out any bugs and/or user experience issues.
* Some bugs left to fix.

[`Back to top ⇧`](#the-review-page)


### Issues-and-Bugs
---
1. When trying to open book page I got this error:
UnboundLocalError: local variable 'critics_reviews' referenced before assignment.
Solution: 
I found mistake in a book name which didn't match with in "critics_reviews" and "books" collections. Fixed name and problem was fixed. 
2. The picture of the book was not showing in the page. 
Solution: 
This erros was because of bad path:
static/img/books-img/Boyfriend-Material.jpg and it should be /static/img/books-img/Boyfriend-Material.jpg. 
3. jQuery.Deferred exception: Cannot set properties of null (setting 'value') TypeError: Cannot set properties of null (setting 'value')
This issue is not fixed because I got results I needed. Adding If statement doesn't helped and removed information from inputs.
4. ImportError: cannot import name 'app' from partially initialized module 'first' (most likely due to a circular import) (/workspace/MS-3-book-review/first.py).
Solution:
Fixed by removing import routes from user.

[`Back to top ⇧`](#the-review-page)

## Automated Testing

### Code Validation
The [FreeFormatter Validator](https://www.freeformatter.com/html-validator.html) service was used to validate the `HTML` code used.
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate the `CSS` coded used.


**Results:**

- Not added at the moment.




[`Back to top ⇧`](#the-review-page)

## Deployment

Information coming soon!

[`Back to top ⇧`](#the-review-page)

## Credits 

### Audio & Media

- All the book images came from [Amazon](https://amazon.com/ "Link to Unsplash") 
- The text used in the 404 error page was sourced from [CopyAndPasteFonts](https://www.copyandpastefont.com/ "Link to Font editor") and edited by the developer.

# Technologies Used
### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [Java Script](https://en.wikipedia.org/wiki/JavaScript "Link to JS Wiki")

[`Back to top ⇧`](#the-review-page)

### Frameworks, Libraries & Programs Used
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts was used to import the fonts "Lora" into the style.css file.
- [JQuery](https://jquery.com/ "Link to Jquery")
    - JQuery was used to simplify Java Script code.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used to import icons mute/unmute.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
- [Figma](https://www.figma.com/ "Link to Figma homepage")
     - Figma was used to create the wireframes during the design phase of the project.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used in order to see responsive design throughout the process and to generate mockup imagery to be used.


[`Back to top ⇧`](#the-review-page)

## Acknowledgements

- I would like to thank my friends and family for their valued opinions and critic during the process of design and development.
- I would like to thank my mentor, Seun, for her invaluable help and guidance throughout the process.
- I would like to thank tutor support for showing me the way with my issues.

[`Back to top ⇧`](#the-review-page)

***