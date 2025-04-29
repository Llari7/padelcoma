instructions = [
    "SET FOREIGN_KEY_CHECKS=0;",
    "DROP TABLE IF EXISTS product;",
    "DROP TABLE IF EXISTS user;",
    "SET FOREIGN_KEY_CHECKS=1;",
    """
        CREATE TABLE user (
                id INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL
        )
    """
        ,
    """
        CREATE TABLE product (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) UNIQUE NOT NULL,
            price INT NOT NULL,
            description TEXT NOT NULL
        )
    """
]
