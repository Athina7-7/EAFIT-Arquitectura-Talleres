import datetime

from ..domain.interfaces import ProcesadorPago


class BancoNacionalProcesador(ProcesadorPago):
    """
    Implementación concreta de la infraestructura.
    Simula un banco local escribiendo en un log.
    """

    def pagar(self, monto: float) -> bool:
        # Sustituye por tu identidad (tutorial): Athina Cappelletti
        archivo_log = "pagos_locales_Athina_Cappelletti.log"
        with open(archivo_log, "a") as f:
            f.write(
                f"[{datetime.datetime.now()}] Transaccion exitosa por : ${monto}\n"
            )
        return True
