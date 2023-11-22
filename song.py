"""Song Class."""

class Song:
    def __init__(self, title="", artist="", year=0, is_learned=False):
        """
        Constructor for the Song class.

        :param title: str - Title of the song.
        :param artist: str - Artist of the song.
        :param year: int - Release year of the song.
        :param is_learned: bool - Indicates whether the song has been learned.
        """
        self.title = title  # Title of the song.
        self.artist = artist  # Artist of the song.
        self.year = year  # Release year of the song.
        self.is_learned = is_learned  # Learned status of the song.

    def __str__(self):
        """
        String representation of the Song object.

        :return: str - Formatted string showing song details.
        """
        # Return a formatted string with song details.
        return f"{self.title} by {self.artist}, Released: {self.year}, Learned: {self.is_learned}"

    def mark_as_learned(self):
        """Mark the song as learned."""
        self.is_learned = True  # Update the learned status to True.

    def mark_as_unlearned(self):
        """Mark the song as unlearned."""
        self.is_learned = False  # Update the learned status to False.

    def to_dict(self):
        """
        Convert the Song object to a dictionary.

        :return: dict - Dictionary representation of the song.
        """
        # Return a dictionary with the song's properties.
        return {
            'title': self.title,
            'artist': self.artist,
            'year': self.year,
            'is_learned': self.is_learned
        }

