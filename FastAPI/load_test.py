from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    
    def on_start(self):
        self.client.post("/api/users/login/", {
            "username": "username",
            "password": "password"
        })
    
    @task
    def index(self):
        self.client.get("/")
        self.client.get("/profile")
        
    @task
    def about(self):
        self.client.get("/about/")

    @task
    def home(self):
        self.client.get("/home")

    @task
    def competition(self):
        self.client.get("/competition")
    
    @task
    def refer(self):
        self.client.get("/refer")

    @task
    def course(self):
        self.client.get("/courses/1")