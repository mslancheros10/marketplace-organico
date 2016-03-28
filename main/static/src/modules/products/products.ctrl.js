(function (ng) {
    var mod = ng.module('productsModule');

    mod.controller('productsCtrl', ['$scope', 'productsService', function ($scope, productsService) {

        $scope.loading = true;

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
                }, responseError);
            }
            else{
                return productsService.getCertifiedProducts().then(function (response) {
                    $scope.loading = false;
                    console.log(response);
                    $scope.products = response.data;
                }, responseError);
            }

        };

    }]);
})(window.angular);
