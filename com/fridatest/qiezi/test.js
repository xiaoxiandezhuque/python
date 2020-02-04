setImmediate(function () {
    Java.perform(function () {


        var EncryptUtilsClz = Java.use("com.live.eggplant.base.encrypt.EncryptUtils");

        EncryptUtilsClz.getUmeng_iv.implementation = function () {
            var str = this.getUmeng_iv();
            send(str);
            return str;
        }
        EncryptUtilsClz.getUmeng_kv.implementation = function () {
            var str = this.getUmeng_kv();
            send(str);
            return str;
        }

        var utilclz = Java.use("com.live.eggplant.util.EncryptUtils");
        utilclz.getUmengMv.implementation = function () {
            var str = this.getUmengMv();
            send("i need k== " + str);
            return str;
        }
        var enuclz = Java.use("com.live.eggplant.base.encrypt.EncryUtil");
        enuclz.encryptMd5.implementation = function (map) {
            var keyset = map.keySet();
            var it = keyset.iterator();
            while (it.hasNext()) {
                var keystr = it.next();
                var valuestr = arguments[0].get(keystr);
                send("key==" + keystr + "----value==" + valuestr)
            }

            var str = this.encryptMd5(map);

            send("i need s== " + str);
            return str;
        }
    });
})



