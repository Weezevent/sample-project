# Sample Project for technical test

## All useful commands

### Build the project
  ```shell
  docker compose build
  docker compose --rm run web python manage.py migrate
  ```

### Launch
  ```shell
  docker compose up web
  ```

### Migrations
  ```shell
  docker compose --rm run web python manage.py makemigrations
  ```

### Unit test
```shell
All tests
docker compose run pytest sample_project

One test file 
docker compose run pytest sample_project/events/tests/test_views.py

One specific test in a file
docker compose run pytest sample_project/events/tests/test_views.py::test_list_event
```