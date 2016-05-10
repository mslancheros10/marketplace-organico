(function (ng) {
    var mod = ng.module('productsModule');

    mod.service('productsService', ['$http', 'productsContext', function ($http, context) {

        this.getProducts = function () {
            return $http({
                method: 'GET',
                url: '/allProducts'
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

        this.getProductsFarm = function () {
            return $http({
                method: 'GET',
                url: '/productsFarm'
            });
        };

        this.addProduct = function (id,unitName,unitValue,price,quantity) {
            return $http({
                method: 'GET',
                url: '/addProductFarm/'+id+'/'+unitName+'/'+unitValue+'/'+price+'/'+quantity
            });
        };

        this.regsisterList = function (data) {
            return $http({
                method: 'POST',
                url: '/registerProductList',
                data:data
            });
        };

    }]);
})(window.angular);
