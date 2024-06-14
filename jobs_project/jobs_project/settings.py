BOT_NAME = 'jobs_project'

SPIDER_MODULES = ['jobs_project.spiders']
NEWSPIDER_MODULE = 'jobs_project.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'jobs_project.pipelines.JobsPipeline': 300,
}
