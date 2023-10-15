import doctest

if __name__ == "__main__":
    print("Iniciando Doctest")
    print("Testando get_data_ready...")
    doctest.testfile("test-get_data_ready.txt")
    print("Testando size_manager...")
    doctest.testfile("test-size_manager.txt")
    print("Doctest concluído!")
