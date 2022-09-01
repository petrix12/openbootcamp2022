module com.example.clases {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.clases to javafx.fxml;
    exports com.example.clases;
}