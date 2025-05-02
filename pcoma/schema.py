instructions = [
    "SET FOREIGN_KEY_CHECKS=0;",
    "DROP TABLE IF EXISTS product;",
    "DROP TABLE IF EXISTS user;",
    "SET FOREIGN_KEY_CHECKS=1;",
    """
        CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(200) NOT NULL
        )
    """
        ,
    """
        CREATE TABLE product (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) UNIQUE NOT NULL,
            price INT NOT NULL,
            description TEXT,
            brand VARCHAR(50) NOT NULL,
            image VARCHAR(50) NOT NULL
        )
    """
        ,
    """
        INSERT INTO product (name, price, description, brand, image) values
        ("Fuji", 180, "Kombat Fuji by Manu Martin", "Kombat","kombat-fuji.webp"),
        ("Krakatoa", 180, "Kombat Krakatoa by Manu Martin", "Kombat", "kombat-krakatoa.webp"),
        ("Teide", 180, "Kombat Teide by Manu Martin", "Kombat", "kombat-teide.webp"),
        ("Ultimate Pro+", 300, "Oxdog Ultimate Pro+", "Oxdog", "oxdog-ultimate-pro-plus.png"),
        ("Pure Pro+", 250, "Oxdog Pure Pro+", "Oxdog", "oxdog-pure-pro-plus.png")
    """
 
]
