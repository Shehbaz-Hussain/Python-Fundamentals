"""
Project 09: Media Player System

Description:
    Demonstrates polymorphism and duck typing.

    The media classes do not inherit from a common parent class.
    The program works with any object that provides the required
    play() behavior.
"""


class Song:
    """Represent a song."""

    def __init__(self, title, artist):
        """Initialize a song."""
        self.title = title
        self.artist = artist

    def play(self):
        """Play the song."""
        print(
            f"Playing song: {self.title} "
            f"by {self.artist}"
        )


class Podcast:
    """Represent a podcast."""

    def __init__(self, title, host):
        """Initialize a podcast."""
        self.title = title
        self.host = host

    def play(self):
        """Play the podcast."""
        print(
            f"Playing podcast: {self.title} "
            f"hosted by {self.host}"
        )


class Video:
    """Represent a video."""

    def __init__(self, title, creator):
        """Initialize a video."""
        self.title = title
        self.creator = creator

    def play(self):
        """Play the video."""
        print(
            f"Playing video: {self.title} "
            f"created by {self.creator}"
        )


def start_media(media):
    """
    Start any object that provides a compatible play() method.

    This function demonstrates duck typing because it does not
    require the object to belong to a particular class hierarchy.
    """
    media.play()


media_items = [
    Song(
        "Python Tutorial",
        "Ali",
    ),
    Podcast(
        "AI Engineering",
        "Ayesha",
    ),
    Video(
        "Machine Learning Course",
        "Hamza",
    ),
]

print("Media Player System")
print("=" * 40)

for media in media_items:
    start_media(media)