IDIR =./
CC=icc
CFLAGS=-I$(IDIR)
LIBS=-lm
MKL=-mkl=sequential
AVX=-xAVX
DEBUG=_PRINT_

$(IDIR)/%.x:	%.cpp 
	$(CC) $(MKL) $(AVX) -o $@ $<

$(IDIR)/%.d:	%.cpp
	$(CC) -D$(DEBUG) $(MKL) $(AVX) -o $@ $<

.PHONY: clean
clean:
	rm -f *.x *.d *.data
