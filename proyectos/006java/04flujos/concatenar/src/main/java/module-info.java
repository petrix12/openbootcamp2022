module com.example.concatenar {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.concatenar to javafx.fxml;
    exports com.example.concatenar;
}