#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
download_dataset.py

Script to download the 'yasserh/wine-quality-dataset' from Kaggle using
kagglehub and move it into the 'data/' folder at the project root.

Author: Pierre Fromont Boissel
Date: 2025-04-11
"""

import kagglehub  # type: ignore
import shutil
import os


def download_and_move_dataset() -> None:
    """
    Downloads the 'yasserh/wine-quality-dataset' from Kaggle using kagglehub and moves all files into the 'data/' directory at the project root.

    This function performs the following steps:
        1. Downloads the dataset using kagglehub.
        2. Ensures the 'data/' directory exists at the project root.
        3. Copies all files from the downloaded dataset directory to the 'data/' directory.

    Side Effects
    ------------
    - Creates the 'data/' directory at the project root if it does not exist.
    - Copies files from the downloaded dataset to the 'data/' directory, potentially overwriting files with the same name.
    - Prints progress and status messages to the console.

    Raises
    ------
    OSError
        If there is an error creating the directory or copying files.
    kagglehub.KaggleHubError
        If the dataset download fails (see kagglehub documentation for details).

    Examples
    --------
    >>> download_and_move_dataset()
    📥 Downloading dataset...
    ✔ Copied: WineQT.csv
    ...
    ✅ Dataset files are now in: /path/to/project/data

    Notes
    -----
    - The function is intended to be run as a script or called directly in Python code.
    """

    # Download the dataset
    print("📥 Downloading dataset...")
    downloaded_path = kagglehub.dataset_download("yasserh/wine-quality-dataset")

    # Ensure the 'data/' folder exists at the project root
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
    os.makedirs(data_dir, exist_ok=True)

    # Copy all files into 'data/'
    for file_name in os.listdir(downloaded_path):
        src_path = os.path.join(downloaded_path, file_name)
        dest_path = os.path.join(data_dir, file_name)
        shutil.copy(src_path, dest_path)
        print(f"✔ Copied: {file_name}")

    print(f"\n✅ Dataset files are now in: {data_dir}")


if __name__ == "__main__":
    download_and_move_dataset()
