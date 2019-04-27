#include <Python/Python.h>

int* ptr;

static PyObject* helloworld(PyObject* self) {
   ptr = (int*) malloc(250*1024 * sizeof(int));
   printf("%s\n","Native call invoked");
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