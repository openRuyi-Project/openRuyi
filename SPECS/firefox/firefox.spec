# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: Maybe we need to remove this for licensing reasons
%bcond fdk_aac 0

# TODO: Official branding is tricky
# https://www.mozilla.org/en-US/foundation/trademarks/policy/
%bcond official_branding 0

Name:           firefox
Version:        154.0.1
Release:        %autorelease
Summary:        Free web browser backed by Mozilla
License:        MPL-2.0
URL:            https://www.firefox.com
# https://bugzilla.mozilla.org/show_bug.cgi?id=1863519
VCS:            git:https://github.com/mozilla-firefox/firefox
#!RemoteAsset:  sha256:9cbe191fc74b46108376b1d9bf607c0a40288074e0f2333671253789d6ebbd15
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/source/%{name}-%{version}.source.tar.xz
# We need the language packs
#!RemoteAsset:  sha256:8c2e1a9cdbc0d1e830a8254f5d9df95989649545806b3076acea4e9ccdb47159
Source1:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ach.xpi
#!RemoteAsset:  sha256:452e6a7d9a478beb25f9a64b0f52bb31a6b60b16685961c5626a6b1b09b2ac06
Source2:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/af.xpi
#!RemoteAsset:  sha256:5ab43ec6163bee5423c8ecdbc866eaa1f2b4576149051d2349973ec3c849ce98
Source3:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/an.xpi
#!RemoteAsset:  sha256:b873f2814ed91ec1204e6ea0d79d2d617206e5e5c6b8821de7173baff753210c
Source4:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ar.xpi
#!RemoteAsset:  sha256:7d3c18c160dc7afcc5f84a72894a897cbe1dcc0e37bcb65fa9a6767ccc63a157
Source5:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ast.xpi
#!RemoteAsset:  sha256:a69be66824a8bb1bb6c007d7da22097a38531b5835dac2c70b6ee4d47b95ce5b
Source6:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/az.xpi
#!RemoteAsset:  sha256:142fddaf35a67a7aeaf055e845b99ddf41a5276892b8bb63ba0b4993583161e0
Source7:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/be.xpi
#!RemoteAsset:  sha256:5742ff32a072d7c67d8be49269eaa85a8d1aa18b26f4ff86d9fbb55d32d82333
Source8:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bg.xpi
#!RemoteAsset:  sha256:b962b23595379732bfcab3951a69164cab55e19cbad5f40e16c37dd8090c0cef
Source9:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bn.xpi
#!RemoteAsset:  sha256:482673daa5b8d2601c3d0422e24b37d484a8a94e739ae601cfda505d68ca9504
Source10:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/br.xpi
#!RemoteAsset:  sha256:a2c0eb2c015fd1975cdbd34de531906d2bf4d6f6a2676acc41ce347e9773653e
Source11:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bs.xpi
#!RemoteAsset:  sha256:e1003a43cf2823da50b02b267054c579345f89db68281a3ebfe32edbb3dd70ab
Source12:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca-valencia.xpi
#!RemoteAsset:  sha256:ba11f4567ecb150bbb96320051486b6a9c33151c64f115ca7d25183284ae8e4e
Source13:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca.xpi
#!RemoteAsset:  sha256:943f39070927af1dc3691c12bb99c478a396b94c146753c450402d45e89f79fa
Source14:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cak.xpi
#!RemoteAsset:  sha256:48cb2f8dddb2ddf92b48cc070f976466709e3c75e0f94e25921b600f5f8abc5d
Source15:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cs.xpi
#!RemoteAsset:  sha256:78f7a0da3f5297622a7a9f7cabc86fcd8fc44d9b5deacc7d158818b2280d09e7
Source16:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cy.xpi
#!RemoteAsset:  sha256:e5d28d5e594ed1e7821df3792dc5a41ecc3e1b19a11192cb362a779785be1404
Source17:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/da.xpi
#!RemoteAsset:  sha256:3d1bd997ea907a132720df8fc70c544b6ed1770d2703cee072a625e4fecba91f
Source18:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/de.xpi
#!RemoteAsset:  sha256:3c1f8f1e35f41cf21476af161bc195adcba975251b98a3ced4b927b1377674e6
Source19:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/dsb.xpi
#!RemoteAsset:  sha256:363f201d954f7a9eab668da18b5db39ab4cf983bbd4a4c33120f5b8e12f86d94
Source20:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/el.xpi
#!RemoteAsset:  sha256:7ba2c633506420107b27159abd68c4c4fd175a425152f471992c7f4617cf5ef7
Source21:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-CA.xpi
#!RemoteAsset:  sha256:5e2e9eccf5b20c8bfa6d63791e612148e0dd9a664cfa6799ff5aed3280b64732
Source22:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-GB.xpi
#!RemoteAsset:  sha256:56e8e6952f65377a1a2393a5e158bd7b0808b55f8e2e50ee3910e040a45ceea7
Source23:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-US.xpi
#!RemoteAsset:  sha256:f52bdb6de1f9b67253b80288134a190878abf04e8a790e6b1c91b7e4d773dd33
Source24:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eo.xpi
#!RemoteAsset:  sha256:4f5ebd1b99db41bda51c588bbf79b062e312a0e5a73587a90c3d472950f84250
Source25:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-AR.xpi
#!RemoteAsset:  sha256:0dca7abeff35990f0a4dc7e34e43c084c723f13b57d5b162a6a469b28ad2c7d4
Source26:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-CL.xpi
#!RemoteAsset:  sha256:3f44dbf6181d1fcd5e385fc1f5e1ebac1688449ec2a27b73678497a762fc9052
Source27:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-ES.xpi
#!RemoteAsset:  sha256:b398c480bbd36c46e98aed57e3fe48d592e25b7daadf48cc58ed7d0fb5007bce
Source28:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-MX.xpi
#!RemoteAsset:  sha256:c16576f72b2e090a7b01e3ac1ca3c0dbfe71ed970a28c522517ac89c4dafe688
Source29:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/et.xpi
#!RemoteAsset:  sha256:8cb7f3ff3512e82bdfe7563c93040700a65835ffecbca0325b083324c940bd6a
Source30:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eu.xpi
#!RemoteAsset:  sha256:31ef904d445826e00937bdf39f4407ff3216670d6e83ddc7a05292548f8cca5c
Source31:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fa.xpi
#!RemoteAsset:  sha256:7bc9da3870b234264102dc36fbcf27c485f7013ef4feb8d934adc1ea527b95a7
Source32:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ff.xpi
#!RemoteAsset:  sha256:ddb8befd2d71687d6198585da26d04d7419f7a6095cf2a8627a1581ff260021f
Source33:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fi.xpi
#!RemoteAsset:  sha256:7e008d1a3b3f58e70b2dc2b2b73206940cf0b60aa149dd7a3dc9b8745bc3753d
Source34:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fr.xpi
#!RemoteAsset:  sha256:5e939cc1f9acfe3c05e2c8aef48e25b1cc2fc77413a9a188b809be6b2b1ee2d6
Source35:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fur.xpi
#!RemoteAsset:  sha256:7e303fec006b82505f3bd14eade9667c629ab8eb12ee302ce5f2f2f4654743ee
Source36:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fy-NL.xpi
#!RemoteAsset:  sha256:4c913cb73c9db3529a51a1b0d362372cfe16113c56f24f04d765d921a6d53c6f
Source37:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ga-IE.xpi
#!RemoteAsset:  sha256:a609dca5a32dbaf86fca81e52c8715cb14ad5477f17b617cfffc4ad423e9cca0
Source38:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gd.xpi
#!RemoteAsset:  sha256:644183a27792ced6b926728759f96e3e22b4346c2abe7be87c322be23575ceec
Source39:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gl.xpi
#!RemoteAsset:  sha256:6e46d0ff41fc2716a00311bf1266532f91e1554baa2dd570f9218437fe0264c9
Source40:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gn.xpi
#!RemoteAsset:  sha256:75c4caa25d9be1880e1c597deab84745203751887d5c7773fe4bd2c23322cb4c
Source41:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gu-IN.xpi
#!RemoteAsset:  sha256:0dcbf236d5ea12e13420feb5a34d601466df99b78fcf14129a605d6be4ed3433
Source42:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/he.xpi
#!RemoteAsset:  sha256:5a6e7042e7f96c085a8b8f606e926ea9c0a72eae6d87053c8786d1a34fa44bcf
Source43:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hi-IN.xpi
#!RemoteAsset:  sha256:dea3be0311f7a023dc28889944c4283354783bca011dc78eb797d85168055193
Source44:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hr.xpi
#!RemoteAsset:  sha256:5289dd7d87b594a655a2bee283e62942a3a479dcb88eea5123e2cb2cb94789d7
Source45:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hsb.xpi
#!RemoteAsset:  sha256:56c1397d184cc6b3dc961ef6469b8b5733410613fb1f0e92f54680d5b6e740ae
Source46:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hu.xpi
#!RemoteAsset:  sha256:c7f2f1e812c3ea19a27c6997e014d60de29cac5956e171ec2782a69a0755dfee
Source47:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hy-AM.xpi
#!RemoteAsset:  sha256:934f625aa5999e44412501dac71bdca16a04a5c3a62d4b2f8c56311778d4ced8
Source48:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ia.xpi
#!RemoteAsset:  sha256:081b3e4b03c500889a83b80a01bee2cea0cb1c5b0bfb5ed2dc1e2d6a0d794e94
Source49:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/id.xpi
#!RemoteAsset:  sha256:8544dfcf5ec77e491adb93ea3f6c9e7a9cbde8dd182b11fe5303e8bdc033c09a
Source50:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/is.xpi
#!RemoteAsset:  sha256:f235dde282b61c974b05e8687f63dfbd81ffde31de49bcfffc6a09e5791a2639
Source51:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/it.xpi
#!RemoteAsset:  sha256:af9b6b2630246535bc64f2c9c181216b649722fda42e15664e952b871937fa52
Source52:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ja.xpi
#!RemoteAsset:  sha256:46d6861978f0d2445bf6e7ffa33063c9fc4e24c986d6b1f78a9c1f3278a63616
Source53:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ka.xpi
#!RemoteAsset:  sha256:aa9c0103243b312407e975d01a77e54c642c692499db1a690597734a2dd6be62
Source54:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kab.xpi
#!RemoteAsset:  sha256:06d2574d16da30f320f10856d4b63861c0dc4eafeba1528af6cd80ef98085ce3
Source55:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kk.xpi
#!RemoteAsset:  sha256:3e147442fbd303c9b9daa2604835f1e4ffe6ea20c6a6de9361b3c32bb6b14577
Source56:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/km.xpi
#!RemoteAsset:  sha256:404f86e10485ce49a125489598907a9c717fff588d9ad0227acacb989b81c8f7
Source57:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kn.xpi
#!RemoteAsset:  sha256:91a93c0dd25081ee5abbd3619b88026c329d1ae242a016275f1100ea3ddafd22
Source58:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ko.xpi
#!RemoteAsset:  sha256:095b66a9b01ac3b232afced346ba61930741a3d6e425707395f62aaa64d7c24b
Source59:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lij.xpi
#!RemoteAsset:  sha256:53c048c29645494553a52c82987ea51875f6bbc592088ca81590a6b22e5ab6bd
Source60:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lt.xpi
#!RemoteAsset:  sha256:dbe5b88a211969cdf59c348ea3a5973eaa396d3b1db5629a923a1a63841409b2
Source61:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lv.xpi
#!RemoteAsset:  sha256:bdb1a9709fbe9a2f4b33017ae9afd34e63bd6bc7979620ae5d5ce84345f223c1
Source62:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mk.xpi
#!RemoteAsset:  sha256:1c48dec3e0bfa796da4e0988de7474731766fa5e385ca21595781cbf3f93e82a
Source63:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mr.xpi
#!RemoteAsset:  sha256:0d08d936a50fbe89a2a4088d9cd2f83e936c02bde646aa4fa5bf21e22ce165d2
Source64:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ms.xpi
#!RemoteAsset:  sha256:c55e2f2b687e249a8cfa5c6c5dc24c263535ca2c1b3cff83496faf1f1582c3c1
Source65:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/my.xpi
#!RemoteAsset:  sha256:d93f869fbe43047bf08485fa331e3d2a8b9e91a47ceb7b99a25e2c57e9de7a35
Source66:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nb-NO.xpi
#!RemoteAsset:  sha256:170b87e5bebac585ed21357f465237540d7f8a726e658a2aa563235963c765be
Source67:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ne-NP.xpi
#!RemoteAsset:  sha256:74f66637756482670a3ddf25d2fbcfe5162f260158d8efaff7b372e20799707c
Source68:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nl.xpi
#!RemoteAsset:  sha256:19a7ba91ff52a6b235c0fc8603f406b56f9f2f92eb4b874635f6b4fa83774d2d
Source69:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nn-NO.xpi
#!RemoteAsset:  sha256:077bd2ddcfab154c9ddb92f0ff0260e99432c6ccc7d04890f2be30a3b67cda3d
Source70:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/oc.xpi
#!RemoteAsset:  sha256:e097545e641f86e77f18aab0a8a9076a6a37748fdd71f010b1864c0ced7343be
Source71:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pa-IN.xpi
#!RemoteAsset:  sha256:3a8ab58905371d5e5907bfb988b0b431eccd7b16ad63c364ff48fc37c726bea2
Source72:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pl.xpi
#!RemoteAsset:  sha256:ca20b29a4d125ca95b1c60979a2f9839158b528be256d26a9d24dba8ccd0a6e5
Source73:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-BR.xpi
#!RemoteAsset:  sha256:45397fe7ce652a2b88e842f2e945e0d4fe218936f914127736dff9caefc21dea
Source74:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-PT.xpi
#!RemoteAsset:  sha256:29d332cdf7efbda3962b37ac596b0d2c8596ee7c1b970d99e717593ec50b3581
Source75:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/rm.xpi
#!RemoteAsset:  sha256:07c5ee4e5ebde1483b947299c692b7cc31a25a13e91cd93a1f3c1f1c661c10d8
Source76:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ro.xpi
#!RemoteAsset:  sha256:f35ea034ed4c1da77fdd7d2715e9eb34ad0da48570a8af078b5f2c169e66018e
Source77:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ru.xpi
#!RemoteAsset:  sha256:f56586bc95eca698e78ee81313c70540c850770f447196942ba5a41576def7ae
Source78:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sat.xpi
#!RemoteAsset:  sha256:8a7fb2dfa60da7adffebcd273758a6f049a82a84d9f7af5e41fda0d2aaecfd27
Source79:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sc.xpi
#!RemoteAsset:  sha256:c90c970da4f255b0ba83050d468d48c79023f156579d375bdeb72ab1c74286f5
Source80:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sco.xpi
#!RemoteAsset:  sha256:5b9b5350714f7b93184611dc42064ff0e5e06adeb9b28422f54df3316432249c
Source81:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/si.xpi
#!RemoteAsset:  sha256:7db5ca10ea62ff8854c352f008cc98a7c05310fa4e380974e49ceb0f1af26ec6
Source82:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sk.xpi
#!RemoteAsset:  sha256:d643d5b01992426a4b0662534d77bf85453fa6c686a0f1cffd37e410072fa4fd
Source83:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/skr.xpi
#!RemoteAsset:  sha256:92ef26c1dc106d59dc956e5d9efe38932b7ed3c123d7ba06096ea2e7a4b353d6
Source84:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sl.xpi
#!RemoteAsset:  sha256:17c52bd9a4e4e9120c0c7e97e6a1a661eafe2c304c117bdce78185f84a4c7977
Source85:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/son.xpi
#!RemoteAsset:  sha256:5c003a754142daa35d33073b723cd4e2ded80b15ab343861e91b5bd498b15f8a
Source86:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sq.xpi
#!RemoteAsset:  sha256:6e787e63bbc98ea28aba97b0e446742702f2f2e0e89ac7a79ae9e280b1daf9b0
Source87:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sr.xpi
#!RemoteAsset:  sha256:ccb0fe5a602da67786a3bba6e904b3bb2b4f40daf3a4a008d606c85ffd2c0d2d
Source88:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sv-SE.xpi
#!RemoteAsset:  sha256:11073ed7a9ebf8a0ed708acc114b99a67c20191c8663339bd27368d0ddfb9d9c
Source89:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/szl.xpi
#!RemoteAsset:  sha256:4d703442475d5dd66914478afa74d3923b1cbdc903345bf24f889889043be63a
Source90:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ta.xpi
#!RemoteAsset:  sha256:bd44c7e608bbbc7bee57d91f5fa333bcdffce8266efb559f317caa3048dfa09a
Source91:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/te.xpi
#!RemoteAsset:  sha256:860bdcc6e5ee467a2bc4aa5f553f67e94a4ffce58555ba403fff271650e69266
Source92:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tg.xpi
#!RemoteAsset:  sha256:441a00d495fcf5b23a4a1cb33f893fcef9e1c73ee5427474caf1d936e7648945
Source93:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/th.xpi
#!RemoteAsset:  sha256:6ce23ac148b0655faabaca73e49c09446554de02f991204297ab3b8f50ce4122
Source94:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tl.xpi
#!RemoteAsset:  sha256:02adf8240b50ff2b3139415da7d3b4529e292293382bbf0af0d1d513fae96d40
Source95:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tr.xpi
#!RemoteAsset:  sha256:d79300d7f270e2fdb111bb714be899ceee670aee9bcf5d045584223924097a0f
Source96:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/trs.xpi
#!RemoteAsset:  sha256:08511a31c82a0d391edf6a10dd6bfd26d48343ed1beba2002ead16972cc0fdc0
Source97:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uk.xpi
#!RemoteAsset:  sha256:47d14523677e74e4d7fbb32fd74914728bfa9762ffea8100376915a49e99b17c
Source98:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ur.xpi
#!RemoteAsset:  sha256:000610ede9a318d3468c289c8d7d7634d6e153213cb904203d9843415df66ef6
Source99:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uz.xpi
#!RemoteAsset:  sha256:697abf15cf23387d54b35b915a50b9267607250342542c0415ed5b13487d0506
Source100:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/vi.xpi
#!RemoteAsset:  sha256:3bdb49d3ac6c48d85fa39685304234025d058c965cc9930b82850a54757616bd
Source101:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/xh.xpi
#!RemoteAsset:  sha256:9c1e161d098a6f5afcab59f82a59a5ff38ae69f3ce9c0575cc62cce4bd329fa9
Source102:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/zh-CN.xpi
#!RemoteAsset:  sha256:a18e778e18145290f9599399cf06b3facfd01c23493496d8f21e8538d7ca92d3
Source103:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/zh-TW.xpi
# What if firefox add another language? We should start at 200 - 251
# https://www.chromium.org/developers/how-tos/api-keys/
# Note: This key is for openRuyi use ONLY.
# For your own distribution, please get your own set of keys.
Source200:      google-api-key
Source201:      firefox.desktop
Source202:      firefox.js
Source203:      distribution.ini.in
Source204:      firefox.xml
Source205:      run-wayland-compositor.sh

BuildRequires:  appstream-glib
BuildRequires:  autoconf
BuildRequires:  cargo
BuildRequires:  cbindgen
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  cmake(LLVM)
BuildRequires:  compiler-rt
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  nodejs
BuildRequires:  pciutils
BuildRequires:  perl-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(vpx)
# We can't remove this because of desktop_capture_gn:
#    modules/desktop_capture/linux/x11/screen_capturer_x11.h
# This header will include <X11/extensions/Xdamage.h>
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rust
BuildRequires:  unzip
BuildRequires:  zip
# For PGO desktop
#BuildRequires:  kscreenlocker
BuildRequires:  kf6-kconfig
BuildRequires:  kf6-kwallet
BuildRequires:  kwin
BuildRequires:  desktop-file-utils

Requires:       ffmpeg

%patchlist
# https://bugzilla.mozilla.org/show_bug.cgi?id=2055545
# Can remove this patch after Firefox 115 release.
0001-Bug-2055545-Part-1-Return-BufferOffset.patch
0002-Bug-2055545-Part-2-Register-deadline-after-emitting.patch
2000-riscv64-Use-long-tail-jump-for-xptcall-stubs.patch
# https://bugzilla.mozilla.org/show_bug.cgi?id=1865601
2001-riscv64-enable-gles-rendering.patch
2003-blindly-set-rust-rva23-target-when-needed.patch
2005-add-riscv64-support-for-crash-context.patch
2006-enable-crashreporter-for-riscv64.patch
# https://github.com/ggml-org/ggml/pull/1571
# Rebased onto third_party/llama.cpp (ggml-cpu.c is ggml-cpu-c.c there);
# arch/riscv/repack.cpp and llamafile/sgemm.cpp hunks dropped, not vendored.
2007-riscv64-ggml-gate-RVV-code-on-the-target-extension.patch

%description
Mozilla Firefox is a free, open-source web browser developed by
the Mozilla Foundation, focused on user privacy, speed, and
customization.

%prep
%autosetup -p1 -n %{name}-%{version}

%conf
# Configure build file for openRuyi (Globally)
cat > .mozconfig <<EOF
# Release & Branding
mk_add_options BUILD_OFFICIAL=1
mk_add_options MOZILLA_OFFICIAL=1
ac_add_options --enable-update-channel=release

# Install directories
mk_add_options MOZ_OBJDIR=${PWD@Q}/obj
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --includedir=%{_includedir}

# Updater
ac_add_options --disable-updater
# Addon sideload
ac_add_options --allow-addon-sideload
ac_add_options --with-unsigned-addon-scopes=app,system

# Debug Symbols
# Normally we disable debug build because of the build time... - 251
ac_add_options --disable-debug
# But we need debug symbols
ac_add_options --enable-debug-symbols
# Let rpm do it's job - 251
ac_add_options --disable-strip
ac_add_options --disable-install-strip

# Optimization related
ac_add_options --enable-optimize
ac_add_options --enable-hardening
ac_add_options --enable-rust-simd
# Build
ac_add_options --enable-linker=lld

# Use system libraries
ac_add_options --with-system-gbm
ac_add_options --with-system-jpeg
ac_add_options --with-system-libdrm
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-pipewire
ac_add_options --with-system-webp
ac_add_options --with-system-zlib
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

# Multimedia & network related
ac_add_options --enable-pulseaudio
ac_add_options --enable-libproxy

# We use wayland
ac_add_options --enable-default-toolkit=cairo-gtk3-wayland

# sandbox libraries
ac_add_options --without-wasm-sandboxed-libraries

# Google Services
# Not free anymore... - 251
#ac_add_options --with-google-location-service-api-keyfile=%{SOURCE200}
ac_add_options --with-google-safebrowsing-api-keyfile=%{SOURCE200}

# Firefox crash reporter
ac_add_options --enable-crashreporter
# Misc
ac_add_options --disable-bootstrap
ac_add_options --disable-tests
# Enable SpiderMonkey JS shell
ac_add_options --enable-js-shell
EOF

# Some optimization related - 251
echo "ac_add_options --enable-lto" >> .mozconfig

%if %{with official_branding}
echo "ac_add_options --enable-official-branding" >> .mozconfig
%endif

# Some libraries we don't have but i think we should? - 251
%if %{with fdk_aac}
echo "ac_add_options --with-system-fdk-aac" >> .mozconfig
%endif

%build
echo "export CFLAGS=\"%{optflags}\""   >> .mozconfig
echo "export CXXFLAGS=\"%{optflags}\"" >> .mozconfig
echo "export LDFLAGS=\"%{build_ldflags}\"" >> .mozconfig
echo "export LLVM_PROFDATA=\"llvm-profdata\"" >> .mozconfig
echo "export AR=\"llvm-ar\"" >> .mozconfig
echo "export NM=\"llvm-nm\"" >> .mozconfig
echo "export RANLIB=\"llvm-ranlib\"" >> .mozconfig
# Fix: Could not find libclang to generate rust bindings for C/C++
echo "ac_add_options --with-libclang-path=`llvm-config --libdir`" >> .mozconfig

# https://firefox-source-docs.mozilla.org/build/buildsystem/pgo.html
%ifarch x86_64
echo "ac_add_options MOZ_PGO=1" >> .mozconfig

cp %{SOURCE205} .
. ./run-wayland-compositor.sh
%endif

./mach build -v

%install
DESTDIR=%{buildroot} make -C obj install

install -Dm0644 %{SOURCE201} %{buildroot}%{_datadir}/applications/firefox.desktop

# Install icons
%if %{with official_branding}
for s in 16 22 24 32 48 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    cp -p browser/branding/official/default${s}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/firefox.png
done
%else
for s in 16 22 24 32 48 256; do
    mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    cp -p browser/branding/unofficial/default${s}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/firefox.png
done
%endif

# We use %lang() for langpacks
echo > %{name}.lang
mkdir -p %{buildroot}%{_libdir}/firefox/langpacks
for langpack in %{_sourcedir}/*.xpi; do
    language="$(basename "$langpack" .xpi)"
    extensionID="langpack-$language@firefox.mozilla.org"

    rm -rf "$extensionID" "${extensionID}.xpi"
    mkdir -p "$extensionID"
    unzip -qq "$langpack" -d "$extensionID"
    find "$extensionID" -type f | xargs chmod 644

    cd "$extensionID"
    zip -qq -r9mX "../${extensionID}.xpi" .
    cd -

    install -m 644 "${extensionID}.xpi" %{buildroot}%{_libdir}/firefox/langpacks
    language="$(echo "$language" | sed -e 's/-/_/g')"
    echo "%%lang($language) %{_libdir}/firefox/langpacks/${extensionID}.xpi" >> %{name}.lang
done

# Install langpack workaround
function create_default_langpack() {
    language_long=$1
    language_short=$2
    cd %{buildroot}%{_libdir}/firefox/langpacks
    ln -s langpack-$language_long@firefox.mozilla.org.xpi langpack-$language_short@firefox.mozilla.org.xpi
    cd -
    echo "%%lang($language_short) %{_libdir}/firefox/langpacks/langpack-$language_short@firefox.mozilla.org.xpi" >> %{name}.lang
}

# Table of fallbacks for each language
create_default_langpack "es-AR" "es"
create_default_langpack "fy-NL" "fy"
create_default_langpack "ga-IE" "ga"
create_default_langpack "gu-IN" "gu"
create_default_langpack "hi-IN" "hi"
create_default_langpack "hy-AM" "hy"
create_default_langpack "nb-NO" "nb"
create_default_langpack "nn-NO" "nn"
create_default_langpack "pa-IN" "pa"
create_default_langpack "pt-PT" "pt"
create_default_langpack "sv-SE" "sv"
create_default_langpack "zh-TW" "zh"

# Default config
mkdir -p %{buildroot}%{_libdir}/firefox/browser/defaults/preferences
cp %{SOURCE202} %{buildroot}%{_libdir}/firefox/browser/defaults/preferences

# Add distribution.ini
mkdir -p %{buildroot}%{_libdir}/firefox/distribution
sed -e "s/__NAME__/%(source /etc/os-release; echo ${NAME})/" \
    -e "s/__ID__/%(source /etc/os-release; echo ${ID})/" \
    %{SOURCE203} > %{buildroot}%{_libdir}/firefox/distribution/distribution.ini

# Install appdata
# https://bugzilla.mozilla.org/show_bug.cgi?id=1071061
# We modify the upstream one here
mkdir -p %{buildroot}%{_datadir}/metainfo
sed -e "s/__VERSION__/%{version}/" \
    -e "s/__DATE__/$(date '+%F')/" \
    %{SOURCE204} > %{buildroot}%{_datadir}/metainfo/firefox.appdata.xml

# Install license file
install -Dpm0644 LICENSE %{buildroot}%{_libdir}/firefox

# Directory for system extensions
mkdir -p %{buildroot}%{_datadir}/mozilla/extensions/\{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
mkdir -p %{buildroot}%{_libdir}/mozilla/extensions/\{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}

# Use the system hunspell dictionaries
rm -rf %{buildroot}%{_libdir}/firefox/dictionaries
ln -s %{_datadir}/hunspell %{buildroot}%{_libdir}/firefox/dictionaries

# Delete unwanted files
rm -f %{buildroot}%{_libdir}/firefox/update-settings.ini
rm -f %{buildroot}%{_libdir}/firefox/removed-files

# There's no reason for any check, we already using PGO.
%check

%preun
# is it a final removal?
if [ $1 -eq 0 ]; then
    rm -rf %{_libdir}/firefox/components
    rm -rf %{_libdir}/firefox/extensions
    rm -rf %{_libdir}/firefox/plugins
    rm -rf %{_libdir}/firefox/langpacks
fi

%files -f %{name}.lang
%license %{_libdir}/firefox/LICENSE
%dir %{_datadir}/mozilla/extensions/*
%dir %{_libdir}/mozilla/extensions/*
%dir %{_libdir}/firefox/langpacks
%{_bindir}/firefox
%{_libdir}/firefox/application.ini
%{_libdir}/firefox/browser
%{_libdir}/firefox/crashreporter
%{_libdir}/firefox/crashhelper
%{_libdir}/firefox/defaults/pref/channel-prefs.js
%{_libdir}/firefox/dependentlibs.list
%{_libdir}/firefox/dictionaries
%{_libdir}/firefox/distribution
%{_libdir}/firefox/firefox
%{_libdir}/firefox/firefox-bin
%{_libdir}/firefox/fonts/TwemojiMozilla.ttf
%{_libdir}/firefox/glxtest
%{_libdir}/firefox/gmp-clearkey
%{_libdir}/firefox/omni.ja
%{_libdir}/firefox/pingsender
%{_libdir}/firefox/platform.ini
%ifarch riscv64
%{_libdir}/firefox/v4l2test
%endif
%{_libdir}/firefox/vaapitest
%{_libdir}/firefox/vulkantest
%{_libdir}/firefox/*.so
%{_datadir}/applications/firefox.desktop
%{_datadir}/icons/hicolor/16x16/apps/firefox.png
%{_datadir}/icons/hicolor/22x22/apps/firefox.png
%{_datadir}/icons/hicolor/24x24/apps/firefox.png
%{_datadir}/icons/hicolor/256x256/apps/firefox.png
%{_datadir}/icons/hicolor/32x32/apps/firefox.png
%{_datadir}/icons/hicolor/48x48/apps/firefox.png
%{_datadir}/metainfo/firefox.appdata.xml

%changelog
%autochangelog
