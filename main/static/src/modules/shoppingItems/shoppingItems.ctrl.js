(function (ng) {
    var mod = ng.module('shoppingItemsModule');

    mod.controller('shoppingItemsCtrl', ['$scope', 'shoppingItemsService','$routeParams', function ($scope, shoppingItemsService,$routeParams) {

        $scope.loading = true;

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.getShoppingItems = function () {
            return shoppingItemsService.svcGetShoppingItems().then(function (response) {
                $scope.loading = false;
                console.log(response);
                $scope.shoppingItems = response.data;
            }, responseError);
        };
        
        this.addProduct = function (id) {
            
           return shoppingItemsService.svcAddProduct(id).then(function (response) {
                    console.log('El producto: '+id + '- response: '+ response.data);
                    alert('Producto agregado.');
                    window.location.assign('#/main');
                    window.location.reload(true);
                }, responseError);

        };
        
        

    }]);
})(window.angular);