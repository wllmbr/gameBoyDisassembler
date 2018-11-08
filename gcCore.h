#ifndef GC_CORE_H
#define GC_CORE_H

struct gameboyProcessorCore{

	uint8_t Flags;
	uint8_t A;
	uint8_t B;
	uint8_t C;
	uint8_t D;
	uint8_t E;
	uint8_t H;
	uint8_t L;

	uint16_t SP;
	uint16_t PC;

	
}

#endif