import os
import time

while True:
    path = input("Path to the desired folder: ")
    print("Your path: "+ path)

    folder_name = os.path.basename(os.path.normpath(path))
    print("Your selected folder: "+folder_name)

    time.sleep(1)
    print("\nProcessing ...\n")

    def write_structure(folder_path, file, indent=0):
        try:
            file.write("\t" * indent + os.path.basename(folder_path) + "\n")
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    write_structure(item_path, file, indent + 1)
                else:
                    file.write("\t" * (indent + 1) + item + "\n")
        except PermissionError:
            # If access is not allowed.
            file.write("\t" * (indent + 1) + "[Access denied]\n")

    output_file = folder_name + "_structure.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        write_structure(path, f)
    print("Done! Structure saved as", output_file)

    print("\n\n")
