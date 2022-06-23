# User Research and Stories

## User Research:

- https://docs.google.com/spreadsheets/d/13kh966aGOydhDeBK_Q5uxwu9TM3_mHhM9NCqLyIA8l4/edit?usp=sharing

- https://www.notion.so/astrocyte/SlashTag-635bcde1ee9049d18ee685cb9710f801

## User Stories:

These are the core tasks that user completes

### Annotate Data within Slack app

1. Install SlashTag app
2. Create a channel (or use an existing channel)
3. write `/tag project-name <file> @users #channel`
4. `/tag` will open a modal to allow you to tag a file
5. SlashTag will send a notification to the users in the channel
6. Each user will type `/tag` to see the private message to tag. Each model will have the tagging information
7. If user tags `/tag status` will be sent to the channel the list of users tagged
8. `/tag export` will export the tagged data to a file in slack to be downloaded

### Create an annotation project from python

1. Install SlashTag app
2. `pip install slashtag`
3. call `/tag api` to get the api key and show 'hello world' example.

```
import slashtag
st = slashtag(api_key)
project = st.create_project(*args, **kwargs)
# project = st.get_project(project_name)
project.to_slack(df)
print(project.status())
df2 = project.get_labels()
# update model with df2
```

### Data Enrichment: Subscribe to message in a slack channel

Could also use a webhook to get the data, zappier integration or n8n integration

1. Install SlashTag app
2. In the channel with messages, apply the filter `has:tag` or `from:@user`
3. Write `/tag <filter> @users #channel --since=2d` (by omiting the channel, it will default to the channel you are in, requires filters)
4. SlashTag will send a notification to the users in the channel that the subscription is applied
5. Additional notifications will be sent to users in the channel when a new batch of messages is ready to be tagged.

### Model Performance Monitoring

Production Models send data to SlashTag to monitor performance

1. Install SlashTag app
2. `pip install slashtag`
3. call `/tag api` to get the api key and show 'hello world' example.

```
import slashtag
st = slashtag(api_key)
project = st.create_project(*args, **kwargs)
# project = st.get_project(project_name)

# Perhaps don't send all to slack
have_a_human_check = random.random() < 0.01

# Samples as a function of confidence
# hard code curve
# merge two beta distributions with peaks at 0.2 and 0.8 respectively.  Additionally merge with variance curve `p*(1-p)`. to further attenuate the tops of the curves and bulk up the center of the distribution.

if project.send_sample(confidence):
    project.prediction_to_slack(item: dict, label:SlackLabel, confidence:float)

# View performance curves
stats = project.stats()

# also view in channel by calling `/tag stats`
```
