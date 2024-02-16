# tests

Please run the test.py files in the Test folders.


# API Stress Test

To run the test:

-- open the `tests` project folder in VS Code

-- `Ctrl + J` to open the terminal

-- in the terminal, type `cd API_Stress_Test` to get into the actual project folder

-- once in the folder, and you have something like this `C:\your_folder\your_folder\tests\API_Stress_Test>`, then run this command `locust`

-- you will see something like this 👇🏽

![Alt text](<API_Stress_Test/img/start_locust.png>)

-- once you got a response with a port above, then go to your browser and search `http://localhost:8089/`

![Alt text](<API_Stress_Test/img/locust_start_page.png>)

-- you'll get above page

-- there you can fill in the details you want; amount of users, the rate at which you want the endpoints to get hit in seconds, then the host, which is `https://api2.painelconstru.com.br`, then you can start swarming.

-- the rest should be easy and straightforward from there.


# Tests With Authorized User

-- to run the unauthorized version, open the terminal and `cd` into the `tests_with_authorized_user` directory, then type `locust -f locustfile.py` and run.

-- to run the authorized version, open the terminal and `cd` into the `tests_with_authorized_user` directory, then type `locust -f test_authorized.py` and run.

-- once you got a response with a port number, then go to your browser and search `http://localhost:8089/`