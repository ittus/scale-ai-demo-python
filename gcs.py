import os
from os.path import join, dirname
from dotenv import load_dotenv
import scaleapi

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_TOKEN = os.environ.get("API_TOKEN")

client = scaleapi.ScaleClient(API_TOKEN)

## create project
# project = client.create_project(project_name="test_project_2", type="imageannotation", params = {
#     "instruction": "This is a test project"
# })
# print(project)

## Create task

tasks = [
    "gs://books-jp/bulksplash-ananogrey-HESw7t6aQqI.jpg",
    "gs://books-jp/bulksplash-aquintero210-xvlzYmY3Tz8.jpg",
    "gs://books-jp/bulksplash-artcoastdesign-oJ_5bY6KCag.jpg"
]

for task in tasks:
    res = client.create_imageannotation_task(
        project='test_project_2',
        instruction="Draw a box around each baby cow and big cow.",
        attachment_type="image",
        attachment=task,
        geometries={
            "box": {
                "objects_to_annotate": ["Engineer Book", "Social book"],
                "min_height": 10,
                "min_width": 10
            }
        }
    )
    print(res.status, res.response)
