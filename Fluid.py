class Fluid:
    """
    A class to represent a fluid in a one-dimensional pipe.

    ...

    Attributes
    ----------
    name: str
        The name of the fluid
    pipeLength: float
        The length of the pipe containing the fluid
    maxTime: float
        The time for which the fluid is evolved to in time
    positionsSteps: int
        The amount of positions measured within the pipe
    timeSteps: int
        The amount of time increments leading up to the maximum time
    Methods
    -------
    positionInfo():
        Calculates the position step and returns a tuple containing the pipe length and position step
    timeInfo():
        Calcualtes the time step and returns a tuple containing the maximum time and time step
    """
    def __init__(
        self,
        name = 'Water',
        pipeLength = 10.0,
        maxTime = 10.0,
        positionsSteps = 1000,
        timeSteps = 30000
    ):
        self.name = name
        self.pipeLength = pipeLength
        self.maxTime = maxTime
        self.positionSteps = positionsSteps
        self.timeSteps=timeSteps

    def __str__(self):
        return "Fluid: {0}, Pipe Length: {1}, Maximum Time: {2}, Position Intervals: {3}, Time Intervals: {4}".format(
        self.name,self.pipeLength,self.maxTime,self.positionSteps,self.timeSteps)

    def positionInfo(self):
        """
        Calculates the position step based off the pipe length and position steps of a defined fluid

            Returns:
                x, deltaX (tuple with dtype: float): Tuple containing the pipe length and the calculated position step
        """
        x = self.pipeLength
        deltaX = x/self.positionSteps
        return x, deltaX

    def timeInfo(self):
        """
        Calculates the time step based off the pipe length and time steps of a defined fluid

            Returns:
                t, deltaT (tuple with dtype: float): Tuple containing the maximum time and the calculated time step
        """
        t = self.maxTime
        deltaT = t/self.timeSteps
        return t, deltaT
    
