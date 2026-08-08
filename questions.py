MCQ_QUESTIONS = [
    # ---------------- OOPs ----------------
    {
        "question": "Which OOP concept refers to wrapping data and methods together "
                    "and restricting direct access to some of an object's components?",
        "options": ["Inheritance", "Encapsulation", "Polymorphism", "Abstraction"],
        "answer": 1,
        "concept": "OOPs",
    },
    {
        "question": "What is method overriding in OOP?",
        "options": [
            "Defining multiple methods with the same name but different parameters in the same class",
            "A subclass providing its own implementation of a method already defined in its parent class",
            "Hiding a class's data members from other classes",
            "Creating multiple constructors in a class",
        ],
        "answer": 1,
        "concept": "OOPs",
    },
    {
        "question": "Which of these best describes an abstract class?",
        "options": [
            "A class that cannot be inherited from",
            "A class that can be instantiated directly like any normal class",
            "A class that cannot be instantiated on its own and may contain abstract "
            "(unimplemented) methods meant to be defined by subclasses",
            "A class with only static methods",
        ],
        "answer": 2,
        "concept": "OOPs",
    },
    {
        "question": "What does 'inheritance' allow in object-oriented programming?",
        "options": [
            "A class to hide its private variables",
            "A class to acquire properties and behaviors of another (parent) class",
            "Multiple objects to share the same memory address",
            "A function to call itself recursively",
        ],
        "answer": 1,
        "concept": "OOPs",
    },

    # ---------------- OS ----------------
    {
        "question": "What is the main purpose of an operating system's scheduler?",
        "options": [
            "To manage the file system's directory structure",
            "To decide which process gets access to the CPU and when",
            "To compile source code into machine code",
            "To allocate IP addresses to devices",
        ],
        "answer": 1,
        "concept": "OS",
    },
    {
        "question": "What is a deadlock in operating systems?",
        "options": [
            "A process running faster than expected",
            "A situation where two or more processes are each waiting for a resource "
            "held by the other, so none of them can proceed",
            "A process that has finished execution",
            "An error caused by insufficient RAM",
        ],
        "answer": 1,
        "concept": "OS",
    },
    {
        "question": "Which scheduling algorithm selects the process with the smallest "
                    "estimated run time to execute next?",
        "options": ["First Come First Serve (FCFS)", "Round Robin", "Shortest Job First (SJF)", "Priority Scheduling"],
        "answer": 2,
        "concept": "OS",
    },
    {
        "question": "What is the purpose of paging in memory management?",
        "options": [
            "To divide a process's memory into fixed-size blocks to avoid external "
            "fragmentation and allow non-contiguous allocation",
            "To speed up the CPU clock",
            "To permanently delete unused files",
            "To merge multiple processes into one",
        ],
        "answer": 0,
        "concept": "OS",
    },

    # ---------------- COA (Computer Organization and Architecture) ----------------
    {
        "question": "What does 'pipelining' in a CPU aim to improve?",
        "options": [
            "Disk read/write speed",
            "Instruction throughput, by overlapping the execution of multiple instructions",
            "Network bandwidth",
            "The size of the register file",
        ],
        "answer": 1,
        "concept": "COA",
    },
    {
        "question": "Which type of memory is fastest but smallest in a typical "
                    "memory hierarchy?",
        "options": ["RAM", "Cache memory", "Hard disk (HDD)", "Registers"],
        "answer": 3,
        "concept": "COA",
    },
    {
        "question": "In computer architecture, what does RISC stand for?",
        "options": [
            "Rapid Instruction Set Computing",
            "Reduced Instruction Set Computer",
            "Random Internal System Cache",
            "Registered Instruction Sequence Control",
        ],
        "answer": 1,
        "concept": "COA",
    },
    {
        "question": "What is the role of the ALU (Arithmetic Logic Unit) in a CPU?",
        "options": [
            "To store the program counter",
            "To perform arithmetic and logical operations on data",
            "To manage input/output devices",
            "To hold the operating system kernel",
        ],
        "answer": 1,
        "concept": "COA",
    },

    # ---------------- DSA ----------------
    {
        "question": "Which data structure follows the LIFO (Last In First Out) principle?",
        "options": ["Queue", "Stack", "Linked List", "Array"],
        "answer": 1,
        "concept": "DSA",
    },
    {
        "question": "What is the time complexity of searching for an element in a "
                    "balanced binary search tree?",
        "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
        "answer": 2,
        "concept": "DSA",
    },
    {
        "question": "Which traversal visits the root node first, then the left subtree, "
                    "then the right subtree?",
        "options": ["In-order", "Pre-order", "Post-order", "Level-order"],
        "answer": 1,
        "concept": "DSA",
    },
    {
        "question": "What is the main advantage of a linked list over an array?",
        "options": [
            "Faster random access to elements",
            "Dynamic size and efficient insertion/deletion without shifting elements",
            "Uses less memory per element",
            "Better cache performance",
        ],
        "answer": 1,
        "concept": "DSA",
    },

    # ---------------- DAA (Design and Analysis of Algorithms) ----------------
    {
        "question": "What is the time complexity of Bubble Sort in the worst case?",
        "options": ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "answer": 2,
        "concept": "DAA",
    },
    {
        "question": "Which algorithm design technique does Merge Sort use?",
        "options": ["Greedy", "Dynamic Programming", "Divide and Conquer", "Backtracking"],
        "answer": 2,
        "concept": "DAA",
    },
    {
        "question": "What is the main idea behind Dynamic Programming?",
        "options": [
            "Always choosing the locally optimal choice at each step",
            "Breaking a problem into independent subproblems that never overlap",
            "Solving overlapping subproblems once and storing/reusing their results",
            "Randomly guessing solutions until one works",
        ],
        "answer": 2,
        "concept": "DAA",
    },
    {
        "question": "Which of these is an example of a greedy algorithm?",
        "options": [
            "0/1 Knapsack (exact solution)",
            "Dijkstra's shortest path algorithm",
            "Matrix chain multiplication",
            "Longest common subsequence",
        ],
        "answer": 1,
        "concept": "DAA",
    },
]