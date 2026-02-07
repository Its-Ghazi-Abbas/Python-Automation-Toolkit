from pathlib import Path

# Define file categories
pdf_extensions = ('.pdf',)
image_extensions = ('.png', '.jpg', '.jpeg')
video_extensions = ('.mp4', '.mkv')
application_extensions = ('.exe', '.ini')


def main():
    # Intro message
    print("=== Welcome to File Organizer ===")
    print("This script organizes files by type into a master folder.\n")

    # 1 Ask user for folder to organize (Enter = default Downloads)
    folder_path = input("Enter the folder path you want to organize (Press Enter for default Downloads): ").strip()
    if folder_path == "":
        source_folder = Path.home() / "Downloads"
    else:
        source_folder = Path(folder_path)

    if not source_folder.exists():
        print("Error: Source folder does not exist.")
        return

    # 2 Ask user for output location (Enter = same as source)
    output_path = input("Enter the folder where sorted folders should be created (Press Enter for same folder): ").strip()
    if output_path == "":
        output_folder = source_folder
    else:
        output_folder = Path(output_path)

    if not output_folder.exists():
        print("Error: Output folder does not exist.")
        return

    # 3 Create master folder
    master_folder = output_folder / "Organized_Files"
    master_folder.mkdir(exist_ok=True)

    # Create category folders inside master
    pdf_folder = master_folder / "PDFs"
    image_folder = master_folder / "Images"
    video_folder = master_folder / "Videos"
    application_folder = master_folder / "Applications"
    other_folder = master_folder / "Others"

    for folder in [pdf_folder, image_folder, video_folder, application_folder, other_folder]:
        folder.mkdir(exist_ok=True)

    print(f"\nScanning folder: {source_folder}")
    print(f"Sorted files will be saved in: {master_folder}\n")

    # Access top-level items
    files = list(source_folder.iterdir())
    total_items = len(files)
    print(f"Total items found in folder: {total_items}\n")

    # Counters
    scanned_files = 0
    moved_count = 0
    skipped_count = 0

    # Classify and move files
    for file in files:
        if file.is_dir():
            continue
        scanned_files += 1

        ext = file.suffix.lower()

        # Decide destination
        if ext in pdf_extensions:
            destination_folder = pdf_folder
            category = "PDFs"
        elif ext in image_extensions:
            destination_folder = image_folder
            category = "Images"
        elif ext in video_extensions:
            destination_folder = video_folder
            category = "Videos"
        elif ext in application_extensions:
            destination_folder = application_folder
            category = "Applications"
        else:
            destination_folder = other_folder
            category = "Others"

        destination = destination_folder / file.name

        # Safety check
        if destination.exists():
            print(f"Skipped (already exists): {file.name}")
            skipped_count += 1
            continue

        file.replace(destination)
        moved_count += 1
        print(f"Moved: {file.name} -> {category}")

    # Summary
    print("\n=== Organization Complete ===")
    print(f"Total files scanned: {scanned_files}")
    print(f"Moved: {moved_count}")
    print(f"Skipped: {skipped_count}")


if __name__ == "__main__":
    main()
