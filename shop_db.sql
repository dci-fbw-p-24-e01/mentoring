-- Active: 1705494784526@@127.0.0.1@5432@shop_db


-- create table product (
-- id serial primary key,
-- name varchar(120),
-- price decimal,
-- quantity int,
-- created_at timestamp
-- );

-- INSERT INTO product (
--     name, price, quantity, created_at
-- ) VALUES
-- ('Phone', 999.99, 100, now()),
-- ('Laptop', 1500.99, 50, now()),
-- ('Keyboard', 100.99, 25, now()),
-- ('Monitor', 400.99, 70, now()),
-- ('Mouse', 50.99, 30, now()),
-- ('Headphone', 80.99, 40, now()),
-- ('Camera', 800.99, 120, now()),
-- ('PS5', 700.99, 20, now());


-- SELECT * FROM product;


-- SELECT 
--     name, 
--     price,
--     (SELECT MAX(price) FROM product) AS max_price
-- FROM 
--     product;


-- SELECT MAX(price) FROM product AS max_price;



-- SELECT 
--     name, 
--     price,
--     (SELECT MAX(price) FROM product) AS max_price,
--     (SELECT AVG(price) FROM product) AS avg_price
-- FROM 
--     product;


-- SELECT 
--     name, 
--     price,
--     (SELECT MAX(price) FROM product) AS max_price,
--     (SELECT AVG(price) FROM product) AS avg_price,
--     (SELECT COUNT(price) FROM product) AS count_price,
--     (SELECT COUNT(name) FROM product) AS count_name
-- FROM 
--     product;




-- SELECT 
--     name, 
--     price
-- FROM 
--     product
-- WHERE
--     price > (SELECT price FROM product WHERE name = 'Monitor')  
-- ;


-- SELECT price FROM product WHERE name = 'Monitor';


-- SELECT 
--     name, 
--     price
-- FROM 
--     product
-- WHERE
--     price < (SELECT price FROM product WHERE name = 'Monitor')
-- ;


-- SELECT 
--     name, 
--     price
-- FROM 
--     product
-- WHERE
--     price > (SELECT AVG(price) FROM product)
-- ;


-- SELECT 
--     name, 
--     price,
--     quantity
-- FROM 
--     product p1
-- WHERE
--     quantity > (SELECT AVG(quantity) FROM product)
-- ;



-- SELECT 
--     name, 
--     price,
--     quantity
-- FROM 
--     product p1
-- WHERE
--     p1.name = 'Camera'
-- ;

-- SELECT 
--     p1.name, 
--     p1.price AS product_price,
--     p1.quantity,
--     p2.price AS electronics_price
-- FROM 
--     product p1
-- JOIN
--     product p2
-- ON
--     p1.id = p2.id
-- WHERE
--     p1.price = p2.price
-- ;



SELECT 
    p1.name, 
    p1.price AS product_price,
    p1.quantity,
    p2.price AS electronics_price
FROM 
    product p1
JOIN
    product p2
ON
    p1.id = p2.id
WHERE
    (SELECT MIN(price) FROM product) < (SELECT AVG(price) FROM product)
ORDER BY p1.quantity DESC
LIMIT 3
;


--     (SELECT MIN(price) FROM product) = (SELECT AVG(price) FROM electronics)
-- ;