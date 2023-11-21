# O assert sempre verifica se o retorno da condição é True
assert True

# assert numbers
num_esperado = 3
num_obtido = 2
# assert num_esperado > num_obtido, f"Esperado {num_esperado} não é maior que o número atual {num_obtido}."
# assert num_esperado != num_obtido, f"Esperado {num_esperado} é diferente que o número atual {num_obtido}."

# assert text
# text_esperado = "Selenium Webdriver"
# text_obtido = "Selenium webdriver"
# assert text_esperado.lower() == text_obtido.lower(), f"Esperado {text_esperado}. Atual {text_obtido}."
# lower transforma o texto para tudo minuscula

# assert text in string
text_esperado = "Selenium Webdriver"
text_obtido = "Selenium W ebdriver"
# assert text_esperado in text_obtido, f"Esperado '{text_esperado}'. Atual '{text_obtido}'."
assert text_esperado not in text_obtido, f"Esperado '{text_esperado}'. Atual '{text_obtido}'."

# assert is_displayed/is enabled/is_selected
