setImmediate(function () {
    Java.perform(function () {

        // clz.0000.implementation = function () {
        //     send("1111");
        //
        //     // var kinstance = kClz.$new();
        //     // send("2222");
        //     kClz.a(arguments[0], 1, arguments[5]);
        //     send("3333");
        //     // this.setData(arg1);
        //
        // }

        var clazz = Java.use("java.lang.Class");
        var jniClz = Java.use("com.mcto.cupid.CupidJni");

        jniClz.jniSetMemberStatus.implementation = function () {
            send("jniSetMemberStatus：" + arguments[0] + "____" + arguments[1] + "_____" + arguments[2]);
            this.jniSetMemberStatus(arguments[0], arguments[1], arguments[2]);
        }


        //关键函数  设置map的值
        // var auClz = Java.use("com.qiyi.video.qysplashscreen.ad.au");
        // auClz.b.overload("java.util.Map").implementation = function () {
        //     this.b(arguments[0])
        //     send("关键函数  设置map的值" + arguments[0].toString());
        //
        //
        //     var keyset = arguments[0].keySet();
        //     var it = keyset.iterator();
        //     while (it.hasNext()) {
        //         var keystr = it.next();
        //         var valuestr = arguments[0].get(keystr);
        //         send("key==" + keystr + "----value==" + valuestr)
        //     }
        //
        // }


        //
        // var userSaveClaz = Java.use("com.iqiyi.psdk.base.a.e");
        // userSaveClaz.a.overload("com.iqiyi.passportsdk.model.UserInfo").implementation = function () {
        //     send("userinfo  set");
        //     return this.a(arguments[0]);
        //
        // }
        // userSaveClaz.a.overload().implementation = function () {
        //     send("userinfo  get");
        //     return this.a();
        // }
        //
        //
        // var userInfo = Java.use("com.iqiyi.passportsdk.model.UserInfo");
        // var viplistbeanClz = Java.use("com.iqiyi.passportsdk.model.UserInfo$VipListBean");
        // userInfo.$init.overload().implementation = function () {
        //     send("userinfo  构造 没参数");
        //     this.$init();
        // }
        // userInfo.$init.overload("android.os.Parcel").implementation = function () {
        //     send("userinfo  构造 有参数");
        //     this.$init(arguments[0]);
        // }
        // userInfo.getLoginResponse.overload().implementation = function () {
        //     // send("userinfo  构造 没参数");
        //     var response = this.getLoginResponse();
        //     if (response != null) {
        //         if (response.vip.value.a.value==null){
        //             response.vip.value.a.value = "A00000";
        //             response.vip.value.c.value = "1";
        //             response.vip.value.d.value = "1";
        //             response.vip.value.g.value = "1";
        //             response.vip.value.h.value = "1";
        //             response.vip.value.i.value = "2020年1月22日";
        //             response.vip.value.k.value = "0";
        //         }
        //
        //         var list = response.mVipList.value;
        //         if (list.size() == 0) {
        //             var viplistbean = viplistbeanClz.$new();
        //             viplistbean.a.value = "A00000";
        //             viplistbean.b.value = "";
        //             viplistbean.c.value = "1";
        //             viplistbean.d.value = "1";
        //             viplistbean.e.value = "0";
        //             viplistbean.g.value = "1";
        //             viplistbean.h.value = "1";
        //             viplistbean.i.value = "1579671987000";
        //             viplistbean.k.value = "0";
        //             list.add(viplistbean);
        //         }
        //     }
        //     // send(response.toString());
        //
        //     return response;
        // }

        var userInfo = Java.use("com.iqiyi.passportsdk.model.UserInfo");
        var viplistbeanClz = Java.use("com.iqiyi.passportsdk.model.UserInfo$VipListBean");
        var fClz = Java.use("com.iqiyi.passportsdk.iface.a.e");
        fClz.b.implementation = function (jSONObject) {

            // if (jSONObject != null) {
            //     send("登录数据：==" + jSONObject.toString())
            // } else {
            //     send("登录数据：null")
            // }

            var response = this.b(jSONObject);
            if (response != null) {
                if (response.vip.value.a.value == null) {
                    response.vip.value.a.value = "A00000";
                    response.vip.value.c.value = "1";
                    response.vip.value.d.value = "1";
                    response.vip.value.g.value = "1";
                    response.vip.value.h.value = "1";
                    response.vip.value.i.value = "2020年1月22日";
                    response.vip.value.k.value = "0";
                }

                var list = response.mVipList.value;
                if (list.size() == 0) {
                    var viplistbean = viplistbeanClz.$new();
                    viplistbean.a.value = "A00000";
                    viplistbean.b.value = "";
                    viplistbean.c.value = "1";
                    viplistbean.d.value = "1";
                    viplistbean.e.value = "0";
                    viplistbean.g.value = "1";
                    viplistbean.h.value = "1";
                    viplistbean.i.value = "1579671987000";
                    viplistbean.k.value = "0";
                    list.add(viplistbean);
                }
            }
            return response;
        }

        var fragclz = Java.use("com.qiyi.vertical.verticalplayer.bq");
        fragclz.onResume.overload().implementation = function () {

            send("进入这个fragment")
            this.onResume()
        }


        var bclz = Java.use("com.iqiyi.video.qyplayersdk.cupid.b.b");
        bclz.a.overload("int", "com.mcto.cupid.constant.AdEvent").implementation = function (i, event) {
            send("jniOnAdEvent" + "___" + i + "____" + event.value());
            this.a(i, event);

        }

        // var getfclz = Java.use("org.iqiyi.video.activity.PlayerActivity");
        // getfclz.onAttachFragment.overload("android.support.v4.app.Fragment").implementation = function (fragment) {
        //     send("fragment==" + fragment.getClass().getName());
        //     this.onAttachFragment(fragment)
        //
        // }

        var playerVideoInfoclz = Java.use("com.iqiyi.video.qyplayersdk.cupid.data.model.CupidAD");
        playerVideoInfoclz.getVideoType.implementation = function () {
            send("修改1111")
            return 1;
        }

        //实现了 隐藏右上角时间隐藏的功能，但实际的广告并没有隐藏掉
        var fClz = Java.use("com.iqiyi.video.adview.roll.a");
        fClz.a.overload("com.iqiyi.video.qyplayersdk.cupid.data.model.CupidAD","boolean").implementation = function () {
            send("调用  点击隐藏")
            this.a(arguments[0],arguments[1]);
            var mclz = Java.use("com.iqiyi.video.adview.roll.m");
            var click =mclz.$new(this);
            click.onClick(null);
        }

        //跳过广告的点击事件
        var mclz = Java.use("com.iqiyi.video.adview.roll.m");
        mclz.onClick.implementation = function () {
            send("执行了");
            this.onClick(arguments[0])
        }
    });
})



