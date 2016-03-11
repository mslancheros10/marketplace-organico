(function (ng) {

    var marketplaceOrganico = ng.module('marketplaceOrganico', [
        'ngRoute',
        'mainModule',
    ]);

    marketplaceOrganico.config(['$routeProvider', function ($routeProvider) {

        $routeProvider
            .when('/main', {
                templateUrl: 'static/src/modules/main/main.tpl.html',
                controller: 'managerCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/main');

    }]);
})(window.angular);
