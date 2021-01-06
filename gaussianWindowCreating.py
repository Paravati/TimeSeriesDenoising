import numpy as np
import matplotlib.pyplot as plt


def gausWindowGenerator(timeVecRange, timeVecSamp,  fwhm, plot=True):
    """ Function for cerating Gaussian Window to filter signals.
        Parameters:
        + timeVecRange - range for time vector in ms (max value for time range),
        + timeVecSamp - time vector samples generated based on
        + fwhm - full-width half-maximum -> the key Gaussian parameter"""

    gaussianWindow = np.exp(-(4 * np.log(2) * timeVecSamp ** 2) / fwhm ** 2)

    # ******** compute empirical FWHM  ********
    pstPeakHalf = timeVecRange + np.argmin((gaussianWindow[timeVecRange:] - .5) ** 2)
    prePeakHalf = np.argmin((gaussianWindow - .5) ** 2)
    empFWHM = timeVecSamp[pstPeakHalf] - timeVecSamp[prePeakHalf]

    if plot:  # show the Gaussian
        plt.plot(timeVecSamp, gaussianWindow, 'ko-')
        plt.plot([timeVecSamp[prePeakHalf], timeVecSamp[pstPeakHalf]], [gaussianWindow[prePeakHalf], gaussianWindow[pstPeakHalf]], 'm')
        plt.title('Gaussian kernel with requeted FWHM ' + str(fwhm) + ' ms (' + str(empFWHM) + ' ms achieved)')
        plt.xlabel('Time (ms)')
        plt.ylabel('Gain')

        gauswin = gaussianWindow / np.sum(gaussianWindow)  # normalize Gaussian to unit energy
        plt.figure()
        plt.plot(gauswin)
        plt.title('Gaussian window normalized to unit energy')
        plt.xlabel('Time (ms)')
        plt.ylabel('Gain')

        plt.show()

    return gaussianWindow, empFWHM


if __name__ == "__main__":
    fs = 1000  # sampling rate in Hz
    timeVectorRange = 100
    timeSamples = 1000 * np.arange(-timeVectorRange, timeVectorRange) / fs
    gaussianWin, FWHM = gausWindowGenerator(timeVecRange=100, timeVecSamp=timeSamples, fwhm=25)
