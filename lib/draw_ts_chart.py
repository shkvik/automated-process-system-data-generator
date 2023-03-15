from matplotlib import pyplot as plt
from primitive_operations import generator
from matplotlib.widgets import Slider

class time_serias_chart:
    def __init__(self, stop: int, step:int = 10) -> None:

        self.step = step

        self.Plot, self.Axis = plt.subplots(3)
        plt.subplots_adjust(bottom=0.2)

        self.First   = self.Axis[0]
        self.Second  = self.Axis[1]
        self.Third   = self.Axis[2]

        # Choose the Slider color
        slider_color = 'White'
        
        # Set the axis and slider position in the plot
        self.axis_position = plt.axes([0.2, 0.1, 0.65, 0.03],facecolor = slider_color)

        self.axis_position2 = plt.axes([0.2, 0.05, 0.65, 0.03],facecolor = slider_color)

        self.freq = Slider(ax=self.axis_position,
                        label='Pos',
			            valmin=0,
			            valmax=stop)
        
        self.freq2 = Slider(ax=self.axis_position2,
                        label='Pos',
			            valmin=0,
			            valmax=stop)

        self.freq.on_changed(self.updatePosition)

    def updateStep(self, val): 
        self.step = self.freq.val
        self.Plot.canvas.draw_idle()

    def updatePosition(self, val):
        pos = self.freq.val

        self.First.axis([pos, pos+self.step, 0, 100])
        self.Second.axis([pos, pos+self.step, 0, 100])
        self.Third.axis([pos, pos+self.step, 0, 100])

        self.Plot.canvas.draw_idle()

    def fillFirst(self, seq: list[float]):
        self.First.plot(seq)

    def fillSecond(self, seq: list[float]):
        self.Second.plot(seq)

    def fillThird(self, seq: list[float]):
        self.Third.plot(seq)

    def drawCharts(self):
        plt.show()


gen1 = generator()
gen1.setVariance(-0.5,0.5)
gen1.increaseLinear(1000)
gen1.decreaseLinear(1000)
gen1.staticSequense(1000)
gen1.increaseLinear(1000)
gen1.decreaseLinear(1000)


gen2 = generator()
gen2.setVariance(-0.5,0.5)
gen2.staticSequense(1000)
gen2.increaseLinear(1000)
gen2.decreaseParabol(1000)
gen2.staticSequense(1000)
gen2.increaseLinear(1000)

gen3 = generator()
gen3.staticSequense(1000)
gen3.logicTrue()
gen3.staticSequense(1000)
gen3.staticSequense(1000)
gen3.logicFalse()
gen3.staticSequense(1000)
gen3.logicTrue()
gen3.staticSequense(500)
gen3.logicFalse()
gen3.staticSequense(500)
gen3.logicTrue()

draw = time_serias_chart(gen1.getLastIndex(), step=400)

draw.fillFirst(gen1.sequense)
draw.fillSecond(gen2.sequense)
draw.fillThird(gen3.sequense)

draw.drawCharts()