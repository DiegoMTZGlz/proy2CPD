CREATE OR REPLACE PROCEDURE create_order(
    p_order_id IN NUMBER,
    p_order_date IN TIMESTAMP,
    p_order_mode IN VARCHAR2,
    p_customer_id IN NUMBER,
    p_order_status IN NUMBER,
    p_order_total IN NUMBER,
    p_sales_rep_id IN NUMBER,
    p_promotion_id IN NUMBER
)
IS
BEGIN
    INSERT INTO orders (
        ORDER_ID, ORDER_DATE, ORDER_MODE, CUSTOMER_ID,
        ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID
    ) VALUES (
        p_order_id, p_order_date, p_order_mode, p_customer_id,
        p_order_status, p_order_total, p_sales_rep_id, p_promotion_id
    ); 
    COMMIT;
END create_order;
/

CREATE OR REPLACE FUNCTION read_order(
    p_order_id IN NUMBER
) RETURN SYS_REFCURSOR
IS
    v_cursor SYS_REFCURSOR;
BEGIN
    OPEN v_cursor FOR
        SELECT * FROM orders WHERE ORDER_ID = p_order_id;
    RETURN v_cursor;
END read_order;
/

CREATE OR REPLACE PROCEDURE list_orders(
    p_cursor OUT SYS_REFCURSOR
)
IS
BEGIN
    OPEN p_cursor FOR
        SELECT * FROM orders;
END list_orders;
/

CREATE OR REPLACE PROCEDURE update_order(
    p_order_id IN NUMBER,
    p_order_date IN TIMESTAMP,
    p_order_mode IN VARCHAR2,
    p_customer_id IN NUMBER,
    p_order_status IN NUMBER,
    p_order_total IN NUMBER,
    p_sales_rep_id IN NUMBER,
    p_promotion_id IN NUMBER
)
IS
BEGIN
    UPDATE orders SET
        ORDER_DATE = p_order_date,
        ORDER_MODE = p_order_mode,
        CUSTOMER_ID = p_customer_id,
        ORDER_STATUS = p_order_status,
        ORDER_TOTAL = p_order_total,
        SALES_REP_ID = p_sales_rep_id,
        PROMOTION_ID = p_promotion_id
    WHERE ORDER_ID = p_order_id;
    COMMIT;
END update_order;
/

CREATE OR REPLACE PROCEDURE delete_order(
    p_order_id IN NUMBER
)
IS
BEGIN
    DELETE FROM orders WHERE ORDER_ID = p_order_id;
    COMMIT;
END delete_order;
/

CREATE OR REPLACE PROCEDURE create_order_item(
    p_order_id IN NUMBER,
    p_line_item_id IN NUMBER,
    p_product_id IN NUMBER,
    p_unit_price IN NUMBER,
    p_quantity IN NUMBER
)
IS
BEGIN
    INSERT INTO order_items (
        ORDER_ID, LINE_ITEM_ID, PRODUCT_ID, UNIT_PRICE, QUANTITY
    ) VALUES (
        p_order_id, p_line_item_id, p_product_id, p_unit_price, p_quantity
    );
    COMMIT;
END create_order_item;
/

CREATE OR REPLACE PROCEDURE list_order_items(
    p_cursor OUT SYS_REFCURSOR
)
IS
BEGIN
    OPEN p_cursor FOR
        SELECT * FROM order_items;
END list_order_items;
/

CREATE OR REPLACE PROCEDURE update_order_item(
    p_order_id IN NUMBER,
    p_line_item_id IN NUMBER,
    p_product_id IN NUMBER,
    p_unit_price IN NUMBER,
    p_quantity IN NUMBER
)
IS
BEGIN
    UPDATE order_items SET
        PRODUCT_ID = p_product_id,
        UNIT_PRICE = p_unit_price,
        QUANTITY = p_quantity
    WHERE ORDER_ID = p_order_id AND LINE_ITEM_ID = p_line_item_id;
    COMMIT;
END update_order_item;
/

CREATE OR REPLACE PROCEDURE delete_order_item(
    p_order_id IN NUMBER,
    p_line_item_id IN NUMBER
)
IS
BEGIN
    DELETE FROM order_items WHERE ORDER_ID = p_order_id AND LINE_ITEM_ID = p_line_item_id;
    COMMIT;
END delete_order_item;
/

CREATE OR REPLACE PROCEDURE create_product_information(
    p_product_id IN NUMBER,
    p_product_name IN VARCHAR2,
    p_product_description IN VARCHAR2,
    p_category_id IN NUMBER,
    p_weight_class IN NUMBER,
    p_warranty_period IN INTERVAL YEAR TO MONTH,
    p_supplier_id IN NUMBER,
    p_product_status IN VARCHAR2,
    p_list_price IN NUMBER,
    p_min_price IN NUMBER,
    p_catalog_url IN VARCHAR2
)
IS
BEGIN
    INSERT INTO product_information (
        PRODUCT_ID, PRODUCT_NAME, PRODUCT_DESCRIPTION, CATEGORY_ID, WEIGHT_CLASS,
        WARRANTY_PERIOD, SUPPLIER_ID, PRODUCT_STATUS, LIST_PRICE, MIN_PRICE, CATALOG_URL
    ) VALUES (
        p_product_id, p_product_name, p_product_description, p_category_id, p_weight_class,
        p_warranty_period, p_supplier_id, p_product_status, p_list_price, p_min_price, p_catalog_url
    );
    COMMIT;
END create_product_information;
/

CREATE OR REPLACE PROCEDURE list_product_information(
    p_cursor OUT SYS_REFCURSOR
)
IS
BEGIN
    OPEN p_cursor FOR
        SELECT * FROM product_information;
END list_product_information;
/

CREATE OR REPLACE PROCEDURE update_product_information(
    p_product_id IN NUMBER,
    p_product_name IN VARCHAR2,
    p_product_description IN VARCHAR2,
    p_category_id IN NUMBER,
    p_weight_class IN NUMBER,
    p_warranty_period IN INTERVAL YEAR TO MONTH,
    p_supplier_id IN NUMBER,
    p_product_status IN VARCHAR2,
    p_list_price IN NUMBER,
    p_min_price IN NUMBER,
    p_catalog_url IN VARCHAR2
)
IS
BEGIN
    UPDATE product_information SET
        PRODUCT_NAME = p_product_name,
        PRODUCT_DESCRIPTION = p_product_description,
        CATEGORY_ID = p_category_id,
        WEIGHT_CLASS = p_weight_class,
        WARRANTY_PERIOD = p_warranty_period,
        SUPPLIER_ID = p_supplier_id,
        PRODUCT_STATUS = p_product_status,
        LIST_PRICE = p_list_price,
        MIN_PRICE = p_min_price,
        CATALOG_URL = p_catalog_url
    WHERE PRODUCT_ID = p_product_id;
    COMMIT;
END update_product_information;
/

CREATE OR REPLACE PROCEDURE delete_product_information(
    p_product_id IN NUMBER
)
IS
BEGIN
    DELETE FROM product_information WHERE PRODUCT_ID = p_product_id;
    COMMIT;
END delete_product_information;
/