#!/data/data/com.termux/files/usr/bin/bash

# Update dan upgrade package
echo "Mengupdate dan mengupgrade package..."
pkg update && pkg upgrade -y

# Install Python dan pip
echo "Menginstall Python dan pip..."
pkg install python -y
pkg install python-pip -y

# Install dependencies lainnya
echo "Menginstall dependencies lainnya..."
pkg install git -y

# Menjalankan script Python
echo "Menjalankan script Python..."
python script.py
