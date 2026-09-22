# Mini English Compiler

A simple **Mini Compiler for English Sentences** developed as a Compiler Construction academic project using Python.

The project demonstrates the basic phases of a compiler pipeline by taking an English sentence as input and processing it through lexical analysis, tokenization, syntax analysis, semantic analysis, symbol table generation, intermediate code generation, and final validation.

## 🔹 Compiler Phases

### 1. Lexical Analysis

Checks whether the input is empty and begins the compiler processing.

### 2. Tokenization

Breaks the sentence into individual words/tokens.

### 3. Syntax Analysis

Checks the sentence structure using predefined subjects, verbs, and nouns.

### 4. Parse Tree

Displays a simple tree representation of the sentence structure using:

* S (Sentence)
* NP (Noun Phrase)
* VP (Verb Phrase)

### 5. Semantic Analysis

Checks basic subject-verb compatibility.

### 6. Symbol Table

Displays the identified subject, verb, and object.

### 7. Intermediate Code

Generates a simple intermediate representation (IR) of the sentence.

Example:

```text
EAT(I, apple)
```

### 8. Final Validation

Checks capitalization and sentence-ending punctuation.

## ✨ Features

* English sentence validation
* Manual tokenization
* Syntax checking
* Semantic checking
* Parse tree generation
* Symbol table generation
* Intermediate code generation
* Final sentence validation
* Multiple sentence input
* Exit command

## 🛠️ Technologies Used

* Python
* Compiler Construction concepts

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone or download this repository and open it in VS Code.

Run:

```bash
python project.py
```

Enter an English sentence when prompted.

Example:

```text
Enter Sentence: I eat apple.
```

The compiler will process the sentence through each phase and display the results.

Type:

```text
exit
```

to stop the compiler.

## 📁 Project Structure

```text
Mini-English-Compiler/
│
├── project.py
└── README.md
```

## 📚 Concepts Demonstrated

* Lexical Analysis
* Tokenization
* Syntax Analysis
* Parse Trees
* Semantic Analysis
* Symbol Tables
* Intermediate Representation
* Compiler Pipeline
* Input Validation

## 🎓 Project Type

**Compiler Construction – Academic Project**

This project was developed to demonstrate the implementation of fundamental compiler phases using a simple English sentence validator.
