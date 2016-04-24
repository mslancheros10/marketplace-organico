(function (ng) {
    var mod = ng.module('registerModule');

    mod.controller('registerCtrl', ['$scope', 'registerService', function ($scope, registerService) {

        this.showRegisterProvider = false;

        $scope.newProvider = {
            username:'',
            password:'',
            certified:false,
            farm_name:'',
            farm_latitude:'4.601472',
            farm_longitude:'-74.065326',
            farm_size:'',
            farm_address:''
        };


        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.registerProvider = function () {
            return registerService.registerProvider($scope.newProvider).then(function (response) {
                console.log(response);
                window.location.assign('#/main');
                window.location.reload(true);
                alert('Registro Exitoso!. Espera la confirmación por parte de nosotros para ser activado en el sistema.');
            }, responseError);
        };

        this.geocoderAddress = function () {
            return registerService.geocoderAddress($scope.newProvider.farm_address).then(function (response) {
                console.log(response);
                if (response.data.status === 'OK') {
                    $scope.newProvider.farm_latitude = response.data.results[0].geometry.location.lat;
                    $scope.newProvider.farm_longitude = response.data.results[0].geometry.location.lng;

                }
                $("#idFarmMap").empty();
                document.getElementById("idFarmMap").innerHTML ='<img onmousemove="" style="margin:auto; height: 600px; width: auto" src="https://maps.googleapis.com/maps/api/staticmap?center='+ $scope.newProvider.farm_latitude +','+ $scope.newProvider.farm_longitude +'&zoom=13&size=300x300&maptype=roadmap&markers=color:red%7Clabel:C%7C'+ $scope.newProvider.farm_latitude +','+ $scope.newProvider.farm_longitude +'&key=AIzaSyCL1qoAd2fWDwWM8y-SyngJ42ywrReHAEM">';
            }, responseError);
        };

        this.enableClientRegister = function () {
            this.showRegisterProvider = false;
        };

        this.enableProviderRegister = function () {
            this.showRegisterProvider = true;
        };


    }]);
})(window.angular);
