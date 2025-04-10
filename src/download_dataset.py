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


def download_and_move_dataset():
    # Download the dataset
    print("📥 Downloading dataset...")
    downloaded_path = kagglehub.dataset_download(
        "yasserh/wine-quality-dataset")

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
