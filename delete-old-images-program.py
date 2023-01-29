import docker
from datetime import datetime, timedelta, timezone
import dateutil.parser

client = docker.from_env()

images = client.images.list()
for image in images:
    # datetime.fromisoformat from Python versions < 3.11 cannot parse the docker timestamp string
    created = dateutil.parser.isoparse(image.attrs["Created"])
    delta = datetime.now(tz=timezone.utc) - created
    if delta < timedelta(days=14):
        print(f"deleting image {image.attrs['RepoTags'][0]}")
        client.images.remove(image.id, force=True)
