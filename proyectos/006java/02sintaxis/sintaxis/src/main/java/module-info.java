module com.solucionespp.sintaxis {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.solucionespp.sintaxis to javafx.fxml;
    exports com.solucionespp.sintaxis;
}