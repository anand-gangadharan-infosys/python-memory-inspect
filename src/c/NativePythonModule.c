#include <Python/Python.h>

int* ptr;

static int BUFF_SIZE = 250*1024;

static PyObject* helloworld(PyObject* self) {
   printf("%s\n","Native call invoked");
   ptr = (int*) malloc(BUFF_SIZE* sizeof(int));
   int i;
   for(i=0;i<BUFF_SIZE;i++){
        *(ptr+i) = 500;
    }
   printf("%s\n","Buffer Filled with 500");
   return Py_BuildValue("s", "Hello, Python extensions!!");
}

static char helloworld_docs[] =
   "helloworld( ): Any message you want to put here!!\n";

static PyMethodDef helloworld_funcs[] = {
   {"helloworld", (PyCFunction)helloworld, 
      METH_NOARGS, helloworld_docs},
      {NULL}
};

void inithelloworld(void) {
   Py_InitModule3("helloworld", helloworld_funcs,
                  "Extension module example!");
}