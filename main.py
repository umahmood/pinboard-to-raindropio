import argparse
import pathlib
import json
import csv


def write_to_csv(rows: list, filename: str):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_headers = ["folder",
                           "url",
                           "title",
                           "description",
                           "tags",
                           "created"]
            spamwriter = csv.writer(csvfile,
                                    delimiter=',',
                                    quoting=csv.QUOTE_NONNUMERIC)
            spamwriter.writerow(csv_headers)
            for row in rows:
                spamwriter.writerow(row)
    except PermissionError as e:
        print(f"permission denied when saving to {csv_file}.")


def read_pinboard_json_file(filename: str):
    try:
        with open(filename, 'r') as reader:
            bookmarks = json.loads(reader.read())
            return bookmarks
    except FileNotFoundError as e:
        print(f"file {pinboard_bookmarks} not found.")


def convert_json_to_csv(bookmarks: list, collection: str):
    # preserve the to read bookmarks list by adding a 'toread' tag
    for bookmark in bookmarks:
        if bookmark['toread'] == 'yes':
            bookmark['tags'] = bookmark['tags'] + " toread"

    folder = collection if collection else "Pinboard"
    rows = []

    def format_tags(tags):
        return ', '.join([x for x in tags.split(" ") if x])

    for bookmark in bookmarks:
        href = bookmark['href']
        title = bookmark['description']
        extended = bookmark['extended'].replace(
            "<blockquote>", "").replace("</blockquote>", "")
        tags = format_tags(bookmark['tags'])
        created = bookmark['time']
        rows.append([folder, href, title, extended, tags, created])

    return rows


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--pinboard",
        type=str,
        required=True,
        help="Path to Pinboard backup JSON file")

    parser.add_argument(
        "--csv",
        type=str,
        required=True,
        help="CSV file to write bookmarks too (include .csv extension)")

    parser.add_argument(
        "--collection",
        type=str,
        required=False,
        help="The collection (folder) where the bookmarks should be placed")

    args = parser.parse_args()
    bookmarks = read_pinboard_json_file(args.pinboard)
    rows = convert_json_to_csv(bookmarks, args.collection)
    write_to_csv(rows, args.csv)


if __name__ == "__main__":
    main()
