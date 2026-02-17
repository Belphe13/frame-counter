import sys

def calculate_frame_range(input_str):
    """
    Calculates frame range from input string in format "page-column-frame [count]"
    """
    try:
        parts = input_str.strip().split()
        if not parts:
            return None
        
        coords = parts[0]
        count = None
        if len(parts) > 1:
            count = int(parts[1])
        
        # Parse x-y-z (page-column-frame)
        if '-' not in coords:
             # Basic validation or fallback if user types differently, though requirement says x-y-z
             return "Error: Input must be in format page-column-frame (e.g., 1-2-1)"
             
        # Split by '-'
        coord_parts = coords.split('-')
        if len(coord_parts) != 3:
            return "Error: Input must have 3 parts separated by '-' (page-column-frame)"

        x_str, y_str, z_str = coord_parts
        x = int(x_str)
        y = int(y_str)
        z = int(z_str)
        
        # Constants based on user template
        FRAMES_PER_COL = 34
        COLS_PER_PAGE = 11
        FRAMES_PER_PAGE = FRAMES_PER_COL * COLS_PER_PAGE # 374
        
        # Calculate start frame
        # Formula: (x-1)*34*11 + (y-1)*34 + z
        # (x-1) pages before
        # (y-1) columns before in current page
        # z frames into current column
        start_frame = (x - 1) * FRAMES_PER_PAGE + (y - 1) * FRAMES_PER_COL + z
        
        if count is not None:
            # If count (m) is provided, output range
            end_frame = start_frame + count - 1
            return f"{start_frame}-{end_frame}"
        else:
            # If no count, output single frame number
            return f"{start_frame}"
            
    except ValueError:
        return "Error: Invalid number format. Please ensure page, column, frame, and count are integers."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Film Frame Calculator for 'The Perfect Human'")
    print("Enter coordinates in format: page-column-frame [count]")
    print("(e.g., '1-2-1 10' or '1-2-1')")
    print("Type 'exit' or 'quit' to close.")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("> ").strip()
            
            if user_input.lower() in ('exit', 'quit'):
                break
            if not user_input:
                continue
            
            result = calculate_frame_range(user_input)
            if result:
                print(result)
                
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
