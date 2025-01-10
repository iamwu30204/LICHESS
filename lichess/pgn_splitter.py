import chess.pgn
import os

def split_pgn_into_chunks(input_file_path, output_folder, chunk_size_mb=200):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Calculate chunk size in bytes
    chunk_size_bytes = chunk_size_mb * 1024 * 1024

    with open(input_file_path, 'rb') as pgn_file:
        chunk_number = 1
        current_chunk_size = 0
        current_chunk_path = os.path.join(output_folder, f"chunk_{chunk_number}.pgn")

        with open(current_chunk_path, 'wb') as current_chunk:
            while True:
                data = pgn_file.read(1024)
                if not data:
                    break
                current_chunk.write(data)
                current_chunk_size += len(data)

                # Check for the end of a game and create a new chunk
                if current_chunk_size >= chunk_size_bytes and b'\n\n' in data:
                    print(f"Chunk {chunk_number} saved to {current_chunk_path}")
                    current_chunk_size = 0
                    chunk_number += 1
                    current_chunk_path = os.path.join(output_folder, f"chunk_{chunk_number}.pgn")
                    current_chunk = open(current_chunk_path, 'wb')

                if chunk_number == 31:
                    break
    print(f"Last chunk {chunk_number} saved to {current_chunk_path}")

# Specify the path to your input PGN file
input_pgn_file = "D:\lichess_db_standard_rated_2024-08.pgn"

# Specify the folder where you want to save the chunks
output_folder = r"C:\Users\user\Desktop\lichess\CHUNK"

# Specify the desired chunk size in MB
chunk_size_mb = 200

# Call the function to split the PGN file into chunks
split_pgn_into_chunks(input_pgn_file, output_folder, chunk_size_mb)
