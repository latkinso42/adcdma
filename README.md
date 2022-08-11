ADC DMA

     This little program uses analogio AnalogFastIn interface, which creates the setup software device for an ADC pin corresponding to one of the four channels to read or run 'free' while DMA write to a provided buffer. The interface provides the complex setup, including sample rate specification.
     
     An additional method, against the software device, actually initiates the capture, while the deinit method retuen the DMA channel and ADC resource pin. The result is a one shot, rapid fill up to 0.5Million Samples per second rate or as low as 2 microseconds per conversion for the Raspberry Pi Pico.
     
     The user supplies buffer which is filled by the capture method. Thus the sw device can be created once for setup and the capture can be called multiple times against the sw device. After use the user should call deinit to clear resources.
     
     The current version is preliminary, converts at the maximum rate and has been tested against a 1000 H sized (16bit) array. The resulting buffer has values between 0 and 4095 (12 bit ADC).
     
     Other enhancements or generaliztino for other platforms is forth comming. The implementation is an addition to the analogio module. Possilble alternative implementations might (A) simply extend AnalogIn with optional arguments, or (B) create an entirely new module.
     
     
     

