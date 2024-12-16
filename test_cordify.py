from music21 import converter, chord, stream

def test_cordify(input_file):
    """
    Test the chordify function of music21.

    Parameters:
        input_file (str): Path to the MusicXML file.

    Returns:
        None
    """
    # Load the MusicXML file
    try:
        score = converter.parse(input_file)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # Apply the chordify function
    try:
        chordified_score = score.chordify()
    except Exception as e:
        print(f"Error during chordification: {e}")
        return

    # Extract and print the chords
    chords = []
    for element in chordified_score.recurse():
        if isinstance(element, chord.Chord):
            chords.append(element)

    # Output the chords
    if chords:
        print("Chords in the file:")
        for c in chords:
            print(f"{c.commonName}: {c.notes}")
    else:
        print("No chords found in the file.")

if __name__ == "__main__":
    # Example usage
    input_file = input("Enter the path to the MusicXML file: ")
    test_cordify(input_file)
