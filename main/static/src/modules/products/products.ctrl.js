(function (ng) {
    var mod = ng.module('productsModule');

    mod.controller('productsCtrl', ['$scope', 'productsService', '$window', '$filter',  function ($scope, productsService, $window, $filter) {

        var precio = 0;

        $scope.loading = true;

        $scope.filteredProducts = [];
        $scope.currentPage = 1;
        $scope.numPerPage = 6;
        $scope.maxSize = 10;

        $scope.newProd = {
            idProduct:'',
            unit_value:'',
            price:'',
            unit_name:'',
            quantity:''
        };

        $scope.$watch('search', function(val) {
            $scope.filteredProducts = $scope.products
            $filter('filter')($scope.filteredProducts, val);
        });

        $scope.$watch('currentPage + numPerPage', function() {
            var begin = (($scope.currentPage - 1) * $scope.numPerPage);
            var end = begin + $scope.numPerPage;

            //$scope.filteredProducts = $scope.products.slice(begin, end);
        });

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.getProducts = function () {
            if(!$scope.certified){
                return productsService.getProducts().then(function (response) {
                    $scope.loading = false;
                    console.log(response);
                    $scope.products = response.data;

                    var begin = (($scope.currentPage - 1) * $scope.numPerPage);
                    var end = begin + $scope.numPerPage;

                    $scope.filteredProducts = $scope.products.slice(begin, end);

                    }, responseError);
            }
            else{
                return productsService.getCertifiedProducts().then(function (response) {
                    $scope.loading = false;
                    console.log(response);
                    $scope.products = response.data;
                    var begin = (($scope.currentPage - 1) * $scope.numPerPage);
                    var end = begin + $scope.numPerPage;

                    $scope.filteredProducts = $scope.products.slice(begin, end);
                }, responseError);
            }

        };

        this.getDetails = function (id) {
            $('#msgNoAutenticado').html(" ");
           return productsService.getDetails(id).then(function (response) {
                $scope.details = response.data;
            }, responseError);

        };


        $scope.addMyProduct = function () {
            var id = $scope.newProd.idProduct;
            var unitName = $scope.newProd.unit_name;
            var unitValue = $scope.newProd.unit_value;
            var price = $scope.newProd.price;
            var quantity = $scope.newProd.quantity;

            document.getElementById("addProductModal").style.display="none";
            var fades = document.getElementsByClassName("modal-backdrop fade in");
            for (var i = 0; i < fades.length; i++) {
                fades[i].style.display="none";
            }

            return productsService.addProduct(id, unitName, unitValue, price, quantity).then(function (response) {

                console.log(response.data);

                $('#table-products').bootstrapTable('load', response.data);

                $scope.product = response.data;

            }, responseError);

        };


        this.getProductsFarm = function () {

            return productsService.getProductsFarm().then(function (response) {

                $scope.loading = false;
                console.log(response);
                $scope.products = response.data;

                var begin = (($scope.currentPage - 1) * $scope.numPerPage);
                var end = begin + $scope.numPerPage;

                $scope.filteredProducts = $scope.products.slice(begin, end);

            }, responseError);
        };


        this.shareTwitter = function(details){

            $window.open("https://twitter.com/intent/tweet?text=Encontré este grandioso producto: " +details.name+" a $" + details.price+ " visita:&url=https://grupo5-marketplace-organico.herokuapp.com&via=MpOrganico");
        };

        this.initDetails = function(){

            $scope.details = {};

        };

        $scope.registerList = function () {
            productsService.regsisterList({
                    'list': document.getElementById("productList").value
            });
        }



        var setProductsFarm = function(){

            var url_submit = '/productsFarm';
            var url_mod = 'id';

            $.ajax({type:'GET',async:true,url:url_submit,
                error:function(jqXHR,textStatus,errorThrown){
                },
                success:function(data,textStatus,jqXHR){
                       $('#table-products').bootstrapTable(
                            {   data:data,
                                columns:[
                                    {field:'image',
                                        formatter:function(value,row,index){return '<img src="'+value+'" alt="Smiley face" height="42" width="42">';}},
                                    {field:'name',
                                        formatter:function(value,row,index){return value;}},
                                    {field:'description',
                                        formatter:function(value,row,index){return value;}},
                                    {field:'price',
                                        formatter:function(value,row,index){return value;}},
                                    {field:'id',
                                        formatter:function(value,row,index){return '<div style="text-align:center"><i class="fa fa-pencil"></i> </a></div>';}},
                                    {field:'id',
                                        formatter:function(value,row,index){return '<div style="text-align:center"><i class="fa fa-trash"></i> </a></div>';}}
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

        angular.element(document).ready(function(){setProductsFarm()});

    }]);
})(window.angular);



