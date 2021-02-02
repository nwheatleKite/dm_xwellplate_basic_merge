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
#* @post /basic_merge2
function(req) {
    xwellplate <- req$body$plate_layout
    rawdata_list <- req$body$raw_data
    # output <- basic_merge(xwellplate, rawdata_list)
    is_string <- is.character(rawdata_list) & length(rawdata_list) == 1
    is_vector <- is.vector(rawdata_list)
    is_dataframe <- is.data.frame(rawdata_list)
    is_list <- is.list(rawdata_list)
    thetype <- typeof(rawdata_list)

    # leng <- len(rawdata_list)
   list('is_string' = is_string, 'is_vector'=is_vector,'rawdata_list'=rawdata_list, 'is_dataframe'=is_dataframe, 'is_list'=is_list, 'thetype'=thetype)
}

#* @serializer unboxedJSON
#* @post /basic_merge3
function(req) {
    xwellplate <- req$body$plate_layout
    rawdata_list <- req$body$raw_data
    # output <- basic_merge(xwellplate, rawdata_list)
    return(xwellplate)
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