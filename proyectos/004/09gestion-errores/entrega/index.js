const logger = require('./logger')

try {
    logger.info("Hola esto es un mensaje informativo")
} catch (error) {
    logger.error("Esto es un error")
}