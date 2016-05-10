(function (ng) {
    var mod = ng.module('productsModule');

    mod.controller('productsCtrl', ['$scope', 'productsService', '$window', '$filter',  function ($scope, productsService, $window, $filter) {

        $scope.loading = true;

        $scope.filteredProducts = [];
        $scope.currentPage = 1;
        $scope.numPerPage = 6;
        $scope.maxSize = 10;

        $scope.$watch('search', function(val) {
            $scope.filteredProducts = $scope.products
            $filter('filter')($scope.filteredProducts, val);
        });

        $scope.$watch('currentPage + numPerPage', function() {
            var begin = (($scope.currentPage - 1) * $scope.numPerPage);
            var end = begin + $scope.numPerPage;

            $scope.filteredProducts = $scope.products.slice(begin, end);
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


        this.getProductsFarm = function (user) {

            return productsService.getProductsFarm(user).then(function (response) {
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



    }]);
})(window.angular);
