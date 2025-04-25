import csv

def split_csv(input_file, output_prefix, batch_size=49999):
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Save the header

        file_count = 1
        batch = []

        for i, row in enumerate(reader, start=1):
            batch.append(row)
            if i % batch_size == 0:
                output_file = f"{output_prefix}_part{file_count}.csv"
                with open(output_file, 'w', newline='', encoding='utf-8') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerow(header)
                    writer.writerows(batch)
                print(f"✅ Written: {output_file} with {len(batch)} records")
                batch = []
                file_count += 1

        # Write remaining rows
        if batch:
            output_file = f"{output_prefix}_part{file_count}.csv"
            with open(output_file, 'w', newline='', encoding='utf-8') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(header)
                writer.writerows(batch)
            print(f"✅ Written: {output_file} with {len(batch)} records")

# Example usage
split_csv("Mapping-template.csv", "Output")
