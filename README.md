# fastapi

Learning about making API with Python (FastAPI)

This is me learning about making an API with Python from the video down below:
https://youtu.be/0sOvCWFmrtA

I will keep track of my progress here. I am already at 6:49:34. I will continue from here

So what have i learned until now. I think reviewing is needed because i lost on track for weeks now i think.
First of all what is FastAPI. FastAPI from what i have learned is a framework to make RESTful API.
So it's like a place where you handle connecting data from front-end to database.
You make the connection using (GET, POST, DELETE, PUT. ETC)

Dont forget to use virtual env so anything we install is within the venv.

Platform where people can login and post things in.

main.py = Where everything is connected
routers = simply where we put the API we made seperated by the group (user, post)
models = simply the table where we connect it to db to initialize the table.
schemas = we can use schemas for the response of the API // Also to specify how we want to restrict what user input
init = every folder need to have **init** file so they know that the folder is a python folder
utils = place where we place every function that we need to use and can be reused.
database = place where we define a db session.

Progress for each day: (PS: this is not really day one. I must say, i have been so lazy and im trying to change for the better)

Day 1: 6:49:34 - 7:10:10

Day 2: 7:10:10 - 7:39:04 (1 Hour of study)

I get how to authenticate now so only when user login and get the token, it can create post. I dont understand a little bit about what depends is and what oauth2passwordbearer does. But maybe just a guess it specify where the oauth2 should be??? well thats what i get today.

Day 3: 7:39:04 - 8:21:30 (1 Hour 30 Minutes of study)

So in oauth2, we use the get_current_user function to literally get the current user in which we query the thingies there.

I also understand that postman has environment, So we can set up a variable with values inside and everytime we change the environment, it will get that value for what we set up in the environment.

I got an idea of making a really cool application. So from this video, i got some really interesting idea when the teacher inside the video said that it doesnt make sense to make an application in which other people can delete your own post and BOOM IT CAME TO ME. It actually make sense. So the idea i got is, i can make an application where each user has its own account of course, but at that single moment of time. they can post anything they want, something like video, or anything, and in 5 minutes, the video or post that has been posted, can actually be deleted by another user. Then i can make a leaderboard on video that exist the longest. that would be fun. I know this idea is pretty absurd but i really think that it can be fun. Where u can always consume new video, post, and everything live straight up from the person. Its like instagram but it leaves no trace. You can gain followers and stuff. But this is just for like people who wants to know about your daily life or something. 5 minutes in and boom the video is gone. No trace. With this, we will have no problem on not having enough storage for everyone. IDK i just think of some random stuff. I imagine a post where someone pleaded to having their post not deleted for the longest time. It would be impossible man. Thats enough wandering of.

So what i learn today is also how to connect each post to each user. Well thats logical... OR IS ITTTTT MEUEHHEHEHEHE. NO enough. So yeah i learn that its easy to connect user to each post just by some simple foreign key usage. And thats it. Im gonna go offline now. See you tomorrow, or i guess today (in my place its 00:08 AM).

Day 4: 8:21:30 - 8:53:56 (49 minutes of study)

Man im really tired right now, have been doing my paper for 8 hours, well idc im still gonna study.

I am just really tired today really. What do i learn today? umm... I think its about, okay its hard to focus because im really tired. I learn about restraining other people on deleting and updating other people's post. and then clean up some code. And also i learn about this ? thing inside a web. I forgot what its called but you can filter something based on it. Thats all i learn today i guess. Oh and i can also retrieve the information of the post owner just from the post. Thats all. See you tomorrow

Day 5: 8:53:56 - 9:21:20 (40 minutes of study)

Man im not tired today but its 23:01 now, im gonna study.

So today i learn about making environment, okay i put my password inside github, idk if im dumb or not but i think yes i am dumb for putting that in, but come on, who knows me at this point? i dont think anybody see my repo xdd so its fine. i just change it, idk if theres like changes history which people can see or not and see my password. Well maybe i will figure it out in the future. Thats what i learn today. Its not much but man, its something yeah? see you tomorrow i guess.

Day 6: 9:21:20 - 9:52:40 (50 minutes of study)

Hello its 17:31 now, im gonna study now

So today its vote model. I already make it the vote model, and yeah its not much, i only study for 40 minutes again, well better than nothing right? IDK if i can study tomorrow or not. i will study if i can. See you tomorrow or maybe later idk

Day 7: Im preparing to go home so i cant study today. Im really sorry. Im really sorry... I will make it up tomorrow. I promise. I need to pack my things, I will study with my phone, i will watch youtube video regarding other computer science to make it up. See you tomorrow

Update (Written on day 9): I learn about dynamic programming for 1 hour 30 minutes on my phone.

Day 9: 9:52:40 - 10:35:00 (1 Hours 45 minute of study)
I skipped day 8, im really sorry. Im gonna study today. I got a reason for it. I am really tired because i just got home and i sleep pretty early. Its 14:42 now, i will study at 15:30.

I learning about join in SQL right now, might as well try to understand all join because why not.

1. Inner Join = simply AnB Some like 2 circle but only the middle is filled.
2. Left Join = simply AuB` like 2 circle but only the left and middle part is filled
3. Left Outer Join = simply AnB` like 2 circle but only the left is filled
4. Right Join = Reverse of Left Join
5. Right Outer Join = Reverse of Left Outer JOin
6. Full Outer Join = All filled, So all will be listed but the part where there is not match will be blanked

Okay stop right there. I learn about the SQL Join thingies again and i found somethings wrong from my previous note. So the difference between inner and outer, Inner only contains something that is totally the same and outer contains everything inside the said table and if there no same value, then the table will be filled as null. So dont mind the previous note.

New Notes

1. Inner = Take everything that has same value from the connected table
2. Outer = Take everything even if they got no same value, The one with no value on the other side will be filled as null.

I also learned how to query join using sqlalchemy.

Day 10: 10:35:00 - 11:14:28 (1 Hour of study)

Its 17:52 now and im gonna study now. Todays alembic day.
I learn about alembic, pretty much i guess. The most important thing is alembic revision and alembic upgrade / downgrade

So thats it see you tomorrow. Oh and also the alembic is on another file, i need to know how to actually push something with git ignore. I will do that tomorrow. See you.

Day 11: 11:14:28 - 11:34:40 (1 Hour of study)

Its 21:10 now and im gonna study at 21:30.
OH NO MAN, the video teach me how to track changes to git, but man i already check the thingies and now its not repairable, or i guess it still is but i just need to make a new repo i guess. So, see you in the new repo xddd. So long. oh wait now it works?? or idk. UMM let me try to make it so i dont need to make a new repo. I already made a new repo but if i can, i will use the repo before

Umm okay, its to complex and time wasting. Im just gonna keep it this way and i guess i will only commit on the fastapi workspace git in which fastapi2 is the thingies, what i still dont understand is, i still have the **pycache** file in the new git? even tho i already put gitignore. nah well. AND MY VENV FILE IS STILL ON THE GIT??? wait i really need to fix this.

Okay everything is fixed and i fixed everything in a brute force way. I think im gonna stop for now. I know today i dont learn to much, Only learned about CORS (Cross-Origin Resource Sharing) which simply from my understanding allow us to make the request from another website with console.

Just testing...I dont understand why this dont work
