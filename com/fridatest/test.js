setImmediate(function () {
    Java.perform(function () {
        // var encodeClz = Java.use("com.xh.encodendk.util.EncodeUtil");
        //
        // encodeClz.stringFromJNI.implementation = function () {
        //     send("zifuchuan" + this.stringFromJNI());
        //
        //     //获取一个类的成员变量，第一个传入类名
        //     // var field =Java.case("xxx",encodeClz).getDeclaredField("xxx");
        //     // field.setAccessible(true);
        //     // field.getInt();
        //
        //
        //
        //     return "hook after";
        // }
        //
        // var logClz=Java.use("com.blankj.utilcode.util.LogUtils");
        // logClz.e.implementation= function () {
        //     send(arguments[0].toString())
        //     //  获取调用的日志栈  adb logcat -s AndroidRuntime 可以获取日志
        //     // throw Java.use("java.lang.Exception").$new("test");
        // }
        var myclaz=Java.use("com.xh.encodendk.util.MyClass");
        myclaz.getName.implementation= function () {
            // send(this.name.value);
            // this.name.value = "new name";
            // send(this.name.value)

            return [3];
        }




    });
})



