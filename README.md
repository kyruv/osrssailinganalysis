# A quick and dirty analysis of the twitch users that chatted during the sailing portion of 'The Summer Summit' twitch stream

![Estimation of Twitch User Sentiment During the Sailing Portion of 'The Summer Summit!'](https://github.com/kyruv/osrssailinganalysis/assets/109682849/875f5faf-3a47-4a99-92ba-da7175d9f225)


# Summary

Of the 2817 users that wrote in twitch chat during the time window, I classified 880 of them as "for sailing", 564 of them as "against sailing", and 1373 as "unsure/neutral/unrelated comments". The above chart ignores the users I was unsure about.

# Details

Using, https://github.com/lay295/TwitchDownloader I downloaded the chat messages sent for this video https://www.twitch.tv/videos/1903147447 between the timestamp 1hr 47min and 2hr 16min which is the time that sailing was the main topic of discussion. I then tried to figure out how many commenters for or against sailing using a list of rules to match keywords (see osrssailing.py). Its by no means perfect but I do think gives a fairly decent representation. I provided all the different classifications that I made as well as the code I used and the raw comments. Feel free to poke through and manually classify all of them which would be the most accurate thing.

