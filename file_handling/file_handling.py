filename = "file_handling/sample.txt"

# 1. Write Mode ("w") → overwrite/create
with open(filename, "w") as f:
    f.write("Hello World\n")
    f.write("This is Python File Handling Example\n")

# 2. Read Mode ("r")
with open(filename, "r") as f:
    print("Read Mode:")
    print(f.read())


# 3. Append Mode ("a") → adds to file
with open(filename, "a") as f:
    f.write("Appended Line 1\n")

# 4. Read + Write Mode ("r+")
with open(filename, "r+") as f:
    content = f.read()
    print("\nRead+Write Mode (before writing):")
    print(content)
    f.seek(0)  # move cursor to beginning
    f.write("Modified First Line\n")

# 5. Write + Read Mode ("w+")
with open("file_handling/newfile.txt", "w+") as f:
    f.write("New file created with w+\n")
    f.seek(0)
    print("\nWrite+Read Mode:")
    print(f.read())

# 6. Append + Read Mode ("a+")
with open(filename, "a+") as f:
    f.write("Appended with a+\n")
    f.seek(0)
    print("\nAppend+Read Mode:")
    print(f.read())

# 7. Exclusive Create ("x")
try:
    with open("file_handling/unique.txt", "x") as f:
        f.write("This file is created with 'x' mode\n")
except FileExistsError:
    print("\nFile already exists (x mode)")

# 8. Binary Mode Example ("wb", "rb")
data = b"This is binary data"
with open("file_handling/binary.dat", "wb") as f:
    f.write(data)

with open("file_handling/binary.dat", "rb") as f:
    print("\nBinary Mode:")
    print(f.read())

# 9.user feedback
feedback = input("Enter your Feedback:")

with open("file_handling/feedback.txt","a") as log:
    log.write(feedback + "\n")
    
print("Thank you, your feedback is saved")