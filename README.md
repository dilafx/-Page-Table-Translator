# EEX5564 Mini Project - Group A: Page Table Translator

This project is a software simulation of an Operating System's memory management unit (MMU). It demonstrates how **Logical Addresses** are translated into **Physical Addresses** using a Page Table.

This project was developed for the **EEX5564 - Computer Architecture and Operating Systems** module at The Open University of Sri Lanka.

## 📋 Project Overview

* **Group:** A (Page Table Translator)
* **Language:** Python 3
* **Page Size:** 1 KB (1024 Bytes)
* **Virtual Memory:** 8 Pages
* **Physical Memory:** 6 Frames

### 🎯 Objectives
The main goal is to simulate the hardware logic used by a CPU to access memory:
1.  Accept a **Logical Address**.
2.  Calculate the **Page Number** and **Offset**.
3.  Look up the **Frame Number** in a Page Table.
4.  Calculate the final **Physical Address** or report a **Page Fault**.

## ⚙️ How It Works (The Logic)

The program uses standard paging formulas to perform the translation:

1.  **Calculate Page Number ($p$):**
    `p = Logical Address // Page Size` (Integer Division)

2.  **Calculate Offset ($d$):**
    `d = Logical Address % Page Size` (Remainder)

3.  **Physical Address ($PA$):**
    `PA = (Frame Number * Page Size) + Offset`

### Status Codes
* **Valid:** The page is mapped to a frame in memory.
* **Page Fault:** The page table entry is `-1`, meaning the page is not currently in RAM.
* **Out of Bounds:** The address asks for a page number higher than the maximum allowed (Page 8+).

## 🚀 How to Run the Project

### Prerequisites
You need **Python 3.x** installed on your computer.

### Steps
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/yourusername/EEX5564-PageTable.git](https://github.com/yourusername/EEX5564-PageTable.git)
    ```
2.  **Navigate to the Folder:**
    ```bash
    cd EEX5564-PageTable
    ```
3.  **Run the Script:**
    ```bash
    python main.py
    ```

## 📊 Example Output

When you run the program, it displays a formatted table like this:

```text
--- Group A: Page Table Translator ---
---------------------------------------------------------------------------
Logical    | Page#    | Offset   | Frame#   | Physical   | Status
---------------------------------------------------------------------------
100        | 0        | 100      | 3        | 3172       | Valid
1050       | 1        | 26       | -        | -          | Page Fault Occurred
2500       | 2        | 452      | 0        | 452        | Valid
5000       | 4        | 904      | 5        | 6024       | Valid
8500       | -        | -        | -        | -          | Error: Out of Bounds
