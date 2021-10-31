# alpha
The purpose of this project is to develop an API using Django that fetches the price of BTC/USD from the alphavantage API every hour, and stores it on postgres. This API has been secured which means that you will need an API key to use it. There should be two endpoints: GET /api/v1/quotes - returns exchange rate and POST /api/v1/quotes which triggers force requesting the prices from alphavantage. The API &amp; DB has been containerized using Docker as well. - Every part has been implemented as simple as possible.The technologies has been used: Celery, Redis or RabbitMQ, Docker and Docker Compose. - The sensitive data such as alphavantage API key, should be passed from the .env

## Required

* Install **the Docker:** **https://docs.docker.com/docker-for-windows/install/ (for Windows) and for other environment https://docs.docker.com/engine/install/**
* **Docker-compose: https://docs.docker.com/compose/install/**

## Steps to Run 
> 1. Download or Clone the Repository:    **git clone https://github.com/aazamrke/alpha.git**
> 2. Go to the Dockerfile change the APIKEY to your APIKEY:    **APIKEY == Your-API-KEY.**
> 3. Run the container: **sudo docker-compose up**
> 4. Create the superuser using this command Run the: **docker exec -it container_id python manage.py createsuperuser**
> 5. Login with username and password.**http://localhost:8000/login**. This will return the access token.
> 6. Request with Bearer token using this endpoint: **http://localhost:8000/api/v1/quotes**
> 7. For the GET and POST request 

## Steps to build the Docker(if it's not build)
>  Build the Docker container by using:   **docker-compose build**

## Screenshot

### 1. **Create API Key**(https://www.alphavantage.co/support/#api-key)
![Screenshot from 2021-10-31 22-15-42](https://user-images.githubusercontent.com/11086459/139596603-5df7e41c-4bdd-4fd7-a84a-f712909ecc46.png)


### 2. **Login Page**

![login]
![Screenshot from 2021-10-31 22-20-42](https://user-images.githubusercontent.com/11086459/139596468-5f98e779-3265-4dd6-bf8e-4348f96f3a00.png)


### 3. **Returning all the data through GET request**

![Screenshot from 2021-10-31 22-50-53](https://user-images.githubusercontent.com/11086459/139596519-6acac14d-3720-48ab-bfd1-7e6dd63e9a71.png)


### 4. **Trigger the data through POST request**

![Screenshot from 2021-10-31 22-26-40](https://user-images.githubusercontent.com/11086459/139596535-3705cea7-de6f-4741-be03-250fd878a037.png)

## Code Screenshots
![Screenshot from 2021-10-31 23-54-27](https://user-images.githubusercontent.com/11086459/139596790-dd66ce01-94f7-4fea-8e83-d5b6fba51be9.png)
![Screenshot from 2021-10-31 23-52-32](https://user-images.githubusercontent.com/11086459/139596801-f885a6c4-98c3-4b38-b862-403944395220.png)
![Screenshot from 2021-10-31 23-52-19](https://user-images.githubusercontent.com/11086459/139596810-2701d563-ca54-4219-bfb6-3c9b5f2cc032.png)
![Screenshot from 2021-10-31 23-52-05](https://user-images.githubusercontent.com/11086459/139596814-bc7ecc17-1f31-4b62-8f85-a29887e789b5.png)
![Screenshot from 2021-10-31 23-51-51](https://user-images.githubusercontent.com/11086459/139596821-7910d7da-ee0f-4cb8-b8db-5f9d148cccc0.png)







## Thank You
