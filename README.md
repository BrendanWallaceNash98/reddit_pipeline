# Reddit Pipeline

In this project, I built a pipeline using the Reddit API to collect data from the r/dataengineering subreddit and then store it in a Redshift database.


I used Airflow to orchestrate two DAGs, one extracting the data from Reddit and one uploading the data into an S3 bucket.

Once in an S3 bucket, I used a Glue Crawler to automate the data transformation and insertion into a Redshift table. In the transformation using the Glue Crawler, I concatenated two columns that had boolean data to consolidate some of what I viewed as less informative data, making for a more concise table.

With the data in Redshift, I am going to look at doing some sentiment analysis and present it on a platform like Google Looker Studio. The idea would be to use it to view emerging technologies and trends.

At the moment the collection only takes posts from the current day and a limit of 100 posts. This is more than enough as the subreddit isn't that fast-moving.

