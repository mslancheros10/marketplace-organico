
var setProductsFarm=function(){

    var url_submit = '/productsFarm/2';
    var url_mod = 'id';

    $.ajax({type:'GET',async:true,url:url_submit,
        error:function(jqXHR,textStatus,errorThrown){
           alert('error');
        },
        success:function(data,textStatus,jqXHR){
               $('#table-products').bootstrapTable(
                    {   data:data,
                        columns:[
                            {field:'image_url',
                                formatter:function(value,row,index){return '<img src='+value+' alt="Smiley face" height="42" width="42">';}},
                            {field:'name',
                                formatter:function(value,row,index){return value;}},
                            {field:'description',
                                formatter:function(value,row,index){return value;}},
                            {field:'price',
                                formatter:function(value,row,index){return value;}},
                            {field:'id',
                                formatter:function(value,row,index){return '<div style="text-align:center"><a href="'+url_mod.replace('id',row.id)+'" > <i class="fa fa-pencil"></i> </a></div>';}},
                            {field:'id',
                                formatter:function(value,row,index){return '<div style="text-align:center"><a href="'+url_mod.replace('id',row.id)+'" data-role="disabled"> <i class="fa fa-trash"></i> </a></div>';}}
                        ],

                        pagination:false,
                        pageSize:10,
                        per_page: 100,
                        sortable:true,
                        striped:true,
                        sidePagination:'client',
                    }
                );

        }})
}

$(document).ready(function(){setProductsFarm()});


