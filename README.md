# LEETCinematics

**LEETCinematics** is a tool that allows you to make **cinematics/trailers** from your [LEET.CC](https://leet.cc) server. No more manual moves! This tool will allow you to **define the positions** you want to pass through, then it will automatically generate a **smooth path**.

## How to use it

In order to be able to use this tool, you must have **MadCommands** plugin on your server. Then all you have to do is to copy all the commands in the [LEETCinematics.madcmd](LEETCinematics.madcmd) file to your server (directly or with the help of a [RCON tool](https://edroid.me/projects/rcon++/beta/)). You will find below the user guide and you can use the command ```/lcin help``` to see all the features.

### User Guide
You want to use the tool on your server? Simply follow these steps:
 1. **Define** the points you want to pass through by positioning yourself there and using the command ```/lcin pos```. **Be careful**, where you look is also important!
 2. If you **set a wrong position**, you can reset the set using ```/lcin reset```. You must then redefine each position **from the beginning**.
 3. Once **all the positions** have been defined, choose a **travel time** (in seconds) and use the ```/lcin play <time>``` command to **start the travelling**. Don't forget to start your **screen recorder** first!
 4. When **the travelling is over**, you can save your video file and use it as you wish! **Don't forget** to use ```/lcin reset``` to reset the positions for the next recording!

## Set up your own API server

You are an **advanced user** and you want to set up **your own API server**? Here are some important elements to consider.

### ① Prerequisites
In order for the API server to work properly, you must have **Python 3.6** installed on your machine. Your machine must also be **accessible on the Internet**.

### ② Configuration
In order to modify parameters on the API server, you will need to **edit the code**. You will need to modify the **MadCommands code** on **line 1** to add the **API address** as follows:
```
let %apiURL% = \"<server adress>/api\"
```

### ③ Starting the server
The API server can work in **two different ways** depending on your needs:
- If you use the **Flask** framework, you can use the [FlaskApp.py](FlaskApp.py) file.
- Otherwise, the [HTTPServer.py](HTTPServer.py) code can be run directly **without any other installation**.

## License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.