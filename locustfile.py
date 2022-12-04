from locust import HttpUser, task
import random

# locust  -L DEBUG --logfile lc.log -f ./locustfile.py
# http://localhost:8089


class LocustTests(HttpUser):
    primeSamples = (412, 523523, 85927, 523897, 95115,
                    234962325, 9823572398, 23672306230986)

    # @task
    # def primeEndpoint(self):
    #     self.client.get(f"/prime/{random.choice(self.primeSamples)}")

    @task
    def invertImageEndpoint(self):
        rand = random.randint(1, 5)
        with open(f"./testImages/test{rand}.jpg", "rb") as imageFile:
            print(imageFile.read())
            self.client.post(
                "/picture/invert2/", files={"file": ("filename", imageFile, "image/jpeg")})

    # @task
    # def loginEndpoint(self):
    #     self.client.get(f"/prime/{random.choice(self.primeSamples)}")
