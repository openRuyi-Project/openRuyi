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
Version:        152.0.5
Release:        %autorelease
Summary:        Free web browser backed by Mozilla
License:        MPL-2.0
URL:            https://www.firefox.com
# https://bugzilla.mozilla.org/show_bug.cgi?id=1863519
VCS:            git:https://github.com/mozilla-firefox/firefox
#!RemoteAsset:  sha256:0a0341b05ac68834c4071665fe11f1e6729084b4e4ffcd70241097b0ad2cb224
Source0:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/source/%{name}-%{version}.source.tar.xz
# We need the language packs
#!RemoteAsset:  sha256:7af371b3da22dd067e5f5ae6c1aa7810f44642c4e8eeace9e50baf8e606a2720
Source1:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ach.xpi
#!RemoteAsset:  sha256:1309e34bdc3994c86a4f985917933379088d60851a0aa379c1f15d3c2c277f3e
Source2:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/af.xpi
#!RemoteAsset:  sha256:aceecd90d63374bcdf81935d6262b54137704ff7bed49ae11bae5b34fc95ebe5
Source3:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/an.xpi
#!RemoteAsset:  sha256:26cbaf7978fb35bb560e179179031215056b8fc667688eac1bcc084d76d63b96
Source4:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ar.xpi
#!RemoteAsset:  sha256:4446b0f30789080e16605e6dedff9a55c74f2aabf45ba986bdf9553b0977a63a
Source5:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ast.xpi
#!RemoteAsset:  sha256:e875e7ec55414d85df6380f5fa5958d8178ae6d63da3f0d64f7601a3e861d323
Source6:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/az.xpi
#!RemoteAsset:  sha256:62e785862572e973b5e471e649b78db080699348f25eef4041b307163e2a86e9
Source7:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/be.xpi
#!RemoteAsset:  sha256:f36f5fb5ecbcd7a68fffcbaaafb6d8069dc8c255e718c98d1ed84df3edf2a2cc
Source8:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bg.xpi
#!RemoteAsset:  sha256:6a0cdef8a6d2f0f9db51c6f45d9badd34be9b1a5c2f35a4ae484fdd9da08277d
Source9:        https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bn.xpi
#!RemoteAsset:  sha256:8437b9fc89b2b0ae389e21fdcffd22edf4147e07597d4d8e9ecc745f8e2a01d4
Source10:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/br.xpi
#!RemoteAsset:  sha256:de17a51e2d2ea9b099b6f3f13fe58501b564e9df20f26f8b050ff1a84513cff4
Source11:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/bs.xpi
#!RemoteAsset:  sha256:7899d003acf661f45d9fe969ae16652e15834ec7be1d996941469932c32a368b
Source12:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca-valencia.xpi
#!RemoteAsset:  sha256:bd048509c2142763d21d79642ff19daa69abd9da9413e353fc5896ec783ac0f6
Source13:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ca.xpi
#!RemoteAsset:  sha256:efa486ccaf7bfa473a367039fcf8e3c49c87ceef5bc78a87f0ee14ca447ed92e
Source14:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cak.xpi
#!RemoteAsset:  sha256:a815d03c348d0838189803d44cb4975ce8a25dde11072836c6929e39c00094e7
Source15:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cs.xpi
#!RemoteAsset:  sha256:da284d3ca0d5e0a3900a40c66e9c7fa435ad3281ad78d23e9c8dfe1e38407ab0
Source16:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/cy.xpi
#!RemoteAsset:  sha256:813d55caa9fc5c86c7207fa2cd2044e4a4c15acf0ca8c68b43f17b25909fb58d
Source17:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/da.xpi
#!RemoteAsset:  sha256:f38e26bb515c1427d46cd3638dfb2161d2111a087f54c97d6849be79d96f4e12
Source18:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/de.xpi
#!RemoteAsset:  sha256:ba0c49b444bbd462be4a6bc887fc9dcdf2829c139af36a24bb199103b8e59f88
Source19:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/dsb.xpi
#!RemoteAsset:  sha256:1efd93381861aa78104807d297fbad57c4d662ae00d662adb8068c8ceb17a567
Source20:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/el.xpi
#!RemoteAsset:  sha256:37c6a70f54e6824ad106d161029fbebbb2a6b9f7e73c2f9018e7576631d43d27
Source21:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-CA.xpi
#!RemoteAsset:  sha256:7b154475909e749842ff6512bd43e2a1a9b32784f1bafc932e5f2d06bb989071
Source22:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-GB.xpi
#!RemoteAsset:  sha256:a169754faef950792284f09e82c1f2c66d0f6d16821c5ddf06ac9a4cdc1afd5b
Source23:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/en-US.xpi
#!RemoteAsset:  sha256:a27392248da63b05cd734fc593b9074dc23ffce14266a7e45fb514cd7fb1d247
Source24:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eo.xpi
#!RemoteAsset:  sha256:f36561de8d963a576d36b0cd61730397f3c88c1fb51c9367f4bb6d0f25f93b5a
Source25:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-AR.xpi
#!RemoteAsset:  sha256:3f4708c33ad457cc5e4dbd1719de736d2e26a832662fb8e40e4fcafbb9077c72
Source26:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-CL.xpi
#!RemoteAsset:  sha256:0d947f75d45e24ee882b7cf922bd58ea0272ac118e5391dc82cd7d58fb4e8e92
Source27:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-ES.xpi
#!RemoteAsset:  sha256:f632cb706bf3899fecf2a2c5e6a78a809361add56d63d48cfe0d873968b2fcf6
Source28:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/es-MX.xpi
#!RemoteAsset:  sha256:d2a8f26376c755751a819835c858797c4b832b9e8cfea3d53e6c18f43d85de78
Source29:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/et.xpi
#!RemoteAsset:  sha256:111bf487a7316bda26dd73485c9bd8412885cb9b6a38881207286675200e2289
Source30:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/eu.xpi
#!RemoteAsset:  sha256:e43dfcfb88bc75905ecbd89dceaac89bc9a34320e7faf97a318587dbf35b1705
Source31:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fa.xpi
#!RemoteAsset:  sha256:6e7d97f7264f140436ac51064d8742ae7b1a42435c8bee2d7ede920c33a13112
Source32:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ff.xpi
#!RemoteAsset:  sha256:e66f446659bcf5dbba24c355f2e0947553ac670b342d2cf62a4ef5352e536d0d
Source33:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fi.xpi
#!RemoteAsset:  sha256:c74d25cdbba3fd65b76357a36af61cc6900b455baabca25e862f9249de556708
Source34:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fr.xpi
#!RemoteAsset:  sha256:0d8550faa4d94ecac9005ec500c0720488eab65ca78d5beb7b29c91c2dd908ba
Source35:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fur.xpi
#!RemoteAsset:  sha256:93458b241fc27ed7c64f79eeb5c982b13ddd117910d5bcce6d9e7601e97bb58f
Source36:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/fy-NL.xpi
#!RemoteAsset:  sha256:f47670f6bbc2fe813fec0378e14ebcd720aad5d1f3ddad275539d0feb8786715
Source37:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ga-IE.xpi
#!RemoteAsset:  sha256:7aa4ec326bcc3b3a310cc3b92ed2e731ff10b5735653aa54f7196454a2e624d7
Source38:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gd.xpi
#!RemoteAsset:  sha256:f563cf8573ce26b899bbdb9230f9d3060944349d5a8ac4a67a22c56ceddc524b
Source39:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gl.xpi
#!RemoteAsset:  sha256:6ba28b7d8b2c760c3a5a0500ab5476ce429e12cc9c4ccaf2bef9fabb829ac7cb
Source40:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gn.xpi
#!RemoteAsset:  sha256:b1b4af040bc440888e1e38012f851ca3987fa4c885f491eacdb6f5d6db9267d1
Source41:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/gu-IN.xpi
#!RemoteAsset:  sha256:e47bbf8869937d725fc66c268ded2f5df241fec0db6161eeb1edbbe8a1902805
Source42:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/he.xpi
#!RemoteAsset:  sha256:1986cf477e74c81bac8292a774fcab585e08901bd7cbc450d2ebe4779f33925e
Source43:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hi-IN.xpi
#!RemoteAsset:  sha256:5d088485e7d0fdd9ab814791f704ffbd46fb21606a92173e60d690a0cf89f369
Source44:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hr.xpi
#!RemoteAsset:  sha256:1d0c60e681e7ba8da1c37f87f3c149a033991ae0a37413ace9af3888af5e77fe
Source45:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hsb.xpi
#!RemoteAsset:  sha256:2777156e5da1bb3cc6d9dee3ff1d0844edf7d036092fd7a4c6dbf593d8e1b0b9
Source46:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hu.xpi
#!RemoteAsset:  sha256:156e6da63a44e9b6533adb6f8643d3f4c696c9685f8a3b4052c0d0e39cdbba60
Source47:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/hy-AM.xpi
#!RemoteAsset:  sha256:b1a9df7664da90868924651469a4becf6561baedaec7116b7f9421e89407a871
Source48:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ia.xpi
#!RemoteAsset:  sha256:b6970dccd1185d808c312e17ab36d413f39067e4216971ff627e49bc0bd30277
Source49:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/id.xpi
#!RemoteAsset:  sha256:6d55a2508565d3b70c7aeae387d092d4bfff17e06b9e24968b50d8f17618d625
Source50:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/is.xpi
#!RemoteAsset:  sha256:22b42d04d5894acfd7f34ae7b8ad39efcf02e05c8d2ef0cc43e2542966dfafdf
Source51:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/it.xpi
#!RemoteAsset:  sha256:686f61700505cbde0d38875b202aade08f48375ba5ef8f524a407b526fbe3fdc
Source52:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ja.xpi
#!RemoteAsset:  sha256:a16bfcac22dc8b5cee9a723e5a2779337e755ec68b7919797700dba1edaa68ed
Source53:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ka.xpi
#!RemoteAsset:  sha256:2900e420364f87679f86f95d9f29c29b59540b380c5510676e0c6420e2a61231
Source54:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kab.xpi
#!RemoteAsset:  sha256:ad1970632cca370f09b43a2bf95141364da139f0e1d818852465eaa094b4cebb
Source55:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kk.xpi
#!RemoteAsset:  sha256:1c05bab4e775ed7f1da59c704dd480f2c2ce64c1828e04ee0eda232d9dd03d4d
Source56:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/km.xpi
#!RemoteAsset:  sha256:90b2b9dab5e815d570c2096d27b92b4ba9d8b8d2f04f7014596ec04e97589530
Source57:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/kn.xpi
#!RemoteAsset:  sha256:6b92578d3941043ab07d4d6a7e936dcee50c90f62025c18f8de93edd5bed3a7a
Source58:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ko.xpi
#!RemoteAsset:  sha256:3ccbddbb641af18d5dc6e69ee8ecda61658ea90da88d9b11a29b73794f6689c9
Source59:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lij.xpi
#!RemoteAsset:  sha256:72d5324ec1222120cc12ecb88223c0b539ba4e92e587cfb49bc5e73f2243cc6a
Source60:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lt.xpi
#!RemoteAsset:  sha256:8f7f9c9298b6a7defaa51353f103e22e37454c3c0d5d234a0d4f0d3769974140
Source61:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/lv.xpi
#!RemoteAsset:  sha256:152cb5f0f3b52592781996ad03c25fa62e12b449fbfbbabc675ea06ee9f6531d
Source62:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mk.xpi
#!RemoteAsset:  sha256:df9a32e765f07810a838425e405ad5a46bc392f3ed9caaa179636c67f3b4e579
Source63:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/mr.xpi
#!RemoteAsset:  sha256:c0f50a58054f4d704f29fefa57b6a9ed0168a638ecd96ae46a91159e8535aed8
Source64:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ms.xpi
#!RemoteAsset:  sha256:b09ec2e5da92c04b5daabc2891562ae98cd1c11c840d8db61cb831415dd601b9
Source65:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/my.xpi
#!RemoteAsset:  sha256:1a1c8be5be93650a9ffda454452064e9ba55a760fd71bfff3b07a86ed5c5ea1d
Source66:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nb-NO.xpi
#!RemoteAsset:  sha256:7826aa1474464b5004f511fd861a3b630a0855c92d98cb6b0b49368f3505197d
Source67:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ne-NP.xpi
#!RemoteAsset:  sha256:454ea693dff710ef20bf4f2efea2844030d42337f272fc2f2adfca278b286ad9
Source68:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nl.xpi
#!RemoteAsset:  sha256:a70a49da9cb3002db5271176f61bc24b876fa37e6605c79ff15db607b78b16c5
Source69:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/nn-NO.xpi
#!RemoteAsset:  sha256:78209a2b196270afc58c966d9a03c41950cfb11467aaf92f7956faa9c1b736e5
Source70:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/oc.xpi
#!RemoteAsset:  sha256:5830fcffda1df1982359b63987c7b5b916567b8cec3b3fa24354a30794b5aa9a
Source71:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pa-IN.xpi
#!RemoteAsset:  sha256:fe04566f5be369eb8b538c86efc1cde6280b0e158a986718928fe674cb245e17
Source72:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pl.xpi
#!RemoteAsset:  sha256:2ed3b54b21d326a84f625b2ea383bcc75508aa464dfaff02fcda09be41585cdc
Source73:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-BR.xpi
#!RemoteAsset:  sha256:c0a87c9a5736b448cc626562aaad6b20adcd986a4f2eeade769efa96c81152dd
Source74:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/pt-PT.xpi
#!RemoteAsset:  sha256:513a01eece06a91e3423af00687ee40458a5fcf1ccce3ae62d0c9c12e5da514b
Source75:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/rm.xpi
#!RemoteAsset:  sha256:d796b1c47df389705f385be056da04f503531c14ec1b31a359ead9a008733e58
Source76:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ro.xpi
#!RemoteAsset:  sha256:5c84d664ae422410f149feabf2ce974e5c6e2003a90c06403e730f3c9960a547
Source77:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ru.xpi
#!RemoteAsset:  sha256:6fc49957aeee4b27205cd6a0a214ee40d8aa25b04fe9aa997d6a893d906bf7ef
Source78:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sat.xpi
#!RemoteAsset:  sha256:f7f479e6008f522839a5ee2f4ac7adf5f743b570186736ba8dff40f697753372
Source79:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sc.xpi
#!RemoteAsset:  sha256:de4900a5797ca84c90c19e14283619ede9d99999829ec13e47066251593b418d
Source80:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sco.xpi
#!RemoteAsset:  sha256:2e4320ccc98c1dda7f2d2d2a957ac44d208604fe8e4a16f093817b736ffdac35
Source81:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/si.xpi
#!RemoteAsset:  sha256:f8b976d95085c00059321f1181e226013e33a22ad8065b8e933e5d5bd2224635
Source82:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sk.xpi
#!RemoteAsset:  sha256:47aeaabefa6aefcb5b88cad446326f1bd9e7077c860f4834413292a55b28b90d
Source83:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/skr.xpi
#!RemoteAsset:  sha256:ed43041cd14b37b53aac487c73cef46ff39b05412b5ef74304917c9f313da395
Source84:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sl.xpi
#!RemoteAsset:  sha256:f026eaff6ff183473c04bad15ea66886328ce98f89d4e702288f1995f60ed265
Source85:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/son.xpi
#!RemoteAsset:  sha256:14fbadb53f5fbbc096392941377be42a01320072cad101efdd6987ca1ac6d184
Source86:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sq.xpi
#!RemoteAsset:  sha256:a7649799f98ece7c38f79c1e88e9db8c270188e3efc4f6e5236aec9062f80a77
Source87:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sr.xpi
#!RemoteAsset:  sha256:fe4639d2dcdf8bf5afe998fe94287a79a5dea0403474c2b6a85cd69bf6cfe046
Source88:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/sv-SE.xpi
#!RemoteAsset:  sha256:b08641e264d31ab2080d1d78458cab19e876ce6e5f44fb764a8a8af7acd163d2
Source89:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/szl.xpi
#!RemoteAsset:  sha256:65ebe38d61fa54298b6c6800e8706cebc4cf296be56f07e68e77878ac71c0333
Source90:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ta.xpi
#!RemoteAsset:  sha256:ef7d510a1fc1fd7f2e731eef6279a9e92b0a4a4629562953eee8f4c74587244b
Source91:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/te.xpi
#!RemoteAsset:  sha256:f0ced7e3e00be272c304a46a36f98db6d6e787ac0a6e55f279ef15ed3c4e6f6f
Source92:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tg.xpi
#!RemoteAsset:  sha256:51e2f359809ed091edae91cf6fdec8b2b5b49c74d4e5c30bef3a81c9db87bca9
Source93:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/th.xpi
#!RemoteAsset:  sha256:7714542cd4ee5e1c780eb8d59f4c0da3733b3c1037a81f644ebacb121fa701cc
Source94:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tl.xpi
#!RemoteAsset:  sha256:066f77d9fc236049fbef3a2af7a989170e52be8f3a94505e83a1b8e6c7e54dd1
Source95:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/tr.xpi
#!RemoteAsset:  sha256:d66a7093437ebe5cca3b773b529d62676ef9be19ad2f5e37d7989bc79f742ceb
Source96:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/trs.xpi
#!RemoteAsset:  sha256:5be0b8689096bf3fa0832063a224a46602c0de8b402232cf33ea4b0acf4d66eb
Source97:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uk.xpi
#!RemoteAsset:  sha256:1c963b8865e17c71189935eb9e7d5f27f2c8cb73f2612d70b8e744be955d84c5
Source98:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/ur.xpi
#!RemoteAsset:  sha256:6452f0695ed9000a3b7f31f72e6d6b8919619e9d4c424b65a5f5e44673e743cf
Source99:       https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/uz.xpi
#!RemoteAsset:  sha256:58289247a16ce549d0e8afd399c4d22a867df562a4bfcf53b9debc96852ea878
Source100:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/vi.xpi
#!RemoteAsset:  sha256:ed1c80355b0746831c004c7e4a7101824bc34e13a7a23af929411ccaf8f90540
Source101:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/xh.xpi
#!RemoteAsset:  sha256:01813d257e74a83c573ef1817f481fb4d242ba646d8c51c6584b7d0577e2cfa7
Source102:      https://ftp.mozilla.org/pub/firefox/releases/%{version}/linux-x86_64/xpi/zh-CN.xpi
#!RemoteAsset:  sha256:54ab8b50e4ad6387603d3d313074657848508271d4d8b93974b37da65df5a3eb
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
0001-add-GetSystemProxyDirect-to-libproxy-path.patch
2000-riscv64-Use-long-tail-jump-for-xptcall-stubs.patch
# https://bugzilla.mozilla.org/show_bug.cgi?id=1865601
2001-riscv64-enable-gles-rendering.patch
# https://phabricator.services.mozilla.com/D301784
2002-riscv64-libyuv-add-RVV-sources-to-build.patch
2003-blindly-set-rust-rva23-target-when-needed.patch
# Add riscv64 JIT simulator include guard patch for 152
2004-fix-riscv64-native-JIT-build-with-simulator-headers.patch

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

# Firefox crash reporter
%ifarch riscv64
# TODO: Still need porting for C++ breakpad
echo "ac_add_options --disable-crashreporter" >> .mozconfig
%else
echo "ac_add_options --enable-crashreporter" >> .mozconfig
%endif

# Some libraries we don't have but i think we should? - 251
%if %{with fdk_aac}
echo "ac_add_options --with-system-fdk-aac" >> .mozconfig
%endif

%build
%ifarch riscv64
FF_OPTFLAGS="%{optflags}"
# Otherwise will segmentation fault w/ V extension
# https://github.com/llvm/llvm-project/issues/198699
FF_OPTFLAGS="${FF_OPTFLAGS//-fstack-clash-protection/}"
echo "export CFLAGS=\"$FF_OPTFLAGS\""  >> .mozconfig
echo "export CXXFLAGS=\"$FF_OPTFLAGS\"" >> .mozconfig
%else
echo "export CFLAGS=\"%{optflags}\""   >> .mozconfig
echo "export CXXFLAGS=\"%{optflags}\"" >> .mozconfig
%endif
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
%ifnarch riscv64
%{_libdir}/firefox/crashreporter
%{_libdir}/firefox/crashhelper
%endif
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
