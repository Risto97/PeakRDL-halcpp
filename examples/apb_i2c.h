#ifndef _ARCHI_APB_I2C_H_
#define _ARCHI_APB_I2C_H_

#include <stdint.h>


template <typename D> 
class APB_I2C_CRTP {
private:
  D &impl() { return *static_cast<D *>(this); } // CRTP

  uint32_t _BASE_ADDR;

public:
    APB_I2C_CRTP (uint32_t base) : _BASE_ADDR(base) { };

/* STATUS_REG 
   I2C status register
*/

    inline void status_reg_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 0, val);}
    inline uint32_t status_reg_get(){ return impl().ARCHI_READ(_BASE_ADDR, 0);}
    
    /* BUSY FIELD 
       High when module is performing an I2C operation
    */
    inline uint32_t status_reg_busy_get(){ return status_reg_get() & 0x1 >> 0;}

    /* BUS_CONT FIELD 
       High when module has control of active bus
    */
    inline uint32_t status_reg_bus_cont_get(){ return status_reg_get() & 0x2 >> 1;}

    /* BUS_ACT FIELD 
       High when bus is active
    */
    inline uint32_t status_reg_bus_act_get(){ return status_reg_get() & 0x4 >> 2;}

    /* MISS_ACK FIELD 
       set high when an ACK pulse from a slave device is not seen; write 1 to clear
    */
    inline void status_reg_miss_ack_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 0, (status_reg_get() & 0xfffffff7) | val << 3  );}
    inline uint32_t status_reg_miss_ack_get(){ return status_reg_get() & 0x8 >> 3;}

    /* CMD_EMPTY FIELD 
       Command FIFO empty
    */
    inline uint32_t status_reg_cmd_empty_get(){ return status_reg_get() & 0x100 >> 8;}

    /* CMD_FULL FIELD 
       Command FIFO full
    */
    inline uint32_t status_reg_cmd_full_get(){ return status_reg_get() & 0x200 >> 9;}

    /* CMD_OVF FIELD 
       Command FIFO overflow; write 1 to clear
    */
    inline void status_reg_cmd_ovf_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 0, (status_reg_get() & 0xfffffbff) | val << 10  );}
    inline uint32_t status_reg_cmd_ovf_get(){ return status_reg_get() & 0x400 >> 10;}

    /* WR_EMPTY FIELD 
       Write data FIFO empty
    */
    inline uint32_t status_reg_wr_empty_get(){ return status_reg_get() & 0x800 >> 11;}

    /* WR_FULL FIELD 
       Write data FIFO full
    */
    inline uint32_t status_reg_wr_full_get(){ return status_reg_get() & 0x1000 >> 12;}

    /* WR_OVF FIELD 
       Write data FIFO overflow; write 1 to clear
    */
    inline void status_reg_wr_ovf_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 0, (status_reg_get() & 0xffffdfff) | val << 13  );}
    inline uint32_t status_reg_wr_ovf_get(){ return status_reg_get() & 0x2000 >> 13;}

    /* RD_EMPTY FIELD 
       Read data FIFO is empty
    */
    inline uint32_t status_reg_rd_empty_get(){ return status_reg_get() & 0x4000 >> 14;}

    /* RD_FULL FIELD 
       Read data FIFO is full
    */
    inline uint32_t status_reg_rd_full_get(){ return status_reg_get() & 0x8000 >> 15;}

/* COMMAND_REG 
   Controls the operation of I2C
Setting more than one command bit is allowed.  Start or repeated start
will be issued first, followed by read or write, followed by stop.  Note
that setting read and write at the same time is not allowed, this will
result in the command being ignored.
*/

    inline void command_reg_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 4, val);}
    inline uint32_t command_reg_get(){ return impl().ARCHI_READ(_BASE_ADDR, 4);}
    
    /* CMD_ADDRESS FIELD 
       Address to be written on the I2C bus
    */
    inline void command_reg_cmd_address_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 4, (command_reg_get() & 0xffffff80) | val << 0  );}
    inline uint32_t command_reg_cmd_address_get(){ return command_reg_get() & 0x7f >> 0;}

    /* CMD_START FIELD 
       Set high to issue I2C start, write to push on command FIFO
    */
    inline void command_reg_cmd_start_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 4, (command_reg_get() & 0xffffff7f) | val << 7  );}
    inline uint32_t command_reg_cmd_start_get(){ return command_reg_get() & 0x80 >> 7;}

    /* CMD_READ FIELD 
       Set high to start read, write to push on command FIFO
    */
    inline void command_reg_cmd_read_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 4, (command_reg_get() & 0xfffffeff) | val << 8  );}
    inline uint32_t command_reg_cmd_read_get(){ return command_reg_get() & 0x100 >> 8;}

    /* CMD_WRITE FIELD 
       Set high to start write, write to push on command FIFO
    */
    inline void command_reg_cmd_write_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 4, (command_reg_get() & 0xfffffdff) | val << 9  );}
    inline uint32_t command_reg_cmd_write_get(){ return command_reg_get() & 0x200 >> 9;}

    /* CMD_WRITE_MULTIPLE FIELD 
       Set high to start block write, write to push on command FIFO
    */
    inline void command_reg_cmd_write_multiple_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 4, (command_reg_get() & 0xfffffbff) | val << 10  );}
    inline uint32_t command_reg_cmd_write_multiple_get(){ return command_reg_get() & 0x400 >> 10;}

    /* CMD_STOP FIELD 
       Set high to issue I2C stop, write to push on command FIFO
    */
    inline void command_reg_cmd_stop_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 4, (command_reg_get() & 0xfffff7ff) | val << 11  );}
    inline uint32_t command_reg_cmd_stop_get(){ return command_reg_get() & 0x800 >> 11;}

/* DATA_REG 
   Send and receive data register
*/

    inline void data_reg_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 8, val);}
    inline uint32_t data_reg_get(){ return impl().ARCHI_READ(_BASE_ADDR, 8);}
    
    /* DATA FIELD 
       I2C data, write to push on write data FIFO, read to pull from read data FIFO
    */
    inline void data_reg_data_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 8, (data_reg_get() & 0xffffff00) | val << 0  );}
    inline uint32_t data_reg_data_get(){ return data_reg_get() & 0xff >> 0;}

    /* DATA_VALID FIELD 
       Indicates valid read data, must be accessed with atomic 16 bit reads and writes
    */
    inline void data_reg_data_valid_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 8, (data_reg_get() & 0xfffffeff) | val << 8  );}
    inline uint32_t data_reg_data_valid_get(){ return data_reg_get() & 0x100 >> 8;}

    /* DATA_LAST FIELD 
       Indicate last byte of block write (write_multiple), must be accessed with atomic 16 bit reads and writes
    */
    inline void data_reg_data_last_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 8, (data_reg_get() & 0xfffffdff) | val << 9  );}
    inline uint32_t data_reg_data_last_get(){ return data_reg_get() & 0x200 >> 9;}

/* PRESCALE_REG 
   Set prescale value. Set prescale to 1/4 of the minimum clock period in units of input clk cycles
      FIELD DESCRIPTION: 
      Prescale = Fclk / (FI2Cclk * 4)
*/

    inline void prescale_reg_set(uint32_t val){ impl().ARCHI_WRITE(_BASE_ADDR, 12, val);}
    inline uint32_t prescale_reg_get(){ return impl().ARCHI_READ(_BASE_ADDR, 12);}
    

};


class APB_I2C  : public APB_I2C_CRTP<APB_I2C> {
    public:
    uint32_t ARCHI_READ(uint32_t base, uint32_t offset){ 
        return *(volatile uint32_t*)(base + offset);
    }
    void ARCHI_WRITE(uint32_t base, uint32_t offset, uint32_t value){
        *(volatile uint32_t*)(base + offset) = value;

    }

    APB_I2C (uint32_t base) : APB_I2C_CRTP(base) {
    }
};

#endif