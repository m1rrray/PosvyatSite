import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from registration.models import Registration
from resettlement.models import Resettlement
from transfer.models import Transfer

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = '1w5u-71ezRExkVrox6hX1-DNx_lEV4AJ7YdAO1b74HWs'


def authorize_google():
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    service = build("sheets", "v4", credentials=credentials)
    sheets = service.spreadsheets()

    return sheets


def save_transfer_to_google():
    sheets = authorize_google()

    data = Transfer.objects.all()

    range_to_update = f"transfer!A2"

    data_to_update = []
    for transfer in data:
        data_to_update.append([
            transfer.surname,
            transfer.name,
            transfer.patronymic,
            transfer.email,
            transfer.vkurl,
            transfer.tgurl,
            str(transfer.phone)
        ])

    body = {'values': data_to_update}
    sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=range_to_update, valueInputOption="USER_ENTERED",
                           body=body).execute()


def save_registration_to_google():
    sheets = authorize_google()

    data = Registration.objects.all()

    range_to_update = f"registration!A2"

    data_to_update = []
    for registration in data:
        data_to_update.append([
            registration.surname,
            registration.name,
            registration.patronymic,
            registration.email,
            registration.vkurl,
            registration.tgurl,
            str(registration.phone),
            registration.birth_date.strftime('%Y-%m-%d'),
            registration.sex,
            registration.univer,
            registration.faculty,
            registration.program,
            registration.year,
            registration.group,
            registration.transfer,
            registration.health
        ])

    body = {'values': data_to_update}
    sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=range_to_update, valueInputOption="USER_ENTERED",
                           body=body).execute()


def save_resettlement_to_google():
    sheets = authorize_google()

    data = Resettlement.objects.all()

    range_to_update = f"resettlement!A2"

    data_to_update = []
    for resettlement in data:

        names = []
        for item in resettlement.people_custom:
            names.append(item["FIO"])

        data_to_update.append([
                                  resettlement.surname,
                                  resettlement.name,
                                  resettlement.patronymic,
                                  resettlement.vkurl,
                                  resettlement.tgurl,
                                  resettlement.year,
                                  resettlement.program,
                                  resettlement.group,

                              ] + names)

    body = {'values': data_to_update}
    sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=range_to_update, valueInputOption="USER_ENTERED",
                           body=body).execute()
