from invoke import task

@task
def startApp(c):
    c.run("flask --app j4e --debug run --host=0.0.0.0")
    
@task
def gitLog(c):
    c.run("git log --all --decorate --oneline --graph")
    
@task
def shutdown(c):
    c.run("sudo shutdown -r now")