setImmediate(function () {
    Java.perform(function () {
        //跳过启动页广告

        var hclass = Java.use("com.estrongs.android.pop.h");
        hclass.br.implementation = function () {
            send("成功");
            this.C(true);
            return true;
        }

    });
})



