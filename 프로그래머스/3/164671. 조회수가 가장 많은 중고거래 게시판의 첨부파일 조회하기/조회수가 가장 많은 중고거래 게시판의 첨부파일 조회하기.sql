SELECT CONCAT('/home/grep/src/', B.BOARD_ID, "/", FILE_ID, FILE_NAME, FILE_EXT) FILE_PATH
FROM (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
) B
JOIN USED_GOODS_FILE F
ON B.BOARD_ID = F.BOARD_ID
ORDER BY FILE_ID DESC
