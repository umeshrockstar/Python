#Write a program that merges lines alternatively from two files and writes the results to new file. 
# If one file has less number of lines than the other, the remaining lines from the larger file should be simply copied into the target 
# file.
with open("file1.txt", 'r') as f1, open("file2.txt", 'r') as f2, open("merged.txt", 'w') as out:
    
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    max_len = max(len(lines1), len(lines2))

    for i in range(max_len):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])
