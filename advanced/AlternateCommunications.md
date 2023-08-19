
UART - In/out for wireless configuration. Usually two computers talking (Both with clocks)
SPI - Serial Periferal Interface (ADC) Analog to Digital Conversion. Clock, data and Chip/latch enabled (all get but Chip/latch acts an an accept message switch). Sends data serially.
    Clock Signal - SCLK; Data Stream  SDIO or MOSI/MISO); Peripheral select line (CE)
I2C - Barometer - Clock and Data lines; Wind speed. Clock and Data (includes address) + ground.

Parallel - Reading all the pins to get the current values.


## Issues
Noise

UART - short wire length
SPI - I2C - 10 meters

10hz sensor produces information a 0.01ms