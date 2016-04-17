(function (ng) {
    var mod = ng.module('shoppingItemsModule');

    mod.service('shoppingItemsService', ['$http', 'shoppingItemsContext', function ($http, context) {

        this.svcGetShoppingItems = function () {
            return $http({
                method: 'GET',
                url: '/shoppingItems'
            });
        };
        this.svcAddProduct = function (id){
            return $http ({
                method: 'GET',
                url: '/addProduct/'+id
            });
        };

    }]);
})(window.angular);