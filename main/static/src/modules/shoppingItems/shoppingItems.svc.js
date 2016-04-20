(function (ng) {
    var mod = ng.module('shoppingItemsModule');

    mod.service('shoppingItemsService', ['$http', 'shoppingItemsContext', function ($http) {

        this.svcGetShoppingItems = function () {
            return $http({
                method: 'GET',
                url: '/shoppingItems'
            });
        };
        this.svcAddProduct = function (id, tipo){
            return $http ({
                method: 'GET',
                url: '/addProduct/'+id+'/'+tipo
            });
        };
        this.svcDeleteProduct = function (id){
            return $http ({
                method: 'GET',
                url: '/deleteProduct/'+id
            });
        };

    }]);
})(window.angular);
