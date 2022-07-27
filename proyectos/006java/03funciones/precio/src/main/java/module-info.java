module com.example.precio {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.precio to javafx.fxml;
    exports com.example.precio;
}