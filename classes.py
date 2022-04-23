class Television:
    """
    A class representing details for a Television object.
    :param MIN_CHANNEL: Minimum TV channel
    :param MAX_CHANNEL: Maximum TV channel
    :param MIN_VOLUME: Minimum TV volume
    :param MAX_VOLUME: Maximum TV volume
    """

    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self):
        """
        Constructor to create initial state of a Television object.
        :param channel: Channel number of television.
        :param volume: Volume level of television.
        :param power: Power state of television.
        """
        self.__channel = 0
        self.__volume = 0
        self.__power = False

    def power(self):
        """
        Method used to turn the television on/off.
        :param power: Power state of television.
        """
        if self.__power == False:
            self.__power = True
        elif self.__power == True:
            self.__power = False

    def channel_up(self):
        """
        Method used to adjust the TV channel by incrementing its value.
        :param power: Power state of television.
        :param channel: Channel number of television.
        """
        if self.__power == True:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        Method used to adjust the TV channel by decrementing its value.
        :param power: Power state of television.
        :param channel: Channel number of television.
        """
        if self.__power == True:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1
        
        pass

    def volume_up(self):
        """
        Method used to adjust the TV volume by incrementing its value.
        :param volume: Volume level of television.
        :param power: Power state of television.
        """
        if self.__power == True:
            if self.__volume == self.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
        
        pass

    def volume_down(self):
        """
        Method used to adjust the TV volume by decrementing its value.
        :param volume: Volume level of television.
        :param power: Power state of television.
        """
        if self.__power == True:
            if self.__volume == self.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        
        pass

    def __str__(self):
        """
        Method used to return the TV status using the format shown in the comments of main.py
        :return: Television status.
        """
        return f"TV status: Is on = {self.__power}, Channel = {self.__channel}, Volume = {self.__volume}"
