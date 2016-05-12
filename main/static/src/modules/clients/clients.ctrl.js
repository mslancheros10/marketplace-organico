(function (ng) {
    var mod = ng.module('clientsModule');

    mod.controller('clientsCtrl', ['$scope', 'clientsService', function ($scope, clientsService) {

        this.statusForm = '';


        $scope.infoClient = {
            username:'',
            firstname:'',
            lastname:'',
            email:'',
            address:'',
            phone:''
        };

        function responseError(response) {
            console.log(response);
            $scope.loading = false;
        }

        this.getClient = function(){
            return clientsService.getClient().then(function (response) {
                 if(response.data.status=='OK') {
                     $scope.infoClient.username = response.data.username;
                     $scope.infoClient.firstname = response.data.firstname;
                     $scope.infoClient.lastname = response.data.lastname;
                     $scope.infoClient.email = response.data.email;
                     $scope.infoClient.address = response.data.address;
                     $scope.infoClient.phone = response.data.phone;
                 }
            }, responseError);

        };

        this.updateClient = function () {
            return clientsService.updateClient($scope.infoClient).then(function (response) {
                console.log(response);
                if(response.data.status=='OK'){
                    $('#clientModal .close').attr("onclick","window.location.assign('#/main');window.location.reload(true)");
                    $('#clientModal .modal-title').html("Registro Exitoso!")
                    $('#clientModal .modal-body').html("Su perfil se actualizó correctamente.")
                }else{
                    $('#clientModal .modal-title').html("Error!")
                    $('#clientModal .modal-body').html(response.data.status)
                }

            }, responseError);
        };

    }]);
})(window.angular);
