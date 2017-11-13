# PURPLEMIND Muse 

MUSE is the engine behind PURPLEMIND it powers the Web App and hooks up to the clients [OSX, iOS & Android] via RESTful API. 
## Development 

PURPLEMIND Mandates that all developers use the PyCharm IDE for local Django Development, because we also rely on web-tech like Angular, it makes sense to make use of cross-compatability between JetBrains WebStorm & PyCharm IDE's. 
Always test locally, before deploying to staging. 

> Any fool can write code that a computer can understand, Good programmers write code that humans can understand. 
##### -------> We work with lean, efficient & well documented codebases. 

## Deploying

Muse is deployed to Heroku-Staging automatically after a push to the Master Branch. [ Codeship will perform various Continuous Integration Tests on your code before it passes deployment ] 

![](https://purplemind.nyc3.digitaloceanspaces.com/Screen%20Shot%202017-11-13%20at%2015.34.26.png)

You may wish to read about: 
 - Using Git from [the command line](https://github.com/codepath/ios_guides/wiki/Using-Git-with-Terminal) 
 - Using Git [with Pycharm](https://www.jetbrains.com/help/pycharm/using-git-integration.html)
 
Always format commit messages as such
```sh
cd ../purplemindMUSE
git commit -m "## 0.0.3.4 ALPHA   - Change - Change - Fix - Change - Etc " 
git push
```
 #### Staging
Staging is accesible from: development-env.purplemind.io and it is restricted to developers who are a member of the PURPLEMIND Github Organisation. 

**When successfully deployed, PM Github bot will ping slack**
![](https://purplemind.nyc3.digitaloceanspaces.com/Screen%20Shot%202017-11-13%20at%2015.36.12.png)
#### Production
Prod resides on 
```sh
app.purplemind.io
```
> Staging changes can be promoted to the production environment via Heroku's web interface or CLI. Permissions required. 

