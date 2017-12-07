import numpy as np

def nonmax_suppression(det, phase):
  gmax = np.zeros(det.shape)
  phase[phase < 0] += 360
  for i in xrange(1, gmax.shape[0] - 1):
    for j in xrange(1, gmax.shape[1] - 1):
      if (abs(phase[i][j]%180)  < 22.5):
        if det[i][j + 1] <= det[i][j] >= det[i][j - 1]:
          gmax[i][j] = det[i][j]
      elif (abs(phase[i][j]%180)  < 67.5):
        if det[i - 1][j + 1] <= det[i][j] >= det[i + 1][j - 1]:
          gmax[i][j] = det[i][j]
      elif (abs(phase[i][j]%180)  < 112.5):
        if det[i - 1][j] <= det[i][j] >= det[i + 1][j]:
          gmax[i][j] = det[i][j]
      else:
        if det[i - 1][j - 1] <= det[i][j] >= det[i + 1][j + 1]:
          gmax[i][j] = det[i][j]
  return gmax
