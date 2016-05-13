(function (ng) {
    var mod = ng.module('productsModule');

    mod.service('productsService', ['$http', 'productsContext', function ($http, context) {

        this.getProducts = function () {
            return $http({
                method: 'GET',
                url: '/products'
            });
        };

        this.getDetails = function (id){
            return $http ({
                method: 'GET',
                url: '/details/'+id
            });
        };

        this.getCertifiedProducts = function () {
            return $http({
                method: 'GET',
                url: '/certifiedProducts'
            });
        };

        this.getProductsFarm = function (user) {
            return $http({
                method: 'GET',
                url: '/productsFarm/'+user
            });
        };

        this.addProduct = function (data) {
            return $http({
                method: 'POST',
                url: '/addProductFarm',
                data:data
            });
        };

    }]);
})(window.angular);
