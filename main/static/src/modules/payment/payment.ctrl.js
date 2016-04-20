(function (ng) {
    var mod = ng.module('paymentModule');

    mod.controller('paymentCtrl', ['$scope', 'shoppingItemsService', '$location', 'paymentService', function ($scope, shoppingItemsService, $location, paymentService) {

            var totalpayment= 0;
            this.getShoppingItems = function () {

                shoppingItemsService.svcGetShoppingItems().then(function (response) {
                    $scope.loading = false;
                    $scope.shoppingItems = response.data;
                    $scope.paymentMethod = '';
                    $scope.cardNumber = '';
                    $scope.readonly = false;
                    $scope.total=0;
                    $scope.taxes = 0;
                    $scope.totalandtaxes=0;
                    for (var i = 0; i < $scope.shoppingItems.length; i++) {
                        for (var j = 0; j < $scope.shoppingItems[i].baskets.length; j++) {
                            for(var k = 0; k< $scope.shoppingItems[i].baskets[j].products.length; k++){
                                $scope.totalandtaxes += $scope.shoppingItems[i].baskets[j].products[k].price * $scope.shoppingItems[i].baskets[j].products[k].quantity;
                            }

                        }
                        for (var j = 0; j < $scope.shoppingItems[i].products.length; j++) {
                            $scope.totalandtaxes += $scope.shoppingItems[i].products[j].price * $scope.shoppingItems[i].quantity;
                        }
                    }
                    $scope.taxes = $scope.totalandtaxes*0.16;
                    $scope.total = $scope.totalandtaxes - $scope.taxes;
                    this.totalpayment = $scope.total;
                    console.log('Respuesta de la vista: '+response);
                }, responseError);


            };

         $scope.endPayment = function () {
                var error = "";
                var valide = true;
                var re = "";
                if ($scope.paymentMethod === '1' || $scope.paymentMethod === '2') {
                    re = /^(?:4[0-9]{12}(?:[0-9]{3})?)/.exec($scope.cardNumber);
                    if (re === null) {
                        valide = false;
                        error = "Por favor ingrese un número de tarjeta válido. Ejemplo: 4512345678912345";
                    }
                }
                if (valide) {
                    paymentService.svcPayCart({
                                'price': this.totalpayment
                        });

                    document.getElementById("paymentModal").style.display="none";
                    document.getElementById("shoppingItemsModal").style.display="none";
                    var fades = document.getElementsByClassName("modal-backdrop fade in");
                    for (var i = 0; i < fades.length; i++) {
                        fades[i].style.display="none";
                    }
                    $location.path('payf');
                }
                else {
                    $scope.cardNumber = '';
                    $scope.validationError = "error";
                    alert(error);
                }
            };

        $scope.reset = function () {
                $scope.paymentMethod = '';
                $scope.cardNumber = '';
            };

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

    }]);


})(window.angular);