### Welcome to my CodeClan Python Project.

#### The brief:

#### Gym

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

#### MVP

- The app should allow the gym to create and edit Members
- The app should allow the gym to create and edit Classes
- The app should allow the gym to book members on specific classes
- The app should show a list of all upcoming classes
- The app should show all members that are booked in for a particular class

#### Inspired By

[Glofox](https://www.glofox.com/club-solution/), [Pike13](https://www.pike13.com/pike13-scheduling-software-demo)

#### Possible Extensions

- Classes could have a maximum capacity, and users can only be added while there is space remaining.
- The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
- The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.

### Setup

Before you can run this code repository on your own machine you will need to:
download the whole folder called project_code.

Then change directory so you start inside project_code. You should see the console.py file as well as run_tests.py and app.py (run this file if you want to start with an empty database).

On the command line you will need to run a few things to get going:-

- createdb gym_emulator
- psql -d gym_emulator -f db/gym_emulator.sql
- python3 console.py
- You will see this response in the command line but nothing to worry about.
    (This is your error message:  no results to fetch
     This is your error message:  no results to fetch)
- flask run

Then copy/paste the IP address of the local host that flask started for you. Something like http://127.0.0.1:4999. You can also right click on the address and Open Link.

You should see the homepage of the gym_emulator. The navigation bar at the top will take you to Sessions to see Gym Sessions available, Show details and Add new session. To edit a current session, follow the Show details link and then Edit session. A form will appear already populated and ready to be edited. Click Update session to save the changes. You will be redirected to the Sessions page.

The same format is followed by the Members nav link.

The Bookings link shows a list of all current bookings. Click Add new booking to be directed to a form populated with sessions available in a drop down menu and the same for all members. Chose both then click Add booking. You will be redirected to the full listing of bookings.

To view the list of members booked on a specific session, return to the Gym sessions page and show details of the session. A list of members will be shown.

Further work is needed to make use of the premium member and premium session attributes I have added and I would like to be able to deactivate and re-activate members and sessions.
