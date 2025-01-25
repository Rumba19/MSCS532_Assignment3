# MSCS532 Assignment 3: Algorithm Efficiency and Scalability

## **Overview**
This project is part of the MSCS532 course assignment to analyze and compare the efficiency and scalability of two algorithms:
1. **Randomized Quicksort**: A sorting algorithm with a randomized pivot selection.
2. **Hashing with Chaining**: A hash table implementation that resolves collisions using linked lists.

The project includes:
- Implementation of the two algorithms.
- Theoretical analysis of their time complexity.
- Empirical evaluation of Randomized Quicksort vs. Deterministic Quicksort.
- Benchmarking results and insights into algorithm performance.

---

### **Prerequisites to run the script**
1. **Python**: Ensure Python 3.x is installed. You can download it from [python.org](https://www.python.org/).
2. **Install Dependencies**: Run the following command to install the required library (`numpy`):
   ```bash
   pip3 install numpy

## **Clone the Repository**
  ```bash
git clone https://github.com/Rumba19/MSCS532_Assignment3
cd MSCS532_ASSIGNMENT3
python3 randomized_quicksort.py
python3 determinstic.quicksort.py
python3 benchmark.py