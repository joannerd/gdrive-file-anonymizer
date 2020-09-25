import argparse, hashlib, json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def get_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', help='file name to search in Google Drive', type=str, default='')
    parser.add_argument('-t', '--trashed', help='optional y/n depending on whether to search in the trash bin', type=str, default='n')

    print(parser.format_help())
    return parser.parse_args()


def configure_gdrive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive


def fetch_gdrive_files(drive, query, is_trashed):
    files = drive.ListFile({'q': f"title contains '{query}' and trashed={is_trashed}"}).GetList()
    return files


def anonymize_file_and_download(drive, files):
    logs = {}
    state = 1
    for file in files:
        if 'fileExtension' in file and 'id' in file and 'title' in file:
            anonymized_file = drive.CreateFile({'id': file['id']})
            anonymized_file.GetContentFile(f"{str(state)}.{file['fileExtension']}")
            logs[state] = file['title']
            state += 1
    return logs


def upload_rename_logs(drive, logs):
    file_rename_logs = drive.CreateFile({'title': 'file-rename-logs.txt'})
    json_logs = json.dumps(logs)
    file_rename_logs.SetContentString(json_logs)
    file_rename_logs.Upload()


if __name__ == '__main__':
    args = get_cli_args()
    print(args)
    drive = configure_gdrive()
    is_trashed = True if args.trashed.lower() == 'y' else False
    files = fetch_gdrive_files(drive, args.query, is_trashed)
    logs = anonymize_file_and_download(drive, files)
    upload_rename_logs(drive, logs)

