(function (ng) {
    var mod = ng.module('shoppingItemsModule');

    mod.controller('shoppingItemsCtrl', ['$scope', 'shoppingItemsService','$routeParams', function ($scope, shoppingItemsService,$routeParams) {

        $scope.loading = true;

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.getShoppingItems = function () {
             $('#msgProcesando').html(" ");
            return shoppingItemsService.svcGetShoppingItems().then(function (response) {
                $scope.loading = true;
                $scope.shoppingItems = response.data;
                $scope.loading = false;
            }, responseError);
        };

        this.addProduct = function (id, tipo) {

            $('#msgNoAutenticado').html("Procesando...");

            shoppingItemsService.svcAddProduct(id,tipo).then(function (response) {
                if(response.data == 'no autenticado'){
                    if(tipo == 'canasta'){
                        $('#mostrarModal').click();
                    }else{
                        document.getElementById("msgNoAutenticado").innerHTML = "Para agregar este producto debe estar autenticado."

                    }
                }else{
                    if(tipo=='product') {
                        $('#msgNoAutenticado').html("Producto agregado.");
                        parent.window.location.reload(true);
                    }
                    else {
                        $('#msgModal .modal-body').html("Producto agregado.")
	                    $('#mostrarModal').click();

                    }
                }
            }, responseError);

            return shoppingItemsService.svcGetShoppingItems().then(function (response) {
                $scope.shoppingItems = response.data;
            }, responseError);

        };

        this.deleteProduct = function (id) {

            $scope.loading = true;

            shoppingItemsService.svcDeleteProduct(id).then(function (response) {}, responseError);

            return shoppingItemsService.svcGetShoppingItems().then(function (response) {
                $scope.shoppingItems = response.data;

                $scope.loading = false;

            }, responseError);
        };


    }]);
})(window.angular);
