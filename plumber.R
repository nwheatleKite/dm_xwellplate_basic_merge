library(reticulate)
library(plumber)

reticulate::source_python('python_scripts.py')

#* @serializer unboxedJSON
#* @post /basic_merge
function(req) {
    xwellplate <- req$body$plate_layout
    rawdata_list <- req$body$rawdata
    output <- basic_merge(xwellplate, rawdata_list)
    return(output)
}

#* @serializer unboxedJSON
#* @post /validate_xwellplate
function(req) {
    xwellplate <- req$body$plate_layout
    rawdata_list <- req$body$rawdata
    output <- basic_merge(xwellplate, rawdata_list)
    return(output)
}

#* @serializer unboxedJSON
#* @post /validate_rawdata
function(req) {
    rawdata_list <- req$body$data
    output <- basic_merge(xwellplate, rawdata_list)
    return(output)
}