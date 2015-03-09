from matplotlib import pyplot as plt

f = plt.figure()
ax = f.gca()
f.show()

for i in range(10):
    ax.plot(i, i, 'ko')
    f.canvas.draw()
    raw_input('pause : press any key ...')
