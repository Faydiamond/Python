varr <- "melero"
print(varr)
cuboo <- function(x) 
{
  x^3 -(3^x) * sin(x)
}
print(cuboo(4))

prodcutt <- function(x,y)
{
  x*y
}
print(prodcutt(4,5))
#sumar
sumar <- function(x)
{
  res <- x +10;
  res
}
sumar(10)

ls()
rm (varr)
ls()