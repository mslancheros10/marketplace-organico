/**
 * Created by ANDRES on 05/05/2016.
 */
(function (ng) {
    var mod = ng.module('commentsModule');

    mod.controller('commentsCtrl', ['commentsService', function (commentsService) {
        var vm = this;
        vm.requestState = "";
        vm.registerComment = function(comment){

            vm.requestState = "Estamos procesando..."
            commentsService.registerComment({comment: comment}).then(function(){
                vm.comment = "";
                vm.requestState = "Email enviado"
            },function(){
                vm.requestState = "Error!!"
            })
        }

    }]);
})(window.angular);