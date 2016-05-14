/**
 * Created by ANDRES on 05/05/2016.
 */
(function (ng) {
    var mod = ng.module('commentsModule');

    /*mod.config(function($httpProvider, $cookies){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    })*/

    mod.service('commentsService', ['$http', 'commentsContext', function ($http, context) {

        this.registerComment = function (data) {
            return $http({
                method: 'POST',
                url: '/comments' ,
                data:data
            });
        };

    }]);
})(window.angular);