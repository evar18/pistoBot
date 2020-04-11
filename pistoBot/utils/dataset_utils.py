import logging
from typing import List, Tuple

import nltk
import numpy as np


def read_dataset(file_path: str, file_encoding: str = "utf-8") -> str:
    text = open(file_path, 'r', encoding=file_encoding).read()
    return text


def text_parser(text: str, lowercase: bool) -> str:
    # TODO enhance the parser (auto_nlp?)
    if lowercase:
        text = text.lower()
        logging.debug("Text reduced to uncased")
    return text


def text_tokenizer(text: str, level: str) -> List[str]:
    if level == "word":
        text = nltk.word_tokenize(text, language='italian', preserve_line=False)  # TODO nltk don't preserve \n char
        logging.debug("Text tokenized at <word> level")
    else:
        logging.debug("Text tokenized at <char> level")
    return text


def create_vocabulary(text_tokenized: List[str]) -> Tuple[dict, np.ndarray]:
    text_tokens = sorted(set(text_tokenized))  # text_chars = List
    token2idx = {u: i for i, u in enumerate(text_tokens)}
    idx2token = np.array(text_tokens)
    return token2idx, idx2token


def print_input_batch(dataset_ml, idx2token: np.ndarray):
    logging.info("----------------------------")
    logging.info("[Example of ML batch]")
    logging.info("train --> label")
    for x_batch, y_batch in dataset_ml.take(1):
        # Take one batch
        for idx, (batch_el_x, batch_el_y) in enumerate(zip(x_batch, y_batch)):
            logging.info(f"{idx} | {idx2token[batch_el_x.numpy()]} --> {idx2token[batch_el_y.numpy()]}")
    logging.info("----------------------------")