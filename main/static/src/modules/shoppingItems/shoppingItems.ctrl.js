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
                $scope.shoppingItems = response.data;
                console.log('Respuesta de la vista: '+response);
            }, responseError);
        };

        this.addProduct = function (id, tipo) {
           return shoppingItemsService.svcAddProduct(id,tipo).then(function (response) {
                    if(response.data == 'no autenticado'){
                        if(tipo == 'canasta'){
                            $('#mostrarModal').click();
                        }else{
                            $('#msgAutenticacion').html('Para agregar este producto debe estar autenticado.');
                        }
                    }else{
                        alert('entrar');
                        window.location.assign('#/main');
                        window.location.reload(true);
                    }
                    console.log('Info Angular - Parametros enviados: idProducto: '+id +', tipo: '+tipo+ ', respuesta de la vista: '+ response.data);

                }, responseError);

        };



    }]);
})(window.angular);
