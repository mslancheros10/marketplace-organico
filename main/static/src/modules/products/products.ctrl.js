(function (ng) {
    var mod = ng.module('productsModule');

    mod.controller('productsCtrl', ['$scope', 'productsService', function ($scope, productsService) {

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
            return productsService.getProducts().then(function (response) {
                $scope.loading = false;
                console.log(response);
                $scope.products = response.data;

                var begin = (($scope.currentPage - 1) * $scope.numPerPage);
                var end = begin + $scope.numPerPage;

                $scope.filteredProducts = $scope.products.slice(begin, end);

            }, responseError);
        };

    }]);
})(window.angular);
