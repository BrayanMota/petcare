from decouple import config

APP_ID = "pet_care"

ELASTIC_APM = {
    "SERVICE_NAME": "pet_care",
    "SERVER_URL": config("ELASTIC_APM_SERVER_URL"),
    "DEBUG": config("DEBUG", default=False, cast=bool),
    "ENVIRONMENT": config("ENVIRONMENT", default="desenvolvimento"),
}