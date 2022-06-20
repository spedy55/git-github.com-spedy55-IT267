from measure_convert import c_to_i,i_to_c

lenght = float(input("กรอกความยาวที่ต้องการ : "))
print(f'===============')
print(f'{lenght} นิ้ว = {c_to_i(lenght):.2f} เซนติเมตร')
print(f'{lenght} เซนติเมตร = {i_to_c(lenght):.2f} นิ้ว')