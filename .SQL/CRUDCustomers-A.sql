CREATE OR REPLACE PROCEDURE create_customer(
    p_customer_id IN NUMBER,
    p_cust_first_name IN VARCHAR2,
    p_cust_last_name IN VARCHAR2,
    p_credit_limit IN NUMBER,
    p_cust_email IN VARCHAR2,
    p_income_level IN VARCHAR2,
    p_region IN VARCHAR2
)
IS
BEGIN
    IF p_region IN ('A', 'B') THEN
        INSERT INTO customers_fragmented_db1 (
            CUSTOMER_ID, CUST_FIRST_NAME, CUST_LAST_NAME,
            CREDIT_LIMIT, CUST_EMAIL, INCOME_LEVEL, REGION
        ) VALUES (
            p_customer_id, p_cust_first_name, p_cust_last_name,
            p_credit_limit, p_cust_email, p_income_level, p_region
        );
    ELSIF p_region IN ('C', 'D') THEN
        INSERT INTO customers_db2 (
            CUSTOMER_ID, CUST_FIRST_NAME, CUST_LAST_NAME,
            CREDIT_LIMIT, CUST_EMAIL, INCOME_LEVEL, REGION
        ) VALUES (
            p_customer_id, p_cust_first_name, p_cust_last_name,
            p_credit_limit, p_cust_email, p_income_level, p_region
        );
    ELSE
        RAISE_APPLICATION_ERROR(-20001, 'Región no válida. Las regiones válidas son A, B, C o D.');
    END IF;
END create_customer;

CREATE OR REPLACE PROCEDURE update_customer(
    p_customer_id IN NUMBER,
    p_cust_first_name IN VARCHAR2,
    p_cust_last_name IN VARCHAR2,
    p_credit_limit IN NUMBER,
    p_cust_email IN VARCHAR2,
    p_income_level IN VARCHAR2,
    p_region IN VARCHAR2
)
IS
BEGIN
    IF p_region IN ('A', 'B') THEN
        UPDATE customers_fragmented_db1 SET
            CUST_FIRST_NAME = p_cust_first_name,
            CUST_LAST_NAME = p_cust_last_name,
            CREDIT_LIMIT = p_credit_limit,
            CUST_EMAIL = p_cust_email,
            INCOME_LEVEL = p_income_level
        WHERE CUSTOMER_ID = p_customer_id;
    ELSIF p_region IN ('C', 'D') THEN
        UPDATE customers_db2 SET
            CUST_FIRST_NAME = p_cust_first_name,
            CUST_LAST_NAME = p_cust_last_name,
            CREDIT_LIMIT = p_credit_limit,
            CUST_EMAIL = p_cust_email,
            INCOME_LEVEL = p_income_level
        WHERE CUSTOMER_ID = p_customer_id;
    ELSE
        RAISE_APPLICATION_ERROR(-20001, 'Región no válida. Las regiones válidas son A, B, C o D.');
    END IF;
END update_customer;


CREATE OR REPLACE PROCEDURE delete_customer(
    p_customer_id IN NUMBER
)
IS
    v_region VARCHAR2(1);
BEGIN
    SELECT REGION INTO v_region
    FROM (
        SELECT REGION FROM customers_fragmented_db1 WHERE CUSTOMER_ID = p_customer_id
        UNION ALL
        SELECT REGION FROM customers_db2 WHERE CUSTOMER_ID = p_customer_id
    );
    IF v_region IN ('A', 'B') THEN
        DELETE FROM customers_fragmented_db1
        WHERE CUSTOMER_ID = p_customer_id;
    ELSIF v_region IN ('C', 'D') THEN
        DELETE FROM customers_db2
        WHERE CUSTOMER_ID = p_customer_id;
    ELSE
        RAISE_APPLICATION_ERROR(-20002, 'El cliente con ID ' || TO_CHAR(p_customer_id) || ' no se encontró en ninguna región.');
    END IF;
END delete_customer;

CREATE OR REPLACE PROCEDURE list_all_customers(
    p_cursor OUT SYS_REFCURSOR
)
IS
BEGIN
    OPEN p_cursor FOR
        SELECT * FROM customers_fragmented_db1
        UNION ALL
        SELECT * FROM customers_db2;
END list_all_customers;



