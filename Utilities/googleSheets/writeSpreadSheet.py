values = [
    [
        # Cell values ...
    ],
    # Additional rows ...
]
body = {
    'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id, range=range_name,
    valueInputOption=value_input_option, body=body).execute()
print('{0} cells updated.'.format(result.get('updatedCells')))