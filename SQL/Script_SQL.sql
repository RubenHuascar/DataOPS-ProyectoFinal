USE Kaggle
GO

---En caso no existe la tabla
IF NOT EXISTS (SELECT * FROM sys.tables WHERE object_id = OBJECT_ID(N'dbo.olympics') AND type='U')
	CREATE TABLE dbo.olympics(
	NOC VARCHAR(10),
	Gold INT,
	Silver INT,
	Bronze INT,
	Total INT
	)

	GO
	--Si ya existe la tabla
	TRUNCATE TABLE dbo.olympics;
	GO

	--Importar dbo.olympics
	BULK INSERT dbo.olympics
	FROM 'C:\Users\ASUS\Downloads\DataOPS\Proyecto_Parcial\dataset\Athens 2004 Olympics Nations Medals.csv'
	WITH
	(
		FIRSTROW = 2,  --empieza en la 2da fila, ya que la 1era es la cabecera
		FIELDTERMINATOR = ',', --indicamos separador de columnas
		ROWTERMINATOR = '0X0a' -----SALTO DE LINEA
	)

	GO









