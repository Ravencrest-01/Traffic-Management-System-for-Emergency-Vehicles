input_string = "^ ^ > ^ ^ > > >"
output_list = input_string.split()
formatted_output = ', '.join(["'" + x + "'" for x in output_list])
print(formatted_output)
