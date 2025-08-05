class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None


class MusicPlaylist:
    def __init__(self):
        self.head = None

    def create_playlist(self, song_list):
        for title in song_list:
            self.insert_song(title, self.get_length())  # Append to end

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert_song(self, title, position):
        """Insert a song at the specified position in the playlist."""
        new_node = SongNode(title)
        if position <= 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            print(f"Song '{title}' inserted at position 0 (start of playlist).")
            return

        temp = self.head
        index = 0
        while temp.next and index < position - 1:
            temp = temp.next
            index += 1

        new_node.next = temp.next
        temp.next = new_node
        print(f"Song '{title}' inserted at position {index + 1}.")

    def delete_song(self, title):
        temp = self.head
        prev = None
        while temp:
            if temp.title == title:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"Song '{title}' deleted from the playlist.")
                return
            prev = temp
            temp = temp.next
        print(f"Song '{title}' not found in the playlist.")

    def display_playlist(self):
        if not self.head:
            print("Playlist is empty.")
            return
        print("Music Playlist:")
        temp = self.head
        index = 0
        while temp:
            print(f"{index}: {temp.title}")
            temp = temp.next
            index += 1


def main():
    playlist = MusicPlaylist()

    while True:
        print("\n--- Music Playlist Menu ---")
        print("1. Create Playlist")
        print("2. Insert Song")
        print("3. Delete Song")
        print("4. Display Playlist")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            songs = input("Enter song titles separated by commas: ").split(",")
            songs = [song.strip() for song in songs]
            playlist.create_playlist(songs)
        elif choice == '2':
            title = input("Enter song title to insert: ").strip()
            try:
                position = int(input("Enter the position to insert at (starting from 0): ").strip())
                playlist.insert_song(title, position)
            except ValueError:
                print("Invalid position. Please enter an integer.")
        elif choice == '3':
            title = input("Enter song title to delete: ").strip()
            playlist.delete_song(title)
        elif choice == '4':
            playlist.display_playlist()
        elif choice == '5':
            print("Exiting Music Playlist. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
