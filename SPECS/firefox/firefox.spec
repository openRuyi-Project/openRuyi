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
Version:        159.0
Release:        %autorelease
Summary:        Free web browser backed by Mozilla
License:        MPL-2.0
URL:            https://www.firefox.com
# https://bugzilla.mozilla.org/show_bug.cgi?id=1863519
VCS:            git:https://github.com/mozilla-firefox/firefox
#!RemoteAsset:  sha256:3d98df785894057fce60603e845828e758a5411ad79aaaaff2b8230597f500d9
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/source/%{name}-%{version}.source.tar.xz
# We need the language packs
#!RemoteAsset:  sha256:e5b17fbe5261c0889bc061553fbcf6fcfce43218c3729a33cebe417e769a7678
Source1:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ach.xpi
#!RemoteAsset:  sha256:1a77121c115b5a4d3f9fa9a745781b479a8018273260c856f0904f69bcd51103
Source2:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/af.xpi
#!RemoteAsset:  sha256:775e66d83e96bc117ba531d8de4dc58cca5478a4692e5d5945301ebfcf3c8a04
Source3:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/an.xpi
#!RemoteAsset:  sha256:3d846d4659f9e08051cdd33210b60ec0eea2448755353d755534c7f8df1d392f
Source4:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ar.xpi
#!RemoteAsset:  sha256:088bb8f69d756ce0625a26a1ea22a3af745d0af4627bcdb229c9ba4f5d355d00
Source5:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ast.xpi
#!RemoteAsset:  sha256:46a66d6a76fbf57f2954b21f730ebaa2f6ab6ef9fc9d500a45e977dd8a216aa8
Source6:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/az.xpi
#!RemoteAsset:  sha256:9ceedeba2fa992fb9ae884106ed684df78cf2c3b6c9e8dba9b23effcf73abdcb
Source7:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/be.xpi
#!RemoteAsset:  sha256:9f914af94a65298bc614eb12b148d150b403f7e086c51c0158d0314bc676075f
Source8:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bg.xpi
#!RemoteAsset:  sha256:169b70bdaf8ecdd15daa75ffc469f04e4eaa4bccfd8751b9a526c19a50781909
Source9:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bn.xpi
#!RemoteAsset:  sha256:0b24241b39d14809964d0231be10101fcc3c4ab35852207a5a2eea13403cf237
Source10:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/br.xpi
#!RemoteAsset:  sha256:9e252e8e73b99c2854c4b1c6870c6353165facdc32b3d3ea1fb09b461ae85e85
Source11:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bs.xpi
#!RemoteAsset:  sha256:36e157168474006d8ec07e0c690a0b09105a26a9f6b2b0b7679acd9084c1ae4e
Source12:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca-valencia.xpi
#!RemoteAsset:  sha256:1614ed1e08844fe7a11d56241cba1ccc3c84cb8f4cf432b7453a0f6f25f7b8e0
Source13:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca.xpi
#!RemoteAsset:  sha256:4ef7a1f9c9394745543b86701535ea573c2de13a44f6adbbd55242cf45255149
Source14:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cak.xpi
#!RemoteAsset:  sha256:3415c7c2f17b702d499282cdc197d9e2dadd6edb54400b40c8cb0eab4fdf8c7e
Source15:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cs.xpi
#!RemoteAsset:  sha256:c9dd28096a8f73f1eb7c930ea3214827a77bc98829f7080d9cf2b16973434d18
Source16:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cy.xpi
#!RemoteAsset:  sha256:7a559c43683f372fa734b9c91734b2be3ff2d5f0a8cf22d60af5ee61014a7997
Source17:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/da.xpi
#!RemoteAsset:  sha256:6f660f5a85e1e12d3d73057ec321903b521a7ea3662d2b560529cc07b83188ff
Source18:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/de.xpi
#!RemoteAsset:  sha256:ae055d246f560d3d38b6d4ae672419a562248038d00ce3251cf1d332cc11238b
Source19:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/dsb.xpi
#!RemoteAsset:  sha256:efd2035b2b92734600615bf04ed2936ba3b246c391d0b6aa851f7ff9dec39541
Source20:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/el.xpi
#!RemoteAsset:  sha256:77a9fa63c8f063372b30d256ea68d59f13b2fc847d8c03f124a308bafd6d90e5
Source21:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-CA.xpi
#!RemoteAsset:  sha256:ecf4f140533901c82e284f88c72ae51f2d15b8e19a06e7adfa31f732e13c1f23
Source22:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-GB.xpi
#!RemoteAsset:  sha256:a0de8f28794fbaf6423f9036ced22f932479249f7f44da767dd6e4c5fd1b395e
Source23:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-US.xpi
#!RemoteAsset:  sha256:327217d794fc57565943e64a5b232e10f73fa889c1efeffb246c930072b3d2a8
Source24:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eo.xpi
#!RemoteAsset:  sha256:eea37600376c006675b064852b754d9a649fea7c03253695a6e297efc8300feb
Source25:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-AR.xpi
#!RemoteAsset:  sha256:c518faa8c175902438ff42f1a3f88f108b5ce83f62f7792aef07d56cfa2e40cf
Source26:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-CL.xpi
#!RemoteAsset:  sha256:78fa34a356dbe72480d7829d2b10f2948e95d8a9b74df8a50f532ffc3f0736e8
Source27:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-ES.xpi
#!RemoteAsset:  sha256:dc6880425ffc3acbb7705bf7149dee0f88b4823a25098af30c1284ad5161ceb8
Source28:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-MX.xpi
#!RemoteAsset:  sha256:7a10dee8b9aee9b6916cf81454b6256b83002680bfe9e1210624a9d135412c7b
Source29:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/et.xpi
#!RemoteAsset:  sha256:5eb2d88c1aeff060a4916904940d684c4042fbf9dfe8b570c4af118a72d128a1
Source30:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eu.xpi
#!RemoteAsset:  sha256:b8d33f5f8203e456e91d0b279c07861bd66c5f85876ed823a0fdc77dda08cc27
Source31:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fa.xpi
#!RemoteAsset:  sha256:c8b60b676b913c3ce80928e198751799d4cfe9b37867427fe0d387bdfcf6e674
Source32:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ff.xpi
#!RemoteAsset:  sha256:61e58b89de11b1a1cbef0f73c2833f671074cb6299a5114c38b7742bc29bcc70
Source33:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fi.xpi
#!RemoteAsset:  sha256:e28de6d23ffe775957b15dd11539de21ca5e204a13e3abf68c96377c91d61115
Source34:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fr.xpi
#!RemoteAsset:  sha256:307794761dfc7039627ab477a8c7f488a1f7ec66fb260e61fd71fcc6f01bd114
Source35:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fur.xpi
#!RemoteAsset:  sha256:a7443853d8af5131b2fb1733172238aedb58d207c14cf5f328866b95e1e99a98
Source36:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fy-NL.xpi
#!RemoteAsset:  sha256:a12ea47deff2007f5d523c3a3f353e9db25e7399b14d0bfa0a66fa0e123604de
Source37:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ga-IE.xpi
#!RemoteAsset:  sha256:90abb4644d94c0fd097fda5dabb823b1fa3f8167ee7de1984bcc24c1cc66d61b
Source38:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gd.xpi
#!RemoteAsset:  sha256:269d35fb8f60d3a5c1b457dbaf82f0b59503918d0de0258510590b7093d7c440
Source39:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gl.xpi
#!RemoteAsset:  sha256:a9701902550492c900aec48a468c1bb8e948bfde06936c9ed554bd1c6df8662f
Source40:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gn.xpi
#!RemoteAsset:  sha256:1e618383a505b9bf783fbcb91c2fe0e8d62a6a83b66fae46a3e341e9a0144fd5
Source41:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gu-IN.xpi
#!RemoteAsset:  sha256:5b01fd00697c4564131763eec4a9250f3711ca614e0ac6957feef35acdcd6a4d
Source42:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/he.xpi
#!RemoteAsset:  sha256:59f064c0194c5bff3ca1fbf5209a7508ded45eebe728a25956809fb89691b82b
Source43:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hi-IN.xpi
#!RemoteAsset:  sha256:d0f9f2ad1140f43d54900446f7256c44d4dad0670f7072d0b146c2ea0b7f6d78
Source44:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hr.xpi
#!RemoteAsset:  sha256:b7549d1df4d7219fa1db417d84973dfc510b0d8f9515c7d5b0295b97f2dc0047
Source45:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hsb.xpi
#!RemoteAsset:  sha256:42da4a95c545491f6617598b8799b6048e3ba17fc36712919a035726746be818
Source46:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hu.xpi
#!RemoteAsset:  sha256:97408da2585814dda8955bcf96d32bb04edae7bf0db9422e374f2c640ab33681
Source47:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hy-AM.xpi
#!RemoteAsset:  sha256:465abfe8e7382d18a18a0ee6c7c22289f6a1c89f89cafa36e4f107f37d3fbc09
Source48:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ia.xpi
#!RemoteAsset:  sha256:5cd16168657dddbe26601e10e877f61d8a49b686de4c94886eae54dfdde3e703
Source49:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/id.xpi
#!RemoteAsset:  sha256:a6bd05c7dcea07a538e155c4907af4045457df9ea3117009e869eb73d3805f01
Source50:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/is.xpi
#!RemoteAsset:  sha256:3a36ed068618bfccdd117edbf0b53274aede7634f6f7b7440edaf361b3df098d
Source51:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/it.xpi
#!RemoteAsset:  sha256:774798788dc221d9dc54244c29bc5e31d41682cd2c6ff3ef92a1faa9dacccfb2
Source52:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ja.xpi
#!RemoteAsset:  sha256:00e9da9eeaac98d7f547ccd6d2f0a5a1d1525d835c88e7037cde7c2d4c6d3647
Source53:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ka.xpi
#!RemoteAsset:  sha256:042fc72db32d4e56f7558d94fa46299814c953eeb19f97dd2d65850600248c5a
Source54:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kab.xpi
#!RemoteAsset:  sha256:030fb6ad5ada8b507fdeecd752a3bb9399787b5f3876b8c7c9f4c15cdcde7e0d
Source55:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kk.xpi
#!RemoteAsset:  sha256:a20d54f7acd95172e143942e102e8a6e8617ca0bd303056485395a27a3481176
Source56:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/km.xpi
#!RemoteAsset:  sha256:684ec2e407680e6ab6c1c108af0049b929ef661fd941907eb85a950990b6d78b
Source57:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kn.xpi
#!RemoteAsset:  sha256:45f6c49482978403c1a0d1c8df4f1ec5b67c3e1f8fbb9a88c94144a745acae6b
Source58:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ko.xpi
#!RemoteAsset:  sha256:fb083740b2bc49796687bdace0e52d288d59b60aa48805741080860904ecb113
Source59:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lij.xpi
#!RemoteAsset:  sha256:9d93a6ee9f3be2a74cf1831b84dc9dcf75480d2a5eca5d08e2a74ae380d95ebf
Source60:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lt.xpi
#!RemoteAsset:  sha256:2a0686219f1cd533496c79b4b92001349784095a67ad0158915948e9016ecf74
Source61:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lv.xpi
#!RemoteAsset:  sha256:edf3f90b155b2a5153d1be16ecc6b123f8b8ad8e2aaaf4a04514b9daeb11d1f9
Source62:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mk.xpi
#!RemoteAsset:  sha256:1868b8a00972c7b00b1cc09da7816a9bb15bb3577c9a39af089b30831e94e8c4
Source63:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mr.xpi
#!RemoteAsset:  sha256:4b138d236aeaa12c4da621b1ba83e47dfd06d79dfcd8e5a74c86946c67649e65
Source64:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ms.xpi
#!RemoteAsset:  sha256:9db90b05ee3b35ebbf4638886287675e61ad7d86f6609cd10206a9281be70994
Source65:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/my.xpi
#!RemoteAsset:  sha256:a86b935940073d33dd180f4906a11d7af4d22169b493d21f7b21742f388ed622
Source66:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nb-NO.xpi
#!RemoteAsset:  sha256:3ea6bdc96bf1c8865b2503b241a414f95190f0fed5f614caded532705481eb4b
Source67:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ne-NP.xpi
#!RemoteAsset:  sha256:ee6d9694bda5c19c35a7de82f09e60f9d4d47a2b2c7f0865fdaec3c425bc1b1a
Source68:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nl.xpi
#!RemoteAsset:  sha256:d3cfb76087b281f60690f55ddab3c0c101ca2074ba6329dab3bec218957516d9
Source69:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nn-NO.xpi
#!RemoteAsset:  sha256:41962ddcba96272604b796ca8e06c482340d2076f5a9e1117b60af3872e9a6f5
Source70:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/oc.xpi
#!RemoteAsset:  sha256:6b48119ecb53afba6a4844719c711db01b185b6028c92d9679dc34d96383ff91
Source71:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pa-IN.xpi
#!RemoteAsset:  sha256:cacabb8f25d0e01a1d6a66f533aacd0932ad36b29b15e2b6127e9e62852e9873
Source72:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pl.xpi
#!RemoteAsset:  sha256:be70476ae8e47b5aeb79bcad91ceb7e66c460d5084f595d66d46cf60317995ef
Source73:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-BR.xpi
#!RemoteAsset:  sha256:e55e237112dedef3dc2240c4c9c7230d7bd56f5d899466d0555b734f6cb69258
Source74:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-PT.xpi
#!RemoteAsset:  sha256:4acf4874b7974db5a3269406591339ff2ed890eaaadce73b3b19b21f62f3ee61
Source75:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/rm.xpi
#!RemoteAsset:  sha256:3a81ee028bae6e55103453bfde6384d7393d549cd44b2dd556f8145389c84444
Source76:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ro.xpi
#!RemoteAsset:  sha256:2363b28c647470ab0b4431c38bdb1684f23cd73f2fdcb96154cfb5aa05476077
Source77:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ru.xpi
#!RemoteAsset:  sha256:1f3ff36742af836d81fb3c386382b1774da8a8b103245213f7b038b8bad17679
Source78:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sat.xpi
#!RemoteAsset:  sha256:01fa075203ce02e10841803eec71036761dabcd249609723c2eb7338a79218e9
Source79:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sc.xpi
#!RemoteAsset:  sha256:a14775ce73d0e89cfad8d8ad106d068f115c1c91a5ff0fcfc5c0b79d249140e7
Source80:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sco.xpi
#!RemoteAsset:  sha256:2837968809f3e7e5c61105fdd1723fcf36f7e9c53643068eec7ab10449dfe2a4
Source81:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/si.xpi
#!RemoteAsset:  sha256:213937c0bf72ae347bae434425a46f7d62c85a5d4ca3e807552e1a3568665e5c
Source82:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sk.xpi
#!RemoteAsset:  sha256:c962fc3d7f3f6ca17a419ac0759a82dccf451fe0a88585a13fb30e7d2834e107
Source83:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/skr.xpi
#!RemoteAsset:  sha256:cd8409db5273a2d521af62aea971d38f1ea48d6f4032bd030462d3101e819bb2
Source84:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sl.xpi
#!RemoteAsset:  sha256:0832cde6a50f13818f35440141fa0b2a08155f11e0ff3daa09ab0cc8a227b90d
Source85:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/son.xpi
#!RemoteAsset:  sha256:feea176d59c9f20327d9eca2bebf2b348e5118ce292ac292a93d787e8b56204a
Source86:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sq.xpi
#!RemoteAsset:  sha256:82abdbbfe17f1f0607f6c92987b1bfc70a1a2f009a21b560c886e5b6519c447e
Source87:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sr.xpi
#!RemoteAsset:  sha256:63bf41fb7c068c221eaa64ea156ac1a87b1a40225510109edec7806d1ad8e7e1
Source88:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sv-SE.xpi
#!RemoteAsset:  sha256:07ad7fae24c80a6b2406531a98b954d73c9c372ef72bf1f57f3e4485806c8a68
Source89:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/szl.xpi
#!RemoteAsset:  sha256:f31d389d61f8f5d28327e9c258bba0e17f1565fb05aad886dd443421a437b57e
Source90:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ta.xpi
#!RemoteAsset:  sha256:65b7f2728d0a030f37c05681d1ebe132713a0915479eeda83d8f4791ab504d7a
Source91:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/te.xpi
#!RemoteAsset:  sha256:39090df7d5ad3572bc97a0d8244be66339c66e71e6cda48fcbc6de622df8e78c
Source92:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tg.xpi
#!RemoteAsset:  sha256:79e0a2945f5c4e02d31fb445ff5a4395ba93cec53fd2a3afd477a583cc6e759f
Source93:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/th.xpi
#!RemoteAsset:  sha256:ca8a505d775954b62594f37c6bddf08d26ee0f8808ff290155cf1a253f9a9daa
Source94:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tl.xpi
#!RemoteAsset:  sha256:37b2dc82b6cfa1101ae418aedd7e417ce12344d8ac79be8ea862a2a66117de21
Source95:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tr.xpi
#!RemoteAsset:  sha256:d9e9af0552eea94680b2289b0a7aacea306b9c8cfb6ac34631e06b4883252357
Source96:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/trs.xpi
#!RemoteAsset:  sha256:4fe935ccbd53c447a4293a0dbbd05dcb94f01e8851388b9a4155c50acab8b746
Source97:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uk.xpi
#!RemoteAsset:  sha256:22444459e9279978f1b1700d84b7f17a5a57ce498dadb1209b3f0e4310dabd28
Source98:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ur.xpi
#!RemoteAsset:  sha256:9354c5ab982505bb52dd98f6e74dfd8ffdd34dc025d42fe1d0b80a491da838fb
Source99:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uz.xpi
#!RemoteAsset:  sha256:9b63d0f577ed292dea470359f2d610fcaca1491c49ea0d44ef74aae5f80e6e9c
Source100:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/vi.xpi
#!RemoteAsset:  sha256:3dd8d8a37aface01effc4c7052c2fd8b9f1714c655cbe85872d267bd493d51d2
Source101:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/xh.xpi
#!RemoteAsset:  sha256:9f7280e52ce27330a407979be5afbdcff2b56e04a26b0bcc811ec4df2c90de88
Source102:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/zh-CN.xpi
#!RemoteAsset:  sha256:172d8b64dadffd4b88c1096c090605f1ad288b70d29c3df5d751dfd26ef070d7
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
# https://bugzilla.mozilla.org/show_bug.cgi?id=1865601
2000-riscv64-enable-gles-rendering.patch
2001-blindly-set-rust-rva23-target-when-needed.patch
2002-add-riscv64-support-for-crash-context.patch
2003-enable-crashreporter-for-riscv64.patch
# https://github.com/ggml-org/ggml/pull/1571
# Rebased onto third_party/llama.cpp (ggml-cpu.c is ggml-cpu-c.c there);
# arch/riscv/repack.cpp and llamafile/sgemm.cpp hunks dropped, not vendored.
2004-riscv64-ggml-gate-RVV-code-on-the-target-extension.patch

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
%{_libdir}/firefox/gfxtest
%{_libdir}/firefox/gmp-clearkey
%{_libdir}/firefox/omni.ja
%{_libdir}/firefox/pingsender
%{_libdir}/firefox/platform.ini
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
