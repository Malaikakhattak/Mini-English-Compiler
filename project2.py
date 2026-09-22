# -------- MINI COMPILER FOR ENGLISH SENTENCES --------

# ---------------- LEXICAL ANALYSIS ----------------
def lexical(sentence):
    print("\n🔹 Phase 1: Lexical Analysis")

    if not sentence.strip():
        print("❌ Empty input")
        return False

    print("✔ Tokens generated (manual split)")
    return True


# ---------------- TOKENIZATION ----------------
def tokenize(sentence):
    print("\n🔹 Phase 2: Tokenization")

    tokens = sentence.replace('.', '').replace('?', '').replace('!', '').split()

    if tokens:
        tokens[0] = tokens[0].capitalize()

    print("Tokens:", tokens)
    return tokens


# ---------------- SYNTAX ANALYSIS ----------------
def syntax(tokens):
    print("\n🔹 Phase 3: Syntax Analysis")

    subjects = ["I", "He", "She", "They", "We"]
    verbs = ["eat", "eats", "read", "reads", "drive", "drives",
             "like", "likes", "play", "plays", "watch", "watches"]
    nouns = ["apple", "book", "car", "food", "mango", "movie", "song", "game"]

    if len(tokens) < 2:
        print("❌ Syntax Error: Incomplete sentence")
        return False

    if tokens[0] not in subjects:
        print("❌ Syntax Error: Invalid subject")
        return False

    if tokens[1] not in verbs:
        print("❌ Syntax Error: Invalid verb")
        return False

    if len(tokens) > 2 and tokens[2] not in nouns:
        print("❌ Syntax Error: Invalid object")
        return False

    print("✔ Syntax Correct")
    return True


# ---------------- PARSE TREE ----------------
def parse_tree(tokens):
    print("\n🔹 Phase 4: Parse Tree")

    print("\n        S")
    print("       / \\")
    print("     NP   VP")

    print(f"     |    / \\")
    print(f"    {tokens[0]}  V   NP")

    if len(tokens) > 2:
        print(f"         |     |")
        print(f"        {tokens[1]}  {tokens[2]}")
    else:
        print(f"         |")
        print(f"        {tokens[1]}")


# ---------------- SEMANTIC ANALYSIS ----------------
def semantic(tokens):
    print("\n🔹 Phase 5: Semantic Analysis")

    subject = tokens[0]
    verb = tokens[1]

    if subject in ["He", "She"] and verb in ["eat", "read", "drive"]:
        print("❌ Semantic Error: Subject-Verb mismatch")
        return False

    print("✔ Semantic Correct")
    return True


# ---------------- SYMBOL TABLE ----------------
def symbol_table(tokens):
    print("\n🔹 Phase 6: Symbol Table")

    print("Subject →", tokens[0])
    print("Verb →", tokens[1])

    if len(tokens) > 2:
        print("Object →", tokens[2])


# ---------------- INTERMEDIATE CODE ----------------
def intermediate(tokens):
    print("\n🔹 Phase 7: Intermediate Code")

    if len(tokens) > 2:
        print(f"IR: {tokens[1].upper()}({tokens[0]}, {tokens[2]})")
    else:
        print(f"IR: {tokens[1].upper()}({tokens[0]})")


# ---------------- FINAL VALIDATION ----------------
def final(sentence):
    print("\n🔹 Phase 8: Final Validation")

    if not sentence[0].isupper():
        print("❌ Must start with capital letter")
        return False

    if sentence[-1] not in ".?!":
        print("❌ Must end with punctuation")
        return False

    print("✔ Format Correct")
    return True


# ---------------- MAIN COMPILER PIPELINE ----------------
def run(sentence):

    print("\n================ COMPILER START ================\n")

    if not lexical(sentence):
        return

    tokens = tokenize(sentence)

    if not syntax(tokens):
        return

    parse_tree(tokens)

    if not semantic(tokens):
        return

    symbol_table(tokens)

    intermediate(tokens)

    if not final(sentence):
        return

    print("\n🎉 FINAL OUTPUT: VALID SENTENCE (ACCEPTED BY COMPILER)")


# ---------------- MULTIPLE INPUT LOOP ----------------
while True:
    sentence = input("\nEnter Sentence (or type exit): ")

    if sentence.lower() == "exit":
        print("Compiler Stopped.")
        break

    run(sentence)