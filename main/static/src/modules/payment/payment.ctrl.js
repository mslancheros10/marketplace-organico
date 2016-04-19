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
                            $scope.totalandtaxes += $scope.shoppingItems[i].baskets[j].price * $scope.shoppingItems[i].quantity;
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
            /*$scope.paymentMethod = '';
            $scope.cardNumber = '';
            $scope.readonly = false;
            var hola=getShoppingItems();
            //var aaa = $scope.shoppingItems[0];
            $scope.pruebita = "";

            var oldFetch = this.fetchRecords;
            this.fetchRecords = function () {
                return oldFetch.call(this).then(function (data) {
                    self.calcTotal();
                    return data;
                });
            };
            this.fetchRecords();
            this.readOnly = true;
            $scope.lastQuantity = 0;
            $scope.total = 0;
            $scope.taxes = 0;
            this.calcTotal = function () {
                $scope.total = 0;
                for (var i = 0; i < $scope.shoppingItems.length; i++) {
                    $scope.total += $scope.shoppingItems[i].artwork.price * $scope.records[i].quantity;
                    if ($scope.records[i].artwork.discount)
                    {
                        $scope.total += (1 - $scope.records[i].artwork.discount / 100) * $scope.records[i].artwork.price * $scope.records[i].quantity;
                    } else {
                        $scope.total += $scope.records[i].artwork.price * $scope.records[i].quantity;
                    }
                }
                $scope.taxes = $scope.total * 0.16;
                $scope.totalandtaxes = $scope.taxes + $scope.total;
            };
            $scope.endPayment = function () {
                var error = "";
                var valide = true;
                var re = "";
                if ($scope.paymentMethod === '1' || $scope.paymentMethod === '2') {
                    re = /^(?:4[0-9]{12}(?:[0-9]{3})?)/.exec($scope.cardNumber);
                    if (re === null) {
                        valide = false;
                        error = "Please insert a validad card number. Example: 4512345678912345";
                    }
                }
                if ($scope.paymentMethod === '3') {
                    re = /[^@]+@[^@]+\.[a-zA-Z]{2,6}/.exec($scope.cardNumber);
                    if (re === null) {
                        valide = false;
                        error = "Please insert a validad email address. Example: example@gmail.com";
                    }
                }
                if (valide) {
                    paymentSvc.createItem({
                        method: $scope.paymentMethod,
                        subtotal: $scope.total,
                        taxes: $scope.taxes,
                        total: $scope.totalandtaxes,
                        reference: $scope.cardNumber
                    });
                    for (var i = 0; i < $scope.records.length; i++) {
                        svc.payItem($scope.records[i]);
                    }
                    $scope.paymentMethod = '1';
                    $scope.cardNumber = '';
                    $location.path('payf');
                }
                else {
                    $scope.cardNumber = '';
                    $scope.validationError = "error";
                    self.showError(error);
                }
            };
            $scope.reset = function () {
                $scope.paymentMethod = '';
                $scope.cardNumber = '';
            };
       */
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
                    /*
                    paymentSvc.createItem({
                        method: $scope.paymentMethod,
                        subtotal: $scope.total,
                        taxes: $scope.taxes,
                        total: $scope.totalandtaxes,
                        reference: $scope.cardNumber
                    });
                    for (var i = 0; i < $scope.records.length; i++) {
                        svc.payItem($scope.records[i]);
                    }
                    $scope.paymentMethod = '1';
                    $scope.cardNumber = '';*/
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