library(reticulate)
library(plumber)

reticulate::source_python('python_funcs.py')

#* @assets ./example_files /example_file
list()

#* @get /example_files_list
function() {
    list.files(path="./example_files")
}

#* @serializer unboxedJSON
#* @post /basic_merge
function(req) {
    xwellplate <- req$body$plate_layout
    rawdata_list <- req$body$raw_data
    output <- basic_merge(xwellplate, rawdata_list)
    return(output)
}

#* @serializer unboxedJSON
#* @post /validate_xwellplate
function(req) {
    xwellplate <- req$body$data
    output <- validate_xwellplate(xwellplate)
    return(output)
}

#* @serializer unboxedJSON
#* @post /validate_rawdata
function(req) {
    rawdata_list <- req$body$data
    output <- validate_rawdata(rawdata_list)
    return(output)
}