from invoke import task

@task
def run(c):
    c.run("flask --app j4e --debug run --host=0.0.0.0")