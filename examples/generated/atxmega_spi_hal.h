#ifndef __ATXMEGA_SPI_HAL_H_
#define __ATXMEGA_SPI_HAL_H_

#include <stdint.h>
#include "halcpp_base.h"

namespace _atxmega_spi_hal_nm {


template<uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
class CTRL : public halcpp::RegRW<BASE, WIDTH, PARENT_TYPE> {
public:
    halcpp::FieldRW<0, 1, CTRL<BASE, WIDTH, PARENT_TYPE> > PRESCALER;
    halcpp::FieldRW<2, 3, CTRL<BASE, WIDTH, PARENT_TYPE> > MODE;
    halcpp::FieldRW<4, 4, CTRL<BASE, WIDTH, PARENT_TYPE> > MASTER;
    halcpp::FieldRW<5, 5, CTRL<BASE, WIDTH, PARENT_TYPE> > DORD;
    halcpp::FieldRW<6, 6, CTRL<BASE, WIDTH, PARENT_TYPE> > ENABLE;
    halcpp::FieldRW<7, 7, CTRL<BASE, WIDTH, PARENT_TYPE> > CLK2X;

    CTRL() {} 

    using halcpp::RegRW<BASE, WIDTH, PARENT_TYPE>::operator=;

};



template<uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
class INTCTRL : public halcpp::RegRW<BASE, WIDTH, PARENT_TYPE> {
public:
    halcpp::FieldRW<0, 1, INTCTRL<BASE, WIDTH, PARENT_TYPE> > INTLVL;

    INTCTRL() {} 

    using halcpp::RegRW<BASE, WIDTH, PARENT_TYPE>::operator=;

};



template<uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
class STATUS : public halcpp::RegRO<BASE, WIDTH, PARENT_TYPE> {
public:
    halcpp::FieldRO<6, 6, STATUS<BASE, WIDTH, PARENT_TYPE> > WRCOL;
    halcpp::FieldRO<7, 7, STATUS<BASE, WIDTH, PARENT_TYPE> > IF;

    STATUS() {} 


};


/*
* The DATA register is used for sending and receiving data.
* Writing to the register initiates the data transmission, and the byte
* written to the register will be shifted out on the SPI output line.
* Reading the register causes the shift register receive buffer to be read,
* returning the last byte successfully received
*/
template<uint32_t BASE, uint32_t WIDTH, typename PARENT_TYPE>
class DATA : public halcpp::RegRW<BASE, WIDTH, PARENT_TYPE> {
public:
    halcpp::FieldWO<0, 7, DATA<BASE, WIDTH, PARENT_TYPE> > WDATA;
    halcpp::FieldRO<0, 7, DATA<BASE, WIDTH, PARENT_TYPE> > RDATA;

    DATA() {} 

    using halcpp::RegRW<BASE, WIDTH, PARENT_TYPE>::operator=;

};


}

/*
* Register description of Atmel XMEGA AU's SPI controller
* Transcribed from original manual as an example exercise:
* http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-8331-8-and-16-bit-AVR-Microcontroller-XMEGA-AU_Manual.pdf
*/
template <uint32_t BASE, typename PARENT_TYPE=void>
class ATXMEGA_SPI_HAL : public AddrmapNode<BASE, PARENT_TYPE> {
public:

_atxmega_spi_hal_nm::CTRL<0x0,  8, ATXMEGA_SPI_HAL<BASE, PARENT_TYPE>> CTRL;
_atxmega_spi_hal_nm::INTCTRL<0x1,  8, ATXMEGA_SPI_HAL<BASE, PARENT_TYPE>> INTCTRL;
_atxmega_spi_hal_nm::STATUS<0x2,  8, ATXMEGA_SPI_HAL<BASE, PARENT_TYPE>> STATUS;
_atxmega_spi_hal_nm::DATA<0x3,  8, ATXMEGA_SPI_HAL<BASE, PARENT_TYPE>> DATA;

    ATXMEGA_SPI_HAL() {}

};


#endif