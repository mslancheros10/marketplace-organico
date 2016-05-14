(function (ng) {
    var mod = ng.module('productsModule');

    mod.service('productsService', ['$http', 'productsContext', '$location', function ($http, context, $location) {

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

        this.regsisterList = function (data) {
            return $http({
                method: 'POST',
                url: '/registerProductList',
                data: data
            }).success(function (response) {
                if(response=='OK'){
                    $location.path('main');

                }else{
                    alert("Debe iniciar sesión como administrador para realizar esta tarea.")
                }
            }).error(function (response) {
                alert("La lista de entrada tiene errores.")
            });
        };

    }]);
})(window.angular);
