module com.pruebas.hola {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.pruebas.hola to javafx.fxml;
    exports com.pruebas.hola;
}