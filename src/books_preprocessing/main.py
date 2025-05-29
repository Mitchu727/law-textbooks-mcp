import pymupdf
import re
from src.utils import get_books_path
import json

def replace_unsupported_characters(text):
    return text.replace('\xa0', ' ').replace('\xad', '-').replace('\u2002', ' ').replace('  ', ' ')

def load_content(doc):
    pages = []
    for page in doc[book["content"]["start"]:book["content"]["end"]]:
        text = page.get_text()
        text = replace_unsupported_characters(text)
        text += "PAGE_END"
        pages.append(text)
    return pages

def load_part(doc, book, part):
    part_text = ""
    for page in doc[book[part]["start"]:book[part]["end"]]:
        text = page.get_text()
        part_text += text
    return replace_unsupported_characters(part_text)

def preprocess_table_of_contents(doc, book):
    table_of_contents = load_part(doc, book, "table_of_contents")
    table_of_contents = re.sub(r'(\.)+\t(\n| |X)', " ", table_of_contents)
    table_of_contents = re.sub(r'\n.*\nSpis treści', " ", table_of_contents)
    table_of_contents = re.sub(r' +', " ", table_of_contents)
    with open(book["path"] / "table_of_contents.txt", "w", encoding="UTF-8") as f:
        f.write(table_of_contents)

def preprocess_subject_index(doc, book):
    subject_index = load_part(doc, book, "subject_index")
    with open(book["path"] / "subject_index.txt", "w", encoding="UTF-8") as f:
        f.write(subject_index)

def preprocess_content(doc, book):
    content = load_content(doc)
    pages_json = []
    for i, page in enumerate(content):
        if i % 2 == 0:
            page_content, paragraph_ids = parse_odd_page(page)
            page_dict = {
                "number": i+1,
                "page_content": page_content,
                "paragraph_ids": paragraph_ids,
            }
            pages_json.append(page_dict)
        elif i % 2 == 1:
            page_content, paragraph_ids = parse_even_page(page)
            page_dict = {
                "number": i+1,
                "page_content": page_content,
                "paragraph_ids": paragraph_ids,
            }
            pages_json.append(page_dict)
        print(i)

    with open(book["path"] / "content.json", "w", encoding="UTF-8") as f:
        json.dump(pages_json, f)

    # with open(book["path"] / "content.txt", "w", encoding="UTF-8") as f:
    #     f.write(content)


def parse_odd_page(page_content):
    page_content = re.sub("[0-9]+\nNb\..*\n","", page_content)
    page_content = re.sub("Nb\..*\n(Rozdział.*)",r"\1", page_content)
    page_content = re.sub("§.*\nPAGE_END", "PAGE_END", page_content)
    paragraph_ids = re.search("([0-9]+\n)*PAGE_END", page_content).group()
    paragraph_ids = paragraph_ids.replace("\nPAGE_END", "").split("\n")
    page_content = re.sub("([0-9]+\n)*PAGE_END", "", page_content)
    return page_content, paragraph_ids


def parse_even_page(page_content):
    page_content = re.sub("[0-9]+\n.*\nNb\..*\n", "", page_content)
    page_content = re.sub("Nb\..*\n(Rozdział.*)",r"\1", page_content)
    paragraph_ids = re.search("([0-9]+\n)*PAGE_END", page_content).group()
    paragraph_ids = paragraph_ids.replace("\nPAGE_END", "").split("\n")
    page_content = re.sub("([0-9]+\n)*PAGE_END", "", page_content)
    return page_content, paragraph_ids

book_one = {
    "path": get_books_path() / "RadwanskiCzescOgolna",
    "table_of_contents": {
        "start": 7,
        "end": 20
    },
    "subject_index": {
        "start": 453,
        "end": 462
    },
    "content": {
        "start": 27,
        "end": 451
    }
}


book_two = get_books_path() / "raw" / "Radwański Zobowiązania Część Szczegółowa.pdf"

book = book_one
doc = pymupdf.open(book["path"] / "book.pdf")
preprocess_table_of_contents(doc, book)
preprocess_subject_index(doc, book)

preprocess_content(doc, book)
