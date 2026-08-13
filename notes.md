# Notes

The curse of King Midas meant, everything he touched turned into gold -- a convenient ability that promissed enourmous wealth, but soured quickly once Midas began to touch other humans, as they too promptly turned to gold. Similarly, coding agents turn data and research questions into elaborate analyses and visualizations. However, since they copy everything they touch onto their own servers, when they touch sensitive human data they quickly turn any reserach project into a data breach. 
[why we do not want coding agents to access sensitive data]

so here i would like to outline the idea i have with this project for using coding agents like codex or claude for research that involves sensitive data that these agents should not see because "seeing" in their case means sending the data to their servers which is in and of itself not in line with the agreeements we enter with our participants and even if there are no agreements, like when we do online data scraping, then it is also not ethical to do that becaue we are copying data that is maybe copyright protected or it may contain privacy relevant details, that are inadvertently online because someone else has uploaded them or the person uploading them was not aware of the potential implications of that action. Regardless, we cannot just send data willy nilly to LLM servers because we cannot trust these companies to deal with the data responsibly, we in turn have to adhere to a high standard. And it is possible to do so while making use of coding agents that offer a lot of benefits to us working within computational social science. Among these benefits are that by using an agent to code things we can benefit from the very broad competence of the agents, allowing the utilization of API's and libraries that we are not or only little familar with feasible. Furthermore, these agents can make the publication of code much easier, since a central element of the workflow with them is validating that the code runs as expected, which essentially requires bringing the code into a reviewable state just for one's own sake. Additionally, the process proposed here divides code from data, thus allowing the sharing of the code even if the data itself cannot be shared, as it is often the case in social science. 

So, what is the basic process?
The core issue is that we want to utilize a very capable coding agent but we have to be really careful with it because everything the coding agent touches lands on third-party servers which, we do not want. We therefore, have to prevent the agent to 1. touch our data (if it is sensitive) 2. prevent the agent from going through our computer since, there likely is private and sensitive data as well. This is more difficult than it sounds, becasue the agent on the one hand is extremely skillfull and fast in navigating the file systems of modern operating systems and very very eager to please. So eager to please in fact, that it may do things that we might not want it to do. Especially, if we give it tasks that contradict and it must disappoint one expectation we have of it, it can easily be broad to act in ways we do not want. for exmaple, if we give it access to just one folder and tell it to write a data visualization code to visualize some data in the folder, but overlook that we have put the data in a different folder and the agent knows of it, then the agent is forced to either disappoint our expectation that it writes the code or disappoint that it will only access data in the given folder. This is a prime condition for the agent doing things it should not do and thereby sending data to servers where the data does not belong. 

central issue: everything it looks at is already sent to the external server. So, it cannot stop itself before it looks at something forbidden. 

In a way i feel like this conundrum reminds me of the King Midas myth. While the king was enormously wealthy and everything he touched turned into gold, coding agents are enormously competent coders but everything they touch turns into a data breach.

In this tutorial we explain how we can use "king midas" anyway and keep his golden hands from creating data breaches. 

The idea behind it is that we will use two separated systems: One contains the coding agent and exclusively files that are ok for the agent to touch -- the gold system, and a second system that contains the data that we want to analyze, the vault system. Once this is setup, we can have the coding agent in the gold system write the code, transfer the code, and only the code, from the gold system to the vault system, where it then is executed on the real data. 

None of these steps is particularly difficult. the challenge lies in the combination of several individual software solutions that need to be brought together in order to facilitate this solution. Need are the following:
- two computers, ideally one regular device to mainly work on and a secure remote server that contains the data and allows code execution (technically, the same solution can be arranged on a single device, but that can be more difficult to keep an overview over and increases the chances of mistakes, data breaches)
- Python or R (others work too)
- Docker Sandbox to isolate the gold system from the device it is running on
- a coding agent like ChatGPT's Codex or Claude Code to write the code on the gold system
- git and a GitHub account (or alternatives, but this tutorial uses Github)


## The Basics
Generally
- you need a github account (link to github)
- you needa Docker log-in, for which you can authenticate yourself with your github account
- you need access to a docker sandbox supported coding agent (https://docs.docker.com/ai/sandboxes/agents/) 

On the device with the gold system
- you need to install the free to use (log-in required) docker sandbox (https://docs.docker.com/ai/sandboxes/get-started)
- then authenticate your agent (find the one you want to use here: https://docs.docker.com/ai/sandboxes/agents/)


