class Empleado (object):
    def __init__ (self, nif, sueldo, casado, hijos, irpf, pagoHora, hExtra):
        self.nif= nif;
        self.sueldo = sueldo;
        self.casado= casado;
        self.hijos= hijos;
        self.irpf=irpf;
        self.pagoHora= pagoHora;
        self.hExtra= hExtra;

        
    def devolverComplemento (self):
       return self.hExtra * self.pagoHora;
    
    def devolverSueldoBruto (self):
        return self.sueldo + self.devolverComplemento();

    def devolverSueldoNeto (self):
        return self.devolverSueldoBruto() - self.devolverRetencion();

    def devolverRetencion (self):
        if self.casado==True:
            self.irpf= self.irpf - 0.02
        if self.hijos > 0:
            self.irpf= self.irpf - 0.01
        return self.sueldo * self.irpf;

    def verInformacion (self):
        print 'Informacion del empleado:'; 
        print 'sueldo bruto: ', self.devolverSueldoBruto();
        print 'complemento por horas extra: ', self.devolverComplemento();
        print 'retencion del irpf: ', self.devolverRetencion();
        print 'sueldo neto: ', self.devolverSueldoNeto();

    def imprimirTodo(self):
        print 'Datos del empleado:';
        print 'NIF:', self.nif;
        print 'sueldo base:', self.sueldo;
        print 'irpf:', self.irpf;
        print 'pago por horas extra: ', self.pagoHora;
        print 'hijos: ', self.hijos;
        if self.casado== True:
            print 'casado';
        else:
            print 'soltero';


miEmpleado = Empleado ('12345678A',1500, True, 2, 0.16, 50, 5);

miEmpleado.imprimirTodo();
print
miEmpleado.verInformacion();