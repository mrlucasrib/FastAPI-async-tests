from locust import HttpUser, task

class BlockingAsyncUser(HttpUser):
    @task
    def block_call(self):
        self.client.get("/async_blocking")

class NonBlockingAsyncUser(HttpUser):
    @task
    def block_call(self):
        self.client.get("/async_non_blocking")

class BlockThreadUser(HttpUser):
    @task
    def block_call(self):
        self.client.get("/thread_blocking")

class NonBlockingThreadUser(HttpUser):
    @task
    def block_call(self):
        self.client.get("/thread_non_blocking")

class AsyncUser(HttpUser):
    @task
    def block_call(self):
        self.client.get("/async")