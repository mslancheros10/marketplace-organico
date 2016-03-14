(function (ng) {
    var mod = ng.module('productsModule');

    mod.service('productsService', ['$http', 'productsContext', function ($http, context) {

        this.getProducts = function () {
            return $http({
                method: 'GET',
                url: '/products'
            });
        };

    }]);
})(window.angular);