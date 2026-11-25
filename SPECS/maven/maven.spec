# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Use the upstream binary as the build tool until Maven can build itself.
%bcond bootstrap 1

# No native code: prevent RPM and OBS from generating debug file lists.
%global debug_package %{nil}
%undefine _build_create_debug

%global maven_home %{_datadir}/maven
# Use Aliyun's Maven Central mirror because direct downloads from Central
# failed in OBS source services.
%global maven_central_mirror https://maven.aliyun.com/repository/central

Name:           maven
Version:        3.10.1
Release:        %autorelease
Summary:        Java project management and build tool
License:        Apache-2.0 AND BSD-3-Clause AND EPL-2.0 AND LicenseRef-openRuyi-Public-Domain AND MIT
URL:            https://maven.apache.org/
VCS:            git:https://github.com/apache/maven.git
#!RemoteAsset:  sha256:440846130652a1764c207e076209e71cd2d6bb8fcc45e0f8f224f669231b9951
Source0:        https://archive.apache.org/dist/maven/maven-3/%{version}/source/apache-maven-%{version}-src.tar.gz
%if %{with bootstrap}
#!RemoteAsset:  sha256:810b8348f0a40f9116c202093fae007ebeabf67699bf34d81ee7e272289e085a
Source1:        https://archive.apache.org/dist/maven/maven-3/%{version}/binaries/apache-maven-%{version}-bin.tar.gz
%endif

#!RemoteAsset:  sha256:0addec670fedcd3f113c5c8091d783280d23f75e3acb841b61a9cdb079376a08
Source2:        %{maven_central_mirror}/aopalliance/aopalliance/1.0/aopalliance-1.0.jar
#!RemoteAsset:  sha256:26e82330157d6b844b67a8064945e206581e772977183e3e31fec6058aa9a59b
Source3:        %{maven_central_mirror}/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
#!RemoteAsset:  sha256:a466453608113de9009f99eb2099ef256c9f9f3cc4c0cb86eb4839692ceb54fd
Source4:        %{maven_central_mirror}/com/amazonaws/aws-java-sdk-bom/1.12.791/aws-java-sdk-bom-1.12.791.pom
#!RemoteAsset:  sha256:937afb220b91d8a394d78befdbf587c71aeed289d582e2a91e72a7d92172371d
Source5:        %{maven_central_mirror}/ch/qos/logback/logback-classic/1.2.13/logback-classic-1.2.13.jar
#!RemoteAsset:  sha256:901aa9a2b52aa5fb14c853fabcdd66090c915306b623c41e91e43c11ec85f301
Source6:        %{maven_central_mirror}/ch/qos/logback/logback-classic/1.2.13/logback-classic-1.2.13.pom
#!RemoteAsset:  sha256:07b1586faf220c05821d0f3ed8e2e417e214c83f40641f76e8a90b134c31ff6b
Source7:        %{maven_central_mirror}/ch/qos/logback/logback-core/1.2.13/logback-core-1.2.13.jar
#!RemoteAsset:  sha256:6a1402ecf487bb827315da679e1306e357b2aed2448578a8de058d5af39de9be
Source8:        %{maven_central_mirror}/ch/qos/logback/logback-core/1.2.13/logback-core-1.2.13.pom
#!RemoteAsset:  sha256:fa08315e836e63f337ad9d252194086aff541cdbd787a8b7903515ac3469364f
Source9:        %{maven_central_mirror}/ch/qos/logback/logback-parent/1.2.13/logback-parent-1.2.13.pom
#!RemoteAsset:  sha256:56682f914bb4e561dca08ea7b6fff641b78c7f8b4f2014c2577a95d0eef87bd6
Source10:       %{maven_central_mirror}/com/amazonaws/aws-java-sdk-pom/1.12.791/aws-java-sdk-pom-1.12.791.pom
#!RemoteAsset:  sha256:21ddb598807d3a51a876704eb979d9296e1c6a6f47ab1826ff88c6d6a127a2d0
Source11:       %{maven_central_mirror}/com/fasterxml/jackson/core/jackson-annotations/2.22/jackson-annotations-2.22.jar
#!RemoteAsset:  sha256:38c3ba52a0eade3e3eacc5b13499d56e1038ccbad8ec4bb79426dc21432b46d0
Source12:       %{maven_central_mirror}/com/fasterxml/jackson/core/jackson-annotations/2.22/jackson-annotations-2.22.pom
#!RemoteAsset:  sha256:ff167a6317be15895706c26668f45b898efe40ab8780970658210fe1393d52a6
Source13:       %{maven_central_mirror}/com/fasterxml/jackson/core/jackson-core/2.22.2/jackson-core-2.22.2.jar
#!RemoteAsset:  sha256:d2829cfef4c30d200e04d7f65009b4b112a46382aadf4534a30dd7f90cb164e5
Source14:       %{maven_central_mirror}/com/fasterxml/jackson/core/jackson-core/2.22.2/jackson-core-2.22.2.pom
#!RemoteAsset:  sha256:d0da14c12b16b5d54719aa172d83b542ff4abeb8b0fb7db476fde8ceece760ca
Source15:       %{maven_central_mirror}/com/fasterxml/jackson/core/jackson-databind/2.22.2/jackson-databind-2.22.2.jar
#!RemoteAsset:  sha256:a903aac4221725783341c8c7d30ccee43c1b5af67ff01325d2c5bc886d00941f
Source16:       %{maven_central_mirror}/com/fasterxml/jackson/core/jackson-databind/2.22.2/jackson-databind-2.22.2.pom
#!RemoteAsset:  sha256:a8c82982bdcd64e5b7cc8575a0459eab53d535a8309d6966274c93536e354234
Source17:       %{maven_central_mirror}/com/fasterxml/jackson/jackson-base/2.22.2/jackson-base-2.22.2.pom
#!RemoteAsset:  sha256:f6283647e701fda1cd312dcc21cb132a40f798f19e8e42fafc3fe347c5a51bbb
Source18:       %{maven_central_mirror}/com/fasterxml/jackson/jackson-bom/2.20.0/jackson-bom-2.20.0.pom
#!RemoteAsset:  sha256:a93ad5b8462f8d5920b128647a9b9f236342b4fd4e71287da9f7187fd8642f02
Source19:       %{maven_central_mirror}/com/fasterxml/jackson/jackson-bom/2.22.2/jackson-bom-2.22.2.pom
#!RemoteAsset:  sha256:bd8c30aecec123e7c00af8e8d1040d7bf824dcf175159623879aa28a3b6b2796
Source20:       %{maven_central_mirror}/com/github/chhorz/javadoc-parser/0.3.1/javadoc-parser-0.3.1.jar
#!RemoteAsset:  sha256:a8d9af4593afe065251d2fbfdf12693036aae514f76fb0c50e9d40aac3385c38
Source21:       %{maven_central_mirror}/com/github/chhorz/javadoc-parser/0.3.1/javadoc-parser-0.3.1.pom
#!RemoteAsset:  sha256:2dc0aa0eabd6f9f5a1f2fe62acfaa74caab834ced78518fed3750813e5dbd481
Source22:       %{maven_central_mirror}/com/github/chhorz/javadoc-parser-parent/0.3.1/javadoc-parser-parent-0.3.1.pom
#!RemoteAsset:  sha256:fda65a9ad0e1ac0c88987106e89aa4d8b2a2495e7e042371efa83813f65b7295
Source23:       %{maven_central_mirror}/com/github/cliftonlabs/json-simple/3.0.2/json-simple-3.0.2.jar
#!RemoteAsset:  sha256:b0dacb1479cd4dbe0810d1aa335bf0fb9bc3c4ff55369c87597ba68f5879fe4f
Source24:       %{maven_central_mirror}/com/github/cliftonlabs/json-simple/3.0.2/json-simple-3.0.2.pom
#!RemoteAsset:  sha256:b43b7f5c62e86b164fae70ae17d6911c5db60799af01057360afda82e4845be5
Source25:       %{maven_central_mirror}/com/fasterxml/jackson/jackson-parent/2.20/jackson-parent-2.20.pom
#!RemoteAsset:  sha256:f72ede1b39258faf81277dc58de30c71cbae4253732558d2ce10b53d8b5763d5
Source26:       %{maven_central_mirror}/com/github/luben/zstd-jni/1.5.6-3/zstd-jni-1.5.6-3.jar
#!RemoteAsset:  sha256:dfd2fa7b1d23939216902f844fa5e86a79cdfb9209760e4c04242b5a58d49490
Source27:       %{maven_central_mirror}/com/github/luben/zstd-jni/1.5.6-3/zstd-jni-1.5.6-3.pom
#!RemoteAsset:  sha256:7d45a7efb69df207bed7cc54b87a0bb012f10952c095570a273b49485da0d129
Source28:       %{maven_central_mirror}/com/fasterxml/jackson/jackson-parent/2.22/jackson-parent-2.22.pom
#!RemoteAsset:  sha256:8d6feb1da335f3ab13c584c613e23c7b3c61b392e37956872057baf8f0ca1d6f
Source29:       %{maven_central_mirror}/com/github/luben/zstd-jni/1.5.7-6/zstd-jni-1.5.7-6.jar
#!RemoteAsset:  sha256:794d9b995ed59165c54243dcc73fe9483d7fe1af7fb80fcd89a5ae5b693f3eb7
Source30:       %{maven_central_mirror}/com/github/luben/zstd-jni/1.5.7-6/zstd-jni-1.5.7-6.pom
#!RemoteAsset:  sha256:26ca8ed6f82c9d2ed7cd32298105bb65c0f9d899db61757a09741586fa93a639
Source31:       %{maven_central_mirror}/com/fasterxml/oss-parent/70/oss-parent-70.pom
#!RemoteAsset:  sha256:9206b7dd67fb138036576c3dfca947a2a8f3e2c4d2d9c1f2d1dea519b3a4dae1
Source32:       %{maven_central_mirror}/com/fasterxml/oss-parent/79/oss-parent-79.pom
#!RemoteAsset:  sha256:ceb271653ed99e15ffe52e4aedecdef8918434f19a4378a67f7ebe0ea8439058
Source33:       %{maven_central_mirror}/com/github/albfernandez/juniversalchardet/2.5.0/juniversalchardet-2.5.0.jar
#!RemoteAsset:  sha256:90df5ed604a5caff81967f186fa5aa0e984eaa55ca85932b31d046e11e6a6a7b
Source34:       %{maven_central_mirror}/com/github/albfernandez/juniversalchardet/2.5.0/juniversalchardet-2.5.0.pom
#!RemoteAsset:  sha256:b5499a3b1c40b16c0671fabe478c9aafeab38160c6fde74a6c13f42d86716ecd
Source35:       %{maven_central_mirror}/com/github/javaparser/javaparser-core/3.28.2/javaparser-core-3.28.2.jar
#!RemoteAsset:  sha256:87d2b333dfec96896d5a49e80a95b92ef572f610e848276b45eaa061e05b4132
Source36:       %{maven_central_mirror}/com/github/javaparser/javaparser-core/3.28.2/javaparser-core-3.28.2.pom
#!RemoteAsset:  sha256:a56e782b5b50811ac204073a355a21d915a2107fce13ec711331ad036f660fcc
Source37:       %{maven_central_mirror}/com/google/errorprone/error_prone_annotations/2.41.0/error_prone_annotations-2.41.0.jar
#!RemoteAsset:  sha256:a151df1e2e0b48618d8b06a180748a29b3abb39b1b2396f6a1c879a727488c6e
Source38:       %{maven_central_mirror}/com/google/errorprone/error_prone_annotations/2.41.0/error_prone_annotations-2.41.0.pom
#!RemoteAsset:  sha256:0358ce75bca1a54c141e16b7f1621e973fa177ddf64fe02b0f38df23ad400543
Source39:       %{maven_central_mirror}/com/github/javaparser/javaparser-parent/3.28.2/javaparser-parent-3.28.2.pom
#!RemoteAsset:  sha256:c538388d760a5c1c98dcf06f6ed3cfe5f11a651827db5cbd2ed8288c795cad42
Source40:       %{maven_central_mirror}/com/google/errorprone/error_prone_parent/2.41.0/error_prone_parent-2.41.0.pom
#!RemoteAsset:  sha256:087d02f39a46ab79b18f883ac7c3a3d6c2df1fd3bf7eaafeade699e0743d0dbe
Source41:       %{maven_central_mirror}/com/github/luben/zstd-jni/1.5.7-9/zstd-jni-1.5.7-9.jar
#!RemoteAsset:  sha256:e09d345e73ca3fbca7f3e05f30deb74e9d39dd6b79a93fee8c511f23417b6828
Source42:       %{maven_central_mirror}/com/google/google/5/google-5.pom
#!RemoteAsset:  sha256:4412e133520b8f9d01d3601080ce7fe146ee486f6a5a69ca9278d4a4ec69704d
Source43:       %{maven_central_mirror}/com/github/luben/zstd-jni/1.5.7-9/zstd-jni-1.5.7-9.pom
#!RemoteAsset:  sha256:cbfc3906b19b8f55dd7cfd6dfe0aa4532e834250d7f080bd8d211a3e246b59cb
Source44:       %{maven_central_mirror}/com/google/guava/failureaccess/1.0.3/failureaccess-1.0.3.jar
#!RemoteAsset:  sha256:c54beff37f6d42d43e14722d54a522c9ad51ef97fc5b79277e62a3ebf882f3bb
Source45:       %{maven_central_mirror}/com/google/guava/failureaccess/1.0.3/failureaccess-1.0.3.pom
#!RemoteAsset:  sha256:9646d4cd50094d4abe507e555d3f76d77e34a4c5566b22fb130ef55d4ebbe927
Source46:       %{maven_central_mirror}/com/google/guava/guava/30.1-jre/guava-30.1-jre.pom
#!RemoteAsset:  sha256:337664b30ade9b66e373b6efca1aba7421c1f8ff63643b8aa8b6d05d8efe8e8b
Source47:       %{maven_central_mirror}/com/google/code/gson/gson-parent/2.15.0/gson-parent-2.15.0.pom
#!RemoteAsset:  sha256:96d3dd843dc2911de01cdabcd50064cb9e860353102a0a78c96fd833d396fc7d
Source48:       %{maven_central_mirror}/com/google/code/gson/gson/2.15.0/gson-2.15.0.jar
#!RemoteAsset:  sha256:f8698ab46ca996ce889c1afc8ca4f25eb8ac6b034dc898d4583742360016cc04
Source49:       %{maven_central_mirror}/com/google/guava/guava-parent/26.0-android/guava-parent-26.0-android.pom
#!RemoteAsset:  sha256:e2afb747ebc4fe2328d6a90fa88c5d8a83bb1e32061bb9b10ff43e2c47ad6e73
Source50:       %{maven_central_mirror}/com/google/guava/guava-parent/30.1-jre/guava-parent-30.1-jre.pom
#!RemoteAsset:  sha256:7220ede61026596fbc720ee4b93246fa2d14f328058532b59ef053de397c7d83
Source51:       %{maven_central_mirror}/com/google/guava/guava-parent/33.4.0-android/guava-parent-33.4.0-android.pom
#!RemoteAsset:  sha256:426bc968a4e521865a58dd17a60389fed6195a1c357e3eb8bcb7cae31387bcae
Source52:       %{maven_central_mirror}/com/google/code/gson/gson/2.15.0/gson-2.15.0.pom
#!RemoteAsset:  sha256:18d4b1db26153d4e55079ce1f76bb1fe05cdb862ef9954a88cbcc4ff38b8679b
Source53:       %{maven_central_mirror}/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.pom
#!RemoteAsset:  sha256:142ad4475e19524d2fe3ac995b3f7cbc962fc726f2edb9dbdccc61feab9b2bf9
Source54:       %{maven_central_mirror}/com/google/inject/guice/5.1.0/guice-5.1.0-classes.jar
#!RemoteAsset:  sha256:b3b8dc65213d623fb70ed7958dbdd616324256ba836a31652560c388999fd9cd
Source55:       %{maven_central_mirror}/com/google/inject/guice/5.1.0/guice-5.1.0.pom
#!RemoteAsset:  sha256:63d5c0c641797deba6c051c47d5f6923f3a103ef71e4ebc3a85d01c3e878596c
Source56:       %{maven_central_mirror}/com/google/inject/guice-parent/5.1.0/guice-parent-5.1.0.pom
#!RemoteAsset:  sha256:4667724877f1d37a689202da191e23efa7657c62eef93ccdac406eccfe5cdd0a
Source57:       %{maven_central_mirror}/com/google/errorprone/error_prone_annotations/2.50.0/error_prone_annotations-2.50.0.jar
#!RemoteAsset:  sha256:71a0680d277324bab46bec4b00f6f111c1b794a931d0d8cda79bcb9246982f92
Source58:       %{maven_central_mirror}/com/google/errorprone/error_prone_annotations/2.50.0/error_prone_annotations-2.50.0.pom
#!RemoteAsset:  sha256:ff70c10165714fe9546c418a65d74ecd5d57623ba408cecde9428f0a609b5d1c
Source59:       %{maven_central_mirror}/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.jar
#!RemoteAsset:  sha256:e7ebaead3c95e74934451fc5b5ae9d02066303db67430f59fe219714efcf3bf3
Source60:       %{maven_central_mirror}/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.pom
#!RemoteAsset:  sha256:abf45a019db125b50ff55134ec2af94ae3519761038adf0a60b9bd7b4b8b6254
Source61:       %{maven_central_mirror}/com/google/errorprone/error_prone_parent/2.50.0/error_prone_parent-2.50.0.pom
#!RemoteAsset:  sha256:68719e687c6e4c9ff3e0fecbef7bd20896f0f4f7b314743ed33c72f962568215
Source62:       %{maven_central_mirror}/com/google/guava/guava-parent/33.5.0-jre/guava-parent-33.5.0-jre.pom
#!RemoteAsset:  sha256:552ad56800bc6010f1e6ea8c7638f24c74230e9991a52568df20d5b5aa5c4b20
Source63:       %{maven_central_mirror}/commons-beanutils/commons-beanutils/1.8.3/commons-beanutils-1.8.3.pom
#!RemoteAsset:  sha256:7d938c81789028045c08c065e94be75fc280527620d5bd62b519d5838532368a
Source64:       %{maven_central_mirror}/commons-beanutils/commons-beanutils/1.9.4/commons-beanutils-1.9.4.jar
#!RemoteAsset:  sha256:c35cca7b61d4678d9578cbc0b901b8717b539abf9254441da78b8fe60de064d0
Source65:       %{maven_central_mirror}/commons-beanutils/commons-beanutils/1.9.4/commons-beanutils-1.9.4.pom
#!RemoteAsset:  sha256:31b614120ff2858dd84fded11a96b8c00cb75abc8bfcdd14b6551050e27bcdc1
Source66:       %{maven_central_mirror}/com/google/guava/guava-parent/33.8.0-jre/guava-parent-33.8.0-jre.pom
#!RemoteAsset:  sha256:1e301f0c52ac248b0b14fdc3d12283c77252d4d6f48521d572e7d8c4c2cc4ac7
Source67:       %{maven_central_mirror}/com/google/guava/guava/33.5.0-jre/guava-33.5.0-jre.jar
#!RemoteAsset:  sha256:8f7f8605d68e15bf32db61ec94eac6fdafc51b1bdbe1e0e0802b57d23f387792
Source68:       %{maven_central_mirror}/commons-cli/commons-cli/1.11.0/commons-cli-1.11.0.jar
#!RemoteAsset:  sha256:96651f573e3c080e11052ff08bfc2e4cf04cf6eb1a3e3683010f4979496e0808
Source69:       %{maven_central_mirror}/commons-cli/commons-cli/1.11.0/commons-cli-1.11.0.pom
#!RemoteAsset:  sha256:0478fa78a908b3c31fe6d77be9978aaa621e2a181db84007e3d3b37424a2ac61
Source70:       %{maven_central_mirror}/com/google/guava/guava/33.5.0-jre/guava-33.5.0-jre.pom
#!RemoteAsset:  sha256:97b79ec3f2c0a6313a0c2df51ce1abdf8907e6531803467b81efcaaf99b35161
Source71:       %{maven_central_mirror}/com/google/guava/guava/33.8.0-jre/guava-33.8.0-jre.jar
#!RemoteAsset:  sha256:92a296728dc8d3c32193fdeb7f0a1e744384f1234ab71d306523f97a9d0cd51b
Source72:       %{maven_central_mirror}/com/google/guava/guava/33.8.0-jre/guava-33.8.0-jre.pom
#!RemoteAsset:  sha256:c1e7140d1dea8fdf3528bc1e3c5444ac0b541297311f45f9806c213ec3ee9a10
Source73:       %{maven_central_mirror}/commons-codec/commons-codec/1.11/commons-codec-1.11.pom
#!RemoteAsset:  sha256:b372a037d4230aa57fbeffdef30fd6123f9c0c2db85d0aced00c91b974f33f99
Source74:       %{maven_central_mirror}/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
#!RemoteAsset:  sha256:f700de80ac270d0344fdea7468201d8b9c805e5c648331c3619f2ee067ccfc59
Source75:       %{maven_central_mirror}/commons-codec/commons-codec/1.17.0/commons-codec-1.17.0.jar
#!RemoteAsset:  sha256:c01c4cda5e408f41ed1d83e4a0a170cf53801b6338aba49f0f904786bc1214fc
Source76:       %{maven_central_mirror}/commons-codec/commons-codec/1.17.0/commons-codec-1.17.0.pom
#!RemoteAsset:  sha256:5c3881e4f556855e9c532927ee0c9dfde94cc66760d5805c031a59887070af5f
Source77:       %{maven_central_mirror}/commons-codec/commons-codec/1.19.0/commons-codec-1.19.0.jar
#!RemoteAsset:  sha256:e0f3269fa23de0c83130c5659f5f9514cc5422c0bcdf45f2eae004a78b9fca34
Source78:       %{maven_central_mirror}/commons-codec/commons-codec/1.19.0/commons-codec-1.19.0.pom
#!RemoteAsset:  sha256:84d3a150518485f8140ea99b8a985656749629f6433c92b80c75b36aba3b099b
Source79:       %{maven_central_mirror}/com/google/j2objc/j2objc-annotations/3.1/j2objc-annotations-3.1.jar
#!RemoteAsset:  sha256:14570838500034fc1b47c8205ce1c9d6b255c1ccdd2d1afdcdcbf75e89b24a33
Source80:       %{maven_central_mirror}/com/google/j2objc/j2objc-annotations/3.1/j2objc-annotations-3.1.pom
#!RemoteAsset:  sha256:f94c98bbcfa1c1dac6956d6c3f494ec40265c67bf54ddefc95df4ffdd73ae6d5
Source81:       %{maven_central_mirror}/commons-cli/commons-cli/1.8.0/commons-cli-1.8.0.jar
#!RemoteAsset:  sha256:3ee7dc061eb9127db0c30220973e5aa83541304ffa83d7eab2350d1c885f8199
Source82:       %{maven_central_mirror}/commons-cli/commons-cli/1.8.0/commons-cli-1.8.0.pom
#!RemoteAsset:  sha256:d164fe79f262c32d9b18a0b5b2d317d1c27653d5e98fd2b998c24bf901c72ce4
Source83:       %{maven_central_mirror}/commons-codec/commons-codec/1.22.0/commons-codec-1.22.0.jar
#!RemoteAsset:  sha256:d9a565d978faa69d2b1195fb1ec27e60f29e7feb09afb85adac78f280068f8fe
Source84:       %{maven_central_mirror}/commons-codec/commons-codec/1.22.0/commons-codec-1.22.0.pom
#!RemoteAsset:  sha256:eeeae917917144a68a741d4c0dff66aa5c5c5fd85593ff217bced3fc8ca783b8
Source85:       %{maven_central_mirror}/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar
#!RemoteAsset:  sha256:d5d81fcc288c0d8c711c302007cada4aa9a226ed1a112d4baa64cb1d6322170b
Source86:       %{maven_central_mirror}/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.pom
#!RemoteAsset:  sha256:47504a3ce71d73a1b0af07675546b8d8c5af87f82ef12b6381f9eb3c17dd5a5b
Source87:       %{maven_central_mirror}/commons-codec/commons-codec/1.23.0/commons-codec-1.23.0.jar
#!RemoteAsset:  sha256:8c234370108606fee866044f5795124d941708ff4e70bfe7208e6b3d4d304031
Source88:       %{maven_central_mirror}/commons-codec/commons-codec/1.23.0/commons-codec-1.23.0.pom
#!RemoteAsset:  sha256:7f70f7c35068a99a9e0c527bdd6392a6e07678bd9933ca4429116b8275629f74
Source89:       %{maven_central_mirror}/eu/maveniverse/maven/domtrip/domtrip-core/1.5.1/domtrip-core-1.5.1.jar
#!RemoteAsset:  sha256:7d8ecbd2a7b860ef85b359134b5371c6ed23124cef2a45954a9773bf50c7ac3b
Source90:       %{maven_central_mirror}/eu/maveniverse/maven/domtrip/domtrip-core/1.5.1/domtrip-core-1.5.1.pom
#!RemoteAsset:  sha256:2e016fd7e3244b5f2c20acad834d93aa4790486ee1e4564641361a3e831eef59
Source91:       %{maven_central_mirror}/commons-io/commons-io/2.11.0/commons-io-2.11.0.pom
#!RemoteAsset:  sha256:d8ddc436506a6d2288bcb0cc12c0257793005af1ae67c53d7d7c6c1fd59d82af
Source92:       %{maven_central_mirror}/eu/maveniverse/maven/domtrip/domtrip-maven/1.5.1/domtrip-maven-1.5.1.jar
#!RemoteAsset:  sha256:415b72e29795d7f86711497150fff7fe12e809f2c481f8d591d07b7cedebb5ef
Source93:       %{maven_central_mirror}/eu/maveniverse/maven/domtrip/domtrip-maven/1.5.1/domtrip-maven-1.5.1.pom
#!RemoteAsset:  sha256:f41f7baacd716896447ace9758621f62c1c6b0a91d89acee488da26fc477c84f
Source94:       %{maven_central_mirror}/commons-io/commons-io/2.16.1/commons-io-2.16.1.jar
#!RemoteAsset:  sha256:5777d292251c7895c04a4c57015683ec3b353a12486c9b3e7178e9b0b3c38fff
Source95:       %{maven_central_mirror}/commons-io/commons-io/2.16.1/commons-io-2.16.1.pom
#!RemoteAsset:  sha256:484a939fff5310b8cb5c6b9029c2dcf155d3f93b8b8d6285f3f56bb2ba09fc49
Source96:       %{maven_central_mirror}/commons-io/commons-io/2.17.0/commons-io-2.17.0.pom
#!RemoteAsset:  sha256:824268919b4b62f9f40f08c54381de5993b078f58667e332d17348ae019d72b9
Source97:       %{maven_central_mirror}/commons-io/commons-io/2.19.0/commons-io-2.19.0.jar
#!RemoteAsset:  sha256:542b7a502ed61950d1b83112b51b1617d3407e3a4df5ab56a98d760e0f8c5950
Source98:       %{maven_central_mirror}/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom
#!RemoteAsset:  sha256:f109fb70888e5ec9b42ffd42d2324004a35f9b0eb64ec89092134f0dee3128cc
Source99:       %{maven_central_mirror}/eu/maveniverse/maven/domtrip/domtrip/1.5.1/domtrip-1.5.1.pom
#!RemoteAsset:  sha256:bdbdf81072c190ee9a8b181a5c58f5bd917a750fb13a256debbf53f5dbd33a2a
Source100:      %{maven_central_mirror}/commons-io/commons-io/2.20.0/commons-io-2.20.0.pom
#!RemoteAsset:  sha256:7d643a2afea8b058b762aa6fb90e5b256f6c729739f8b3784c3370ddc609e88d
Source101:      %{maven_central_mirror}/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar
#!RemoteAsset:  sha256:ae47795e721803ec8ff1deed74be28a811a02713bd5a3ab0ac67c2b58cb635ab
Source102:      %{maven_central_mirror}/commons-io/commons-io/2.21.0/commons-io-2.21.0.pom
#!RemoteAsset:  sha256:2b9a7b1f726fb86216dbd2c8321eabe0221dbd5b1be81c18e1cb53811b104758
Source103:      %{maven_central_mirror}/commons-io/commons-io/2.22.0/commons-io-2.22.0.jar
#!RemoteAsset:  sha256:6425cec0ea760035efa77277de85f89fa6dbed147ab3dd95b8d2cbc55340accf
Source104:      %{maven_central_mirror}/commons-io/commons-io/2.22.0/commons-io-2.22.0.pom
#!RemoteAsset:  sha256:ec0c2694d9958218506861f70a4c202efa746d7675b3a61ddcd95be43715f6ab
Source105:      %{maven_central_mirror}/eu/maveniverse/maven/parent/parent/52/parent-52.pom
#!RemoteAsset:  sha256:226cb33a644995b084b3bdd42f2eb861509e6db71d7a343d411ee321387b0860
Source106:      %{maven_central_mirror}/commons-jxpath/commons-jxpath/1.4.0/commons-jxpath-1.4.0.jar
#!RemoteAsset:  sha256:d7b9524036a834ca39e6575a8d124eb2020a1884f069468aed2746630afdb8ac
Source107:      %{maven_central_mirror}/commons-jxpath/commons-jxpath/1.4.0/commons-jxpath-1.4.0.pom
#!RemoteAsset:  sha256:59d50f5c951e6455c474fe5261b7d84b2c546b9c1fc73976fb2cd66db5849338
Source108:      %{maven_central_mirror}/io/netty/netty-bom/4.2.16.Final/netty-bom-4.2.16.Final.pom
#!RemoteAsset:  sha256:f61dde0da283b983ba0dbb42c2f501f81fec2da7945f2933128f2a6e410afc81
Source109:      %{maven_central_mirror}/io/netty/netty-bom/4.2.6.Final/netty-bom-4.2.6.Final.pom
#!RemoteAsset:  sha256:bdbb049465f366edb5a4adbff293a841c9b75b238519e76f86fe4f7bfb9d7e2d
Source110:      %{maven_central_mirror}/jakarta/annotation/ca-parent/1.3.5/ca-parent-1.3.5.pom
#!RemoteAsset:  sha256:85fb03fc054cdf4efca8efd9b6712bbb418e1ab98241c4539c8585bbc23e1b8a
Source111:      %{maven_central_mirror}/jakarta/annotation/jakarta.annotation-api/1.3.5/jakarta.annotation-api-1.3.5.jar
#!RemoteAsset:  sha256:ba6874767f5415c5e0f644fab80e1bad5feab6d18150f22638067681866feaaf
Source112:      %{maven_central_mirror}/jakarta/annotation/jakarta.annotation-api/1.3.5/jakarta.annotation-api-1.3.5.pom
#!RemoteAsset:  sha256:d0f2e16d054e8bb97add9ca26525eb2346f692809fcd2a28787da8ceb3c35ee8
Source113:      %{maven_central_mirror}/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.pom
#!RemoteAsset:  sha256:daddea1ea0be0f56978ab3006b8ac92834afeefbd9b7e4e6316fca57df0fa636
Source114:      %{maven_central_mirror}/commons-logging/commons-logging/1.2/commons-logging-1.2.jar
#!RemoteAsset:  sha256:c91ab5aa570d86f6fd07cc158ec6bc2c50080402972ee9179fe24100739fbb20
Source115:      %{maven_central_mirror}/commons-logging/commons-logging/1.2/commons-logging-1.2.pom
#!RemoteAsset:  sha256:71752ed4c2435a1d8385fe0a4d330f39d04efec89f0d1ba5d1598d39f7397a44
Source116:      %{maven_central_mirror}/org/apache/apache/39/apache-39.pom
#!RemoteAsset:  sha256:9c79f575a59ab5b622f591169411a4fdcfab71f8dc0440beaed87ac6b9b941f7
Source117:      %{maven_central_mirror}/org/apache/apache/40/apache-40.pom
#!RemoteAsset:  sha256:18ccd104cbd97eb44bd57b68c047ab7ff81fbc800987f82d815c68ac4c2304ce
Source118:      %{maven_central_mirror}/io/airlift/airbase/112/airbase-112.pom
#!RemoteAsset:  sha256:fdbef3137a28f63bb0cb93487803080ede746a4ec3d421e36c6f0c305c35e5e4
Source119:      %{maven_central_mirror}/io/airlift/aircompressor/0.27/aircompressor-0.27.jar
#!RemoteAsset:  sha256:5aacda89be38563bdf3bfac79333616c0802ca617070dea66ba649507c994441
Source120:      %{maven_central_mirror}/io/airlift/aircompressor/0.27/aircompressor-0.27.pom
#!RemoteAsset:  sha256:00f93263c267be201b8ae521b44a7137271b16688435340bf629db1bac0a5845
Source121:      %{maven_central_mirror}/org/apache/commons/commons-collections4/4.5.0/commons-collections4-4.5.0.jar
#!RemoteAsset:  sha256:c700f998e1d7a6a5c0aef1d4ceeb6bac7d1702dd6d6eda73a17d67f5d6f2467d
Source122:      %{maven_central_mirror}/org/apache/commons/commons-collections4/4.5.0/commons-collections4-4.5.0.pom
#!RemoteAsset:  sha256:32be0e1e76673092f5d12cb790bd2acb6c2ab04c4ea6efc69ea5ee17911c24fe
Source123:      %{maven_central_mirror}/org/apache/commons/commons-csv/1.14.1/commons-csv-1.14.1.jar
#!RemoteAsset:  sha256:95df735302c0ab92cec05a2b51e2270758e15f0a64186de65662eb148ebd97fd
Source124:      %{maven_central_mirror}/org/apache/commons/commons-csv/1.14.1/commons-csv-1.14.1.pom
#!RemoteAsset:  sha256:13dcf3850478ef8de5d24d298a60eed5e8305eb20538fe632c82ea1dff6b5ea0
Source125:      %{maven_central_mirror}/org/apache/commons/commons-exec/1.6.0/commons-exec-1.6.0.jar
#!RemoteAsset:  sha256:5bdc512196cda20dce9e2632d7ae7b8b4a1d333ed437e033ebda64a499897ac5
Source126:      %{maven_central_mirror}/org/apache/commons/commons-exec/1.6.0/commons-exec-1.6.0.pom
#!RemoteAsset:  sha256:a2af247ec4db6eb8947e18e23e0433e4871a7c5d0a40e1f92e46ede54ae1defe
Source127:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.21.0/commons-lang3-3.21.0.jar
#!RemoteAsset:  sha256:91c77044a50c481636c32d916fd89c9118a72195390452c81065080f957de7ff
Source128:      %{maven_central_mirror}/javax/inject/javax.inject/1/javax.inject-1.jar
#!RemoteAsset:  sha256:943e12b100627804638fa285805a0ab788a680266531e650921ebfe4621a8bfa
Source129:      %{maven_central_mirror}/javax/inject/javax.inject/1/javax.inject-1.pom
#!RemoteAsset:  sha256:9420ac3c5efb5bcf804552a7bec00a2d857120977fc12151f7606a67ba7a184d
Source130:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.21.0/commons-lang3-3.21.0.pom
#!RemoteAsset:  sha256:31a68daabb4b361453788b9045ac87a6ae87c705e578facd99e4d9ddb6a481e9
Source131:      %{maven_central_mirror}/org/apache/commons/commons-parent/105/commons-parent-105.pom
#!RemoteAsset:  sha256:0e6b935bfcb3e451d525956acad53ec86ff916d714abdbd32b3d2039771896f8
Source132:      %{maven_central_mirror}/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.jar
#!RemoteAsset:  sha256:3b39ca3d5ebb9ab757f9d42dcd6b677c88b4828edca7f6079f11bbf2ef3cee58
Source133:      %{maven_central_mirror}/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.pom
#!RemoteAsset:  sha256:030704139e46f32c38d27060edee9e0676b0a0fff8a8be53461515154ba8a7be
Source134:      %{maven_central_mirror}/net/bytebuddy/byte-buddy/1.12.19/byte-buddy-1.12.19.jar
#!RemoteAsset:  sha256:435fb8664aa9b7e120c8dd6c707d4eafa642fa262dff6d5e3f71dc25c69e89eb
Source135:      %{maven_central_mirror}/net/bytebuddy/byte-buddy/1.12.19/byte-buddy-1.12.19.pom
#!RemoteAsset:  sha256:30272167eceb1cb68fa84730a12d1abfd1daed6ae0c19fdefee47a9a9a0cfd33
Source136:      %{maven_central_mirror}/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.jar
#!RemoteAsset:  sha256:8712c22885e16de69179f921d501516493a7cef64997995fc428e7e58b12ea8d
Source137:      %{maven_central_mirror}/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.pom
#!RemoteAsset:  sha256:3a70240de7cdcde04e7c504c2327d7035b9c25ae0206881e3bf4e6798a273ed8
Source138:      %{maven_central_mirror}/net/bytebuddy/byte-buddy-agent/1.12.19/byte-buddy-agent-1.12.19.jar
#!RemoteAsset:  sha256:b5a2cff643681de1687fc40acd251feefdfca23e673e049fb3c3692b53526d4b
Source139:      %{maven_central_mirror}/net/bytebuddy/byte-buddy-agent/1.12.19/byte-buddy-agent-1.12.19.pom
#!RemoteAsset:  sha256:1fceef152e3962c8fbb3a860110324c7b14f417b925b07edf6ba997cdcf52eb9
Source140:      %{maven_central_mirror}/net/bytebuddy/byte-buddy-parent/1.10.14/byte-buddy-parent-1.10.14.pom
#!RemoteAsset:  sha256:72ab6fef409e812921f4728b3c4b6ef4fa53bc25fabb0488fc2cae367368b54d
Source141:      %{maven_central_mirror}/net/bytebuddy/byte-buddy-parent/1.12.19/byte-buddy-parent-1.12.19.pom
#!RemoteAsset:  sha256:60335a34e91f49ce50723b007d7c12514fd5766da17dfffb6732e1131e58cd1b
Source142:      %{maven_central_mirror}/org/apache/commons/commons-parent/70/commons-parent-70.pom
#!RemoteAsset:  sha256:a88b5f6165a659bf835441837bcc5c53e99fde79b92cfbb86988ce2954cd5267
Source143:      %{maven_central_mirror}/org/apache/commons/commons-parent/93/commons-parent-93.pom
#!RemoteAsset:  sha256:58d2da30f058512a1e7f914e39241deca4dff5c27a085b4ed2faa9e7208067f6
Source144:      %{maven_central_mirror}/org/apache/commons/commons-text/1.15.0/commons-text-1.15.0.jar
#!RemoteAsset:  sha256:5e5168687bcedaea2aa8556b8b32f5afa08efcbc31d11b947c8676987bc9d239
Source145:      %{maven_central_mirror}/org/apache/commons/commons-text/1.15.0/commons-text-1.15.0.pom
#!RemoteAsset:  sha256:ff513db0361fd41237bef4784968bc15aae478d4ec0a9496f811072ccaf3841d
Source146:      %{maven_central_mirror}/org/apache/apache/13/apache-13.pom
#!RemoteAsset:  sha256:9f85ff2fd7d6cb3097aa47fb419ee7f0ebe869109f98aba9f4eca3f49e74a40e
Source147:      %{maven_central_mirror}/org/apache/apache/16/apache-16.pom
#!RemoteAsset:  sha256:7831307285fd475bbc36b20ae38e7882f11c3153b1d5930f852d44eda8f33c17
Source148:      %{maven_central_mirror}/org/apache/apache/18/apache-18.pom
#!RemoteAsset:  sha256:91f7a33096ea69bac2cbaf6d01feb934cac002c48d8c8cfa9c240b40f1ec21df
Source149:      %{maven_central_mirror}/org/apache/apache/19/apache-19.pom
#!RemoteAsset:  sha256:af10c108da014f17cafac7b52b2b4b5a3a1c18265fa2af97a325d9143537b380
Source150:      %{maven_central_mirror}/org/apache/apache/21/apache-21.pom
#!RemoteAsset:  sha256:bc10624e0623f36577fac5639ca2936d3240ed152fb6d8d533ab4d270543491c
Source151:      %{maven_central_mirror}/org/apache/apache/23/apache-23.pom
#!RemoteAsset:  sha256:3e49037174820bbd0df63420a977255886398954c2a06291fa61f727ac35b377
Source152:      %{maven_central_mirror}/org/apache/apache/29/apache-29.pom
#!RemoteAsset:  sha256:63dd4a393a9c0dfcb314efe83871a41d243bc8d200cbc7f2d197f30da78239d8
Source153:      %{maven_central_mirror}/org/apache/apache/30/apache-30.pom
#!RemoteAsset:  sha256:555d0c9eaa69c042aff924927b9381e8f8174136d355eead445224452e6291cc
Source154:      %{maven_central_mirror}/org/apache/apache/31/apache-31.pom
#!RemoteAsset:  sha256:cfd872c0ec27f53ae68f43dbc0fecded8add773079a53afbd390e407b42ce72f
Source155:      %{maven_central_mirror}/org/apache/apache/32/apache-32.pom
#!RemoteAsset:  sha256:d78bd8524c5f8380a190a6525686629a95dfe512df21111383a6d8c0923a4415
Source156:      %{maven_central_mirror}/org/apache/apache/33/apache-33.pom
#!RemoteAsset:  sha256:3671ae9d4d062ae3bb985731c76088bb2f6f7d7254e2d304ee9f690b97651328
Source157:      %{maven_central_mirror}/org/apache/apache/34/apache-34.pom
#!RemoteAsset:  sha256:ea297dcd114136e8b8e8b630230d52a76c2fc69f6c5db25d672b1857000728b8
Source158:      %{maven_central_mirror}/org/apache/apache/35/apache-35.pom
#!RemoteAsset:  sha256:524ec4787aff73af6b3a9fafa154c7f1881b648299b663fdbfcadda1286f2353
Source159:      %{maven_central_mirror}/org/apache/apache/37/apache-37.pom
#!RemoteAsset:  sha256:9b0a5f28ddfb4b7500a37022bee8245efdd044fb9a3d79fb827550923eccc4b5
Source160:      %{maven_central_mirror}/org/apache/apache/38/apache-38.pom
#!RemoteAsset:  sha256:9e9323a26ba8eb2394efef0c96d31b70df570808630dc147cab1e73541cc5194
Source161:      %{maven_central_mirror}/org/apache/apache/4/apache-4.pom
#!RemoteAsset:  sha256:75d6c37125ebae7d6386d79fdb9cf8a4654fadbf101617f79e4f4f00f533fc35
Source162:      %{maven_central_mirror}/org/apache/cxf/cxf-bom/4.0.9/cxf-bom-4.0.9.pom
#!RemoteAsset:  sha256:8a312ab82867126a058ff7a081ddece930fb48d460b29172a24ecc8720aceb41
Source163:      %{maven_central_mirror}/org/apache/cxf/cxf/4.0.9/cxf-4.0.9.pom
#!RemoteAsset:  sha256:1397ce1db433adc9f223dbf07496d133681448751f4ae29e58f68e78fb4b6c25
Source164:      %{maven_central_mirror}/org/apache/apache/7/apache-7.pom
#!RemoteAsset:  sha256:4946e60a547c8eda69f3bc23c5b6f0dadcf8469ea49b1d1da7de34aecfcf18dd
Source165:      %{maven_central_mirror}/org/apache/apache/9/apache-9.pom
#!RemoteAsset:  sha256:eb9dba4d79e9984360fe7768671a4c1cfb84d594d92f952803decdcc82a613fe
Source166:      %{maven_central_mirror}/org/apache/apache/resources/apache-jar-resource-bundle/1.8/apache-jar-resource-bundle-1.8.jar
#!RemoteAsset:  sha256:b8ac2332849711b2f7474415937bdbb967d2b9300ef4cffe3f35be3b1aa18a4e
Source167:      %{maven_central_mirror}/org/apache/logging/log4j/log4j-bom/2.25.1/log4j-bom-2.25.1.pom
#!RemoteAsset:  sha256:b465db838dd482a994d32a088bea4bcbaa62cfb8b2853511a9f8c3e769402c74
Source168:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-sink-api/2.1.0/doxia-sink-api-2.1.0.jar
#!RemoteAsset:  sha256:618112f616b84b9cd87165a81c998563c7f114e2b9f39eaeaa09260a1135570c
Source169:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-sink-api/2.1.0/doxia-sink-api-2.1.0.pom
#!RemoteAsset:  sha256:60d320f3a7b36047cc2969397aa8f0ce673afcd88a60ef04e2b032b7c0011969
Source170:      %{maven_central_mirror}/org/apache/maven/doxia/doxia/2.1.0/doxia-2.1.0.pom
#!RemoteAsset:  sha256:cca55222e1de7cb3beb082eca5a18f43c80e4e748313a318b18b2b404d1bd340
Source171:      %{maven_central_mirror}/org/apache/maven/enforcer/enforcer-api/3.6.3/enforcer-api-3.6.3.jar
#!RemoteAsset:  sha256:9168a03141d8fc7eda21a2360d83cc0412bcbb1d6204d992bd48c2573cb3c6b8
Source172:      %{maven_central_mirror}/org/apache/commons/commons-compress/1.26.2/commons-compress-1.26.2.jar
#!RemoteAsset:  sha256:1428719895cd0a913aee33e2424b9a804b10f1197e5d35a9ce99cf2a1174cb0e
Source173:      %{maven_central_mirror}/org/apache/commons/commons-compress/1.26.2/commons-compress-1.26.2.pom
#!RemoteAsset:  sha256:e1522945218456f3649a39bc4afd70ce4bd466221519dba7d378f2141a4642ca
Source174:      %{maven_central_mirror}/org/apache/commons/commons-compress/1.28.0/commons-compress-1.28.0.jar
#!RemoteAsset:  sha256:033f4c78d632da88d0eb8ead974fc14a264392cebf12ab6c68d6cea7adf0c64a
Source175:      %{maven_central_mirror}/org/apache/commons/commons-compress/1.28.0/commons-compress-1.28.0.pom
#!RemoteAsset:  sha256:1c150e3d2df4b4237b47e28fea2079fb0da324578d5cca6a5fed2e37a62082ec
Source176:      %{maven_central_mirror}/org/apache/commons/commons-digester3/3.2/commons-digester3-3.2.jar
#!RemoteAsset:  sha256:5bb8a198adb597c30204b4f1c336fdb3d2816536403e9ad3349ab200032e5445
Source177:      %{maven_central_mirror}/org/apache/commons/commons-digester3/3.2/commons-digester3-3.2.pom
#!RemoteAsset:  sha256:005b5a3a88736bd2584f69cc59467e67c106e6a4b7a2dbd1ba2251267e96011d
Source178:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.10/commons-lang3-3.10.pom
#!RemoteAsset:  sha256:562c3998fa5382f907b6ba6e1c97f987fdf72e8dc7c04e5b586bdb53de7c0eb3
Source179:      %{maven_central_mirror}/org/apache/maven/enforcer/enforcer-api/3.6.3/enforcer-api-3.6.3.pom
#!RemoteAsset:  sha256:110438863bad37c28f906bf87016e38c7a8c758ba321e09d11dc5a2363a8e79e
Source180:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.pom
#!RemoteAsset:  sha256:6ee731df5c8e5a2976a1ca023b6bb320ea8d3539fbe64c8a1d5cb765127c33b4
Source181:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.jar
#!RemoteAsset:  sha256:351c6e4940e939b1f330df47f60f13ba383db81ee008181af541f3a2a6d2a56c
Source182:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom
#!RemoteAsset:  sha256:4eeeae8d20c078abb64b015ec158add383ac581571cddc45c68f0c9ae0230720
Source183:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.18.0/commons-lang3-3.18.0.jar
#!RemoteAsset:  sha256:aa254b373b6f6d46bc9dca86331b072a8ab86eb25ea9921fd439618392e98a16
Source184:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.18.0/commons-lang3-3.18.0.pom
#!RemoteAsset:  sha256:24bad9159ed9af932488bad1be042471a170a5bc822bfc8f7b29f3c297c1e138
Source185:      %{maven_central_mirror}/org/apache/maven/enforcer/enforcer-rules/3.6.3/enforcer-rules-3.6.3.jar
#!RemoteAsset:  sha256:610eec18af07156d273d5ca2acc36d78a015a12b38ce806d47d74b98e911b2ea
Source186:      %{maven_central_mirror}/org/apache/maven/enforcer/enforcer-rules/3.6.3/enforcer-rules-3.6.3.pom
#!RemoteAsset:  sha256:69e5c9fa35da7a51a5fd2099dfe56a2d8d32cf233e2f6d770e796146440263f4
Source187:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar
#!RemoteAsset:  sha256:7ca83b2709c1e7a9e03b576cd41422190379489a80866e542f8c8b955411a2aa
Source188:      %{maven_central_mirror}/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.pom
#!RemoteAsset:  sha256:24f2e52bde65e2dc9cfcebb2fc22d8de0edb3726925ccf80b13db4eeb515a302
Source189:      %{maven_central_mirror}/org/apache/commons/commons-parent/14/commons-parent-14.pom
#!RemoteAsset:  sha256:fb8c5e55e30a7addb4ff210858a0e8d2494ed6757bbe19012da99d51586c3cbb
Source190:      %{maven_central_mirror}/org/apache/commons/commons-parent/22/commons-parent-22.pom
#!RemoteAsset:  sha256:3a2e69d06d641d1f3b293126dc9e2e4ea6563bf8c36c87e0ab6fa4292d04b79c
Source191:      %{maven_central_mirror}/org/apache/commons/commons-parent/34/commons-parent-34.pom
#!RemoteAsset:  sha256:87cd27e1a02a5c3eb6d85059ce98696bb1b44c2b8b650f0567c86df60fa61da7
Source192:      %{maven_central_mirror}/org/apache/commons/commons-parent/39/commons-parent-39.pom
#!RemoteAsset:  sha256:cd313494c670b483ec256972af1698b330e598f807002354eb765479f604b09c
Source193:      %{maven_central_mirror}/org/apache/commons/commons-parent/42/commons-parent-42.pom
#!RemoteAsset:  sha256:63ea934ece526118aab7963da5078f976e29355e1a472e24c54e2c0efecdfb47
Source194:      %{maven_central_mirror}/org/apache/maven/enforcer/enforcer/3.6.3/enforcer-3.6.3.pom
#!RemoteAsset:  sha256:8a8ecb570553bf9f1ffae211a8d4ca9ee630c17afe59293368fba7bd9b42fcb7
Source195:      %{maven_central_mirror}/org/apache/commons/commons-parent/47/commons-parent-47.pom
#!RemoteAsset:  sha256:9037dee318a68d7ee5dd2e20f2e657a39597ed2622b52e325ab9becddfbc4d38
Source196:      %{maven_central_mirror}/org/apache/maven/maven-archiver/3.6.6/maven-archiver-3.6.6.jar
#!RemoteAsset:  sha256:8bd632c00bdf80a7de36c22b60f12452c147d8eca2f00d79d66699ebe7daa02a
Source197:      %{maven_central_mirror}/org/apache/commons/commons-parent/5/commons-parent-5.pom
#!RemoteAsset:  sha256:7b7a2db3f747074b5867f553d5efc8072be26ede32879d052c347e7c81117f06
Source198:      %{maven_central_mirror}/org/apache/commons/commons-parent/50/commons-parent-50.pom
#!RemoteAsset:  sha256:4232a2477bcaacca4cb1b67af032d8683fc6a61aebd96a61a901ebc7e7e391e1
Source199:      %{maven_central_mirror}/org/apache/maven/maven-archiver/3.6.6/maven-archiver-3.6.6.pom
#!RemoteAsset:  sha256:75dbe8f34e98e4c3ff42daae4a2f9eb4cbcd3b5f1047d54460ace906dbb4502e
Source200:      %{maven_central_mirror}/org/apache/commons/commons-parent/52/commons-parent-52.pom
#!RemoteAsset:  sha256:6f19638994e8357b4ed734696f992057efaafa1235673998133299798e2ccddb
Source201:      %{maven_central_mirror}/org/apache/commons/commons-parent/64/commons-parent-64.pom
#!RemoteAsset:  sha256:ca906201ee34de09e76632c5dec04a9b868ee38ce68c134b765fd1871d1d3eed
Source202:      %{maven_central_mirror}/org/apache/maven/maven-parent/49/maven-parent-49.pom
#!RemoteAsset:  sha256:cf9f5cddd094740deb8912cfe06ddeda81f8bd914779aa9037488c27d08fe7da
Source203:      %{maven_central_mirror}/org/apache/maven/maven-parent/50/maven-parent-50.pom
#!RemoteAsset:  sha256:d50da9c39bdca823d618d1b4a03b73f196497fcb8616fd0da727c8623592a9bb
Source204:      %{maven_central_mirror}/org/apache/commons/commons-parent/69/commons-parent-69.pom
#!RemoteAsset:  sha256:4ed44560b07f8448479dfd1e83a422ba4e83e60b36e51b2871ac502a6d5c1bea
Source205:      %{maven_central_mirror}/org/apache/commons/commons-parent/73/commons-parent-73.pom
#!RemoteAsset:  sha256:80eb61b0c87fdd826a069313b28b672da3f1885832da447b51e6e8a6197e7ecb
Source206:      %{maven_central_mirror}/org/apache/commons/commons-parent/74/commons-parent-74.pom
#!RemoteAsset:  sha256:348d4e7c131be6114c854a719ce7a44307a7c39bd366084977b24fd29ad0edb4
Source207:      %{maven_central_mirror}/org/apache/commons/commons-parent/81/commons-parent-81.pom
#!RemoteAsset:  sha256:d189ff2c0027e96bb65d31e6f227ed2af966169b36af1e973dd5ba08926dc7b5
Source208:      %{maven_central_mirror}/org/apache/commons/commons-parent/85/commons-parent-85.pom
#!RemoteAsset:  sha256:f2a6a4668dd833cfe559dd345929196e7b61ed13f6c03f8e087ffba3d85be807
Source209:      %{maven_central_mirror}/org/apache/maven/plugins/maven-compiler-plugin/3.16.0/maven-compiler-plugin-3.16.0.jar
#!RemoteAsset:  sha256:d0b2412f20f2eacfa514299e6a8e1410a8fca52e4171eb99779cca558be9343c
Source210:      %{maven_central_mirror}/org/apache/maven/plugins/maven-compiler-plugin/3.16.0/maven-compiler-plugin-3.16.0.pom
#!RemoteAsset:  sha256:d2f8b6fd4800b6aaf120f5a38226d5f9d5fc6db837af99e2f9b33067868b9872
Source211:      %{maven_central_mirror}/org/apache/commons/commons-parent/91/commons-parent-91.pom
#!RemoteAsset:  sha256:94f6c027b15f6402995dd1b2c7ea35bfe1ebc88b6832b3134368b41998721953
Source212:      %{maven_central_mirror}/org/apache/commons/commons-parent/92/commons-parent-92.pom
#!RemoteAsset:  sha256:e37a8fc9ff47435cc6bda257a4501cf79626c8115610ba33c77775ce23b4c3b7
Source213:      %{maven_central_mirror}/org/apache/maven/plugins/maven-dependency-plugin/3.11.0/maven-dependency-plugin-3.11.0.jar
#!RemoteAsset:  sha256:d40318527f56033e0ff0789971cc38c856aa99a685eea11270814e7f1eda9fba
Source214:      %{maven_central_mirror}/org/apache/commons/commons-parent/98/commons-parent-98.pom
#!RemoteAsset:  sha256:de023257ff166044a56bd1aa9124e843cd05dac5806cc705a9311f3556d5a15f
Source215:      %{maven_central_mirror}/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.jar
#!RemoteAsset:  sha256:b2d4341c921981cb35d5570f4fc9732a08a34b1528dee84c0507c7f2719a334f
Source216:      %{maven_central_mirror}/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.pom
#!RemoteAsset:  sha256:570b5e43230f7a13f9ec8ae0b0993208a5f4c763b6593a87af4123112ce47220
Source217:      %{maven_central_mirror}/org/apache/maven/plugins/maven-dependency-plugin/3.11.0/maven-dependency-plugin-3.11.0.pom
#!RemoteAsset:  sha256:32347686c513894a2fae96eeb11527883f47b8957850d793ea833646ad954dca
Source218:      %{maven_central_mirror}/org/apache/maven/plugins/maven-enforcer-plugin/3.6.3/maven-enforcer-plugin-3.6.3.jar
#!RemoteAsset:  sha256:9f32329a568596122363a78043d7ca2c485118cc3f86c6d5c92a2ecc94f645ad
Source219:      %{maven_central_mirror}/org/apache/maven/plugins/maven-enforcer-plugin/3.6.3/maven-enforcer-plugin-3.6.3.pom
#!RemoteAsset:  sha256:1631b4c05a2102d9ba774c8785f754d0ecf62632c32a6301b77791f9dfb148f7
Source220:      %{maven_central_mirror}/org/apache/maven/plugins/maven-failsafe-plugin/3.6.1/maven-failsafe-plugin-3.6.1.jar
#!RemoteAsset:  sha256:9f6c0b92bbde84fba8d09062401a31cdf281c622270deeb95e34f111f676deb8
Source221:      %{maven_central_mirror}/org/apache/maven/plugins/maven-failsafe-plugin/3.6.1/maven-failsafe-plugin-3.6.1.pom
#!RemoteAsset:  sha256:c83db6059be3fec9a4a68a0e226caefaa944663008617c697e087444415181d5
Source222:      %{maven_central_mirror}/org/apache/maven/plugins/maven-jar-plugin/3.5.1/maven-jar-plugin-3.5.1.jar
#!RemoteAsset:  sha256:32de38ee39a6985e777019a6364774c02781ee312f9f4e530bbdb45b875b1e38
Source223:      %{maven_central_mirror}/org/apache/maven/plugins/maven-jar-plugin/3.5.1/maven-jar-plugin-3.5.1.pom
#!RemoteAsset:  sha256:c8bc7e1c51a6d4ce72f40d2ebbabf1c4b68bfe76e732104b04381b493478e9d6
Source224:      %{maven_central_mirror}/org/apache/httpcomponents/httpclient/4.5.14/httpclient-4.5.14.jar
#!RemoteAsset:  sha256:f18355af4cf80a8a4ef04ebd742a47e90a7eaf080c725b2095dbc4fc5dbdefb7
Source225:      %{maven_central_mirror}/org/apache/httpcomponents/httpclient/4.5.14/httpclient-4.5.14.pom
#!RemoteAsset:  sha256:57014e98ba621d9d254cf79ad4dfcdcf690290fd97a935bab9ebe72bd5be40d3
Source226:      %{maven_central_mirror}/org/apache/maven/plugins/maven-plugins/48/maven-plugins-48.pom
#!RemoteAsset:  sha256:5bad1de4f101447659f89d089868ccbad64a68cc503d2d65410b51f6904aa061
Source227:      %{maven_central_mirror}/org/apache/httpcomponents/httpcomponents-client/4.5.14/httpcomponents-client-4.5.14.pom
#!RemoteAsset:  sha256:4225f860bccdcb48a315de478e70ab817b411077974de5c9d1b8e2761be5f515
Source228:      %{maven_central_mirror}/org/apache/maven/plugins/maven-plugins/49/maven-plugins-49.pom
#!RemoteAsset:  sha256:a67d0fee7dd2db3cf5678a6fa8bdcd8faa4c4454c2ce4a69c327e92b5a653015
Source229:      %{maven_central_mirror}/org/apache/maven/plugins/maven-surefire-plugin/3.6.1/maven-surefire-plugin-3.6.1.jar
#!RemoteAsset:  sha256:f2d75a2c2d423ad18539bf21656d56f88a4091944a662fcaf159d5ae283db7f7
Source230:      %{maven_central_mirror}/org/apache/httpcomponents/httpcomponents-core/4.4.16/httpcomponents-core-4.4.16.pom
#!RemoteAsset:  sha256:a901f87b115c55070c7ee43efff63e20e7b02d30af2443ae292bf1f4e532d3aa
Source231:      %{maven_central_mirror}/org/apache/httpcomponents/httpcomponents-parent/11/httpcomponents-parent-11.pom
#!RemoteAsset:  sha256:80da92a71046396952147a158bbf824beaed602363a53f63aac2f53a9148f562
Source232:      %{maven_central_mirror}/org/apache/maven/plugins/maven-surefire-plugin/3.6.1/maven-surefire-plugin-3.6.1.pom
#!RemoteAsset:  sha256:c0ce14849298720dcf3b09fe9e263b3c576d2d6cd43c61f8aa9d6117e04e5e47
Source233:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/1.9.24/maven-resolver-api-1.9.24.jar
#!RemoteAsset:  sha256:97c497208afe007e11696c9deaa2e3022eb7de5ba9f20167e459aeb77d62cce7
Source234:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/1.9.24/maven-resolver-api-1.9.24.pom
#!RemoteAsset:  sha256:6c9b3dd142a09dc468e23ad39aad6f75a0f2b85125104469f026e52a474e464f
Source235:      %{maven_central_mirror}/org/apache/httpcomponents/httpcore/4.4.16/httpcore-4.4.16.jar
#!RemoteAsset:  sha256:3cbad849b35dacfe6cec31adada2c623c026c3261141b0d26eec7e399c6cd7fa
Source236:      %{maven_central_mirror}/org/apache/httpcomponents/httpcore/4.4.16/httpcore-4.4.16.pom
#!RemoteAsset:  sha256:1ec0c3370158fd631dc3dcfc8b8f24041e6081f34f329dab1b8fe75c1007ca33
Source237:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/2.0.24/maven-resolver-api-2.0.24.jar
#!RemoteAsset:  sha256:bac2ec0e9dc83f177ec5c4e8d41780d2e1841601dca1fdd3e8164ce8fdcc3b53
Source238:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/2.0.24/maven-resolver-api-2.0.24.pom
#!RemoteAsset:  sha256:adc283fcdc44fbcf1cc7b2d5fca955cc580740ccebadb5d78513c4767d83f4ca
Source239:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/2.0.25/maven-resolver-api-2.0.25.jar
#!RemoteAsset:  sha256:59f40c92b9f525bb6ca6f8845ec63b13dab18c3c1da93d17620cb8d2ea4c61b8
Source240:      %{maven_central_mirror}/org/apache/maven/doxia/doxia/2.0.0/doxia-2.0.0.pom
#!RemoteAsset:  sha256:4a41f908fa8088d410b31655c6665dd1d4d6d93fd00eb52ed098c4477a345c8c
Source241:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/2.0.25/maven-resolver-api-2.0.25.pom
#!RemoteAsset:  sha256:a6628e870161519a61a77e1b6641b9f7c657ecb6f51746ae6206019afa4b5a21
Source242:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-connector-basic/2.0.25/maven-resolver-connector-basic-2.0.25.jar
#!RemoteAsset:  sha256:ed51ea4ecd54a8bfba62dd683c3d4e3756f0cc6971da68c11cb0bb7e95c7b2e8
Source243:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-connector-basic/2.0.25/maven-resolver-connector-basic-2.0.25.pom
#!RemoteAsset:  sha256:939183cf5ced6741745b2475a4adf78ca85885ee0dad6dae28dd3f25bd447ff3
Source244:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-core/2.0.0/doxia-core-2.0.0.jar
#!RemoteAsset:  sha256:f3e804d91571075e6367cff9020641d79d66bc46a6c13a62fcba1d369cd8936d
Source245:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-core/2.0.0/doxia-core-2.0.0.pom
#!RemoteAsset:  sha256:8bab5b0b9f3469f107c675aef6d28fc309262e8854781809787b22f4dd2d7c4e
Source246:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-impl/2.0.25/maven-resolver-impl-2.0.25.jar
#!RemoteAsset:  sha256:0c7822f6d8ceccc82e45e92f809e248b78dd4f0cdc3fb54f37ee127ee1a1eea9
Source247:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-impl/2.0.25/maven-resolver-impl-2.0.25.pom
#!RemoteAsset:  sha256:ac7cd5efe558ab7a7b1f2c98077b8e11aa46d2a975a452d81df9fd98d9ce7e33
Source248:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-named-locks/2.0.25/maven-resolver-named-locks-2.0.25.jar
#!RemoteAsset:  sha256:6f6d650f50155c0e7c52178edae418e1709b4840721034dd01745b9804645329
Source249:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-named-locks/2.0.25/maven-resolver-named-locks-2.0.25.pom
#!RemoteAsset:  sha256:4aee72f9b30b507964c2f52b63f70e7b41fb9d957359cb5dc13c428abb4b6189
Source250:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-integration-tools/2.0.0/doxia-integration-tools-2.0.0.jar
#!RemoteAsset:  sha256:b3707bdb06778745b0304985c340a9847eeda20f4ca7f2902faf6c266cc29653
Source251:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-integration-tools/2.0.0/doxia-integration-tools-2.0.0.pom
#!RemoteAsset:  sha256:909eb1df0a618f6c8f33e34aa5f2c35bba2fdb9b04e34b608f164c562c2273f3
Source252:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-spi/2.0.25/maven-resolver-spi-2.0.25.jar
#!RemoteAsset:  sha256:f8044908810ef6a449cbcb1b78e6f6355c7a205f3a5a2296ed6f16c37cd0112c
Source253:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-spi/2.0.25/maven-resolver-spi-2.0.25.pom
#!RemoteAsset:  sha256:6b5645495ecea92c3fd97591ba39b6f67edf7045537adb266f2210f9712f3f63
Source254:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-transport-apache/2.0.25/maven-resolver-transport-apache-2.0.25.jar
#!RemoteAsset:  sha256:f4a846c448ca85358279184a310f6ee3f46fa39688f74a72961c1bfe222f28a6
Source255:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-module-apt/2.0.0/doxia-module-apt-2.0.0.jar
#!RemoteAsset:  sha256:15d5d2bcd6fe003c4d181f1b9e88b3e09611e85385246105fc5977301f2c7e96
Source256:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-module-apt/2.0.0/doxia-module-apt-2.0.0.pom
#!RemoteAsset:  sha256:7956aca14f8adbc48bac86b218701dd44cc990063a69edbfca363b105994a474
Source257:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-module-xdoc/2.0.0/doxia-module-xdoc-2.0.0.jar
#!RemoteAsset:  sha256:c2e591fac5e62327c13a267c41ec21d1330e5fcbb943c56fbd6803132e7b1115
Source258:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-module-xdoc/2.0.0/doxia-module-xdoc-2.0.0.pom
#!RemoteAsset:  sha256:63147269598c5ae289a2ee241c271cf6052ce82acd442cd41d7de6dd89dcae5c
Source259:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-transport-apache/2.0.25/maven-resolver-transport-apache-2.0.25.pom
#!RemoteAsset:  sha256:510dde950dbf437f80fccc9c43899b6f0f107b9841e8f1d3b22fc2f59ce1663f
Source260:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-transport-file/2.0.25/maven-resolver-transport-file-2.0.25.jar
#!RemoteAsset:  sha256:f42ab4899f84b9fdc2bbc03d92ab6b97bda5890583f284536328436a89951ef7
Source261:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-transport-file/2.0.25/maven-resolver-transport-file-2.0.25.pom
#!RemoteAsset:  sha256:de6db5007410f6a735cda7fd651ee7d14f81bef2b8a71ccfb033abbb511ab62a
Source262:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-transport-wagon/2.0.25/maven-resolver-transport-wagon-2.0.25.jar
#!RemoteAsset:  sha256:2e2d88c313aac4aa64b9a1949081ee6a36678212da30cb54cc3aa656389afc35
Source263:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-transport-wagon/2.0.25/maven-resolver-transport-wagon-2.0.25.pom
#!RemoteAsset:  sha256:c91557679a0eb9fde3175055628ceb7b8fd5ab6d308340770d236fb06265dc26
Source264:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-module-xhtml5/2.0.0/doxia-module-xhtml5-2.0.0.jar
#!RemoteAsset:  sha256:3c6bff4151d35b94c3afb4a0c9377c262ced4eb2dd1009970396d4c79eb73e6e
Source265:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-module-xhtml5/2.0.0/doxia-module-xhtml5-2.0.0.pom
#!RemoteAsset:  sha256:aeb7e776a8c47b1c317a2581f299e2525b044cb8abde31164e970bbbefab12b1
Source266:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/1.9.24/maven-resolver-util-1.9.24.jar
#!RemoteAsset:  sha256:72fb9203656c9fcf187b59968f6c76a3532009fe8f240d4ad11764f4ba3e9df3
Source267:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/1.9.24/maven-resolver-util-1.9.24.pom
#!RemoteAsset:  sha256:9c56654ceff62d08b19b802d7d4d77dca54b17548b9802a0ba493f72f2adaf34
Source268:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-modules/2.0.0/doxia-modules-2.0.0.pom
#!RemoteAsset:  sha256:3fb490e1799f18aa22a05babdc57a74a3a1020c924890865a4cab7a7a34cd286
Source269:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/2.0.24/maven-resolver-util-2.0.24.jar
#!RemoteAsset:  sha256:e4c4f004f186d6d97a779bc4b6bde6914df9e2bd53d957d12cf782f09a2edcbc
Source270:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/2.0.24/maven-resolver-util-2.0.24.pom
#!RemoteAsset:  sha256:bed733864689ad4834aae2d4697698e596c5be90f6736299cfca79db421663fb
Source271:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/2.0.25/maven-resolver-util-2.0.25.jar
#!RemoteAsset:  sha256:7ad97a3aef3fd45b03abbc054adacf07e8966285098f3d60da215d892abff757
Source272:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/2.0.25/maven-resolver-util-2.0.25.pom
#!RemoteAsset:  sha256:fba33eaee3b01547bcd14b05ebc37f7dacef1819ad9ee7a5b27899afd3472cf4
Source273:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.jar
#!RemoteAsset:  sha256:4b05895d1cd65013d4b8e7eeb09cde6b567b4c31729fe5c77c0f0898b5e04b88
Source274:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.pom
#!RemoteAsset:  sha256:f6ec9ef75a41d1b826e5ecf02d92c5de90a6bc70ea93d5340988703223bf2205
Source275:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-site-model/2.0.0/doxia-site-model-2.0.0.jar
#!RemoteAsset:  sha256:25a17abcbd162cf65dfae5bd7400611d19e424d679e132e9a9228346c6d78d42
Source276:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-site-model/2.0.0/doxia-site-model-2.0.0.pom
#!RemoteAsset:  sha256:6ad2158ab7ea911d4e0b66ba3838f8e5b1d6b5ab31721770d914d0e8771d2917
Source277:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver/1.9.24/maven-resolver-1.9.24.pom
#!RemoteAsset:  sha256:84e91db544a36e0a9671626c4c89870f52ad54592e449def1b2b64c97696444b
Source278:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver/2.0.24/maven-resolver-2.0.24.pom
#!RemoteAsset:  sha256:6cdee370194f4b9f742d12ef46528042f480d9bdf3de832de2792e1ae9ffc68d
Source279:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-site-renderer/2.0.0/doxia-site-renderer-2.0.0.jar
#!RemoteAsset:  sha256:3add9e92edb232902aaf8f663b48d9f8dbec1792436f4f9c36f3665b86266d8d
Source280:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-site-renderer/2.0.0/doxia-site-renderer-2.0.0.pom
#!RemoteAsset:  sha256:e05dff52497275ed8c94a7f2f620ddb29d53b955f07c856bb95e0327f2176f96
Source281:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver/2.0.25/maven-resolver-2.0.25.pom
#!RemoteAsset:  sha256:ad3dcd30a40d45148350f066f2312ed9f946b7fd94f9c197ede0f3b9558b80a3
Source282:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-sitetools/2.0.0/doxia-sitetools-2.0.0.pom
#!RemoteAsset:  sha256:1c01883172b50855ceaa68f3688b21a4b8d8bc77435d162db08818680b7fed87
Source283:      %{maven_central_mirror}/org/apache/maven/shared/maven-dependency-analyzer/1.17.1/maven-dependency-analyzer-1.17.1.jar
#!RemoteAsset:  sha256:2c390dbed1b9d253084f47ce769040003bdc604f185e3162bc9c41208deb4b6a
Source284:      %{maven_central_mirror}/org/apache/maven/shared/maven-dependency-analyzer/1.17.1/maven-dependency-analyzer-1.17.1.pom
#!RemoteAsset:  sha256:3ced0d90353f49e8eb1458f54664b93ec117d79b9789a576da41e2f6f99723e0
Source285:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-skin-model/2.0.0/doxia-skin-model-2.0.0.jar
#!RemoteAsset:  sha256:10bbc5674fab0fa2bbcf8f7696796d3e1b92ab31525330921fbdb8da74fe1472
Source286:      %{maven_central_mirror}/org/apache/maven/doxia/doxia-skin-model/2.0.0/doxia-skin-model-2.0.0.pom
#!RemoteAsset:  sha256:4a8f3bc226f6f1b7f7362fa2a6e1da451561f86783ec512176e1c467a03708eb
Source287:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/48/maven-shared-components-48.pom
#!RemoteAsset:  sha256:40a6bdfd6e9243c77aaf4119c242b04c7dc72c4886272700a4bc9abcd38df9d9
Source288:      %{maven_central_mirror}/org/apache/maven/surefire/common-java5/3.6.1/common-java5-3.6.1.jar
#!RemoteAsset:  sha256:839fe5ebe08ccfd0c07af30a16ab1b30353551c6565be908920795ade7cf12a0
Source289:      %{maven_central_mirror}/org/apache/maven/surefire/common-java5/3.6.1/common-java5-3.6.1.pom
#!RemoteAsset:  sha256:c71d5496fa762827db549389422c26bb27d44bb9fef790a51935caaf50350552
Source290:      %{maven_central_mirror}/org/apache/maven/surefire/maven-surefire-common/3.6.1/maven-surefire-common-3.6.1.jar
#!RemoteAsset:  sha256:9d2c65943eead0e717c98479871fdbef6fda1587bd0f1129fba30b9c0cb03750
Source291:      %{maven_central_mirror}/org/apache/maven/surefire/maven-surefire-common/3.6.1/maven-surefire-common-3.6.1.pom
#!RemoteAsset:  sha256:de84c80cedda049456cea40dd8bdc2027be13b51187c64a5718c741e7e7fb78c
Source292:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-api/3.6.1/surefire-api-3.6.1.jar
#!RemoteAsset:  sha256:69860b1c11b272d7b9f925caa45e85b9e37207a2e7e98d0abab6225108929880
Source293:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-api/3.6.1/surefire-api-3.6.1.pom
#!RemoteAsset:  sha256:1f895a587df4844d9b7565e8e9a6352afe1d55532458a0dbeb746bc1d02e9216
Source294:      %{maven_central_mirror}/org/apache/maven/maven-archiver/3.6.2/maven-archiver-3.6.2.jar
#!RemoteAsset:  sha256:8b117b0dc205a71abda33463f8c7ff891513cfb92241d8a011f9e8ac5ea21e77
Source295:      %{maven_central_mirror}/org/apache/maven/maven-archiver/3.6.2/maven-archiver-3.6.2.pom
#!RemoteAsset:  sha256:83566129898c7a384bffaa118a76a40667d546948460b43eeb8563fa17635848
Source296:      %{maven_central_mirror}/org/apache/maven/maven-archiver/3.6.3/maven-archiver-3.6.3.jar
#!RemoteAsset:  sha256:bc130259c5e1087a270ea8cf3f8182fecc90bf93113a2074d640a1a67f102ec4
Source297:      %{maven_central_mirror}/org/apache/maven/maven-archiver/3.6.3/maven-archiver-3.6.3.pom
#!RemoteAsset:  sha256:cea5dd2b7c6be818fa8d6b73cff4edacaecefec5842d361a791b7f47974fe156
Source298:      %{maven_central_mirror}/org/apache/maven/maven-archiver/3.6.5/maven-archiver-3.6.5.jar
#!RemoteAsset:  sha256:87b2c403256b17c3903a3ba35320ac32a79b3838b62ab9eda010a0976ca49ba3
Source299:      %{maven_central_mirror}/org/apache/maven/maven-archiver/3.6.5/maven-archiver-3.6.5.pom
#!RemoteAsset:  sha256:7acdda087826580c5a5cb0fcbdbd3e6163298feb3235acc553119c0f11623b47
Source300:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-booter/3.6.1/surefire-booter-3.6.1.jar
#!RemoteAsset:  sha256:aedc7b7ceaf2e1ba4a77e6941b05b1956a4ec81ad55911983786330fce0ac662
Source301:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-booter/3.6.1/surefire-booter-3.6.1.pom
#!RemoteAsset:  sha256:619e0a465e7506c019c5d1627d4629b495c7a171004a778fd9baf3297e8df11e
Source302:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-extensions-api/3.6.1/surefire-extensions-api-3.6.1.jar
#!RemoteAsset:  sha256:da9bfd02374e041e06836dad5db475e9db486eedd84959dc126b2dcd23029ed2
Source303:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-extensions-api/3.6.1/surefire-extensions-api-3.6.1.pom
#!RemoteAsset:  sha256:99ec0c43fd9f644d618d34c44bb8ec98c43a035448a80d623c0205b89d593b3a
Source304:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-extensions-spi/3.6.1/surefire-extensions-spi-3.6.1.jar
#!RemoteAsset:  sha256:4969c424f2db4f53b68934980b21000a139fd70bdf1c8941bc22edb74eeb7b8a
Source305:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-extensions-spi/3.6.1/surefire-extensions-spi-3.6.1.pom
#!RemoteAsset:  sha256:0bcc42a6b4bf8615fcefacc99ceed15a2b46aeb43cb53e2a828465cd6ab33921
Source306:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-junit-platform/3.6.1/surefire-junit-platform-3.6.1.jar
#!RemoteAsset:  sha256:981d9587b308bbd02d183e82a8a3cfd5f4c17bc55fc5eeb37b347d69bf4d9793
Source307:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-junit-platform/3.6.1/surefire-junit-platform-3.6.1.pom
#!RemoteAsset:  sha256:8b785827526c78367dc3554b86f7520b1a432808f70eb3d84b1a5fc13a8449fa
Source308:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-logger-api/3.6.1/surefire-logger-api-3.6.1.jar
#!RemoteAsset:  sha256:f323e39c6e37a14ae8dee7277c8b2cc237828e3f80f1c1b521892b853e0637d9
Source309:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-logger-api/3.6.1/surefire-logger-api-3.6.1.pom
#!RemoteAsset:  sha256:5425501edd9e0bd7b01eca53cc92e06836d24851151304f9c6759e1713541685
Source310:      %{maven_central_mirror}/org/apache/maven/maven-parent/23/maven-parent-23.pom
#!RemoteAsset:  sha256:d4e9f7f782c0eda433885bac4e5767a77d579ddda59d5b4e9dbab5915bddd3c0
Source311:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-providers/3.6.1/surefire-providers-3.6.1.pom
#!RemoteAsset:  sha256:3856e3fcd169502d5f12fe2452604ebf6c7c025f15656bfa558ea99ed29d73ea
Source312:      %{maven_central_mirror}/org/apache/maven/maven-parent/33/maven-parent-33.pom
#!RemoteAsset:  sha256:1a8faf7a6a2b848acb26a959954ee115c0d79dbe75a6206fb3b8c7c2f45a237f
Source313:      %{maven_central_mirror}/org/apache/maven/maven-parent/34/maven-parent-34.pom
#!RemoteAsset:  sha256:cfe4820aa1d96ae51d1dc5b0e2a9dc582c42478c24c95ca8238f547e60bef721
Source314:      %{maven_central_mirror}/org/apache/maven/maven-parent/39/maven-parent-39.pom
#!RemoteAsset:  sha256:762fcdd4ce8621c5fa0a2cf6495ad26972a8093eb432aa3e402bc2d4e2500c53
Source315:      %{maven_central_mirror}/org/apache/maven/maven-parent/41/maven-parent-41.pom
#!RemoteAsset:  sha256:04534dea350a2187970a5b74444338bcf78ba8e537d44f262acfba16ebb33056
Source316:      %{maven_central_mirror}/org/apache/maven/maven-parent/42/maven-parent-42.pom
#!RemoteAsset:  sha256:468a1262e9aaa5febf9d604e2836267f815351f2b4520f28fb17f53c71e33554
Source317:      %{maven_central_mirror}/org/apache/maven/maven-parent/43/maven-parent-43.pom
#!RemoteAsset:  sha256:1c0a088d7352d52ea8f3581d05778c0c4a679613fff2c58737fba55f1007fe24
Source318:      %{maven_central_mirror}/org/apache/maven/maven-parent/44/maven-parent-44.pom
#!RemoteAsset:  sha256:94fe869eb9b4ce9fce3995d05ea86b168c85d927f9d17beb814a1960c76d7e6f
Source319:      %{maven_central_mirror}/org/apache/maven/maven-parent/45/maven-parent-45.pom
#!RemoteAsset:  sha256:82d0112ba1907ff5fd13a2485829c97df66c6a81e075359a561a422f7d1582d3
Source320:      %{maven_central_mirror}/org/apache/maven/maven-parent/47/maven-parent-47.pom
#!RemoteAsset:  sha256:cc9eed84b90a96cbc33aefecc93facb9a49f960ad678909162c579356cfe12c9
Source321:      %{maven_central_mirror}/org/apache/maven/maven-parent/48/maven-parent-48.pom
#!RemoteAsset:  sha256:a6c12347651a68928a9153cd328410c0efbd4b76ea6b1963cf8004716ee3fecc
Source322:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-shared-utils/3.6.1/surefire-shared-utils-3.6.1.jar
#!RemoteAsset:  sha256:fce8fbcf008d491b94fb08220225a28d3f890976e4d59be300be4e12e538f646
Source323:      %{maven_central_mirror}/org/apache/maven/surefire/surefire-shared-utils/3.6.1/surefire-shared-utils-3.6.1.pom
#!RemoteAsset:  sha256:83caadbb007daee4653825100ab85a7a3deb5f32aae61cdd3507bddf968a062e
Source324:      %{maven_central_mirror}/org/apache/maven/surefire/surefire/3.6.1/surefire-3.6.1.pom
#!RemoteAsset:  sha256:b7c76ae8bd983b8be40cc7912538c1ac8af075d47c6bfb6d18dc513bdd37359a
Source325:      %{maven_central_mirror}/org/apache/maven/plugins/maven-assembly-plugin/3.8.0/maven-assembly-plugin-3.8.0.jar
#!RemoteAsset:  sha256:02b4ab89683aa46a7df3df762eeb47fc5dfe8c5e163fade3033e20add9343bfb
Source326:      %{maven_central_mirror}/org/apache/maven/plugins/maven-assembly-plugin/3.8.0/maven-assembly-plugin-3.8.0.pom
#!RemoteAsset:  sha256:6b6eb1840c93231b799cb36505cd78a778b9fcec232a7838f9ffa49276a66e48
Source327:      %{maven_central_mirror}/org/apache/rat/apache-rat-core/0.18/apache-rat-core-0.18.jar
#!RemoteAsset:  sha256:88c761a2d95d61e3f99ec6cf3306e6ee39e42dc3e131ae0a2471d12824e7b226
Source328:      %{maven_central_mirror}/org/apache/rat/apache-rat-core/0.18/apache-rat-core-0.18.pom
#!RemoteAsset:  sha256:c7a3b723bda47c9e448745fc2ab33275bdcc02e1afd7e35418d40243011d60b5
Source329:      %{maven_central_mirror}/org/apache/rat/apache-rat-plugin/0.18/apache-rat-plugin-0.18.jar
#!RemoteAsset:  sha256:76898f9ee346ba9cbfc0706e20a798ae23ae896fdde0caedbe74c109954892b1
Source330:      %{maven_central_mirror}/org/apache/rat/apache-rat-plugin/0.18/apache-rat-plugin-0.18.pom
#!RemoteAsset:  sha256:65c5fe880641dd568ef84c7b975d7639e03a313226f6a5490ff6400ac3de722d
Source331:      %{maven_central_mirror}/org/apache/rat/apache-rat-project/0.18/apache-rat-project-0.18.pom
#!RemoteAsset:  sha256:4b697ae09a76b50102750816e9bd3ad26d89161ba65ddabdeee7ef3830428fd1
Source332:      %{maven_central_mirror}/org/apache/tika/tika-core/3.2.3/tika-core-3.2.3.jar
#!RemoteAsset:  sha256:47db53bc23a69e34cac45235fc924842cddfee0542ca9a42cbdc10bb4af0b113
Source333:      %{maven_central_mirror}/org/apache/tika/tika-core/3.2.3/tika-core-3.2.3.pom
#!RemoteAsset:  sha256:9ed87cfef1d462bcc6ecc69dd74b5d0793107f99c74f9d601b51c01f9302a2fd
Source334:      %{maven_central_mirror}/org/apache/tika/tika-parent/3.2.3/tika-parent-3.2.3.pom
#!RemoteAsset:  sha256:aad6c0c828d370e706670fdac07bc77b9840ccb35c00aa0214170d2301184d6e
Source335:      %{maven_central_mirror}/org/apache/tika/tika-parser-text-module/3.2.3/tika-parser-text-module-3.2.3.jar
#!RemoteAsset:  sha256:29d42ada339c1d204673be714959953997ddae6bf4530a81293b64976a61d11f
Source336:      %{maven_central_mirror}/org/apache/tika/tika-parser-text-module/3.2.3/tika-parser-text-module-3.2.3.pom
#!RemoteAsset:  sha256:a177f84e01c3829a357b8f135686ae7dd8c35d1c2089a390ef089340aa47cd21
Source337:      %{maven_central_mirror}/org/apache/maven/plugins/maven-plugins/43/maven-plugins-43.pom
#!RemoteAsset:  sha256:c0f58b12039f152641e3e53a07acc12887012ef149fac83065a9785aac51de0e
Source338:      %{maven_central_mirror}/org/apache/maven/plugins/maven-plugins/45/maven-plugins-45.pom
#!RemoteAsset:  sha256:58ddbb8e429cb5e9054c2f5f7b7cdfeb7adbcdfda21d92b67f67fa2b94edf982
Source339:      %{maven_central_mirror}/org/apache/maven/plugins/maven-plugins/47/maven-plugins-47.pom
#!RemoteAsset:  sha256:16fd64538837bbe6c6823008fc6153cf16ba833afb1e90a95b7cf1992b434b34
Source340:      %{maven_central_mirror}/org/apache/maven/plugins/maven-remote-resources-plugin/3.3.0/maven-remote-resources-plugin-3.3.0.jar
#!RemoteAsset:  sha256:38f9c044c3eedcdeb173acb4a3f93c07237e682adb3084cd9c534e43e55b313a
Source341:      %{maven_central_mirror}/org/apache/maven/plugins/maven-remote-resources-plugin/3.3.0/maven-remote-resources-plugin-3.3.0.pom
#!RemoteAsset:  sha256:2c923c63a197565a3e78f2b16d762d0f49bb83250dd2b1e6286704ea0f447060
Source342:      %{maven_central_mirror}/org/apache/maven/plugins/maven-resources-plugin/3.5.0/maven-resources-plugin-3.5.0.jar
#!RemoteAsset:  sha256:9f2275ca2ba3a3ab38caf6c2bc21be787c7305ea5333d1c33f52a530afc0bc7f
Source343:      %{maven_central_mirror}/org/apache/maven/plugins/maven-resources-plugin/3.5.0/maven-resources-plugin-3.5.0.pom
#!RemoteAsset:  sha256:3f85b6519c290d5ea451d5fa48168228229d30cc49c92a90b8695535640c6737
Source344:      %{maven_central_mirror}/org/apache/tika/tika-parsers-standard-modules/3.2.3/tika-parsers-standard-modules-3.2.3.pom
#!RemoteAsset:  sha256:c09f7c8cbe8151014fd2d28dc0eca109918c5d7b81be88367905edb1eff7ba24
Source345:      %{maven_central_mirror}/org/apache/tika/tika-parsers-standard/3.2.3/tika-parsers-standard-3.2.3.pom
#!RemoteAsset:  sha256:6e268b03dc7780de64f0ccef42fc77c3cf75a2331bb315e5e099b6a03fa185b7
Source346:      %{maven_central_mirror}/org/apache/tika/tika-parsers/3.2.3/tika-parsers-3.2.3.pom
#!RemoteAsset:  sha256:aa52de46b93a799e1d3f4f93fcea2246ea12c26264376932b200cbead4c7e34b
Source347:      %{maven_central_mirror}/org/assertj/assertj-bom/4.0.0-M1/assertj-bom-4.0.0-M1.pom
#!RemoteAsset:  sha256:6a1e8c6a6698b51cab2064822ff067ae0f0c7d659cdda92ba0ebd765fbc5a3d4
Source348:      %{maven_central_mirror}/org/codehaus/modello/modello-core/2.8.1/modello-core-2.8.1.jar
#!RemoteAsset:  sha256:cb2cbde3c9c7288f7398a250dcf3c90cf92714cff301f22b298e1091b5def33c
Source349:      %{maven_central_mirror}/org/apache/maven/reporting/maven-reporting-api/4.0.0/maven-reporting-api-4.0.0.jar
#!RemoteAsset:  sha256:2032531f05994121c2fdb5df7235ed548f53d294d0b7ac45e797148d85a30ee2
Source350:      %{maven_central_mirror}/org/apache/maven/reporting/maven-reporting-api/4.0.0/maven-reporting-api-4.0.0.pom
#!RemoteAsset:  sha256:e9e70fdb26ff8b1f15435e3a68866a25c85b1694007e0fbdfe84e48e946fe463
Source351:      %{maven_central_mirror}/org/apache/maven/reporting/maven-reporting-impl/4.0.0/maven-reporting-impl-4.0.0.jar
#!RemoteAsset:  sha256:e049cf5b77d09c24e83db9fd8f5019bdf86dc37a3357f5634c56fb157ecda248
Source352:      %{maven_central_mirror}/org/apache/maven/reporting/maven-reporting-impl/4.0.0/maven-reporting-impl-4.0.0.pom
#!RemoteAsset:  sha256:831c3849751101226495acfe9119582feb734a4539b070e0fbd9e85b03b501ce
Source353:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver/1.4.1/maven-resolver-1.4.1.pom
#!RemoteAsset:  sha256:5b1da5c436ba542b4b651da04f9174341d8b56f57dcd8df0fe823554b5a22ded
Source354:      %{maven_central_mirror}/org/codehaus/modello/modello-core/2.8.1/modello-core-2.8.1.pom
#!RemoteAsset:  sha256:c0870a6e68e160851cc7c1108ffc77198edf90715520d1a87c50484e7281c06e
Source355:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver/1.9.25/maven-resolver-1.9.25.pom
#!RemoteAsset:  sha256:8924b41711cce058f83c46d79ad83d6e04edcf13ed5631ec11135656e0b87f56
Source356:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver/1.9.27/maven-resolver-1.9.27.pom
#!RemoteAsset:  sha256:33dc67306cc95da14e5444e8b494d967924abf1d01bae1894676164cbd3f6112
Source357:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/1.4.1/maven-resolver-api-1.4.1.jar
#!RemoteAsset:  sha256:335513ce1dd2cf4c7d1dbfa1b8aa14656d9be5f9f3f0d0875ac528893c9f0f06
Source358:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/1.4.1/maven-resolver-api-1.4.1.pom
#!RemoteAsset:  sha256:1ef85a9bf057b048d3418e24617650e779cc9860787bf97732fabf9178cf8cbd
Source359:      %{maven_central_mirror}/org/codehaus/modello/modello-maven-plugin/2.8.1/modello-maven-plugin-2.8.1.jar
#!RemoteAsset:  sha256:d2a68bc43e04adaf767970122de0c44430458fee25dd967d0039401dc260171a
Source360:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/1.9.25/maven-resolver-api-1.9.25.pom
#!RemoteAsset:  sha256:76e21ab7015574989ab66acc764afd3682b4b2c582e438ff07dc5897d475f73c
Source361:      %{maven_central_mirror}/org/codehaus/modello/modello-maven-plugin/2.8.1/modello-maven-plugin-2.8.1.pom
#!RemoteAsset:  sha256:98dc031f75f2c9b7efeef344e1c74bb3d009c584e36e82a0ec3d263d2bfef373
Source362:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-api/1.9.27/maven-resolver-api-1.9.27.pom
#!RemoteAsset:  sha256:7f3f97fd3aefe87d04892ad4f2343f8e130a0e1de09dcb5e35c2bc7f29f67605
Source363:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-converters/2.8.1/modello-plugin-converters-2.8.1.jar
#!RemoteAsset:  sha256:625e3af908de041c4dd8aae31596e189f7299229aa82c86d91a0001cb0afd87e
Source364:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-converters/2.8.1/modello-plugin-converters-2.8.1.pom
#!RemoteAsset:  sha256:635503247564223f03b706364b41b951049350d6abd8254b43c34fcc4e8fed26
Source365:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-dom4j/2.8.1/modello-plugin-dom4j-2.8.1.jar
#!RemoteAsset:  sha256:7ef5452e6352ada63115b4a4ebe91df581d0976fe602fcc134ecea143fe0349d
Source366:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-dom4j/2.8.1/modello-plugin-dom4j-2.8.1.pom
#!RemoteAsset:  sha256:9c2787ee2aac2d610048858d1e7967b9daa7a78cfbc33c3524969ea056fdb72b
Source367:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-jackson/2.8.1/modello-plugin-jackson-2.8.1.jar
#!RemoteAsset:  sha256:cfc4324501b3f0e62c48368bd976674050ddac3e6e80e46c7e09d91ae1ae3e9c
Source368:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-jackson/2.8.1/modello-plugin-jackson-2.8.1.pom
#!RemoteAsset:  sha256:ec34985a0f813331542746ad0576c84e3e01f92d7b3177ccded9f744baeaec38
Source369:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-java/2.8.1/modello-plugin-java-2.8.1.jar
#!RemoteAsset:  sha256:9c086f9653313c8909ac44ef4e8f7ac0b9e87e626ee0d8cf20264a6ed3bb245c
Source370:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-java/2.8.1/modello-plugin-java-2.8.1.pom
#!RemoteAsset:  sha256:47c467b8b3dc1a6b3a5f4df8a642376917d8cd88813d4591afae513e62997ad3
Source371:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-jdom/2.8.1/modello-plugin-jdom-2.8.1.jar
#!RemoteAsset:  sha256:986f86a57cd9068e714f762bd423723f662424cd050168da2c263f29b6046ce0
Source372:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-jdom/2.8.1/modello-plugin-jdom-2.8.1.pom
#!RemoteAsset:  sha256:a423a3c4de206bfd7973ac3d77a062f582647bd91fe3b56b16d252f4b5b5e16b
Source373:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-jsonschema/2.8.1/modello-plugin-jsonschema-2.8.1.jar
#!RemoteAsset:  sha256:d0ac72f15d2849ed5eea5e99a8f5c0b52d174a5d2ee7bfb557c01b210db35b12
Source374:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-jsonschema/2.8.1/modello-plugin-jsonschema-2.8.1.pom
#!RemoteAsset:  sha256:8af9b9ae843b3c15849adb3fc59f978f61a3c2e2fb86fbea40392cf64312c464
Source375:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-sax/2.8.1/modello-plugin-sax-2.8.1.jar
#!RemoteAsset:  sha256:7bafac8697fea4e162d16665930ab6252e01adcf8ca0e84ff38c69ec2f74462e
Source376:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-sax/2.8.1/modello-plugin-sax-2.8.1.pom
#!RemoteAsset:  sha256:6b2184872fa7cc2ef5a90481b56af9711c15b371e69ab52f0f31bf24e910dd82
Source377:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/1.4.1/maven-resolver-util-1.4.1.jar
#!RemoteAsset:  sha256:a58c932e967e85e7bcb8d4adaedd14a5221a1750a1d089c5086c4d73df505155
Source378:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/1.4.1/maven-resolver-util-1.4.1.pom
#!RemoteAsset:  sha256:45e53a9e194e9562c225da1f2bf15ac7e23c18f2bf7427208455e53c5c38eb3f
Source379:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-snakeyaml/2.8.1/modello-plugin-snakeyaml-2.8.1.jar
#!RemoteAsset:  sha256:96c49e3f1d14fed8116b770c73ece540f25f2d925a4d1f5108e1774cd01e9b41
Source380:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-snakeyaml/2.8.1/modello-plugin-snakeyaml-2.8.1.pom
#!RemoteAsset:  sha256:e31330fdb29045f3087b4985cb488a5b5ebbcbd7d879fda14e6ed4dd61b1fdf7
Source381:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/1.9.25/maven-resolver-util-1.9.25.jar
#!RemoteAsset:  sha256:2283fb0bb5cec9f7524cba93498c6e89739aac5edd25d3a418f0fc4f6ce30007
Source382:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/1.9.25/maven-resolver-util-1.9.25.pom
#!RemoteAsset:  sha256:74a12548f0d6aad13c728666288c1e81201c24bd05bb4e4ec8c1558517b379a7
Source383:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/1.9.27/maven-resolver-util-1.9.27.jar
#!RemoteAsset:  sha256:b2b3c7774cdc61887da814b42338c9421babbab9b1e87c3e6493885ffda53231
Source384:      %{maven_central_mirror}/org/apache/maven/resolver/maven-resolver-util/1.9.27/maven-resolver-util-1.9.27.pom
#!RemoteAsset:  sha256:32ac469785dd1547ac71437e4c3916c4a56a3d69303cb08d789ecdd0bfd1d6de
Source385:      %{maven_central_mirror}/org/apache/maven/shared/file-management/3.2.0/file-management-3.2.0.jar
#!RemoteAsset:  sha256:04e3bdd6d1920d1cdba206bc35dd3c6e0646c5730969f8b5d5397e5f1c7b5edd
Source386:      %{maven_central_mirror}/org/apache/maven/shared/file-management/3.2.0/file-management-3.2.0.pom
#!RemoteAsset:  sha256:1ac88accde99ed71e65253bd130868c0e654f940f01ade073b895eb2f817cf06
Source387:      %{maven_central_mirror}/org/apache/maven/shared/maven-artifact-transfer/0.13.1/maven-artifact-transfer-0.13.1.jar
#!RemoteAsset:  sha256:e4b15a1e7cfbfe480408cfbaa148d66ea3324bf19e9ac6d6c17053bdb18ac4cd
Source388:      %{maven_central_mirror}/org/apache/maven/shared/maven-artifact-transfer/0.13.1/maven-artifact-transfer-0.13.1.pom
#!RemoteAsset:  sha256:034e12a9d1d5f5618a9e0dda23aadda4ed659ec55240876b6e954cc2172be456
Source389:      %{maven_central_mirror}/org/apache/maven/shared/maven-common-artifact-filters/3.1.0/maven-common-artifact-filters-3.1.0.pom
#!RemoteAsset:  sha256:931a77aa9dad6c91f10fcfafa70adc7608c004576b4924c74ecbffb27568a880
Source390:      %{maven_central_mirror}/org/apache/maven/shared/maven-common-artifact-filters/3.4.0/maven-common-artifact-filters-3.4.0.jar
#!RemoteAsset:  sha256:c93581d69b337c1fcc0957c727c430180b6387276ef1d3c2976c175e93765eb1
Source391:      %{maven_central_mirror}/org/apache/maven/shared/maven-common-artifact-filters/3.4.0/maven-common-artifact-filters-3.4.0.pom
#!RemoteAsset:  sha256:dd79c4852c3d49988a058897418a06a9167ab5b29acce61cdaf7eaf318349393
Source392:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-stax/2.8.1/modello-plugin-stax-2.8.1.jar
#!RemoteAsset:  sha256:dc681ea905943eb4308ed772c831d1e5c5c927335515055c9f990fb82d152eb2
Source393:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-stax/2.8.1/modello-plugin-stax-2.8.1.pom
#!RemoteAsset:  sha256:a3353f6a82feb950d5e7e64b0cd4ceadea7eb62112e447172e34974a510316f4
Source394:      %{maven_central_mirror}/org/apache/maven/shared/maven-dependency-tree/3.3.0/maven-dependency-tree-3.3.0.jar
#!RemoteAsset:  sha256:06d3cdd58a0bcec206558ade256147aade63a166b042ef53215df6c51206d920
Source395:      %{maven_central_mirror}/org/apache/maven/shared/maven-dependency-tree/3.3.0/maven-dependency-tree-3.3.0.pom
#!RemoteAsset:  sha256:ff04a5297c69d95f6face0af8934d6ee7bf1389dec50648bdd5e8569fb9d8e26
Source396:      %{maven_central_mirror}/org/apache/maven/shared/maven-filtering/3.4.0/maven-filtering-3.4.0.jar
#!RemoteAsset:  sha256:bb698e6a90534e82a8842a199b7dff470781a822d4e5868fb76ba953ed08ed6a
Source397:      %{maven_central_mirror}/org/apache/maven/shared/maven-filtering/3.4.0/maven-filtering-3.4.0.pom
#!RemoteAsset:  sha256:7adb0e46b5fff4fc03aab4baafbdee0b29e444cffe4478858c63082d497220bf
Source398:      %{maven_central_mirror}/org/apache/maven/shared/maven-filtering/3.5.0/maven-filtering-3.5.0.jar
#!RemoteAsset:  sha256:06b492b0244a82434470161f851b247271ec8fdaeea1c29de98abde066f80c64
Source399:      %{maven_central_mirror}/org/apache/maven/shared/maven-filtering/3.5.0/maven-filtering-3.5.0.pom
#!RemoteAsset:  sha256:d75aee86c26a701ecd73db3ab7c0ee887c0ea68b7ffc1d618976af86c0b9becd
Source400:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-velocity/2.8.1/modello-plugin-velocity-2.8.1.jar
#!RemoteAsset:  sha256:d82408269aada2eb1521ee8ff17f7c67333684f8ed2a09a9e35badd2e7575957
Source401:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom
#!RemoteAsset:  sha256:0a860a93aacc4000fbae518fd76c45d8ba9e69b1f03a4d6e89335860a202f559
Source402:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-velocity/2.8.1/modello-plugin-velocity-2.8.1.pom
#!RemoteAsset:  sha256:f43ff6fee0b32533765b3406648d6a5532f85d5e488079480788cb36e79d0980
Source403:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/33/maven-shared-components-33.pom
#!RemoteAsset:  sha256:64d0edb5f21cfff600b1c3ab7d45f9754cd18ba5fbf83b3d1bb7c4849437d8e3
Source404:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/34/maven-shared-components-34.pom
#!RemoteAsset:  sha256:17e81388d88ba61c4055450ec90a32ee30acd07f46dc6e31e096b8e53735f4b2
Source405:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/39/maven-shared-components-39.pom
#!RemoteAsset:  sha256:c6bd81e2588e0f0f87392d4db590e1d81c126a25ee9253252ef89c506cde1e34
Source406:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/41/maven-shared-components-41.pom
#!RemoteAsset:  sha256:aa66faa11c11b900d099bfef0ee9fe8485d7e7fc74e87193e1f74572ed9587c5
Source407:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/42/maven-shared-components-42.pom
#!RemoteAsset:  sha256:6072dd103bdba3199584c5b73ed45b00567cd3ea918e2160b10bc7437c9e8181
Source408:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/43/maven-shared-components-43.pom
#!RemoteAsset:  sha256:41fbab97912beb3a061b1e3845d2e06d2bb214cc71f92fa7f396480dc765a14e
Source409:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/44/maven-shared-components-44.pom
#!RemoteAsset:  sha256:5879e023d9bcafda006d28b42b2495c6f3db587d3e71eefa0a3cedeeea36d987
Source410:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/45/maven-shared-components-45.pom
#!RemoteAsset:  sha256:3bd3d07c910477091bb9602f931f696c4aa115c86a322bff6a604ec7543afc07
Source411:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-components/47/maven-shared-components-47.pom
#!RemoteAsset:  sha256:61988e54486a5dc38f06c70fdae5b108556c63bd433697b9f4305fcdb30fa40e
Source412:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar
#!RemoteAsset:  sha256:f21d19eb49b4a66cd85354a9ee7335439ea92a368173760a202766008cc19924
Source413:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom
#!RemoteAsset:  sha256:894b002ba0c564b755ac065bb1bcbc877eee6752f398a18b782dee9acda7ad19
Source414:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-xdoc/2.8.1/modello-plugin-xdoc-2.8.1.jar
#!RemoteAsset:  sha256:b613357e1bad4dfc1dead801691c9460f9585fe7c6b466bc25186212d7d18487
Source415:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-utils/3.4.2/maven-shared-utils-3.4.2.jar
#!RemoteAsset:  sha256:a941745d7faeb8dc9a75edc2c330c994b7440b9a44d21142716b6053967a41c1
Source416:      %{maven_central_mirror}/org/apache/maven/shared/maven-shared-utils/3.4.2/maven-shared-utils-3.4.2.pom
#!RemoteAsset:  sha256:d013bdbce2d39aa0e323ef8163e4cf90ede286b280669b7a48f12aa190953fab
Source417:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-xdoc/2.8.1/modello-plugin-xdoc-2.8.1.pom
#!RemoteAsset:  sha256:56c4273c2f4656fec8576a67417a802aa610f6a5f412afc9e1a862094a01e22c
Source418:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-xml/2.8.1/modello-plugin-xml-2.8.1.jar
#!RemoteAsset:  sha256:e4caae24de0a6dd3acf6b029d83d7aa7705d7262986a106db05b6c1c755413e8
Source419:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-xml/2.8.1/modello-plugin-xml-2.8.1.pom
#!RemoteAsset:  sha256:caa377edf95e75801e678ab76ab11ab5ed8c2e393f33db2f6532a45ba1062055
Source420:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-xpp3/2.8.1/modello-plugin-xpp3-2.8.1.jar
#!RemoteAsset:  sha256:2fb2ad3c665551f780c5ea10376fe8603d919ca78a4929de0911b5d46d5bcfbd
Source421:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-xpp3/2.8.1/modello-plugin-xpp3-2.8.1.pom
#!RemoteAsset:  sha256:d3dbd017694a91be271897693189b4af08ba472d708384851bee038f2fd0e480
Source422:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-xsd/2.8.1/modello-plugin-xsd-2.8.1.jar
#!RemoteAsset:  sha256:dc08c5796de427253e68af8aefc156d7069e41f26f3054ac6bd74c3b408b0507
Source423:      %{maven_central_mirror}/org/codehaus/modello/modello-plugin-xsd/2.8.1/modello-plugin-xsd-2.8.1.pom
#!RemoteAsset:  sha256:4881e5ca91e4e568891a76c945e9d9d0e49f6fc93fbb23de434a7b2e6ebd5461
Source424:      %{maven_central_mirror}/org/codehaus/modello/modello-plugins/2.8.1/modello-plugins-2.8.1.pom
#!RemoteAsset:  sha256:945a8f8dcfcd392e689970cc5c5ace32774047d0cda60d6b6cd5cc23c49a8fb3
Source425:      %{maven_central_mirror}/org/codehaus/modello/modello/2.8.1/modello-2.8.1.pom
#!RemoteAsset:  sha256:008f4b132ead4abc1b6124def2f42b3058410bd06fb43546273ea5e2aea504bd
Source426:      %{maven_central_mirror}/org/codehaus/mojo/animal-sniffer-annotations/1.29/animal-sniffer-annotations-1.29.jar
#!RemoteAsset:  sha256:36b775bbcbf50fdfb7b1af01f8d47f77333383a306a5cc685097d890cf494427
Source427:      %{maven_central_mirror}/org/codehaus/mojo/animal-sniffer-annotations/1.29/animal-sniffer-annotations-1.29.pom
#!RemoteAsset:  sha256:da841b1c473e2c43f647cacfec28861315b8a8bcee1bf9d347e4a6715fbff86d
Source428:      %{maven_central_mirror}/org/codehaus/mojo/animal-sniffer-maven-plugin/1.29/animal-sniffer-maven-plugin-1.29.jar
#!RemoteAsset:  sha256:4a09fc8ffc0cf49ec673b02b791cc3882831f124d4469df02c73fff33c0c73e7
Source429:      %{maven_central_mirror}/org/codehaus/mojo/animal-sniffer-maven-plugin/1.29/animal-sniffer-maven-plugin-1.29.pom
#!RemoteAsset:  sha256:0dc57c1b944b201b6ab5cb9f8f6521c39be1bfcaf2213baca4a90d55375c6d88
Source430:      %{maven_central_mirror}/org/codehaus/mojo/animal-sniffer-parent/1.29/animal-sniffer-parent-1.29.pom
#!RemoteAsset:  sha256:d478fcad570d867e58fdadd9bfdb599c3e703b3bb1cd3d07ecb5b15fdd2162a8
Source431:      %{maven_central_mirror}/org/codehaus/mojo/animal-sniffer/1.29/animal-sniffer-1.29.jar
#!RemoteAsset:  sha256:88509cce2160af6b2a20e68a83e47549473bf3c34aef3aeab28f50a827d2555b
Source432:      %{maven_central_mirror}/org/codehaus/mojo/animal-sniffer/1.29/animal-sniffer-1.29.pom
#!RemoteAsset:  sha256:f366631cd160ffc5936efb9f86ceca5e1ed568552f7492842a459747e73d197e
Source433:      %{maven_central_mirror}/org/codehaus/mojo/build-helper-maven-plugin/3.7.0/build-helper-maven-plugin-3.7.0.jar
#!RemoteAsset:  sha256:5d61de9577ce1095ab30c0f1f458f4667ea4b7cb8026b68da160273c462d1e07
Source434:      %{maven_central_mirror}/org/codehaus/mojo/build-helper-maven-plugin/3.7.0/build-helper-maven-plugin-3.7.0.pom
#!RemoteAsset:  sha256:0236de326aad257cbbccdf7e4155cde95c5326b49dbd72fe9fbad5268e74ecca
Source435:      %{maven_central_mirror}/org/codehaus/mojo/exec-maven-plugin/3.6.4/exec-maven-plugin-3.6.4.jar
#!RemoteAsset:  sha256:f2c9c23a2634a9965d5b00dab4f7ca3037223c056d8b07af29cea90892783786
Source436:      %{maven_central_mirror}/org/codehaus/mojo/exec-maven-plugin/3.6.4/exec-maven-plugin-3.6.4.pom
#!RemoteAsset:  sha256:7c10b8bac59268fe7957f2ab2b50965d90069ebf850c756bb55ea807ce440f0b
Source437:      %{maven_central_mirror}/org/apache/maven/wagon/wagon/3.5.3/wagon-3.5.3.pom
#!RemoteAsset:  sha256:afc9216fa97b78dad227b4a8d4d67b9897bf113a57f80598d62993841113e103
Source438:      %{maven_central_mirror}/org/apache/maven/wagon/wagon-file/3.5.3/wagon-file-3.5.3.jar
#!RemoteAsset:  sha256:b89e540a7e432329bb5d93f2dfc578f898960afed66ae6a2dfeaa3d48d32c09c
Source439:      %{maven_central_mirror}/org/apache/maven/wagon/wagon-file/3.5.3/wagon-file-3.5.3.pom
#!RemoteAsset:  sha256:d2b6e48c9fcbe579e1858c622d14464011ff265fa6e28e794004a6882154a509
Source440:      %{maven_central_mirror}/org/apache/maven/wagon/wagon-http/3.5.3/wagon-http-3.5.3.jar
#!RemoteAsset:  sha256:934f2f9c87e497c4f795be4bb05b360b8c231467d460103c19012b79b8c03c6b
Source441:      %{maven_central_mirror}/org/apache/maven/wagon/wagon-http/3.5.3/wagon-http-3.5.3.pom
#!RemoteAsset:  sha256:8e7da766f55164fde8779aaaa125832506c2848cab4876b5305138873e28037f
Source442:      %{maven_central_mirror}/org/apache/maven/wagon/wagon-http-shared/3.5.3/wagon-http-shared-3.5.3.jar
#!RemoteAsset:  sha256:6014b1e64abf455c6834a0918248e15638050f835da12051d33cda7e946d88f8
Source443:      %{maven_central_mirror}/org/apache/maven/wagon/wagon-http-shared/3.5.3/wagon-http-shared-3.5.3.pom
#!RemoteAsset:  sha256:5e72000338945ed3e96f8e4f578d1d0672e1af7e19c0e9014197ae5b31af3ef4
Source444:      %{maven_central_mirror}/org/apache/maven/wagon/wagon-provider-api/3.5.3/wagon-provider-api-3.5.3.jar
#!RemoteAsset:  sha256:64d6a085e8a6bede9607cbd029ea58cd1c87304410862492174a6d59b9d17142
Source445:      %{maven_central_mirror}/org/apache/maven/wagon/wagon-provider-api/3.5.3/wagon-provider-api-3.5.3.pom
#!RemoteAsset:  sha256:807c51ffccdef6c01130b74aeed27815ec162bc2686c01e9d29f16efc526a44a
Source446:      %{maven_central_mirror}/org/apache/maven/wagon/wagon-providers/3.5.3/wagon-providers-3.5.3.pom
#!RemoteAsset:  sha256:c826b1a9a00916fe239de1e35e8e3518dded763de25ba8ee036d6372f95723e2
Source447:      %{maven_central_mirror}/org/codehaus/mojo/extra-enforcer-rules/1.12.1/extra-enforcer-rules-1.12.1.jar
#!RemoteAsset:  sha256:3fc5f6f9c35ab1663308a71384da13d1e55de5e62297a9b5372cbdeebbee1487
Source448:      %{maven_central_mirror}/org/codehaus/mojo/extra-enforcer-rules/1.12.1/extra-enforcer-rules-1.12.1.pom
#!RemoteAsset:  sha256:d9285271c3890576d6dc0bd455a8aa31ad7ab02bbec09ca8a58e8f75b903c4e0
Source449:      %{maven_central_mirror}/org/codehaus/mojo/java-boot-classpath-detector/1.29/java-boot-classpath-detector-1.29.jar
#!RemoteAsset:  sha256:9f1f53f6da1239efb086cf69b022f4e6d22847f8416dc8e467ee99652b259c86
Source450:      %{maven_central_mirror}/org/codehaus/mojo/java-boot-classpath-detector/1.29/java-boot-classpath-detector-1.29.pom
#!RemoteAsset:  sha256:888b0162ad7fabdeb6ee34ff6123025bffe34e064761da962e87de5c8cce5d39
Source451:      %{maven_central_mirror}/org/codehaus/mojo/mojo-parent/97/mojo-parent-97.pom
#!RemoteAsset:  sha256:8258cfdcaa16127f35ffe610a3fa4f76b7ebe51b88922c73c4ee39ce8f378ce5
Source452:      %{maven_central_mirror}/org/apache/velocity/tools/velocity-tools-generic/3.1/velocity-tools-generic-3.1.jar
#!RemoteAsset:  sha256:a6f50cb3f413875c039652269d2a89f8878d0d9fc8cc662fc13591ca20d84758
Source453:      %{maven_central_mirror}/org/apache/velocity/tools/velocity-tools-generic/3.1/velocity-tools-generic-3.1.pom
#!RemoteAsset:  sha256:5a597b88dba795090e77015bcdf53461b41d45da2d7d1764e4ece8b30a226fcd
Source454:      %{maven_central_mirror}/org/apache/velocity/tools/velocity-tools-parent/3.1/velocity-tools-parent-3.1.pom
#!RemoteAsset:  sha256:b1e9798a6d711d1e7760d50c78be8be746bb546b87df0a2d7ef67db5eda5431e
Source455:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.12.0/plexus-archiver-4.12.0.jar
#!RemoteAsset:  sha256:4b3b26c438d0b41d5a0613787115ea4013adeae1478314535976b2b3a65fc2f8
Source456:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.12.0/plexus-archiver-4.12.0.pom
#!RemoteAsset:  sha256:7f88ef8b83d6f2be46b12f17b982439a5ec83c566f5e2a04dad2d684e73cda94
Source457:      %{maven_central_mirror}/org/codehaus/plexus/plexus-classworlds/2.12.1/plexus-classworlds-2.12.1.jar
#!RemoteAsset:  sha256:d4242a6174243f1e680434571ba4e6a1dbae199c0bc350a987d5fb9c3ce1e0d3
Source458:      %{maven_central_mirror}/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.pom
#!RemoteAsset:  sha256:a9eee9d59ac787f9c379ec4f37af7e04f8d62161a1e602a4274014d0dc41b0cb
Source459:      %{maven_central_mirror}/org/apache/velocity/velocity-engine-core/2.4/velocity-engine-core-2.4.pom
#!RemoteAsset:  sha256:1c19157d1171d560088e485be97c93a7a2f7e9f56e517f0a30273c5c39df6231
Source460:      %{maven_central_mirror}/org/apache/velocity/velocity-engine-core/2.4.1/velocity-engine-core-2.4.1.jar
#!RemoteAsset:  sha256:ac7cd94f0d9fb39bcba3b28287c4c40005dc0f53a986fb587e4f67a4ccb3e5b6
Source461:      %{maven_central_mirror}/org/apache/velocity/velocity-engine-core/2.4.1/velocity-engine-core-2.4.1.pom
#!RemoteAsset:  sha256:4c0e4a92f6870f399b946d5bb789d177e4a47941147c3fddc2e6f063e9cb96db
Source462:      %{maven_central_mirror}/org/apache/velocity/velocity-engine-parent/2.3/velocity-engine-parent-2.3.pom
#!RemoteAsset:  sha256:d4b9e31a7e9ea490c562a2bdeced94eef3f08c8d0a5378add3d6bcf8828334bf
Source463:      %{maven_central_mirror}/org/apache/velocity/velocity-engine-parent/2.4/velocity-engine-parent-2.4.pom
#!RemoteAsset:  sha256:8efb661b7e1b44b7a056f23650ab2b43b8fcdb09bbe2ec3d3d02185d5658fd4a
Source464:      %{maven_central_mirror}/org/apache/velocity/velocity-engine-parent/2.4.1/velocity-engine-parent-2.4.1.pom
#!RemoteAsset:  sha256:7a2ac73c90dd104b5a07e6e2cd03e95ec28d29f3b8304f3dd7fffcecb049712e
Source465:      %{maven_central_mirror}/org/apache/velocity/velocity-master/4/velocity-master-4.pom
#!RemoteAsset:  sha256:943a046c1fe36b28b3cea11fb0d34e8b836b245433087f8fa916c0a752393181
Source466:      %{maven_central_mirror}/org/apache/velocity/velocity-master/7/velocity-master-7.pom
#!RemoteAsset:  sha256:c109639d1132ffb035468de43d134b91956148431905a29dc5ccaa6b91f3631d
Source467:      %{maven_central_mirror}/org/codehaus/plexus/plexus-classworlds/2.12.1/plexus-classworlds-2.12.1.pom
#!RemoteAsset:  sha256:1ad3292cd563381e3fd632f3fded1988f9e9b2be7a9f3db63ff4c4cedba13fa5
Source468:      %{maven_central_mirror}/org/codehaus/plexus/plexus-classworlds/2.9.0/plexus-classworlds-2.9.0.jar
#!RemoteAsset:  sha256:d9a3fe6374558b88948a96382b6b8a7ad75c23bed754994ea6f002586bb35f27
Source469:      %{maven_central_mirror}/org/codehaus/plexus/plexus-classworlds/2.9.0/plexus-classworlds-2.9.0.pom
#!RemoteAsset:  sha256:b748c05658b1fed1ceb73f527a05983593572e351d90b411f780ed1fa05b4afa
Source470:      %{maven_central_mirror}/org/codehaus/plexus/plexus-compiler-api/2.17.0/plexus-compiler-api-2.17.0.jar
#!RemoteAsset:  sha256:a17955976070c0573235ee662f2794a78082758b61accffce8d3f8aedcd91047
Source471:      %{maven_central_mirror}/org/apache-extras/beanshell/bsh/2.0b6/bsh-2.0b6.jar
#!RemoteAsset:  sha256:679be8f12aa2864f7c286f7f5bcbac8365851c01821de5b99a12d6f772f521e6
Source472:      %{maven_central_mirror}/org/apache-extras/beanshell/bsh/2.0b6/bsh-2.0b6.pom
#!RemoteAsset:  sha256:b509448ac506d607319f182537f0b35d71007582ec741832a1f111e5b5b70b38
Source473:      %{maven_central_mirror}/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.jar
#!RemoteAsset:  sha256:32355081d109095c3d5d374d5a43b4f4c1b75d549e983ef50723e2772e5302a0
Source474:      %{maven_central_mirror}/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.pom
#!RemoteAsset:  sha256:1c09f6c04c905e1e5cdb22d5dfa5f11a496e19e881de0850b523ed53a0519f5b
Source475:      %{maven_central_mirror}/org/assertj/assertj-bom/3.27.7/assertj-bom-3.27.7.pom
#!RemoteAsset:  sha256:ed9896ab386e164848a24801fb8bb44664fba0b1b0eaacd41ef09231422946cc
Source476:      %{maven_central_mirror}/org/codehaus/plexus/plexus-compiler-api/2.17.0/plexus-compiler-api-2.17.0.pom
#!RemoteAsset:  sha256:b183ab7658582be5b77105a96b69a57643fa0098d30217b9bb19967881f61de4
Source477:      %{maven_central_mirror}/org/codehaus/plexus/plexus-compiler-javac/2.17.0/plexus-compiler-javac-2.17.0.jar
#!RemoteAsset:  sha256:4408d69bebbf7f4d63bcd57f1276b96f14a2ab4d666004d5d7c4f977ad18c91c
Source478:      %{maven_central_mirror}/org/codehaus/plexus/plexus-compiler-javac/2.17.0/plexus-compiler-javac-2.17.0.pom
#!RemoteAsset:  sha256:0f18f85a552c6d3f702867938985d75ec32632209384fe8d76edf8014cedf2c2
Source479:      %{maven_central_mirror}/org/codehaus/plexus/plexus-compiler-manager/2.17.0/plexus-compiler-manager-2.17.0.jar
#!RemoteAsset:  sha256:00eaece2225d5ff2e0936a7041699aa818f668b878f93996065258fc0b8904c7
Source480:      %{maven_central_mirror}/org/codehaus/plexus/plexus-compiler-manager/2.17.0/plexus-compiler-manager-2.17.0.pom
#!RemoteAsset:  sha256:62eae3b1bb053060b4375c393664a9559afdfafd6de133924f81794aa20caf68
Source481:      %{maven_central_mirror}/org/codehaus/plexus/plexus-compiler/2.17.0/plexus-compiler-2.17.0.pom
#!RemoteAsset:  sha256:a7bd62ce59cd3822b8202228471eb363af269128af71db9c3b24ec56c2b1a850
Source482:      %{maven_central_mirror}/org/codehaus/plexus/plexus-compilers/2.17.0/plexus-compilers-2.17.0.pom
#!RemoteAsset:  sha256:457307267f6d2ea2582f5449df9350b86728f46c23ccd486341087ace473e9a1
Source483:      %{maven_central_mirror}/org/codehaus/plexus/plexus-interpolation/1.30.0/plexus-interpolation-1.30.0.jar
#!RemoteAsset:  sha256:c26e2570a02cd28fcf450aaa9b1a517add8362bb4c6c9936aa1e348ccfa0b35a
Source484:      %{maven_central_mirror}/org/codehaus/plexus/plexus-interpolation/1.30.0/plexus-interpolation-1.30.0.pom
#!RemoteAsset:  sha256:6baf4d39fe0797a5d623218215568252b2b94049c984d71e8b4da2925e024705
Source485:      %{maven_central_mirror}/org/codehaus/plexus/plexus-java/1.6.0/plexus-java-1.6.0.jar
#!RemoteAsset:  sha256:e758a3f1464627847d45e3b909fc6dd2f587c1471e0d0daa2975d6434458318d
Source486:      %{maven_central_mirror}/org/codehaus/plexus/plexus-java/1.6.0/plexus-java-1.6.0.pom
#!RemoteAsset:  sha256:57b98b5fd9c81bf78bd34cbe0faf11d9613b2f472ffad0194c0395677ccfcb0a
Source487:      %{maven_central_mirror}/org/codehaus/plexus/plexus-languages/1.6.0/plexus-languages-1.6.0.pom
#!RemoteAsset:  sha256:e5100d411cb5533ffb11e3b8be48c8344aa031d05cf77b46848654df3f2375e4
Source488:      %{maven_central_mirror}/org/codehaus/plexus/plexus-testing/2.2.0/plexus-testing-2.2.0.jar
#!RemoteAsset:  sha256:075b0fbdd1a450ac77622718addf8369023a60b1bfb3b2a47910155cb7868ccb
Source489:      %{maven_central_mirror}/org/codehaus/plexus/plexus-testing/2.2.0/plexus-testing-2.2.0.pom
#!RemoteAsset:  sha256:7c2cdf8b4a02a2ee3f0514b8d74ad5eb6e2365eeb073a5cabd6f2d61d8f871df
Source490:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/3.6.2/plexus-utils-3.6.2.jar
#!RemoteAsset:  sha256:5ee26b9f0529038802fc1c205a5ce55be5eff247af0a5e5b55cf831652c173ed
Source491:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/3.6.2/plexus-utils-3.6.2.pom
#!RemoteAsset:  sha256:421ff6ed146c53a9d4eaade8f629b52b12af7187101f1bd06c2c64e904019f3c
Source492:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/4.0.3/plexus-utils-4.0.3.jar
#!RemoteAsset:  sha256:35736658f3fe1efa395086c91df2592664fafa24c3f2608fdaba1136d17fd360
Source493:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/4.0.3/plexus-utils-4.0.3.pom
#!RemoteAsset:  sha256:6a2fe69e98301882bb2bb05afe36414eb82d6f7c63299cccdb2dc02b4358a968
Source494:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/4.1.0/plexus-utils-4.1.0.jar
#!RemoteAsset:  sha256:449f00ecf08a9e78ec67661ac3b155b6a4493c90aeb4dcb7e2869eef1f067127
Source495:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/4.1.0/plexus-utils-4.1.0.pom
#!RemoteAsset:  sha256:c07d67161cdf7f8fdce4cd921be5d3cccb9e2c259105ca1afeb772cbcb0cbec5
Source496:      %{maven_central_mirror}/org/codehaus/plexus/plexus-xml/3.0.0/plexus-xml-3.0.0.pom
#!RemoteAsset:  sha256:c2bf931dd1512d228dd4cdbe755100df0430c3284e712b4d1d38795dd27629bd
Source497:      %{maven_central_mirror}/org/codehaus/plexus/plexus-xml/3.1.0/plexus-xml-3.1.0.jar
#!RemoteAsset:  sha256:521d5d8f6e90fd09c8a6f419e458c3ec2ac419b7e0ad3f5f4f3f54c1effbe964
Source498:      %{maven_central_mirror}/org/codehaus/plexus/plexus-xml/3.1.0/plexus-xml-3.1.0.pom
#!RemoteAsset:  sha256:dbc7d80d79d3760fed777bea9e41b1c0a370442ea8ecf930d04a6a5620d36b6e
Source499:      %{maven_central_mirror}/org/codehaus/plexus/plexus/27/plexus-27.pom
#!RemoteAsset:  sha256:916b4794d8d8220a59a3fdf6a64dbe794aeb23395e888b81ae36a9b5a2c591a6
Source500:      %{maven_central_mirror}/org/eclipse/ee4j/project/1.0.5/project-1.0.5.pom
#!RemoteAsset:  sha256:232a9fd682e5c5bc82c1a463ef434c806240e62f5c1f9a167c0ad69d15d9fd64
Source501:      %{maven_central_mirror}/org/eclipse/jetty/jetty-bom/11.0.26/jetty-bom-11.0.26.pom
#!RemoteAsset:  sha256:7ace21d11ae572bf8053ba5b200c6b19d0db661db304cb006510f078e4102658
Source502:      %{maven_central_mirror}/org/eclipse/jetty/jetty-bom/12.1.13/jetty-bom-12.1.13.pom
#!RemoteAsset:  sha256:12b8d0878a7eafd9f1de7a50ed2e742881c320a90a970546e3e67b269dd03f4f
Source503:      %{maven_central_mirror}/org/eclipse/jetty/jetty-bom/12.1.14/jetty-bom-12.1.14.pom
#!RemoteAsset:  sha256:15335c4dcf082f599fb8eddcfb58d6a7e9a9c97de2883c257089a479b9b24522
Source504:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.inject/0.9.0.M3/org.eclipse.sisu.inject-0.9.0.M3.jar
#!RemoteAsset:  sha256:57ed17e057ba716cc1f1e5b2d4e014a68c3d50bd33498227a90f712519334dd4
Source505:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.inject/0.9.0.M3/org.eclipse.sisu.inject-0.9.0.M3.pom
#!RemoteAsset:  sha256:6e1b54f45c95627d02808979a3357f6d937088739668feea552c825c6cbbe07f
Source506:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.inject/1.1.2/org.eclipse.sisu.inject-1.1.2.jar
#!RemoteAsset:  sha256:df85d9b968800196ab6cc6d75df894cabf001cabd91287949ba373c77989abbc
Source507:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.inject/1.1.2/org.eclipse.sisu.inject-1.1.2.pom
#!RemoteAsset:  sha256:c99674d3773e26154885661711f0b6d63aa5008f5cc99227a236756d4ad9de5e
Source508:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M3/org.eclipse.sisu.plexus-0.9.0.M3.jar
#!RemoteAsset:  sha256:70596c950b0b5e99ef7942a5cfbd07dc3e76475b3332be3400a0741a7eb77458
Source509:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M3/org.eclipse.sisu.plexus-0.9.0.M3.pom
#!RemoteAsset:  sha256:7ebc52738567e0450b6857a404a147639533d35c38a5ba42e4c5ab2910c6df94
Source510:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/1.1.0/org.eclipse.sisu.plexus-1.1.0.jar
#!RemoteAsset:  sha256:aa1d7867a6612201a31e61bf96366739dc2408bf8a9e6f300530eb35960c2c2d
Source511:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/1.1.0/org.eclipse.sisu.plexus-1.1.0.pom
#!RemoteAsset:  sha256:fc3753740258c74ef9ee26bb8b0b23215da03dc6d32d0c5f1a2d1fd40017e117
Source512:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/1.1.2/org.eclipse.sisu.plexus-1.1.2.jar
#!RemoteAsset:  sha256:8ceb0bac4a1b621a28a43cbc197ddfa358f25527d62f6289e3d03cc8a6fc3aee
Source513:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/1.1.2/org.eclipse.sisu.plexus-1.1.2.pom
#!RemoteAsset:  sha256:2e436563d5caea351bce5f0863ebc6376405cb65a6f664b255faad9e72e3b854
Source514:      %{maven_central_mirror}/org/eclipse/sisu/sisu-inject/0.9.0.M3/sisu-inject-0.9.0.M3.pom
#!RemoteAsset:  sha256:137a304f2e7cddbd5c78726e2c4c37d2e2f8a6f633571ad7c0b39211eab6c3e5
Source515:      %{maven_central_mirror}/org/eclipse/sisu/sisu-inject/1.1.0/sisu-inject-1.1.0.pom
#!RemoteAsset:  sha256:965fd1ec52add0df52b135594eff6a078c41d27b503eaf37ff8464128f50181d
Source516:      %{maven_central_mirror}/org/eclipse/sisu/sisu-inject/1.1.2/sisu-inject-1.1.2.pom
#!RemoteAsset:  sha256:e4dde8e1dea28391e7b991a85d6fd2837143af9ca395f94a97f7bbe8a147124e
Source517:      %{maven_central_mirror}/org/eclipse/sisu/sisu-maven-plugin/1.1.2/sisu-maven-plugin-1.1.2.jar
#!RemoteAsset:  sha256:c06dcd8d3ad374b11315ad87a13644d6517f1a2bbc2046dc4b8788e232fa5e3e
Source518:      %{maven_central_mirror}/org/eclipse/sisu/sisu-maven-plugin/1.1.2/sisu-maven-plugin-1.1.2.pom
#!RemoteAsset:  sha256:8b15e2b28eeb1e0a88a9b7dab4dc0c23524491c56959785dea22f7846897b668
Source519:      %{maven_central_mirror}/org/jsoup/jsoup/1.23.1/jsoup-1.23.1.jar
#!RemoteAsset:  sha256:10faba526d66760cf3a57176636976cc78865935e94faddbf1637f3cce64c21b
Source520:      %{maven_central_mirror}/org/jsoup/jsoup/1.23.1/jsoup-1.23.1.pom
#!RemoteAsset:  sha256:070d75f261fe4c5b8202508366715f7f2d4660f88c8ef7e6d3575e48c9683b66
Source521:      %{maven_central_mirror}/org/jspecify/jspecify/1.0.1/jspecify-1.0.1.jar
#!RemoteAsset:  sha256:55b38bf1a7b1d8ea518cf2f4f3ae9aaa236e61bbf0b6bd31ffb49753a059dd5e
Source522:      %{maven_central_mirror}/org/jspecify/jspecify/1.0.1/jspecify-1.0.1.pom
#!RemoteAsset:  sha256:b50975f5cba86204abda3dcd6f097af919fe22e21ef69478dd6b919f6c740d85
Source523:      %{maven_central_mirror}/org/junit/junit-bom/5.11.0-M1/junit-bom-5.11.0-M1.pom
#!RemoteAsset:  sha256:7278d577c60a4e676c7d28a8c958ff4961fd587fed4693747b4c37cd644f58b6
Source524:      %{maven_central_mirror}/org/junit/junit-bom/6.1.0-M1/junit-bom-6.1.0-M1.pom
#!RemoteAsset:  sha256:28f2a8dab5b9d259b18fa6b0ba5a6f302cbc70dd875f42032ea9e3afea09a870
Source525:      %{maven_central_mirror}/org/junit/jupiter/junit-jupiter-params/5.14.4/junit-jupiter-params-5.14.4.jar
#!RemoteAsset:  sha256:ab1a2b4bb5b74a4aeac1fd220ccf3ad60f279bb7a153b6b0b8232cd3ed81f62b
Source526:      %{maven_central_mirror}/org/junit/jupiter/junit-jupiter-params/5.14.4/junit-jupiter-params-5.14.4.pom
#!RemoteAsset:  sha256:8cce892cfda0272e00dbdbf2acc607ffd5391734629fbdce349c5691ccf8d7fb
Source527:      %{maven_central_mirror}/org/codehaus/mojo/signature/java18/1.0/java18-1.0.signature
#!RemoteAsset:  sha256:09b999a969e73525a6cc3ad2868ea744766e1d93b25c6c656d61a5ff9c881da9
Source528:      %{maven_central_mirror}/org/codehaus/plexus/plexus/1.0.10/plexus-1.0.10.pom
#!RemoteAsset:  sha256:5197630dcd2336f5b4ab8e6d26e5b8675f5ebd83bd8c91d6aba431b09627d626
Source529:      %{maven_central_mirror}/org/codehaus/plexus/plexus/1.0.11/plexus-1.0.11.pom
#!RemoteAsset:  sha256:bba9c521064b9ca132ce97cc1cc7eb4afc2dbe32bc88cb872c88e99f6162301f
Source530:      %{maven_central_mirror}/org/codehaus/plexus/plexus/10/plexus-10.pom
#!RemoteAsset:  sha256:575945dc08966c66eb03d5bae9135bd22ca3920a1865bb99d3ecd93bef55abd3
Source531:      %{maven_central_mirror}/org/codehaus/plexus/plexus/13/plexus-13.pom
#!RemoteAsset:  sha256:68d4eed65a3dbbc342ed80dd138fbe9c67cb7fb4c2abc4f5201cdb5b9f645868
Source532:      %{maven_central_mirror}/org/codehaus/plexus/plexus/16/plexus-16.pom
#!RemoteAsset:  sha256:91526ee66327c7f50fbb25bd41bfcb916e284414b868e31d50a23004bd7deea7
Source533:      %{maven_central_mirror}/org/codehaus/plexus/plexus/17/plexus-17.pom
#!RemoteAsset:  sha256:b43ee89c8890b9e5bc48d079fcb4c44f082b5139253356dc455806a33c3dd8fd
Source534:      %{maven_central_mirror}/org/codehaus/plexus/plexus/18/plexus-18.pom
#!RemoteAsset:  sha256:8d3e51c3902fd7596e548eab121ebf6b0d4aa73857077f26a24fc86f9b8455b4
Source535:      %{maven_central_mirror}/org/codehaus/plexus/plexus/19/plexus-19.pom
#!RemoteAsset:  sha256:d8531a746c988f7f68ed5f188cdea945006aea993ec5df9e524e0d27d61491da
Source536:      %{maven_central_mirror}/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom
#!RemoteAsset:  sha256:d3b2ccc943f11b4005946dbd792da9b82ee84fdbe8ea5217239c4e0f46636ee6
Source537:      %{maven_central_mirror}/org/mockito/mockito-bom/5.22.0/mockito-bom-5.22.0.pom
#!RemoteAsset:  sha256:f4b3694f60fccc7b520d8aea9b6c827d8e9949b652cad09fce10b546bf3ac537
Source538:      %{maven_central_mirror}/org/mockito/mockito-junit-jupiter/4.11.0/mockito-junit-jupiter-4.11.0.jar
#!RemoteAsset:  sha256:a7b594b002fc791733c8e94470d09045f4fd69a93ad5c375752f2057f84633b4
Source539:      %{maven_central_mirror}/org/codehaus/plexus/plexus/20/plexus-20.pom
#!RemoteAsset:  sha256:7728c57471730a6ec9e04654b60f37f57c01a2708e53aa6a0d7005aad29cbb10
Source540:      %{maven_central_mirror}/org/codehaus/plexus/plexus/23/plexus-23.pom
#!RemoteAsset:  sha256:89a1bc79e46c35ab108b7e215bb2c5c215ff8f3af1ae3cfef82d9a2b33b06c51
Source541:      %{maven_central_mirror}/org/codehaus/plexus/plexus/24/plexus-24.pom
#!RemoteAsset:  sha256:faa7947c2020967ad0c92b259ee9fa361d05e90cd036d17c37098bb1edaea3a3
Source542:      %{maven_central_mirror}/org/codehaus/plexus/plexus/25/plexus-25.pom
#!RemoteAsset:  sha256:b724ad13e3e450cb022672fe5ca6f1d38d5d7485246a3ff3d278edf9321e3417
Source543:      %{maven_central_mirror}/org/mockito/mockito-junit-jupiter/4.11.0/mockito-junit-jupiter-4.11.0.pom
#!RemoteAsset:  sha256:a343e44ff5796aed0ea60be11454c935ce20ab1c5f164acc8da574482dcbc7e9
Source544:      %{maven_central_mirror}/org/codehaus/plexus/plexus/5.1/plexus-5.1.pom
#!RemoteAsset:  sha256:ffa349db04e7abf65885bdc5a2062f4197c0ff9d3f1f4e2aa5720b77233f742c
Source545:      %{maven_central_mirror}/org/codehaus/plexus/plexus/8/plexus-8.pom
#!RemoteAsset:  sha256:4c07814ff4a39199999ae82bba1e38aa4f25637467fcac6a66ed63a76535799a
Source546:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.10.0/plexus-archiver-4.10.0.jar
#!RemoteAsset:  sha256:93ca001fd33da53d38b74f6daf19e71bc9736ed6143091ff9003cd4c05ace6c9
Source547:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.10.0/plexus-archiver-4.10.0.pom
#!RemoteAsset:  sha256:0ce7e5f325bb2153febdc5e599e5aabda28bbfb902245ac87951a13b44fce8ac
Source548:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.10.2/plexus-archiver-4.10.2.pom
#!RemoteAsset:  sha256:1f39d4f2906a04f501567cd1211cef3fd95fea4cb979e1eba1d8dd84e4b67098
Source549:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.10.4/plexus-archiver-4.10.4.jar
#!RemoteAsset:  sha256:53a2103d9257c801a8fc9c211d9fedea7e3ee1bf516bbbc28021ef45c1a219c5
Source550:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.10.4/plexus-archiver-4.10.4.pom
#!RemoteAsset:  sha256:d24c3ca2185009d81b1ce3ee90cff1cfeab53b70fadbb3ae0c02a867d7c96034
Source551:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.11.0/plexus-archiver-4.11.0.jar
#!RemoteAsset:  sha256:22a5a7c25e445560604cb0e1e5cc3d3af2669a0549c3d7db8265dcf8d8ebb4e3
Source552:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.11.0/plexus-archiver-4.11.0.pom
#!RemoteAsset:  sha256:7b4a569c92f60c859ae69594f8935d11bcbb940d86c518742c30f0925a48ba9f
Source553:      %{maven_central_mirror}/org/codehaus/plexus/plexus-archiver/4.9.2/plexus-archiver-4.9.2.pom
#!RemoteAsset:  sha256:570ae55a95e1887c3004882d30dc4e9035d2a46ba8d58b991de04175f141d88f
Source554:      %{maven_central_mirror}/org/codehaus/plexus/plexus-build-api/1.2.0/plexus-build-api-1.2.0.jar
#!RemoteAsset:  sha256:47c7b0e65718ca89df6fdf5cb3f24a49e076cacd9499236c7e18ad78e993cddb
Source555:      %{maven_central_mirror}/org/codehaus/plexus/plexus-build-api/1.2.0/plexus-build-api-1.2.0.pom
#!RemoteAsset:  sha256:9a7f1b5c5a9effd61eadfd8731452a2f76a8e79111fac391ef75ea801bea203a
Source556:      %{maven_central_mirror}/org/codehaus/plexus/plexus-cipher/2.0/plexus-cipher-2.0.jar
#!RemoteAsset:  sha256:04842f331b0225b85a5e20439710d228ea7a6302abe6d53c9c9846fbc5bf99ff
Source557:      %{maven_central_mirror}/org/codehaus/plexus/plexus-cipher/2.0/plexus-cipher-2.0.pom
#!RemoteAsset:  sha256:6d0abefb7cbf972ea16edb37ec14835372505063a45f976ab7ea889ed9497895
Source558:      %{maven_central_mirror}/org/ow2/asm/asm-commons/9.10.1/asm-commons-9.10.1.jar
#!RemoteAsset:  sha256:ceb2c43f3a273db88af8652d89ed6312f3e91a1a1e0ffc6f7823169278cf795c
Source559:      %{maven_central_mirror}/org/ow2/asm/asm-commons/9.10.1/asm-commons-9.10.1.pom
#!RemoteAsset:  sha256:3dfb0d5b6a106cd40b5b250e39935fbf2f927f4477546a5369a3ac609cf0506b
Source560:      %{maven_central_mirror}/org/ow2/asm/asm-tree/9.10.1/asm-tree-9.10.1.jar
#!RemoteAsset:  sha256:52f77c5ec49f787c9c417ebed5d6efd9922f44a202f217376e4f94c0d74f3549
Source561:      %{maven_central_mirror}/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.jar
#!RemoteAsset:  sha256:469a6c59f92effa62c0797ce7d52d2c03cf8ee1034b923c360dd78a9f505a7ba
Source562:      %{maven_central_mirror}/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.pom
#!RemoteAsset:  sha256:963eebdea6e2e1ff25c9068b64a238e1585c99f8acd455595ac159a7f52b6c41
Source563:      %{maven_central_mirror}/org/ow2/asm/asm-tree/9.10.1/asm-tree-9.10.1.pom
#!RemoteAsset:  sha256:ed825d10ab1399c8c0cb669e688cf0c8c82629b4c8399b58352b68e92ca10fcb
Source564:      %{maven_central_mirror}/org/ow2/asm/asm/9.10.1/asm-9.10.1.jar
#!RemoteAsset:  sha256:e1b1c3832ca3ac0a9e563c405f4c760118b5556a4920daee14058886197e094d
Source565:      %{maven_central_mirror}/org/ow2/asm/asm/9.10.1/asm-9.10.1.pom
#!RemoteAsset:  sha256:34f38c5d5e8bcb32cbd2d11e44bc12725be1ccdb87c3c96000af57fd81df6e64
Source566:      %{maven_central_mirror}/org/ow2/asm/asm/9.10/asm-9.10.jar
#!RemoteAsset:  sha256:bc038dcf0d45d16b71270eddeef39119672147306b661705fe4b568aa5d487e7
Source567:      %{maven_central_mirror}/org/ow2/asm/asm/9.10/asm-9.10.pom
#!RemoteAsset:  sha256:ae4e6e10d59d0a1500317764b21881ad883f8550e33c66e6142f7032c6fb566c
Source568:      %{maven_central_mirror}/org/ow2/asm/asm/9.11.1/asm-9.11.1.jar
#!RemoteAsset:  sha256:11fbc3d89590bf8a8c76012d4588aa03aacf54fbacfbe94b1e765a77f86c219a
Source569:      %{maven_central_mirror}/org/ow2/asm/asm/9.11.1/asm-9.11.1.pom
#!RemoteAsset:  sha256:32f95628a4baa60ea8a5b052c8cb6e51d07b0fee3e6092414070874f69daf710
Source570:      %{maven_central_mirror}/org/slf4j/jcl-over-slf4j/2.0.20/jcl-over-slf4j-2.0.20.jar
#!RemoteAsset:  sha256:d843ab2d887172b2983490d9939a89492320f6655275638d6a9ebd71b5fef4e8
Source571:      %{maven_central_mirror}/org/slf4j/jcl-over-slf4j/2.0.20/jcl-over-slf4j-2.0.20.pom
#!RemoteAsset:  sha256:405eef6fc9188241ec88579c3e473f5c8997455c69bcd62e142492aca15106bc
Source572:      %{maven_central_mirror}/org/codehaus/plexus/plexus-component-annotations/2.0.0/plexus-component-annotations-2.0.0.jar
#!RemoteAsset:  sha256:dcf193612b315713771e267b42de2d44de090be5945b2577345ed5ab8de2d271
Source573:      %{maven_central_mirror}/org/codehaus/plexus/plexus-component-annotations/2.0.0/plexus-component-annotations-2.0.0.pom
#!RemoteAsset:  sha256:bde3617ce9b5bcf9584126046080043af6a4b3baea40a3b153f02e7bbc32acac
Source574:      %{maven_central_mirror}/org/codehaus/plexus/plexus-component-annotations/2.1.0/plexus-component-annotations-2.1.0.jar
#!RemoteAsset:  sha256:0670b605255f7dc9a454daaec7912918ccf1b5475cbfca374363b51fcfd4ea00
Source575:      %{maven_central_mirror}/org/codehaus/plexus/plexus-component-annotations/2.1.0/plexus-component-annotations-2.1.0.pom
#!RemoteAsset:  sha256:50edb93c73786e62822b4fe1336e22880fdf147191373cf5c911370e16748fcf
Source576:      %{maven_central_mirror}/org/codehaus/plexus/plexus-component-annotations/2.2.0/plexus-component-annotations-2.2.0.jar
#!RemoteAsset:  sha256:c5483fc9c8e1a7ef6b0f899e37aaa6ce2f8afae54955bfa559fd63a33dbb065b
Source577:      %{maven_central_mirror}/org/codehaus/plexus/plexus-component-annotations/2.2.0/plexus-component-annotations-2.2.0.pom
#!RemoteAsset:  sha256:e70deff19306932ca60416bd3246d699a71a2827aeac437704cc9c7ebc61ea9f
Source578:      %{maven_central_mirror}/org/codehaus/plexus/plexus-component-metadata/2.2.0/plexus-component-metadata-2.2.0.jar
#!RemoteAsset:  sha256:c9646f8e148af1da83cefc7281cf12d190a0bacb5075dc26747202964c81bf90
Source579:      %{maven_central_mirror}/org/codehaus/plexus/plexus-component-metadata/2.2.0/plexus-component-metadata-2.2.0.pom
#!RemoteAsset:  sha256:a854365061c28821ddf1a520b8a197991613fd1d56f50f42c468b789b4714f20
Source580:      %{maven_central_mirror}/org/codehaus/plexus/plexus-components/1.1.12/plexus-components-1.1.12.pom
#!RemoteAsset:  sha256:150c40287f7cecdc21b9380caac98e928c4f33c023db6b348df1c5ac977026bf
Source581:      %{maven_central_mirror}/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom
#!RemoteAsset:  sha256:7e1446499b359675d8aabe6af2de86b85e72ae8a2a932c0b40d0e5ba57097439
Source582:      %{maven_central_mirror}/org/slf4j/slf4j-api/2.0.20/slf4j-api-2.0.20.jar
#!RemoteAsset:  sha256:2e625c3f553cddd49f8554cea9926cbf70673b3d6833464f0c5a02f4d9130594
Source583:      %{maven_central_mirror}/org/slf4j/slf4j-api/2.0.20/slf4j-api-2.0.20.pom
#!RemoteAsset:  sha256:be5e3f8e59edce852a0fdaef8caedb32f364bf13db654d15f98e17930e456487
Source584:      %{maven_central_mirror}/org/codehaus/plexus/plexus-containers/2.0.0/plexus-containers-2.0.0.pom
#!RemoteAsset:  sha256:94d5aedb3c46023265396527cf8ce7fc944b7bd79e4ebab907386418eb5a08d7
Source585:      %{maven_central_mirror}/org/codehaus/plexus/plexus-containers/2.1.0/plexus-containers-2.1.0.pom
#!RemoteAsset:  sha256:743f42d967d02826ee79f0601108e2deeb11dd3e6add24fc5f2758b1b68634ec
Source586:      %{maven_central_mirror}/org/codehaus/plexus/plexus-containers/2.2.0/plexus-containers-2.2.0.pom
#!RemoteAsset:  sha256:b87f25b512ffafcafbf4a05ab943812e9c6915291370c6b46016eb3836886c41
Source587:      %{maven_central_mirror}/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.jar
#!RemoteAsset:  sha256:4073a94aadf4d511d85bce597c09f8e9355a458ccbb07f2ed82f4c39303fe374
Source588:      %{maven_central_mirror}/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.pom
#!RemoteAsset:  sha256:995c0792669a031c94d91960a5beb60e1516abcec17a104f9f47470b36e56e27
Source589:      %{maven_central_mirror}/org/codehaus/plexus/plexus-i18n/1.1.0/plexus-i18n-1.1.0.jar
#!RemoteAsset:  sha256:4915a0a3683e9afad03db155ee85050396bbcdc240a83bf04aba58701b36d8ba
Source590:      %{maven_central_mirror}/org/codehaus/plexus/plexus-i18n/1.1.0/plexus-i18n-1.1.0.pom
#!RemoteAsset:  sha256:f78d27b642b4b886eb839fc102b5cd9fe7f30f37599ffe68185be4e1609031e9
Source591:      %{maven_central_mirror}/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom
#!RemoteAsset:  sha256:351a3d34f0886942268efcf291708c48dfadce7f2643837efdb4a6954d4e6c62
Source592:      %{maven_central_mirror}/org/slf4j/slf4j-bom/2.0.20/slf4j-bom-2.0.20.pom
#!RemoteAsset:  sha256:3fb4fb6143fdf964024c3cb738551524b9ea84e5c211cd660c559ad0703e5230
Source593:      %{maven_central_mirror}/org/codehaus/plexus/plexus-interpolation/1.27/plexus-interpolation-1.27.jar
#!RemoteAsset:  sha256:d54fbcbc4399e352322874a4128b9d28fe9fe1583f89ec361de242ea38d33f9b
Source594:      %{maven_central_mirror}/org/codehaus/plexus/plexus-interpolation/1.27/plexus-interpolation-1.27.pom
#!RemoteAsset:  sha256:95cd71e852dfdb29126e58b7b939d57ec2b2e6024391852e0b545dee082bbf3b
Source595:      %{maven_central_mirror}/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom
#!RemoteAsset:  sha256:0f4665c943df2692d75e28b6b24923ab18ff00369b8c7f5eba4bedef07e4ecd4
Source596:      %{maven_central_mirror}/org/codehaus/plexus/plexus-interpolation/1.28/plexus-interpolation-1.28.pom
#!RemoteAsset:  sha256:088d444dbcedfb384630d8686697ece3c401d6f33c8f8b3aa7259ea1c6996878
Source597:      %{maven_central_mirror}/org/codehaus/plexus/plexus-interpolation/1.29/plexus-interpolation-1.29.jar
#!RemoteAsset:  sha256:ce0d5634297bb1e065dddfdc8a2a5675717c08e8f4783edcf581543711516938
Source598:      %{maven_central_mirror}/org/codehaus/plexus/plexus-interpolation/1.29/plexus-interpolation-1.29.pom
#!RemoteAsset:  sha256:d931cf99cfd3554d322809df03c43ef897082cd480d6ff91b44d8f067ca324c8
Source599:      %{maven_central_mirror}/org/slf4j/slf4j-parent/2.0.20/slf4j-parent-2.0.20.pom
#!RemoteAsset:  sha256:965ed28912cf1ae4c628112c4009e0c19819bc44ed5db8af54ee5eda21036a3e
Source600:      %{maven_central_mirror}/org/codehaus/plexus/plexus-io/3.5.0/plexus-io-3.5.0.jar
#!RemoteAsset:  sha256:f5b86cd223a0bf4ba649de19e7e8e4e1f14344ff636f8b0024c89c46d28cc9d8
Source601:      %{maven_central_mirror}/org/codehaus/plexus/plexus-io/3.5.0/plexus-io-3.5.0.pom
#!RemoteAsset:  sha256:9ef476562573cf5df5bababc1e7da701d87a525991828b3dace15e5f2deff54c
Source602:      %{maven_central_mirror}/org/slf4j/slf4j-simple/2.0.20/slf4j-simple-2.0.20-sources.jar
#!RemoteAsset:  sha256:fc0f3effea7514e4f214df1afb672f54c982e78e5ca3b32b34196c7d056a1aa4
Source603:      %{maven_central_mirror}/org/codehaus/plexus/plexus-io/3.6.0/plexus-io-3.6.0.jar
#!RemoteAsset:  sha256:653432ed213573b6b209deb7346dc2ed89f20e647dbdb6fc868051b334b31d27
Source604:      %{maven_central_mirror}/org/codehaus/plexus/plexus-io/3.6.0/plexus-io-3.6.0.pom
#!RemoteAsset:  sha256:8e701404786a4f87219d39d4853c86dfe4e86ae99376a39749df6c08e75022e0
Source605:      %{maven_central_mirror}/org/slf4j/slf4j-simple/2.0.20/slf4j-simple-2.0.20.jar
#!RemoteAsset:  sha256:ae1ee44059883c92170c28e4548998f905c2a16998280936642ce3c29b196056
Source606:      %{maven_central_mirror}/org/slf4j/slf4j-simple/2.0.20/slf4j-simple-2.0.20.pom
#!RemoteAsset:  sha256:2ce717226d1d67b5b1df9707ed98022a366ac892d9e496c5f0173f1ab78a0965
Source607:      %{maven_central_mirror}/org/testcontainers/testcontainers-bom/1.21.3/testcontainers-bom-1.21.3.pom
#!RemoteAsset:  sha256:827baaa0215caedcdca59d091f04480566f7a43996183b9f9871fecff7abebea
Source608:      %{maven_central_mirror}/org/codehaus/plexus/plexus-resources/1.3.0/plexus-resources-1.3.0.jar
#!RemoteAsset:  sha256:e99efc42e01c1a01f2a207e36b8997473406d2cf11b4caab740c553e8a7fcf74
Source609:      %{maven_central_mirror}/org/codehaus/plexus/plexus-resources/1.3.0/plexus-resources-1.3.0.pom
#!RemoteAsset:  sha256:873139960c4c780176dda580b003a2c4bf82188bdce5bb99234e224ef7acfceb
Source610:      %{maven_central_mirror}/org/codehaus/plexus/plexus-sec-dispatcher/2.0/plexus-sec-dispatcher-2.0.jar
#!RemoteAsset:  sha256:9b28bb307017938a94d06c85b2b099bc46912b859d084fb293e569f432eadb7c
Source611:      %{maven_central_mirror}/org/codehaus/plexus/plexus-sec-dispatcher/2.0/plexus-sec-dispatcher-2.0.pom
#!RemoteAsset:  sha256:205acf1ab0a8294f90df6dd99b746ace54ba8c5ce673ca0a093aeadfe8461de2
Source612:      %{maven_central_mirror}/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.jar
#!RemoteAsset:  sha256:7827298f18f1c4804c0100b255568fa8b0070b2a63b62e4c70941ff29d5ddb7d
Source613:      %{maven_central_mirror}/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.pom
#!RemoteAsset:  sha256:687d05a9521ecb8e319e6beb46abcf53e0e61be647f1c7642a86e22f46814336
Source614:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/1.4.5/plexus-utils-1.4.5.pom
#!RemoteAsset:  sha256:3e158a87bd73d8afb4b6e8239c013b7d049c48563f45860ce99cd2e448cf4a6b
Source615:      %{maven_central_mirror}/org/tukaani/xz/1.12/xz-1.12.jar
#!RemoteAsset:  sha256:937b44d869c059c39f07ae194d8cd6219f5aebf2200ef9707f0b50b7837da281
Source616:      %{maven_central_mirror}/org/tukaani/xz/1.12/xz-1.12.pom
#!RemoteAsset:  sha256:93f975e2bb1e35db5a88c687e7899fd850e7c6d883a2afa011adcd7a671eb724
Source617:      %{maven_central_mirror}/org/xmlunit/xmlunit-core/2.14.0/xmlunit-core-2.14.0.jar
#!RemoteAsset:  sha256:365195f80eee5bb5b7a8bc2f78e7a98386a9905e4a0fa7a252eaacc36ed534f0
Source618:      %{maven_central_mirror}/org/xmlunit/xmlunit-core/2.14.0/xmlunit-core-2.14.0.pom
#!RemoteAsset:  sha256:86e0255d4c879c61b4833ed7f13124e8bb679df47debb127326e7db7dd49a07b
Source619:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.jar
#!RemoteAsset:  sha256:94ff68edeb48204d12c99189c767164d3a9f778a1372d1dce11a41462e6236f2
Source620:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.pom
#!RemoteAsset:  sha256:27ef130e32c236090e408fb5498d94cb9ea26d14070fb1c8985d607b62d098d1
Source621:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/3.6.0/plexus-utils-3.6.0.jar
#!RemoteAsset:  sha256:6138300481471c7fe6aeb115f912961f886e1a46ee9c2bd2841b65184824da28
Source622:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/3.6.0/plexus-utils-3.6.0.pom
#!RemoteAsset:  sha256:5b1d3b143f958441c68ee6c640c2ce6fad6b6ab9e9a6c4206c24469c12a15a24
Source623:      %{maven_central_mirror}/org/xmlunit/xmlunit-matchers/2.14.0/xmlunit-matchers-2.14.0.jar
#!RemoteAsset:  sha256:69eb9437a5e22a728b877df4e6f2d742d3a82ce2f6afda147cef3cb39fb5d679
Source624:      %{maven_central_mirror}/org/xmlunit/xmlunit-matchers/2.14.0/xmlunit-matchers-2.14.0.pom
#!RemoteAsset:  sha256:96b9cc44439191d2d0635974e2d44e768736b4fb2abcb65f94cd95e41912fa8b
Source625:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/4.0.1/plexus-utils-4.0.1.jar
#!RemoteAsset:  sha256:bc4235a95cd1ebae42644c81ebba9c1d4c52565f81e96ab204b6e56e3e378cc1
Source626:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/4.0.1/plexus-utils-4.0.1.pom
#!RemoteAsset:  sha256:8957274e75fe2c278b1428dd16a0daeee1dd38152cb6eff816177ac28fccb697
Source627:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/4.0.2/plexus-utils-4.0.2.jar
#!RemoteAsset:  sha256:5151c13bdd7cc3a5569583a7f4267392f013ffd3115eab8db5f86de420a366af
Source628:      %{maven_central_mirror}/org/codehaus/plexus/plexus-utils/4.0.2/plexus-utils-4.0.2.pom
#!RemoteAsset:  sha256:4b7b8b1e7f6baaabad3fa4a7f99ebde02226c8809672e59417bcb5bc21668b3a
Source629:      %{maven_central_mirror}/org/xmlunit/xmlunit-parent/2.14.0/xmlunit-parent-2.14.0.pom
#!RemoteAsset:  sha256:c8f7a98e7394adda02f6317249710e4d1b4c7a25aa8c7eace0c2eea52eb8bf85
Source630:      %{maven_central_mirror}/org/yaml/snakeyaml/2.6/snakeyaml-2.6.jar
#!RemoteAsset:  sha256:3e7e902f492c973cf210ddb8267843a3b65e83f5067467e2f4d9af0051f6b8b9
Source631:      %{maven_central_mirror}/org/codehaus/plexus/plexus-velocity/2.2.0/plexus-velocity-2.2.0.jar
#!RemoteAsset:  sha256:6f6a9b05f40e8e84af4aa9576f6b1e435ded6d5b56931b2a269b697bf72ce49d
Source632:      %{maven_central_mirror}/org/codehaus/plexus/plexus-velocity/2.2.0/plexus-velocity-2.2.0.pom
#!RemoteAsset:  sha256:c1a510a87a62bd2d74ac1472dd31c3f9e9b0b8b8568f37d77c0f135415bebd05
Source633:      %{maven_central_mirror}/org/codehaus/plexus/plexus-xml/3.0.1/plexus-xml-3.0.1.jar
#!RemoteAsset:  sha256:3242ddc20873f71b381c333b22afb9cf3596d6a63b6683036a16bd51bc8721a4
Source634:      %{maven_central_mirror}/org/codehaus/plexus/plexus-xml/3.0.1/plexus-xml-3.0.1.pom
#!RemoteAsset:  sha256:2773b0e948964d21e37b0e1dcf39025e627b873e0ce6aa2a47e23c374303e0c4
Source635:      %{maven_central_mirror}/org/yaml/snakeyaml/2.6/snakeyaml-2.6.pom
#!RemoteAsset:  sha256:e8e4bc459dd2813ef33620dbf4e8a6e7c68d47ed6637342d5adb9de67b40da00
Source636:      %{maven_central_mirror}/software/amazon/awssdk/aws-sdk-java-pom/2.33.4/aws-sdk-java-pom-2.33.4.pom
#!RemoteAsset:  sha256:2ab68297db8684350cf57bbfaf6fbfb1444db3e22caa0a51dcb8849dd5f2e158
Source637:      %{maven_central_mirror}/software/amazon/awssdk/bom/2.33.4/bom-2.33.4.pom
#!RemoteAsset:  sha256:3ab8d7bfe68f3b6ec95c1a0a47e628edbc9d76e90634cb0a0ba121fbb11b8e42
Source638:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.inject/1.0.0/org.eclipse.sisu.inject-1.0.0.jar
#!RemoteAsset:  sha256:ea0fb93dafec8adde218ce2a11f0f84ebec2b822c1d9be8b2ed9cd61ed654cf3
Source639:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.inject/1.0.0/org.eclipse.sisu.inject-1.0.0.pom
#!RemoteAsset:  sha256:b90579bc652eac7331436e0a25533fce14130b9c6e015f2dd3a3d4bb07e942b7
Source640:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M4/org.eclipse.sisu.plexus-0.9.0.M4.jar
#!RemoteAsset:  sha256:90b4be7a71c979d0c4dea20c20a28eb9e76a29df68ab9018cf011019a3e4f562
Source641:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M4/org.eclipse.sisu.plexus-0.9.0.M4.pom
#!RemoteAsset:  sha256:865b5300034fc08c790215d7d97f141914c932191bef9338a7dcef589f7536e9
Source642:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/1.0.0/org.eclipse.sisu.plexus-1.0.0.jar
#!RemoteAsset:  sha256:f9bd338be70d4bc4d8f3f10cdfab7baec089fd3b3ef1013d4ca64c4e7f2163d5
Source643:      %{maven_central_mirror}/org/eclipse/sisu/org.eclipse.sisu.plexus/1.0.0/org.eclipse.sisu.plexus-1.0.0.pom
#!RemoteAsset:  sha256:0c829c9641ccac870d7d7ff012cbbad8447e912eb9a26d0d7283f09cba44c0d9
Source644:      %{maven_central_mirror}/org/eclipse/sisu/sisu-inject/0.9.0.M4/sisu-inject-0.9.0.M4.pom
#!RemoteAsset:  sha256:98656aa9a4841078ac7efde2ae7fdaa87724c1f504afea7a4151acd3ed066fc2
Source645:      %{maven_central_mirror}/org/eclipse/sisu/sisu-inject/1.0.0/sisu-inject-1.0.0.pom
#!RemoteAsset:  sha256:5d66b6a4a680755cb6ed7cb104fa7835ef644667586ff0737adeb977c39ecdbc
Source646:      %{maven_central_mirror}/org/hamcrest/hamcrest/3.0/hamcrest-3.0.jar
#!RemoteAsset:  sha256:4a04a68133bf32461f47b8a53c8ee9df4ce2f49a0dad9794bce8717bee5bac31
Source647:      %{maven_central_mirror}/org/hamcrest/hamcrest/3.0/hamcrest-3.0.pom
#!RemoteAsset:  sha256:0b20f45e3a0fd8f0d12cdc5316b06776e902b1365db00118876f9175c60f302c
Source648:      %{maven_central_mirror}/org/jdom/jdom2/2.0.6.1/jdom2-2.0.6.1.jar
#!RemoteAsset:  sha256:55795e1018b8ae647b937967cf810a99b08582c2374e7873c128734c8c914bf3
Source649:      %{maven_central_mirror}/org/jdom/jdom2/2.0.6.1/jdom2-2.0.6.1.pom
#!RemoteAsset:  sha256:1fad6e6be7557781e4d33729d49ae1cdc8fdda6fe477bb0cc68ce351eafdfbab
Source650:      %{maven_central_mirror}/org/jspecify/jspecify/1.0.0/jspecify-1.0.0.jar
#!RemoteAsset:  sha256:cdab929a3b95211f43d2090c5e2d0dfe8465960e378bc32b35841dab324433a6
Source651:      %{maven_central_mirror}/org/jspecify/jspecify/1.0.0/jspecify-1.0.0.pom
#!RemoteAsset:  sha256:e006dd8894f9fc7b75fc32bb12fe5ed8be65667d5b454f99e2e0b8c5bb8d30b3
Source652:      %{maven_central_mirror}/org/junit/junit-bom/5.10.0/junit-bom-5.10.0.pom
#!RemoteAsset:  sha256:21c4b0286f4b20069577ff4b20978a85c100ac8a46b6f1c8672fbaab337bc3f2
Source653:      %{maven_central_mirror}/org/junit/junit-bom/5.10.1/junit-bom-5.10.1.pom
#!RemoteAsset:  sha256:169dd904a4b0f6520cffe658cc62292bfe9f3c14a989fa92120724cde43a9968
Source654:      %{maven_central_mirror}/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
#!RemoteAsset:  sha256:10937d44c425984cb8739225d34712e1a3145641ca93ac3f7ef186fa25f6babc
Source655:      %{maven_central_mirror}/org/junit/junit-bom/5.10.3/junit-bom-5.10.3.pom
#!RemoteAsset:  sha256:e67459d4882424ac6374f40db1c8f4a2e88946b340ba072c80be932a2be4644d
Source656:      %{maven_central_mirror}/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom
#!RemoteAsset:  sha256:c72124a9c9a79910c1858766b72c350e1a39244cbfb4b076348fbfe078281965
Source657:      %{maven_central_mirror}/org/junit/junit-bom/5.11.1/junit-bom-5.11.1.pom
#!RemoteAsset:  sha256:f48e88538aac145eb3ae0345a9ebd055b28f329a35dce8d1e9281325ca9b0ea2
Source658:      %{maven_central_mirror}/org/junit/junit-bom/5.11.2/junit-bom-5.11.2.pom
#!RemoteAsset:  sha256:19d4b747b204805325b6334553296f986562277a4ac1cb5e593a5e4c4f5e4115
Source659:      %{maven_central_mirror}/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom
#!RemoteAsset:  sha256:7c826bc72beddc817dad9263027f9012a0f55a377d38df89c42932a2501c2bf0
Source660:      %{maven_central_mirror}/org/junit/junit-bom/5.12.1/junit-bom-5.12.1.pom
#!RemoteAsset:  sha256:cef80fec86454f6806bfb0df24669b5c6f32e2cb728539ea859f47dfdc9bbc17
Source661:      %{maven_central_mirror}/org/junit/junit-bom/5.12.2/junit-bom-5.12.2.pom
#!RemoteAsset:  sha256:fa68451ea830572ed43ffe51d75b6a05f7a5e665a602a51f49d6be02063a65f3
Source662:      %{maven_central_mirror}/org/junit/junit-bom/5.13.1/junit-bom-5.13.1.pom
#!RemoteAsset:  sha256:d7a08a99b2502f0bb68cd4e1f984f0bf69324aaa208bd0f73366c03fc3548a42
Source663:      %{maven_central_mirror}/org/junit/junit-bom/5.13.4/junit-bom-5.13.4.pom
#!RemoteAsset:  sha256:01b01dfa366550b40ac5760548a7d728b6109d17c451e83864d1e5e0ce862c94
Source664:      %{maven_central_mirror}/org/junit/junit-bom/5.14.1/junit-bom-5.14.1.pom
#!RemoteAsset:  sha256:ed2dcc7855bd460bccc93a1bf0c962e63b566ff7d8f1ded0f1f2593ba8183aaf
Source665:      %{maven_central_mirror}/org/junit/junit-bom/5.14.2/junit-bom-5.14.2.pom
#!RemoteAsset:  sha256:08a02856e487c9357f9b29e38745f8ae805848111e72d15aad0352338f1632e1
Source666:      %{maven_central_mirror}/org/junit/junit-bom/5.14.3/junit-bom-5.14.3.pom
#!RemoteAsset:  sha256:5706e8f29a0a07f56efbbea4a0670793414194bb8d24d8143ba1e787a2f32856
Source667:      %{maven_central_mirror}/org/junit/junit-bom/5.14.4/junit-bom-5.14.4.pom
#!RemoteAsset:  sha256:cd14aaa869991f82021c585d570d31ff342bcba58bb44233b70193771b96487b
Source668:      %{maven_central_mirror}/org/junit/junit-bom/5.7.2/junit-bom-5.7.2.pom
#!RemoteAsset:  sha256:77144432ffc68bd98a790ab1069619d91032cfc0e4e13c08163aa03da36fd6e2
Source669:      %{maven_central_mirror}/org/junit/junit-bom/5.8.0-M1/junit-bom-5.8.0-M1.pom
#!RemoteAsset:  sha256:4d0329cd9e72f2420e5ca15724cbfe6ffa6e5fd2888361516271190fdc342ed7
Source670:      %{maven_central_mirror}/org/junit/junit-bom/5.9.3/junit-bom-5.9.3.pom
#!RemoteAsset:  sha256:aa1ae085fd92dfdbf85d867e60e59adc599bac183b46fc7e0698198bf426ad3f
Source671:      %{maven_central_mirror}/org/junit/jupiter/junit-jupiter-api/5.14.4/junit-jupiter-api-5.14.4.jar
#!RemoteAsset:  sha256:4c175189fd774dcd90cb23cfcab2ce9dbf2f5d0a16d7ef3702e7cfcd6411a762
Source672:      %{maven_central_mirror}/org/junit/jupiter/junit-jupiter-api/5.14.4/junit-jupiter-api-5.14.4.pom
#!RemoteAsset:  sha256:e1e35cf651ae1635638d431ea4412d5c65938be54150444f07ba659586042b11
Source673:      %{maven_central_mirror}/org/junit/jupiter/junit-jupiter-engine/5.14.4/junit-jupiter-engine-5.14.4.jar
#!RemoteAsset:  sha256:12329741c655ff5010a3d4758bb34b98e57ac8f971a6fa0fb872c6d60ab87e84
Source674:      %{maven_central_mirror}/org/junit/jupiter/junit-jupiter-engine/5.14.4/junit-jupiter-engine-5.14.4.pom
#!RemoteAsset:  sha256:55c8a0c069ac1bc4e1f8bbb26b5eae95cbd10e4ff1b23248441ab61a607381e1
Source675:      %{maven_central_mirror}/org/junit/platform/junit-platform-commons/1.14.4/junit-platform-commons-1.14.4.jar
#!RemoteAsset:  sha256:d77be81708cf9836db7a09908e6d9e4d94c527e090bd594cc4af06711b9d853d
Source676:      %{maven_central_mirror}/org/junit/platform/junit-platform-commons/1.14.4/junit-platform-commons-1.14.4.pom
#!RemoteAsset:  sha256:3c7f3f84a6747aef0db6bd5fdd2a6c8fe37132e653c939bd67387377af66d91c
Source677:      %{maven_central_mirror}/org/junit/platform/junit-platform-engine/1.14.4/junit-platform-engine-1.14.4.jar
#!RemoteAsset:  sha256:180af15472ac69c91902fbbd210566e78a82fd6d34e63d3fbada687f51614e64
Source678:      %{maven_central_mirror}/org/junit/platform/junit-platform-engine/1.14.4/junit-platform-engine-1.14.4.pom
#!RemoteAsset:  sha256:768d62f1b2a523713b702db53609c230af62bbd645fc2c07a7d794df4da32228
Source679:      %{maven_central_mirror}/org/junit/platform/junit-platform-launcher/1.14.4/junit-platform-launcher-1.14.4.jar
#!RemoteAsset:  sha256:1197a74ac2b4d71172f56cb9c4b09e54c001e6ae89f46a7873b38c6e6b608bd5
Source680:      %{maven_central_mirror}/org/junit/platform/junit-platform-launcher/1.14.4/junit-platform-launcher-1.14.4.pom
#!RemoteAsset:  sha256:4b909690cab288c761eb94c0bf0e814496cf3921d8affac84cd87774530351e5
Source681:      %{maven_central_mirror}/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar
#!RemoteAsset:  sha256:2bc2e3c8c8b313fdac231f23822225b07831dc899d067072f49d5f8ae37e739a
Source682:      %{maven_central_mirror}/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.pom
#!RemoteAsset:  sha256:7a8ff780b9ff48415d7c705f60030b0acaa616e7f823c98eede3b63508d4e984
Source683:      %{maven_central_mirror}/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.jar
#!RemoteAsset:  sha256:3dc1377e570974e6f182a6a1680d3284335b5d5cf3a8fea7bec1a5438bbdaff8
Source684:      %{maven_central_mirror}/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.pom
#!RemoteAsset:  sha256:02dfd0b0439a5591e35b708ed2f5474eb0948f53abf74637e959b8e4ef69bfeb
Source685:      %{maven_central_mirror}/org/objenesis/objenesis/3.3/objenesis-3.3.jar
#!RemoteAsset:  sha256:ba0c40da2669a048b6e24ef7066a471f0fbcbfcc509e6a3e856ca4ddfa614ad3
Source686:      %{maven_central_mirror}/org/objenesis/objenesis/3.3/objenesis-3.3.pom
#!RemoteAsset:  sha256:53372dbe8ec3814370937a87c03b42b70facb5ba570f99f89c126937d1d8bbcf
Source687:      %{maven_central_mirror}/org/objenesis/objenesis-parent/3.0.1/objenesis-parent-3.0.1.pom
#!RemoteAsset:  sha256:305c384aa2f1e1c7fe53a96da41c3ec35243b97d428d24a8f779818cc10be4ff
Source688:      %{maven_central_mirror}/org/objenesis/objenesis-parent/3.3/objenesis-parent-3.3.pom
#!RemoteAsset:  sha256:48e2df636cab6563ced64dcdff8abb2355627cb236ef0bf37598682ddf742f1b
Source689:      %{maven_central_mirror}/org/opentest4j/opentest4j/1.3.0/opentest4j-1.3.0.jar
#!RemoteAsset:  sha256:9bf7cffc410f3e8372c2522578df9ca56d9d43bd937e30948706c232a943b355
Source690:      %{maven_central_mirror}/org/opentest4j/opentest4j/1.3.0/opentest4j-1.3.0.pom
#!RemoteAsset:  sha256:3c6fac2424db3d4a853b669f4e3d1d9c3c552235e19a319673f887083c2303a1
Source691:      %{maven_central_mirror}/org/ow2/asm/asm/9.6/asm-9.6.jar
#!RemoteAsset:  sha256:92eee24bc3c843e4881d46c1dd6505471ee3142facfb466b428cfea5a56c6b60
Source692:      %{maven_central_mirror}/org/ow2/asm/asm/9.6/asm-9.6.pom
#!RemoteAsset:  sha256:321ddbb7ee6fe4f53dea6b4cd6db74154d6bfa42391c1f763b361b9f485acf05
Source693:      %{maven_central_mirror}/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
#!RemoteAsset:  sha256:a1374bd368b52b54b252d5281b9391363b58cb667a6375242fd6a3f482bc8c23
Source694:      %{maven_central_mirror}/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.jar
#!RemoteAsset:  sha256:316ff63f5b09e3e240a4d4e1cafeb7fcfb27208ccabaaf17fee8a455e8654a24
Source695:      %{maven_central_mirror}/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.pom
#!RemoteAsset:  sha256:7e0747751e9b67e19dcb5206f04ea22cc03d250c422426402eadd03513f2c314
Source696:      %{maven_central_mirror}/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.pom
#!RemoteAsset:  sha256:d3ef575e3e4979678dc01bf1dcce51021493b4d11fb7f1be8ad982877c16a1c0
Source697:      %{maven_central_mirror}/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar
#!RemoteAsset:  sha256:fb046a9c229437928bb11c2d27c8b5d773eb8a25e60cbd253d985210dedc2684
Source698:      %{maven_central_mirror}/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.pom
#!RemoteAsset:  sha256:afaf8e74019b230d3f56fdd7c93fb1070c0dca34f3d2d5ab5dea9fc616bd5ca4
Source699:      %{maven_central_mirror}/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.pom
#!RemoteAsset:  sha256:c214958b07816cb4412b30c7bdbd4308ffdc6ba2a83767b8f3a9229cbd9274d6
Source700:      %{maven_central_mirror}/org/slf4j/slf4j-nop/1.7.36/slf4j-nop-1.7.36.jar
#!RemoteAsset:  sha256:20a0f7c060020d75fef4470ae6948661d418ebd5ea4549c68abedf20ee86cb65
Source701:      %{maven_central_mirror}/org/slf4j/slf4j-nop/1.7.36/slf4j-nop-1.7.36.pom
#!RemoteAsset:  sha256:11647956e48a0c5bfb3ac33f6da7e83f341002b6857efd335a505b687be34b75
Source702:      %{maven_central_mirror}/org/slf4j/slf4j-parent/1.7.30/slf4j-parent-1.7.30.pom
#!RemoteAsset:  sha256:bb388d37fbcdd3cde64c3cede21838693218dc451f04040c5df360a78ed7e812
Source703:      %{maven_central_mirror}/org/slf4j/slf4j-parent/1.7.36/slf4j-parent-1.7.36.pom
#!RemoteAsset:  sha256:c43bc5a022dbfd9de82be232dffe46208cbc7de12c14385b5da824e331e535bb
Source704:      %{maven_central_mirror}/org/slf4j/slf4j-parent/1.7.5/slf4j-parent-1.7.5.pom
#!RemoteAsset:  sha256:e56188aa8ce51278006aa90bc7e0f304a81e2f1219f462e7d21f262535cd2795
Source705:      %{maven_central_mirror}/org/sonatype/forge/forge-parent/5/forge-parent-5.pom
#!RemoteAsset:  sha256:b51f8867c92b6a722499557fc3a1fdea77bdf9ef574722fe90ce436a29559454
Source706:      %{maven_central_mirror}/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
#!RemoteAsset:  sha256:fb40265f982548212ff82e362e59732b2187ec6f0d80182885c14ef1f982827a
Source707:      %{maven_central_mirror}/org/sonatype/oss/oss-parent/9/oss-parent-9.pom
#!RemoteAsset:  sha256:934171640fbd3d2495c50b79b0d9adb11e2c83e65bad157df8fe34bcac0ff798
Source708:      %{maven_central_mirror}/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.jar
#!RemoteAsset:  sha256:e067317a47ed9e84b2ba85a76d3cf72980e2b0dc873a90b9cbfe74fe80c37c17
Source709:      %{maven_central_mirror}/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.pom
#!RemoteAsset:  sha256:13d15ddfe9946b8427bb7b4b081ab63962285eed0bf6fa5142aea25a46e15814
Source710:      %{maven_central_mirror}/org/sonatype/spice/spice-parent/15/spice-parent-15.pom
#!RemoteAsset:  sha256:95c63c1a55b22dd6453890a419cc1a640f790bbf7d8ae82db1e30aefefb08888
Source711:      %{maven_central_mirror}/org/tukaani/xz/1.10/xz-1.10.jar
#!RemoteAsset:  sha256:ef608b83c3bb6c8e3e6b3beaa38842ba15963b46495e4af91b0746c8b750f3b9
Source712:      %{maven_central_mirror}/org/tukaani/xz/1.10/xz-1.10.pom
#!RemoteAsset:  sha256:0a4077f6aeae2865532a564807af8d30c26acc6f63b7928d93bd7ab1f2190449
Source713:      %{maven_central_mirror}/org/tukaani/xz/1.11/xz-1.11.jar
#!RemoteAsset:  sha256:7bd2fe2f145c8479824757ab76130c0815a7b55850714ef0c28b39bd5d692ca4
Source714:      %{maven_central_mirror}/org/tukaani/xz/1.11/xz-1.11.pom
#!RemoteAsset:  sha256:211b306cfc44f8f96df3a0a3ddaf75ba8c5289eed77d60d72f889bb855f535e5
Source715:      %{maven_central_mirror}/org/tukaani/xz/1.9/xz-1.9.jar
#!RemoteAsset:  sha256:093be1b03331bce2932d6825c37e98272d7621e6a9e9fb93289a002518b8dd5a
Source716:      %{maven_central_mirror}/org/tukaani/xz/1.9/xz-1.9.pom
BuildArch:      noarch

# Disable developer source formatting and SCM discovery in release tarballs.
Patch2000:      2000-disable-formatting-and-scm-for-offline-build.patch
# Use the source tarball's local repository fixture in the Resolver tests.
Patch2001:      2001-use-local-repository-fixtures-in-resolver-tests.patch
# Resolve Maven home when a launcher is called through /bin on merged-usr systems.
Patch2002:      2002-resolve-maven-home-through-directory-symlinks.patch

BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  unzip
%if %{without bootstrap}
BuildRequires:  maven
%endif

# Private libraries shipped in the upstream distribution.
Provides:       bundled(aopalliance) = 1.0
Provides:       bundled(asm) = 9.11.1
Provides:       bundled(commons-cli) = 1.11.0
Provides:       bundled(commons-codec) = 1.23.0
Provides:       bundled(error_prone_annotations) = 2.50.0
Provides:       bundled(failureaccess) = 1.0.3
Provides:       bundled(gson) = 2.15.0
Provides:       bundled(guava) = 33.8.0
Provides:       bundled(guice) = 5.1.0
Provides:       bundled(httpclient) = 4.5.14
Provides:       bundled(httpcore) = 4.4.16
Provides:       bundled(jakarta.annotation-api) = 1.3.5
Provides:       bundled(javax.inject) = 1
Provides:       bundled(jcl-over-slf4j) = 2.0.20
Provides:       bundled(jspecify) = 1.0.1
Provides:       bundled(maven-resolver) = 2.0.25
Provides:       bundled(maven-wagon) = 3.5.3
Provides:       bundled(org.eclipse.sisu.inject) = 1.1.2
Provides:       bundled(org.eclipse.sisu.plexus) = 1.1.2
Provides:       bundled(plexus-cipher) = 2.0
Provides:       bundled(plexus-classworlds) = 2.12.1
Provides:       bundled(plexus-component-annotations) = 2.2.0
Provides:       bundled(plexus-interpolation) = 1.30.0
Provides:       bundled(plexus-sec-dispatcher) = 2.0
Provides:       bundled(plexus-utils) = 3.6.2
Provides:       bundled(slf4j-api) = 2.0.20
Requires:       coreutils
Requires:       java-devel

%description
Apache Maven is a project management and build tool for Java projects. It
provides dependency management, compilation, testing, and packaging through
a declarative project object model.

Maven is compiled from upstream source using a pinned offline repository of
bootstrap dependencies. Its private third-party runtime libraries remain
bundled. The bootstrap build uses the upstream binary as its build tool;
later builds use the maven package by disabling the bootstrap condition.

%prep
%autosetup -n apache-maven-%{version} -p1
# Keep build inputs under target, outside the upstream source license scan.
# OBS fetches the inputs; Maven requires their coordinate directory layout.
install -Dm644 %{SOURCE2} target/repository/aopalliance/aopalliance/1.0/aopalliance-1.0.jar
install -Dm644 %{SOURCE3} target/repository/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
install -Dm644 %{SOURCE4} target/repository/com/amazonaws/aws-java-sdk-bom/1.12.791/aws-java-sdk-bom-1.12.791.pom
install -Dm644 %{SOURCE5} target/repository/ch/qos/logback/logback-classic/1.2.13/logback-classic-1.2.13.jar
install -Dm644 %{SOURCE6} target/repository/ch/qos/logback/logback-classic/1.2.13/logback-classic-1.2.13.pom
install -Dm644 %{SOURCE7} target/repository/ch/qos/logback/logback-core/1.2.13/logback-core-1.2.13.jar
install -Dm644 %{SOURCE8} target/repository/ch/qos/logback/logback-core/1.2.13/logback-core-1.2.13.pom
install -Dm644 %{SOURCE9} target/repository/ch/qos/logback/logback-parent/1.2.13/logback-parent-1.2.13.pom
install -Dm644 %{SOURCE10} target/repository/com/amazonaws/aws-java-sdk-pom/1.12.791/aws-java-sdk-pom-1.12.791.pom
install -Dm644 %{SOURCE11} target/repository/com/fasterxml/jackson/core/jackson-annotations/2.22/jackson-annotations-2.22.jar
install -Dm644 %{SOURCE12} target/repository/com/fasterxml/jackson/core/jackson-annotations/2.22/jackson-annotations-2.22.pom
install -Dm644 %{SOURCE13} target/repository/com/fasterxml/jackson/core/jackson-core/2.22.2/jackson-core-2.22.2.jar
install -Dm644 %{SOURCE14} target/repository/com/fasterxml/jackson/core/jackson-core/2.22.2/jackson-core-2.22.2.pom
install -Dm644 %{SOURCE15} target/repository/com/fasterxml/jackson/core/jackson-databind/2.22.2/jackson-databind-2.22.2.jar
install -Dm644 %{SOURCE16} target/repository/com/fasterxml/jackson/core/jackson-databind/2.22.2/jackson-databind-2.22.2.pom
install -Dm644 %{SOURCE17} target/repository/com/fasterxml/jackson/jackson-base/2.22.2/jackson-base-2.22.2.pom
install -Dm644 %{SOURCE18} target/repository/com/fasterxml/jackson/jackson-bom/2.20.0/jackson-bom-2.20.0.pom
install -Dm644 %{SOURCE19} target/repository/com/fasterxml/jackson/jackson-bom/2.22.2/jackson-bom-2.22.2.pom
install -Dm644 %{SOURCE20} target/repository/com/github/chhorz/javadoc-parser/0.3.1/javadoc-parser-0.3.1.jar
install -Dm644 %{SOURCE21} target/repository/com/github/chhorz/javadoc-parser/0.3.1/javadoc-parser-0.3.1.pom
install -Dm644 %{SOURCE22} target/repository/com/github/chhorz/javadoc-parser-parent/0.3.1/javadoc-parser-parent-0.3.1.pom
install -Dm644 %{SOURCE23} target/repository/com/github/cliftonlabs/json-simple/3.0.2/json-simple-3.0.2.jar
install -Dm644 %{SOURCE24} target/repository/com/github/cliftonlabs/json-simple/3.0.2/json-simple-3.0.2.pom
install -Dm644 %{SOURCE25} target/repository/com/fasterxml/jackson/jackson-parent/2.20/jackson-parent-2.20.pom
install -Dm644 %{SOURCE26} target/repository/com/github/luben/zstd-jni/1.5.6-3/zstd-jni-1.5.6-3.jar
install -Dm644 %{SOURCE27} target/repository/com/github/luben/zstd-jni/1.5.6-3/zstd-jni-1.5.6-3.pom
install -Dm644 %{SOURCE28} target/repository/com/fasterxml/jackson/jackson-parent/2.22/jackson-parent-2.22.pom
install -Dm644 %{SOURCE29} target/repository/com/github/luben/zstd-jni/1.5.7-6/zstd-jni-1.5.7-6.jar
install -Dm644 %{SOURCE30} target/repository/com/github/luben/zstd-jni/1.5.7-6/zstd-jni-1.5.7-6.pom
install -Dm644 %{SOURCE31} target/repository/com/fasterxml/oss-parent/70/oss-parent-70.pom
install -Dm644 %{SOURCE32} target/repository/com/fasterxml/oss-parent/79/oss-parent-79.pom
install -Dm644 %{SOURCE33} target/repository/com/github/albfernandez/juniversalchardet/2.5.0/juniversalchardet-2.5.0.jar
install -Dm644 %{SOURCE34} target/repository/com/github/albfernandez/juniversalchardet/2.5.0/juniversalchardet-2.5.0.pom
install -Dm644 %{SOURCE35} target/repository/com/github/javaparser/javaparser-core/3.28.2/javaparser-core-3.28.2.jar
install -Dm644 %{SOURCE36} target/repository/com/github/javaparser/javaparser-core/3.28.2/javaparser-core-3.28.2.pom
install -Dm644 %{SOURCE37} target/repository/com/google/errorprone/error_prone_annotations/2.41.0/error_prone_annotations-2.41.0.jar
install -Dm644 %{SOURCE38} target/repository/com/google/errorprone/error_prone_annotations/2.41.0/error_prone_annotations-2.41.0.pom
install -Dm644 %{SOURCE39} target/repository/com/github/javaparser/javaparser-parent/3.28.2/javaparser-parent-3.28.2.pom
install -Dm644 %{SOURCE40} target/repository/com/google/errorprone/error_prone_parent/2.41.0/error_prone_parent-2.41.0.pom
install -Dm644 %{SOURCE41} target/repository/com/github/luben/zstd-jni/1.5.7-9/zstd-jni-1.5.7-9.jar
install -Dm644 %{SOURCE42} target/repository/com/google/google/5/google-5.pom
install -Dm644 %{SOURCE43} target/repository/com/github/luben/zstd-jni/1.5.7-9/zstd-jni-1.5.7-9.pom
install -Dm644 %{SOURCE44} target/repository/com/google/guava/failureaccess/1.0.3/failureaccess-1.0.3.jar
install -Dm644 %{SOURCE45} target/repository/com/google/guava/failureaccess/1.0.3/failureaccess-1.0.3.pom
install -Dm644 %{SOURCE46} target/repository/com/google/guava/guava/30.1-jre/guava-30.1-jre.pom
install -Dm644 %{SOURCE47} target/repository/com/google/code/gson/gson-parent/2.15.0/gson-parent-2.15.0.pom
install -Dm644 %{SOURCE48} target/repository/com/google/code/gson/gson/2.15.0/gson-2.15.0.jar
install -Dm644 %{SOURCE49} target/repository/com/google/guava/guava-parent/26.0-android/guava-parent-26.0-android.pom
install -Dm644 %{SOURCE50} target/repository/com/google/guava/guava-parent/30.1-jre/guava-parent-30.1-jre.pom
install -Dm644 %{SOURCE51} target/repository/com/google/guava/guava-parent/33.4.0-android/guava-parent-33.4.0-android.pom
install -Dm644 %{SOURCE52} target/repository/com/google/code/gson/gson/2.15.0/gson-2.15.0.pom
install -Dm644 %{SOURCE53} target/repository/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.pom
install -Dm644 %{SOURCE54} target/repository/com/google/inject/guice/5.1.0/guice-5.1.0-classes.jar
install -Dm644 %{SOURCE55} target/repository/com/google/inject/guice/5.1.0/guice-5.1.0.pom
install -Dm644 %{SOURCE56} target/repository/com/google/inject/guice-parent/5.1.0/guice-parent-5.1.0.pom
install -Dm644 %{SOURCE57} target/repository/com/google/errorprone/error_prone_annotations/2.50.0/error_prone_annotations-2.50.0.jar
install -Dm644 %{SOURCE58} target/repository/com/google/errorprone/error_prone_annotations/2.50.0/error_prone_annotations-2.50.0.pom
install -Dm644 %{SOURCE59} target/repository/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.jar
install -Dm644 %{SOURCE60} target/repository/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.pom
install -Dm644 %{SOURCE61} target/repository/com/google/errorprone/error_prone_parent/2.50.0/error_prone_parent-2.50.0.pom
install -Dm644 %{SOURCE62} target/repository/com/google/guava/guava-parent/33.5.0-jre/guava-parent-33.5.0-jre.pom
install -Dm644 %{SOURCE63} target/repository/commons-beanutils/commons-beanutils/1.8.3/commons-beanutils-1.8.3.pom
install -Dm644 %{SOURCE64} target/repository/commons-beanutils/commons-beanutils/1.9.4/commons-beanutils-1.9.4.jar
install -Dm644 %{SOURCE65} target/repository/commons-beanutils/commons-beanutils/1.9.4/commons-beanutils-1.9.4.pom
install -Dm644 %{SOURCE66} target/repository/com/google/guava/guava-parent/33.8.0-jre/guava-parent-33.8.0-jre.pom
install -Dm644 %{SOURCE67} target/repository/com/google/guava/guava/33.5.0-jre/guava-33.5.0-jre.jar
install -Dm644 %{SOURCE68} target/repository/commons-cli/commons-cli/1.11.0/commons-cli-1.11.0.jar
install -Dm644 %{SOURCE69} target/repository/commons-cli/commons-cli/1.11.0/commons-cli-1.11.0.pom
install -Dm644 %{SOURCE70} target/repository/com/google/guava/guava/33.5.0-jre/guava-33.5.0-jre.pom
install -Dm644 %{SOURCE71} target/repository/com/google/guava/guava/33.8.0-jre/guava-33.8.0-jre.jar
install -Dm644 %{SOURCE72} target/repository/com/google/guava/guava/33.8.0-jre/guava-33.8.0-jre.pom
install -Dm644 %{SOURCE73} target/repository/commons-codec/commons-codec/1.11/commons-codec-1.11.pom
install -Dm644 %{SOURCE74} target/repository/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
install -Dm644 %{SOURCE75} target/repository/commons-codec/commons-codec/1.17.0/commons-codec-1.17.0.jar
install -Dm644 %{SOURCE76} target/repository/commons-codec/commons-codec/1.17.0/commons-codec-1.17.0.pom
install -Dm644 %{SOURCE77} target/repository/commons-codec/commons-codec/1.19.0/commons-codec-1.19.0.jar
install -Dm644 %{SOURCE78} target/repository/commons-codec/commons-codec/1.19.0/commons-codec-1.19.0.pom
install -Dm644 %{SOURCE79} target/repository/com/google/j2objc/j2objc-annotations/3.1/j2objc-annotations-3.1.jar
install -Dm644 %{SOURCE80} target/repository/com/google/j2objc/j2objc-annotations/3.1/j2objc-annotations-3.1.pom
install -Dm644 %{SOURCE81} target/repository/commons-cli/commons-cli/1.8.0/commons-cli-1.8.0.jar
install -Dm644 %{SOURCE82} target/repository/commons-cli/commons-cli/1.8.0/commons-cli-1.8.0.pom
install -Dm644 %{SOURCE83} target/repository/commons-codec/commons-codec/1.22.0/commons-codec-1.22.0.jar
install -Dm644 %{SOURCE84} target/repository/commons-codec/commons-codec/1.22.0/commons-codec-1.22.0.pom
install -Dm644 %{SOURCE85} target/repository/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar
install -Dm644 %{SOURCE86} target/repository/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.pom
install -Dm644 %{SOURCE87} target/repository/commons-codec/commons-codec/1.23.0/commons-codec-1.23.0.jar
install -Dm644 %{SOURCE88} target/repository/commons-codec/commons-codec/1.23.0/commons-codec-1.23.0.pom
install -Dm644 %{SOURCE89} target/repository/eu/maveniverse/maven/domtrip/domtrip-core/1.5.1/domtrip-core-1.5.1.jar
install -Dm644 %{SOURCE90} target/repository/eu/maveniverse/maven/domtrip/domtrip-core/1.5.1/domtrip-core-1.5.1.pom
install -Dm644 %{SOURCE91} target/repository/commons-io/commons-io/2.11.0/commons-io-2.11.0.pom
install -Dm644 %{SOURCE92} target/repository/eu/maveniverse/maven/domtrip/domtrip-maven/1.5.1/domtrip-maven-1.5.1.jar
install -Dm644 %{SOURCE93} target/repository/eu/maveniverse/maven/domtrip/domtrip-maven/1.5.1/domtrip-maven-1.5.1.pom
install -Dm644 %{SOURCE94} target/repository/commons-io/commons-io/2.16.1/commons-io-2.16.1.jar
install -Dm644 %{SOURCE95} target/repository/commons-io/commons-io/2.16.1/commons-io-2.16.1.pom
install -Dm644 %{SOURCE96} target/repository/commons-io/commons-io/2.17.0/commons-io-2.17.0.pom
install -Dm644 %{SOURCE97} target/repository/commons-io/commons-io/2.19.0/commons-io-2.19.0.jar
install -Dm644 %{SOURCE98} target/repository/commons-io/commons-io/2.19.0/commons-io-2.19.0.pom
install -Dm644 %{SOURCE99} target/repository/eu/maveniverse/maven/domtrip/domtrip/1.5.1/domtrip-1.5.1.pom
install -Dm644 %{SOURCE100} target/repository/commons-io/commons-io/2.20.0/commons-io-2.20.0.pom
install -Dm644 %{SOURCE101} target/repository/commons-io/commons-io/2.21.0/commons-io-2.21.0.jar
install -Dm644 %{SOURCE102} target/repository/commons-io/commons-io/2.21.0/commons-io-2.21.0.pom
install -Dm644 %{SOURCE103} target/repository/commons-io/commons-io/2.22.0/commons-io-2.22.0.jar
install -Dm644 %{SOURCE104} target/repository/commons-io/commons-io/2.22.0/commons-io-2.22.0.pom
install -Dm644 %{SOURCE105} target/repository/eu/maveniverse/maven/parent/parent/52/parent-52.pom
install -Dm644 %{SOURCE106} target/repository/commons-jxpath/commons-jxpath/1.4.0/commons-jxpath-1.4.0.jar
install -Dm644 %{SOURCE107} target/repository/commons-jxpath/commons-jxpath/1.4.0/commons-jxpath-1.4.0.pom
install -Dm644 %{SOURCE108} target/repository/io/netty/netty-bom/4.2.16.Final/netty-bom-4.2.16.Final.pom
install -Dm644 %{SOURCE109} target/repository/io/netty/netty-bom/4.2.6.Final/netty-bom-4.2.6.Final.pom
install -Dm644 %{SOURCE110} target/repository/jakarta/annotation/ca-parent/1.3.5/ca-parent-1.3.5.pom
install -Dm644 %{SOURCE111} target/repository/jakarta/annotation/jakarta.annotation-api/1.3.5/jakarta.annotation-api-1.3.5.jar
install -Dm644 %{SOURCE112} target/repository/jakarta/annotation/jakarta.annotation-api/1.3.5/jakarta.annotation-api-1.3.5.pom
install -Dm644 %{SOURCE113} target/repository/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.pom
install -Dm644 %{SOURCE114} target/repository/commons-logging/commons-logging/1.2/commons-logging-1.2.jar
install -Dm644 %{SOURCE115} target/repository/commons-logging/commons-logging/1.2/commons-logging-1.2.pom
install -Dm644 %{SOURCE116} target/repository/org/apache/apache/39/apache-39.pom
install -Dm644 %{SOURCE117} target/repository/org/apache/apache/40/apache-40.pom
install -Dm644 %{SOURCE118} target/repository/io/airlift/airbase/112/airbase-112.pom
install -Dm644 %{SOURCE119} target/repository/io/airlift/aircompressor/0.27/aircompressor-0.27.jar
install -Dm644 %{SOURCE120} target/repository/io/airlift/aircompressor/0.27/aircompressor-0.27.pom
install -Dm644 %{SOURCE121} target/repository/org/apache/commons/commons-collections4/4.5.0/commons-collections4-4.5.0.jar
install -Dm644 %{SOURCE122} target/repository/org/apache/commons/commons-collections4/4.5.0/commons-collections4-4.5.0.pom
install -Dm644 %{SOURCE123} target/repository/org/apache/commons/commons-csv/1.14.1/commons-csv-1.14.1.jar
install -Dm644 %{SOURCE124} target/repository/org/apache/commons/commons-csv/1.14.1/commons-csv-1.14.1.pom
install -Dm644 %{SOURCE125} target/repository/org/apache/commons/commons-exec/1.6.0/commons-exec-1.6.0.jar
install -Dm644 %{SOURCE126} target/repository/org/apache/commons/commons-exec/1.6.0/commons-exec-1.6.0.pom
install -Dm644 %{SOURCE127} target/repository/org/apache/commons/commons-lang3/3.21.0/commons-lang3-3.21.0.jar
install -Dm644 %{SOURCE128} target/repository/javax/inject/javax.inject/1/javax.inject-1.jar
install -Dm644 %{SOURCE129} target/repository/javax/inject/javax.inject/1/javax.inject-1.pom
install -Dm644 %{SOURCE130} target/repository/org/apache/commons/commons-lang3/3.21.0/commons-lang3-3.21.0.pom
install -Dm644 %{SOURCE131} target/repository/org/apache/commons/commons-parent/105/commons-parent-105.pom
install -Dm644 %{SOURCE132} target/repository/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.jar
install -Dm644 %{SOURCE133} target/repository/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.pom
install -Dm644 %{SOURCE134} target/repository/net/bytebuddy/byte-buddy/1.12.19/byte-buddy-1.12.19.jar
install -Dm644 %{SOURCE135} target/repository/net/bytebuddy/byte-buddy/1.12.19/byte-buddy-1.12.19.pom
install -Dm644 %{SOURCE136} target/repository/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.jar
install -Dm644 %{SOURCE137} target/repository/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.pom
install -Dm644 %{SOURCE138} target/repository/net/bytebuddy/byte-buddy-agent/1.12.19/byte-buddy-agent-1.12.19.jar
install -Dm644 %{SOURCE139} target/repository/net/bytebuddy/byte-buddy-agent/1.12.19/byte-buddy-agent-1.12.19.pom
install -Dm644 %{SOURCE140} target/repository/net/bytebuddy/byte-buddy-parent/1.10.14/byte-buddy-parent-1.10.14.pom
install -Dm644 %{SOURCE141} target/repository/net/bytebuddy/byte-buddy-parent/1.12.19/byte-buddy-parent-1.12.19.pom
install -Dm644 %{SOURCE142} target/repository/org/apache/commons/commons-parent/70/commons-parent-70.pom
install -Dm644 %{SOURCE143} target/repository/org/apache/commons/commons-parent/93/commons-parent-93.pom
install -Dm644 %{SOURCE144} target/repository/org/apache/commons/commons-text/1.15.0/commons-text-1.15.0.jar
install -Dm644 %{SOURCE145} target/repository/org/apache/commons/commons-text/1.15.0/commons-text-1.15.0.pom
install -Dm644 %{SOURCE146} target/repository/org/apache/apache/13/apache-13.pom
install -Dm644 %{SOURCE147} target/repository/org/apache/apache/16/apache-16.pom
install -Dm644 %{SOURCE148} target/repository/org/apache/apache/18/apache-18.pom
install -Dm644 %{SOURCE149} target/repository/org/apache/apache/19/apache-19.pom
install -Dm644 %{SOURCE150} target/repository/org/apache/apache/21/apache-21.pom
install -Dm644 %{SOURCE151} target/repository/org/apache/apache/23/apache-23.pom
install -Dm644 %{SOURCE152} target/repository/org/apache/apache/29/apache-29.pom
install -Dm644 %{SOURCE153} target/repository/org/apache/apache/30/apache-30.pom
install -Dm644 %{SOURCE154} target/repository/org/apache/apache/31/apache-31.pom
install -Dm644 %{SOURCE155} target/repository/org/apache/apache/32/apache-32.pom
install -Dm644 %{SOURCE156} target/repository/org/apache/apache/33/apache-33.pom
install -Dm644 %{SOURCE157} target/repository/org/apache/apache/34/apache-34.pom
install -Dm644 %{SOURCE158} target/repository/org/apache/apache/35/apache-35.pom
install -Dm644 %{SOURCE159} target/repository/org/apache/apache/37/apache-37.pom
install -Dm644 %{SOURCE160} target/repository/org/apache/apache/38/apache-38.pom
install -Dm644 %{SOURCE161} target/repository/org/apache/apache/4/apache-4.pom
install -Dm644 %{SOURCE162} target/repository/org/apache/cxf/cxf-bom/4.0.9/cxf-bom-4.0.9.pom
install -Dm644 %{SOURCE163} target/repository/org/apache/cxf/cxf/4.0.9/cxf-4.0.9.pom
install -Dm644 %{SOURCE164} target/repository/org/apache/apache/7/apache-7.pom
install -Dm644 %{SOURCE165} target/repository/org/apache/apache/9/apache-9.pom
install -Dm644 %{SOURCE166} target/repository/org/apache/apache/resources/apache-jar-resource-bundle/1.8/apache-jar-resource-bundle-1.8.jar
install -Dm644 %{SOURCE167} target/repository/org/apache/logging/log4j/log4j-bom/2.25.1/log4j-bom-2.25.1.pom
install -Dm644 %{SOURCE168} target/repository/org/apache/maven/doxia/doxia-sink-api/2.1.0/doxia-sink-api-2.1.0.jar
install -Dm644 %{SOURCE169} target/repository/org/apache/maven/doxia/doxia-sink-api/2.1.0/doxia-sink-api-2.1.0.pom
install -Dm644 %{SOURCE170} target/repository/org/apache/maven/doxia/doxia/2.1.0/doxia-2.1.0.pom
install -Dm644 %{SOURCE171} target/repository/org/apache/maven/enforcer/enforcer-api/3.6.3/enforcer-api-3.6.3.jar
install -Dm644 %{SOURCE172} target/repository/org/apache/commons/commons-compress/1.26.2/commons-compress-1.26.2.jar
install -Dm644 %{SOURCE173} target/repository/org/apache/commons/commons-compress/1.26.2/commons-compress-1.26.2.pom
install -Dm644 %{SOURCE174} target/repository/org/apache/commons/commons-compress/1.28.0/commons-compress-1.28.0.jar
install -Dm644 %{SOURCE175} target/repository/org/apache/commons/commons-compress/1.28.0/commons-compress-1.28.0.pom
install -Dm644 %{SOURCE176} target/repository/org/apache/commons/commons-digester3/3.2/commons-digester3-3.2.jar
install -Dm644 %{SOURCE177} target/repository/org/apache/commons/commons-digester3/3.2/commons-digester3-3.2.pom
install -Dm644 %{SOURCE178} target/repository/org/apache/commons/commons-lang3/3.10/commons-lang3-3.10.pom
install -Dm644 %{SOURCE179} target/repository/org/apache/maven/enforcer/enforcer-api/3.6.3/enforcer-api-3.6.3.pom
install -Dm644 %{SOURCE180} target/repository/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.pom
install -Dm644 %{SOURCE181} target/repository/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.jar
install -Dm644 %{SOURCE182} target/repository/org/apache/commons/commons-lang3/3.17.0/commons-lang3-3.17.0.pom
install -Dm644 %{SOURCE183} target/repository/org/apache/commons/commons-lang3/3.18.0/commons-lang3-3.18.0.jar
install -Dm644 %{SOURCE184} target/repository/org/apache/commons/commons-lang3/3.18.0/commons-lang3-3.18.0.pom
install -Dm644 %{SOURCE185} target/repository/org/apache/maven/enforcer/enforcer-rules/3.6.3/enforcer-rules-3.6.3.jar
install -Dm644 %{SOURCE186} target/repository/org/apache/maven/enforcer/enforcer-rules/3.6.3/enforcer-rules-3.6.3.pom
install -Dm644 %{SOURCE187} target/repository/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.jar
install -Dm644 %{SOURCE188} target/repository/org/apache/commons/commons-lang3/3.20.0/commons-lang3-3.20.0.pom
install -Dm644 %{SOURCE189} target/repository/org/apache/commons/commons-parent/14/commons-parent-14.pom
install -Dm644 %{SOURCE190} target/repository/org/apache/commons/commons-parent/22/commons-parent-22.pom
install -Dm644 %{SOURCE191} target/repository/org/apache/commons/commons-parent/34/commons-parent-34.pom
install -Dm644 %{SOURCE192} target/repository/org/apache/commons/commons-parent/39/commons-parent-39.pom
install -Dm644 %{SOURCE193} target/repository/org/apache/commons/commons-parent/42/commons-parent-42.pom
install -Dm644 %{SOURCE194} target/repository/org/apache/maven/enforcer/enforcer/3.6.3/enforcer-3.6.3.pom
install -Dm644 %{SOURCE195} target/repository/org/apache/commons/commons-parent/47/commons-parent-47.pom
install -Dm644 %{SOURCE196} target/repository/org/apache/maven/maven-archiver/3.6.6/maven-archiver-3.6.6.jar
install -Dm644 %{SOURCE197} target/repository/org/apache/commons/commons-parent/5/commons-parent-5.pom
install -Dm644 %{SOURCE198} target/repository/org/apache/commons/commons-parent/50/commons-parent-50.pom
install -Dm644 %{SOURCE199} target/repository/org/apache/maven/maven-archiver/3.6.6/maven-archiver-3.6.6.pom
install -Dm644 %{SOURCE200} target/repository/org/apache/commons/commons-parent/52/commons-parent-52.pom
install -Dm644 %{SOURCE201} target/repository/org/apache/commons/commons-parent/64/commons-parent-64.pom
install -Dm644 %{SOURCE202} target/repository/org/apache/maven/maven-parent/49/maven-parent-49.pom
install -Dm644 %{SOURCE203} target/repository/org/apache/maven/maven-parent/50/maven-parent-50.pom
install -Dm644 %{SOURCE204} target/repository/org/apache/commons/commons-parent/69/commons-parent-69.pom
install -Dm644 %{SOURCE205} target/repository/org/apache/commons/commons-parent/73/commons-parent-73.pom
install -Dm644 %{SOURCE206} target/repository/org/apache/commons/commons-parent/74/commons-parent-74.pom
install -Dm644 %{SOURCE207} target/repository/org/apache/commons/commons-parent/81/commons-parent-81.pom
install -Dm644 %{SOURCE208} target/repository/org/apache/commons/commons-parent/85/commons-parent-85.pom
install -Dm644 %{SOURCE209} target/repository/org/apache/maven/plugins/maven-compiler-plugin/3.16.0/maven-compiler-plugin-3.16.0.jar
install -Dm644 %{SOURCE210} target/repository/org/apache/maven/plugins/maven-compiler-plugin/3.16.0/maven-compiler-plugin-3.16.0.pom
install -Dm644 %{SOURCE211} target/repository/org/apache/commons/commons-parent/91/commons-parent-91.pom
install -Dm644 %{SOURCE212} target/repository/org/apache/commons/commons-parent/92/commons-parent-92.pom
install -Dm644 %{SOURCE213} target/repository/org/apache/maven/plugins/maven-dependency-plugin/3.11.0/maven-dependency-plugin-3.11.0.jar
install -Dm644 %{SOURCE214} target/repository/org/apache/commons/commons-parent/98/commons-parent-98.pom
install -Dm644 %{SOURCE215} target/repository/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.jar
install -Dm644 %{SOURCE216} target/repository/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.pom
install -Dm644 %{SOURCE217} target/repository/org/apache/maven/plugins/maven-dependency-plugin/3.11.0/maven-dependency-plugin-3.11.0.pom
install -Dm644 %{SOURCE218} target/repository/org/apache/maven/plugins/maven-enforcer-plugin/3.6.3/maven-enforcer-plugin-3.6.3.jar
install -Dm644 %{SOURCE219} target/repository/org/apache/maven/plugins/maven-enforcer-plugin/3.6.3/maven-enforcer-plugin-3.6.3.pom
install -Dm644 %{SOURCE220} target/repository/org/apache/maven/plugins/maven-failsafe-plugin/3.6.1/maven-failsafe-plugin-3.6.1.jar
install -Dm644 %{SOURCE221} target/repository/org/apache/maven/plugins/maven-failsafe-plugin/3.6.1/maven-failsafe-plugin-3.6.1.pom
install -Dm644 %{SOURCE222} target/repository/org/apache/maven/plugins/maven-jar-plugin/3.5.1/maven-jar-plugin-3.5.1.jar
install -Dm644 %{SOURCE223} target/repository/org/apache/maven/plugins/maven-jar-plugin/3.5.1/maven-jar-plugin-3.5.1.pom
install -Dm644 %{SOURCE224} target/repository/org/apache/httpcomponents/httpclient/4.5.14/httpclient-4.5.14.jar
install -Dm644 %{SOURCE225} target/repository/org/apache/httpcomponents/httpclient/4.5.14/httpclient-4.5.14.pom
install -Dm644 %{SOURCE226} target/repository/org/apache/maven/plugins/maven-plugins/48/maven-plugins-48.pom
install -Dm644 %{SOURCE227} target/repository/org/apache/httpcomponents/httpcomponents-client/4.5.14/httpcomponents-client-4.5.14.pom
install -Dm644 %{SOURCE228} target/repository/org/apache/maven/plugins/maven-plugins/49/maven-plugins-49.pom
install -Dm644 %{SOURCE229} target/repository/org/apache/maven/plugins/maven-surefire-plugin/3.6.1/maven-surefire-plugin-3.6.1.jar
install -Dm644 %{SOURCE230} target/repository/org/apache/httpcomponents/httpcomponents-core/4.4.16/httpcomponents-core-4.4.16.pom
install -Dm644 %{SOURCE231} target/repository/org/apache/httpcomponents/httpcomponents-parent/11/httpcomponents-parent-11.pom
install -Dm644 %{SOURCE232} target/repository/org/apache/maven/plugins/maven-surefire-plugin/3.6.1/maven-surefire-plugin-3.6.1.pom
install -Dm644 %{SOURCE233} target/repository/org/apache/maven/resolver/maven-resolver-api/1.9.24/maven-resolver-api-1.9.24.jar
install -Dm644 %{SOURCE234} target/repository/org/apache/maven/resolver/maven-resolver-api/1.9.24/maven-resolver-api-1.9.24.pom
install -Dm644 %{SOURCE235} target/repository/org/apache/httpcomponents/httpcore/4.4.16/httpcore-4.4.16.jar
install -Dm644 %{SOURCE236} target/repository/org/apache/httpcomponents/httpcore/4.4.16/httpcore-4.4.16.pom
install -Dm644 %{SOURCE237} target/repository/org/apache/maven/resolver/maven-resolver-api/2.0.24/maven-resolver-api-2.0.24.jar
install -Dm644 %{SOURCE238} target/repository/org/apache/maven/resolver/maven-resolver-api/2.0.24/maven-resolver-api-2.0.24.pom
install -Dm644 %{SOURCE239} target/repository/org/apache/maven/resolver/maven-resolver-api/2.0.25/maven-resolver-api-2.0.25.jar
install -Dm644 %{SOURCE240} target/repository/org/apache/maven/doxia/doxia/2.0.0/doxia-2.0.0.pom
install -Dm644 %{SOURCE241} target/repository/org/apache/maven/resolver/maven-resolver-api/2.0.25/maven-resolver-api-2.0.25.pom
install -Dm644 %{SOURCE242} target/repository/org/apache/maven/resolver/maven-resolver-connector-basic/2.0.25/maven-resolver-connector-basic-2.0.25.jar
install -Dm644 %{SOURCE243} target/repository/org/apache/maven/resolver/maven-resolver-connector-basic/2.0.25/maven-resolver-connector-basic-2.0.25.pom
install -Dm644 %{SOURCE244} target/repository/org/apache/maven/doxia/doxia-core/2.0.0/doxia-core-2.0.0.jar
install -Dm644 %{SOURCE245} target/repository/org/apache/maven/doxia/doxia-core/2.0.0/doxia-core-2.0.0.pom
install -Dm644 %{SOURCE246} target/repository/org/apache/maven/resolver/maven-resolver-impl/2.0.25/maven-resolver-impl-2.0.25.jar
install -Dm644 %{SOURCE247} target/repository/org/apache/maven/resolver/maven-resolver-impl/2.0.25/maven-resolver-impl-2.0.25.pom
install -Dm644 %{SOURCE248} target/repository/org/apache/maven/resolver/maven-resolver-named-locks/2.0.25/maven-resolver-named-locks-2.0.25.jar
install -Dm644 %{SOURCE249} target/repository/org/apache/maven/resolver/maven-resolver-named-locks/2.0.25/maven-resolver-named-locks-2.0.25.pom
install -Dm644 %{SOURCE250} target/repository/org/apache/maven/doxia/doxia-integration-tools/2.0.0/doxia-integration-tools-2.0.0.jar
install -Dm644 %{SOURCE251} target/repository/org/apache/maven/doxia/doxia-integration-tools/2.0.0/doxia-integration-tools-2.0.0.pom
install -Dm644 %{SOURCE252} target/repository/org/apache/maven/resolver/maven-resolver-spi/2.0.25/maven-resolver-spi-2.0.25.jar
install -Dm644 %{SOURCE253} target/repository/org/apache/maven/resolver/maven-resolver-spi/2.0.25/maven-resolver-spi-2.0.25.pom
install -Dm644 %{SOURCE254} target/repository/org/apache/maven/resolver/maven-resolver-transport-apache/2.0.25/maven-resolver-transport-apache-2.0.25.jar
install -Dm644 %{SOURCE255} target/repository/org/apache/maven/doxia/doxia-module-apt/2.0.0/doxia-module-apt-2.0.0.jar
install -Dm644 %{SOURCE256} target/repository/org/apache/maven/doxia/doxia-module-apt/2.0.0/doxia-module-apt-2.0.0.pom
install -Dm644 %{SOURCE257} target/repository/org/apache/maven/doxia/doxia-module-xdoc/2.0.0/doxia-module-xdoc-2.0.0.jar
install -Dm644 %{SOURCE258} target/repository/org/apache/maven/doxia/doxia-module-xdoc/2.0.0/doxia-module-xdoc-2.0.0.pom
install -Dm644 %{SOURCE259} target/repository/org/apache/maven/resolver/maven-resolver-transport-apache/2.0.25/maven-resolver-transport-apache-2.0.25.pom
install -Dm644 %{SOURCE260} target/repository/org/apache/maven/resolver/maven-resolver-transport-file/2.0.25/maven-resolver-transport-file-2.0.25.jar
install -Dm644 %{SOURCE261} target/repository/org/apache/maven/resolver/maven-resolver-transport-file/2.0.25/maven-resolver-transport-file-2.0.25.pom
install -Dm644 %{SOURCE262} target/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/2.0.25/maven-resolver-transport-wagon-2.0.25.jar
install -Dm644 %{SOURCE263} target/repository/org/apache/maven/resolver/maven-resolver-transport-wagon/2.0.25/maven-resolver-transport-wagon-2.0.25.pom
install -Dm644 %{SOURCE264} target/repository/org/apache/maven/doxia/doxia-module-xhtml5/2.0.0/doxia-module-xhtml5-2.0.0.jar
install -Dm644 %{SOURCE265} target/repository/org/apache/maven/doxia/doxia-module-xhtml5/2.0.0/doxia-module-xhtml5-2.0.0.pom
install -Dm644 %{SOURCE266} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.24/maven-resolver-util-1.9.24.jar
install -Dm644 %{SOURCE267} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.24/maven-resolver-util-1.9.24.pom
install -Dm644 %{SOURCE268} target/repository/org/apache/maven/doxia/doxia-modules/2.0.0/doxia-modules-2.0.0.pom
install -Dm644 %{SOURCE269} target/repository/org/apache/maven/resolver/maven-resolver-util/2.0.24/maven-resolver-util-2.0.24.jar
install -Dm644 %{SOURCE270} target/repository/org/apache/maven/resolver/maven-resolver-util/2.0.24/maven-resolver-util-2.0.24.pom
install -Dm644 %{SOURCE271} target/repository/org/apache/maven/resolver/maven-resolver-util/2.0.25/maven-resolver-util-2.0.25.jar
install -Dm644 %{SOURCE272} target/repository/org/apache/maven/resolver/maven-resolver-util/2.0.25/maven-resolver-util-2.0.25.pom
install -Dm644 %{SOURCE273} target/repository/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.jar
install -Dm644 %{SOURCE274} target/repository/org/apache/maven/doxia/doxia-sink-api/2.0.0/doxia-sink-api-2.0.0.pom
install -Dm644 %{SOURCE275} target/repository/org/apache/maven/doxia/doxia-site-model/2.0.0/doxia-site-model-2.0.0.jar
install -Dm644 %{SOURCE276} target/repository/org/apache/maven/doxia/doxia-site-model/2.0.0/doxia-site-model-2.0.0.pom
install -Dm644 %{SOURCE277} target/repository/org/apache/maven/resolver/maven-resolver/1.9.24/maven-resolver-1.9.24.pom
install -Dm644 %{SOURCE278} target/repository/org/apache/maven/resolver/maven-resolver/2.0.24/maven-resolver-2.0.24.pom
install -Dm644 %{SOURCE279} target/repository/org/apache/maven/doxia/doxia-site-renderer/2.0.0/doxia-site-renderer-2.0.0.jar
install -Dm644 %{SOURCE280} target/repository/org/apache/maven/doxia/doxia-site-renderer/2.0.0/doxia-site-renderer-2.0.0.pom
install -Dm644 %{SOURCE281} target/repository/org/apache/maven/resolver/maven-resolver/2.0.25/maven-resolver-2.0.25.pom
install -Dm644 %{SOURCE282} target/repository/org/apache/maven/doxia/doxia-sitetools/2.0.0/doxia-sitetools-2.0.0.pom
install -Dm644 %{SOURCE283} target/repository/org/apache/maven/shared/maven-dependency-analyzer/1.17.1/maven-dependency-analyzer-1.17.1.jar
install -Dm644 %{SOURCE284} target/repository/org/apache/maven/shared/maven-dependency-analyzer/1.17.1/maven-dependency-analyzer-1.17.1.pom
install -Dm644 %{SOURCE285} target/repository/org/apache/maven/doxia/doxia-skin-model/2.0.0/doxia-skin-model-2.0.0.jar
install -Dm644 %{SOURCE286} target/repository/org/apache/maven/doxia/doxia-skin-model/2.0.0/doxia-skin-model-2.0.0.pom
install -Dm644 %{SOURCE287} target/repository/org/apache/maven/shared/maven-shared-components/48/maven-shared-components-48.pom
install -Dm644 %{SOURCE288} target/repository/org/apache/maven/surefire/common-java5/3.6.1/common-java5-3.6.1.jar
install -Dm644 %{SOURCE289} target/repository/org/apache/maven/surefire/common-java5/3.6.1/common-java5-3.6.1.pom
install -Dm644 %{SOURCE290} target/repository/org/apache/maven/surefire/maven-surefire-common/3.6.1/maven-surefire-common-3.6.1.jar
install -Dm644 %{SOURCE291} target/repository/org/apache/maven/surefire/maven-surefire-common/3.6.1/maven-surefire-common-3.6.1.pom
install -Dm644 %{SOURCE292} target/repository/org/apache/maven/surefire/surefire-api/3.6.1/surefire-api-3.6.1.jar
install -Dm644 %{SOURCE293} target/repository/org/apache/maven/surefire/surefire-api/3.6.1/surefire-api-3.6.1.pom
install -Dm644 %{SOURCE294} target/repository/org/apache/maven/maven-archiver/3.6.2/maven-archiver-3.6.2.jar
install -Dm644 %{SOURCE295} target/repository/org/apache/maven/maven-archiver/3.6.2/maven-archiver-3.6.2.pom
install -Dm644 %{SOURCE296} target/repository/org/apache/maven/maven-archiver/3.6.3/maven-archiver-3.6.3.jar
install -Dm644 %{SOURCE297} target/repository/org/apache/maven/maven-archiver/3.6.3/maven-archiver-3.6.3.pom
install -Dm644 %{SOURCE298} target/repository/org/apache/maven/maven-archiver/3.6.5/maven-archiver-3.6.5.jar
install -Dm644 %{SOURCE299} target/repository/org/apache/maven/maven-archiver/3.6.5/maven-archiver-3.6.5.pom
install -Dm644 %{SOURCE300} target/repository/org/apache/maven/surefire/surefire-booter/3.6.1/surefire-booter-3.6.1.jar
install -Dm644 %{SOURCE301} target/repository/org/apache/maven/surefire/surefire-booter/3.6.1/surefire-booter-3.6.1.pom
install -Dm644 %{SOURCE302} target/repository/org/apache/maven/surefire/surefire-extensions-api/3.6.1/surefire-extensions-api-3.6.1.jar
install -Dm644 %{SOURCE303} target/repository/org/apache/maven/surefire/surefire-extensions-api/3.6.1/surefire-extensions-api-3.6.1.pom
install -Dm644 %{SOURCE304} target/repository/org/apache/maven/surefire/surefire-extensions-spi/3.6.1/surefire-extensions-spi-3.6.1.jar
install -Dm644 %{SOURCE305} target/repository/org/apache/maven/surefire/surefire-extensions-spi/3.6.1/surefire-extensions-spi-3.6.1.pom
install -Dm644 %{SOURCE306} target/repository/org/apache/maven/surefire/surefire-junit-platform/3.6.1/surefire-junit-platform-3.6.1.jar
install -Dm644 %{SOURCE307} target/repository/org/apache/maven/surefire/surefire-junit-platform/3.6.1/surefire-junit-platform-3.6.1.pom
install -Dm644 %{SOURCE308} target/repository/org/apache/maven/surefire/surefire-logger-api/3.6.1/surefire-logger-api-3.6.1.jar
install -Dm644 %{SOURCE309} target/repository/org/apache/maven/surefire/surefire-logger-api/3.6.1/surefire-logger-api-3.6.1.pom
install -Dm644 %{SOURCE310} target/repository/org/apache/maven/maven-parent/23/maven-parent-23.pom
install -Dm644 %{SOURCE311} target/repository/org/apache/maven/surefire/surefire-providers/3.6.1/surefire-providers-3.6.1.pom
install -Dm644 %{SOURCE312} target/repository/org/apache/maven/maven-parent/33/maven-parent-33.pom
install -Dm644 %{SOURCE313} target/repository/org/apache/maven/maven-parent/34/maven-parent-34.pom
install -Dm644 %{SOURCE314} target/repository/org/apache/maven/maven-parent/39/maven-parent-39.pom
install -Dm644 %{SOURCE315} target/repository/org/apache/maven/maven-parent/41/maven-parent-41.pom
install -Dm644 %{SOURCE316} target/repository/org/apache/maven/maven-parent/42/maven-parent-42.pom
install -Dm644 %{SOURCE317} target/repository/org/apache/maven/maven-parent/43/maven-parent-43.pom
install -Dm644 %{SOURCE318} target/repository/org/apache/maven/maven-parent/44/maven-parent-44.pom
install -Dm644 %{SOURCE319} target/repository/org/apache/maven/maven-parent/45/maven-parent-45.pom
install -Dm644 %{SOURCE320} target/repository/org/apache/maven/maven-parent/47/maven-parent-47.pom
install -Dm644 %{SOURCE321} target/repository/org/apache/maven/maven-parent/48/maven-parent-48.pom
install -Dm644 %{SOURCE322} target/repository/org/apache/maven/surefire/surefire-shared-utils/3.6.1/surefire-shared-utils-3.6.1.jar
install -Dm644 %{SOURCE323} target/repository/org/apache/maven/surefire/surefire-shared-utils/3.6.1/surefire-shared-utils-3.6.1.pom
install -Dm644 %{SOURCE324} target/repository/org/apache/maven/surefire/surefire/3.6.1/surefire-3.6.1.pom
install -Dm644 %{SOURCE325} target/repository/org/apache/maven/plugins/maven-assembly-plugin/3.8.0/maven-assembly-plugin-3.8.0.jar
install -Dm644 %{SOURCE326} target/repository/org/apache/maven/plugins/maven-assembly-plugin/3.8.0/maven-assembly-plugin-3.8.0.pom
install -Dm644 %{SOURCE327} target/repository/org/apache/rat/apache-rat-core/0.18/apache-rat-core-0.18.jar
install -Dm644 %{SOURCE328} target/repository/org/apache/rat/apache-rat-core/0.18/apache-rat-core-0.18.pom
install -Dm644 %{SOURCE329} target/repository/org/apache/rat/apache-rat-plugin/0.18/apache-rat-plugin-0.18.jar
install -Dm644 %{SOURCE330} target/repository/org/apache/rat/apache-rat-plugin/0.18/apache-rat-plugin-0.18.pom
install -Dm644 %{SOURCE331} target/repository/org/apache/rat/apache-rat-project/0.18/apache-rat-project-0.18.pom
install -Dm644 %{SOURCE332} target/repository/org/apache/tika/tika-core/3.2.3/tika-core-3.2.3.jar
install -Dm644 %{SOURCE333} target/repository/org/apache/tika/tika-core/3.2.3/tika-core-3.2.3.pom
install -Dm644 %{SOURCE334} target/repository/org/apache/tika/tika-parent/3.2.3/tika-parent-3.2.3.pom
install -Dm644 %{SOURCE335} target/repository/org/apache/tika/tika-parser-text-module/3.2.3/tika-parser-text-module-3.2.3.jar
install -Dm644 %{SOURCE336} target/repository/org/apache/tika/tika-parser-text-module/3.2.3/tika-parser-text-module-3.2.3.pom
install -Dm644 %{SOURCE337} target/repository/org/apache/maven/plugins/maven-plugins/43/maven-plugins-43.pom
install -Dm644 %{SOURCE338} target/repository/org/apache/maven/plugins/maven-plugins/45/maven-plugins-45.pom
install -Dm644 %{SOURCE339} target/repository/org/apache/maven/plugins/maven-plugins/47/maven-plugins-47.pom
install -Dm644 %{SOURCE340} target/repository/org/apache/maven/plugins/maven-remote-resources-plugin/3.3.0/maven-remote-resources-plugin-3.3.0.jar
install -Dm644 %{SOURCE341} target/repository/org/apache/maven/plugins/maven-remote-resources-plugin/3.3.0/maven-remote-resources-plugin-3.3.0.pom
install -Dm644 %{SOURCE342} target/repository/org/apache/maven/plugins/maven-resources-plugin/3.5.0/maven-resources-plugin-3.5.0.jar
install -Dm644 %{SOURCE343} target/repository/org/apache/maven/plugins/maven-resources-plugin/3.5.0/maven-resources-plugin-3.5.0.pom
install -Dm644 %{SOURCE344} target/repository/org/apache/tika/tika-parsers-standard-modules/3.2.3/tika-parsers-standard-modules-3.2.3.pom
install -Dm644 %{SOURCE345} target/repository/org/apache/tika/tika-parsers-standard/3.2.3/tika-parsers-standard-3.2.3.pom
install -Dm644 %{SOURCE346} target/repository/org/apache/tika/tika-parsers/3.2.3/tika-parsers-3.2.3.pom
install -Dm644 %{SOURCE347} target/repository/org/assertj/assertj-bom/4.0.0-M1/assertj-bom-4.0.0-M1.pom
install -Dm644 %{SOURCE348} target/repository/org/codehaus/modello/modello-core/2.8.1/modello-core-2.8.1.jar
install -Dm644 %{SOURCE349} target/repository/org/apache/maven/reporting/maven-reporting-api/4.0.0/maven-reporting-api-4.0.0.jar
install -Dm644 %{SOURCE350} target/repository/org/apache/maven/reporting/maven-reporting-api/4.0.0/maven-reporting-api-4.0.0.pom
install -Dm644 %{SOURCE351} target/repository/org/apache/maven/reporting/maven-reporting-impl/4.0.0/maven-reporting-impl-4.0.0.jar
install -Dm644 %{SOURCE352} target/repository/org/apache/maven/reporting/maven-reporting-impl/4.0.0/maven-reporting-impl-4.0.0.pom
install -Dm644 %{SOURCE353} target/repository/org/apache/maven/resolver/maven-resolver/1.4.1/maven-resolver-1.4.1.pom
install -Dm644 %{SOURCE354} target/repository/org/codehaus/modello/modello-core/2.8.1/modello-core-2.8.1.pom
install -Dm644 %{SOURCE355} target/repository/org/apache/maven/resolver/maven-resolver/1.9.25/maven-resolver-1.9.25.pom
install -Dm644 %{SOURCE356} target/repository/org/apache/maven/resolver/maven-resolver/1.9.27/maven-resolver-1.9.27.pom
install -Dm644 %{SOURCE357} target/repository/org/apache/maven/resolver/maven-resolver-api/1.4.1/maven-resolver-api-1.4.1.jar
install -Dm644 %{SOURCE358} target/repository/org/apache/maven/resolver/maven-resolver-api/1.4.1/maven-resolver-api-1.4.1.pom
install -Dm644 %{SOURCE359} target/repository/org/codehaus/modello/modello-maven-plugin/2.8.1/modello-maven-plugin-2.8.1.jar
install -Dm644 %{SOURCE360} target/repository/org/apache/maven/resolver/maven-resolver-api/1.9.25/maven-resolver-api-1.9.25.pom
install -Dm644 %{SOURCE361} target/repository/org/codehaus/modello/modello-maven-plugin/2.8.1/modello-maven-plugin-2.8.1.pom
install -Dm644 %{SOURCE362} target/repository/org/apache/maven/resolver/maven-resolver-api/1.9.27/maven-resolver-api-1.9.27.pom
install -Dm644 %{SOURCE363} target/repository/org/codehaus/modello/modello-plugin-converters/2.8.1/modello-plugin-converters-2.8.1.jar
install -Dm644 %{SOURCE364} target/repository/org/codehaus/modello/modello-plugin-converters/2.8.1/modello-plugin-converters-2.8.1.pom
install -Dm644 %{SOURCE365} target/repository/org/codehaus/modello/modello-plugin-dom4j/2.8.1/modello-plugin-dom4j-2.8.1.jar
install -Dm644 %{SOURCE366} target/repository/org/codehaus/modello/modello-plugin-dom4j/2.8.1/modello-plugin-dom4j-2.8.1.pom
install -Dm644 %{SOURCE367} target/repository/org/codehaus/modello/modello-plugin-jackson/2.8.1/modello-plugin-jackson-2.8.1.jar
install -Dm644 %{SOURCE368} target/repository/org/codehaus/modello/modello-plugin-jackson/2.8.1/modello-plugin-jackson-2.8.1.pom
install -Dm644 %{SOURCE369} target/repository/org/codehaus/modello/modello-plugin-java/2.8.1/modello-plugin-java-2.8.1.jar
install -Dm644 %{SOURCE370} target/repository/org/codehaus/modello/modello-plugin-java/2.8.1/modello-plugin-java-2.8.1.pom
install -Dm644 %{SOURCE371} target/repository/org/codehaus/modello/modello-plugin-jdom/2.8.1/modello-plugin-jdom-2.8.1.jar
install -Dm644 %{SOURCE372} target/repository/org/codehaus/modello/modello-plugin-jdom/2.8.1/modello-plugin-jdom-2.8.1.pom
install -Dm644 %{SOURCE373} target/repository/org/codehaus/modello/modello-plugin-jsonschema/2.8.1/modello-plugin-jsonschema-2.8.1.jar
install -Dm644 %{SOURCE374} target/repository/org/codehaus/modello/modello-plugin-jsonschema/2.8.1/modello-plugin-jsonschema-2.8.1.pom
install -Dm644 %{SOURCE375} target/repository/org/codehaus/modello/modello-plugin-sax/2.8.1/modello-plugin-sax-2.8.1.jar
install -Dm644 %{SOURCE376} target/repository/org/codehaus/modello/modello-plugin-sax/2.8.1/modello-plugin-sax-2.8.1.pom
install -Dm644 %{SOURCE377} target/repository/org/apache/maven/resolver/maven-resolver-util/1.4.1/maven-resolver-util-1.4.1.jar
install -Dm644 %{SOURCE378} target/repository/org/apache/maven/resolver/maven-resolver-util/1.4.1/maven-resolver-util-1.4.1.pom
install -Dm644 %{SOURCE379} target/repository/org/codehaus/modello/modello-plugin-snakeyaml/2.8.1/modello-plugin-snakeyaml-2.8.1.jar
install -Dm644 %{SOURCE380} target/repository/org/codehaus/modello/modello-plugin-snakeyaml/2.8.1/modello-plugin-snakeyaml-2.8.1.pom
install -Dm644 %{SOURCE381} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.25/maven-resolver-util-1.9.25.jar
install -Dm644 %{SOURCE382} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.25/maven-resolver-util-1.9.25.pom
install -Dm644 %{SOURCE383} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.27/maven-resolver-util-1.9.27.jar
install -Dm644 %{SOURCE384} target/repository/org/apache/maven/resolver/maven-resolver-util/1.9.27/maven-resolver-util-1.9.27.pom
install -Dm644 %{SOURCE385} target/repository/org/apache/maven/shared/file-management/3.2.0/file-management-3.2.0.jar
install -Dm644 %{SOURCE386} target/repository/org/apache/maven/shared/file-management/3.2.0/file-management-3.2.0.pom
install -Dm644 %{SOURCE387} target/repository/org/apache/maven/shared/maven-artifact-transfer/0.13.1/maven-artifact-transfer-0.13.1.jar
install -Dm644 %{SOURCE388} target/repository/org/apache/maven/shared/maven-artifact-transfer/0.13.1/maven-artifact-transfer-0.13.1.pom
install -Dm644 %{SOURCE389} target/repository/org/apache/maven/shared/maven-common-artifact-filters/3.1.0/maven-common-artifact-filters-3.1.0.pom
install -Dm644 %{SOURCE390} target/repository/org/apache/maven/shared/maven-common-artifact-filters/3.4.0/maven-common-artifact-filters-3.4.0.jar
install -Dm644 %{SOURCE391} target/repository/org/apache/maven/shared/maven-common-artifact-filters/3.4.0/maven-common-artifact-filters-3.4.0.pom
install -Dm644 %{SOURCE392} target/repository/org/codehaus/modello/modello-plugin-stax/2.8.1/modello-plugin-stax-2.8.1.jar
install -Dm644 %{SOURCE393} target/repository/org/codehaus/modello/modello-plugin-stax/2.8.1/modello-plugin-stax-2.8.1.pom
install -Dm644 %{SOURCE394} target/repository/org/apache/maven/shared/maven-dependency-tree/3.3.0/maven-dependency-tree-3.3.0.jar
install -Dm644 %{SOURCE395} target/repository/org/apache/maven/shared/maven-dependency-tree/3.3.0/maven-dependency-tree-3.3.0.pom
install -Dm644 %{SOURCE396} target/repository/org/apache/maven/shared/maven-filtering/3.4.0/maven-filtering-3.4.0.jar
install -Dm644 %{SOURCE397} target/repository/org/apache/maven/shared/maven-filtering/3.4.0/maven-filtering-3.4.0.pom
install -Dm644 %{SOURCE398} target/repository/org/apache/maven/shared/maven-filtering/3.5.0/maven-filtering-3.5.0.jar
install -Dm644 %{SOURCE399} target/repository/org/apache/maven/shared/maven-filtering/3.5.0/maven-filtering-3.5.0.pom
install -Dm644 %{SOURCE400} target/repository/org/codehaus/modello/modello-plugin-velocity/2.8.1/modello-plugin-velocity-2.8.1.jar
install -Dm644 %{SOURCE401} target/repository/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom
install -Dm644 %{SOURCE402} target/repository/org/codehaus/modello/modello-plugin-velocity/2.8.1/modello-plugin-velocity-2.8.1.pom
install -Dm644 %{SOURCE403} target/repository/org/apache/maven/shared/maven-shared-components/33/maven-shared-components-33.pom
install -Dm644 %{SOURCE404} target/repository/org/apache/maven/shared/maven-shared-components/34/maven-shared-components-34.pom
install -Dm644 %{SOURCE405} target/repository/org/apache/maven/shared/maven-shared-components/39/maven-shared-components-39.pom
install -Dm644 %{SOURCE406} target/repository/org/apache/maven/shared/maven-shared-components/41/maven-shared-components-41.pom
install -Dm644 %{SOURCE407} target/repository/org/apache/maven/shared/maven-shared-components/42/maven-shared-components-42.pom
install -Dm644 %{SOURCE408} target/repository/org/apache/maven/shared/maven-shared-components/43/maven-shared-components-43.pom
install -Dm644 %{SOURCE409} target/repository/org/apache/maven/shared/maven-shared-components/44/maven-shared-components-44.pom
install -Dm644 %{SOURCE410} target/repository/org/apache/maven/shared/maven-shared-components/45/maven-shared-components-45.pom
install -Dm644 %{SOURCE411} target/repository/org/apache/maven/shared/maven-shared-components/47/maven-shared-components-47.pom
install -Dm644 %{SOURCE412} target/repository/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar
install -Dm644 %{SOURCE413} target/repository/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom
install -Dm644 %{SOURCE414} target/repository/org/codehaus/modello/modello-plugin-xdoc/2.8.1/modello-plugin-xdoc-2.8.1.jar
install -Dm644 %{SOURCE415} target/repository/org/apache/maven/shared/maven-shared-utils/3.4.2/maven-shared-utils-3.4.2.jar
install -Dm644 %{SOURCE416} target/repository/org/apache/maven/shared/maven-shared-utils/3.4.2/maven-shared-utils-3.4.2.pom
install -Dm644 %{SOURCE417} target/repository/org/codehaus/modello/modello-plugin-xdoc/2.8.1/modello-plugin-xdoc-2.8.1.pom
install -Dm644 %{SOURCE418} target/repository/org/codehaus/modello/modello-plugin-xml/2.8.1/modello-plugin-xml-2.8.1.jar
install -Dm644 %{SOURCE419} target/repository/org/codehaus/modello/modello-plugin-xml/2.8.1/modello-plugin-xml-2.8.1.pom
install -Dm644 %{SOURCE420} target/repository/org/codehaus/modello/modello-plugin-xpp3/2.8.1/modello-plugin-xpp3-2.8.1.jar
install -Dm644 %{SOURCE421} target/repository/org/codehaus/modello/modello-plugin-xpp3/2.8.1/modello-plugin-xpp3-2.8.1.pom
install -Dm644 %{SOURCE422} target/repository/org/codehaus/modello/modello-plugin-xsd/2.8.1/modello-plugin-xsd-2.8.1.jar
install -Dm644 %{SOURCE423} target/repository/org/codehaus/modello/modello-plugin-xsd/2.8.1/modello-plugin-xsd-2.8.1.pom
install -Dm644 %{SOURCE424} target/repository/org/codehaus/modello/modello-plugins/2.8.1/modello-plugins-2.8.1.pom
install -Dm644 %{SOURCE425} target/repository/org/codehaus/modello/modello/2.8.1/modello-2.8.1.pom
install -Dm644 %{SOURCE426} target/repository/org/codehaus/mojo/animal-sniffer-annotations/1.29/animal-sniffer-annotations-1.29.jar
install -Dm644 %{SOURCE427} target/repository/org/codehaus/mojo/animal-sniffer-annotations/1.29/animal-sniffer-annotations-1.29.pom
install -Dm644 %{SOURCE428} target/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.29/animal-sniffer-maven-plugin-1.29.jar
install -Dm644 %{SOURCE429} target/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.29/animal-sniffer-maven-plugin-1.29.pom
install -Dm644 %{SOURCE430} target/repository/org/codehaus/mojo/animal-sniffer-parent/1.29/animal-sniffer-parent-1.29.pom
install -Dm644 %{SOURCE431} target/repository/org/codehaus/mojo/animal-sniffer/1.29/animal-sniffer-1.29.jar
install -Dm644 %{SOURCE432} target/repository/org/codehaus/mojo/animal-sniffer/1.29/animal-sniffer-1.29.pom
install -Dm644 %{SOURCE433} target/repository/org/codehaus/mojo/build-helper-maven-plugin/3.7.0/build-helper-maven-plugin-3.7.0.jar
install -Dm644 %{SOURCE434} target/repository/org/codehaus/mojo/build-helper-maven-plugin/3.7.0/build-helper-maven-plugin-3.7.0.pom
install -Dm644 %{SOURCE435} target/repository/org/codehaus/mojo/exec-maven-plugin/3.6.4/exec-maven-plugin-3.6.4.jar
install -Dm644 %{SOURCE436} target/repository/org/codehaus/mojo/exec-maven-plugin/3.6.4/exec-maven-plugin-3.6.4.pom
install -Dm644 %{SOURCE437} target/repository/org/apache/maven/wagon/wagon/3.5.3/wagon-3.5.3.pom
install -Dm644 %{SOURCE438} target/repository/org/apache/maven/wagon/wagon-file/3.5.3/wagon-file-3.5.3.jar
install -Dm644 %{SOURCE439} target/repository/org/apache/maven/wagon/wagon-file/3.5.3/wagon-file-3.5.3.pom
install -Dm644 %{SOURCE440} target/repository/org/apache/maven/wagon/wagon-http/3.5.3/wagon-http-3.5.3.jar
install -Dm644 %{SOURCE441} target/repository/org/apache/maven/wagon/wagon-http/3.5.3/wagon-http-3.5.3.pom
install -Dm644 %{SOURCE442} target/repository/org/apache/maven/wagon/wagon-http-shared/3.5.3/wagon-http-shared-3.5.3.jar
install -Dm644 %{SOURCE443} target/repository/org/apache/maven/wagon/wagon-http-shared/3.5.3/wagon-http-shared-3.5.3.pom
install -Dm644 %{SOURCE444} target/repository/org/apache/maven/wagon/wagon-provider-api/3.5.3/wagon-provider-api-3.5.3.jar
install -Dm644 %{SOURCE445} target/repository/org/apache/maven/wagon/wagon-provider-api/3.5.3/wagon-provider-api-3.5.3.pom
install -Dm644 %{SOURCE446} target/repository/org/apache/maven/wagon/wagon-providers/3.5.3/wagon-providers-3.5.3.pom
install -Dm644 %{SOURCE447} target/repository/org/codehaus/mojo/extra-enforcer-rules/1.12.1/extra-enforcer-rules-1.12.1.jar
install -Dm644 %{SOURCE448} target/repository/org/codehaus/mojo/extra-enforcer-rules/1.12.1/extra-enforcer-rules-1.12.1.pom
install -Dm644 %{SOURCE449} target/repository/org/codehaus/mojo/java-boot-classpath-detector/1.29/java-boot-classpath-detector-1.29.jar
install -Dm644 %{SOURCE450} target/repository/org/codehaus/mojo/java-boot-classpath-detector/1.29/java-boot-classpath-detector-1.29.pom
install -Dm644 %{SOURCE451} target/repository/org/codehaus/mojo/mojo-parent/97/mojo-parent-97.pom
install -Dm644 %{SOURCE452} target/repository/org/apache/velocity/tools/velocity-tools-generic/3.1/velocity-tools-generic-3.1.jar
install -Dm644 %{SOURCE453} target/repository/org/apache/velocity/tools/velocity-tools-generic/3.1/velocity-tools-generic-3.1.pom
install -Dm644 %{SOURCE454} target/repository/org/apache/velocity/tools/velocity-tools-parent/3.1/velocity-tools-parent-3.1.pom
install -Dm644 %{SOURCE455} target/repository/org/codehaus/plexus/plexus-archiver/4.12.0/plexus-archiver-4.12.0.jar
install -Dm644 %{SOURCE456} target/repository/org/codehaus/plexus/plexus-archiver/4.12.0/plexus-archiver-4.12.0.pom
install -Dm644 %{SOURCE457} target/repository/org/codehaus/plexus/plexus-classworlds/2.12.1/plexus-classworlds-2.12.1.jar
install -Dm644 %{SOURCE458} target/repository/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.pom
install -Dm644 %{SOURCE459} target/repository/org/apache/velocity/velocity-engine-core/2.4/velocity-engine-core-2.4.pom
install -Dm644 %{SOURCE460} target/repository/org/apache/velocity/velocity-engine-core/2.4.1/velocity-engine-core-2.4.1.jar
install -Dm644 %{SOURCE461} target/repository/org/apache/velocity/velocity-engine-core/2.4.1/velocity-engine-core-2.4.1.pom
install -Dm644 %{SOURCE462} target/repository/org/apache/velocity/velocity-engine-parent/2.3/velocity-engine-parent-2.3.pom
install -Dm644 %{SOURCE463} target/repository/org/apache/velocity/velocity-engine-parent/2.4/velocity-engine-parent-2.4.pom
install -Dm644 %{SOURCE464} target/repository/org/apache/velocity/velocity-engine-parent/2.4.1/velocity-engine-parent-2.4.1.pom
install -Dm644 %{SOURCE465} target/repository/org/apache/velocity/velocity-master/4/velocity-master-4.pom
install -Dm644 %{SOURCE466} target/repository/org/apache/velocity/velocity-master/7/velocity-master-7.pom
install -Dm644 %{SOURCE467} target/repository/org/codehaus/plexus/plexus-classworlds/2.12.1/plexus-classworlds-2.12.1.pom
install -Dm644 %{SOURCE468} target/repository/org/codehaus/plexus/plexus-classworlds/2.9.0/plexus-classworlds-2.9.0.jar
install -Dm644 %{SOURCE469} target/repository/org/codehaus/plexus/plexus-classworlds/2.9.0/plexus-classworlds-2.9.0.pom
install -Dm644 %{SOURCE470} target/repository/org/codehaus/plexus/plexus-compiler-api/2.17.0/plexus-compiler-api-2.17.0.jar
install -Dm644 %{SOURCE471} target/repository/org/apache-extras/beanshell/bsh/2.0b6/bsh-2.0b6.jar
install -Dm644 %{SOURCE472} target/repository/org/apache-extras/beanshell/bsh/2.0b6/bsh-2.0b6.pom
install -Dm644 %{SOURCE473} target/repository/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.jar
install -Dm644 %{SOURCE474} target/repository/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.pom
install -Dm644 %{SOURCE475} target/repository/org/assertj/assertj-bom/3.27.7/assertj-bom-3.27.7.pom
install -Dm644 %{SOURCE476} target/repository/org/codehaus/plexus/plexus-compiler-api/2.17.0/plexus-compiler-api-2.17.0.pom
install -Dm644 %{SOURCE477} target/repository/org/codehaus/plexus/plexus-compiler-javac/2.17.0/plexus-compiler-javac-2.17.0.jar
install -Dm644 %{SOURCE478} target/repository/org/codehaus/plexus/plexus-compiler-javac/2.17.0/plexus-compiler-javac-2.17.0.pom
install -Dm644 %{SOURCE479} target/repository/org/codehaus/plexus/plexus-compiler-manager/2.17.0/plexus-compiler-manager-2.17.0.jar
install -Dm644 %{SOURCE480} target/repository/org/codehaus/plexus/plexus-compiler-manager/2.17.0/plexus-compiler-manager-2.17.0.pom
install -Dm644 %{SOURCE481} target/repository/org/codehaus/plexus/plexus-compiler/2.17.0/plexus-compiler-2.17.0.pom
install -Dm644 %{SOURCE482} target/repository/org/codehaus/plexus/plexus-compilers/2.17.0/plexus-compilers-2.17.0.pom
install -Dm644 %{SOURCE483} target/repository/org/codehaus/plexus/plexus-interpolation/1.30.0/plexus-interpolation-1.30.0.jar
install -Dm644 %{SOURCE484} target/repository/org/codehaus/plexus/plexus-interpolation/1.30.0/plexus-interpolation-1.30.0.pom
install -Dm644 %{SOURCE485} target/repository/org/codehaus/plexus/plexus-java/1.6.0/plexus-java-1.6.0.jar
install -Dm644 %{SOURCE486} target/repository/org/codehaus/plexus/plexus-java/1.6.0/plexus-java-1.6.0.pom
install -Dm644 %{SOURCE487} target/repository/org/codehaus/plexus/plexus-languages/1.6.0/plexus-languages-1.6.0.pom
install -Dm644 %{SOURCE488} target/repository/org/codehaus/plexus/plexus-testing/2.2.0/plexus-testing-2.2.0.jar
install -Dm644 %{SOURCE489} target/repository/org/codehaus/plexus/plexus-testing/2.2.0/plexus-testing-2.2.0.pom
install -Dm644 %{SOURCE490} target/repository/org/codehaus/plexus/plexus-utils/3.6.2/plexus-utils-3.6.2.jar
install -Dm644 %{SOURCE491} target/repository/org/codehaus/plexus/plexus-utils/3.6.2/plexus-utils-3.6.2.pom
install -Dm644 %{SOURCE492} target/repository/org/codehaus/plexus/plexus-utils/4.0.3/plexus-utils-4.0.3.jar
install -Dm644 %{SOURCE493} target/repository/org/codehaus/plexus/plexus-utils/4.0.3/plexus-utils-4.0.3.pom
install -Dm644 %{SOURCE494} target/repository/org/codehaus/plexus/plexus-utils/4.1.0/plexus-utils-4.1.0.jar
install -Dm644 %{SOURCE495} target/repository/org/codehaus/plexus/plexus-utils/4.1.0/plexus-utils-4.1.0.pom
install -Dm644 %{SOURCE496} target/repository/org/codehaus/plexus/plexus-xml/3.0.0/plexus-xml-3.0.0.pom
install -Dm644 %{SOURCE497} target/repository/org/codehaus/plexus/plexus-xml/3.1.0/plexus-xml-3.1.0.jar
install -Dm644 %{SOURCE498} target/repository/org/codehaus/plexus/plexus-xml/3.1.0/plexus-xml-3.1.0.pom
install -Dm644 %{SOURCE499} target/repository/org/codehaus/plexus/plexus/27/plexus-27.pom
install -Dm644 %{SOURCE500} target/repository/org/eclipse/ee4j/project/1.0.5/project-1.0.5.pom
install -Dm644 %{SOURCE501} target/repository/org/eclipse/jetty/jetty-bom/11.0.26/jetty-bom-11.0.26.pom
install -Dm644 %{SOURCE502} target/repository/org/eclipse/jetty/jetty-bom/12.1.13/jetty-bom-12.1.13.pom
install -Dm644 %{SOURCE503} target/repository/org/eclipse/jetty/jetty-bom/12.1.14/jetty-bom-12.1.14.pom
install -Dm644 %{SOURCE504} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/0.9.0.M3/org.eclipse.sisu.inject-0.9.0.M3.jar
install -Dm644 %{SOURCE505} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/0.9.0.M3/org.eclipse.sisu.inject-0.9.0.M3.pom
install -Dm644 %{SOURCE506} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/1.1.2/org.eclipse.sisu.inject-1.1.2.jar
install -Dm644 %{SOURCE507} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/1.1.2/org.eclipse.sisu.inject-1.1.2.pom
install -Dm644 %{SOURCE508} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M3/org.eclipse.sisu.plexus-0.9.0.M3.jar
install -Dm644 %{SOURCE509} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M3/org.eclipse.sisu.plexus-0.9.0.M3.pom
install -Dm644 %{SOURCE510} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/1.1.0/org.eclipse.sisu.plexus-1.1.0.jar
install -Dm644 %{SOURCE511} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/1.1.0/org.eclipse.sisu.plexus-1.1.0.pom
install -Dm644 %{SOURCE512} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/1.1.2/org.eclipse.sisu.plexus-1.1.2.jar
install -Dm644 %{SOURCE513} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/1.1.2/org.eclipse.sisu.plexus-1.1.2.pom
install -Dm644 %{SOURCE514} target/repository/org/eclipse/sisu/sisu-inject/0.9.0.M3/sisu-inject-0.9.0.M3.pom
install -Dm644 %{SOURCE515} target/repository/org/eclipse/sisu/sisu-inject/1.1.0/sisu-inject-1.1.0.pom
install -Dm644 %{SOURCE516} target/repository/org/eclipse/sisu/sisu-inject/1.1.2/sisu-inject-1.1.2.pom
install -Dm644 %{SOURCE517} target/repository/org/eclipse/sisu/sisu-maven-plugin/1.1.2/sisu-maven-plugin-1.1.2.jar
install -Dm644 %{SOURCE518} target/repository/org/eclipse/sisu/sisu-maven-plugin/1.1.2/sisu-maven-plugin-1.1.2.pom
install -Dm644 %{SOURCE519} target/repository/org/jsoup/jsoup/1.23.1/jsoup-1.23.1.jar
install -Dm644 %{SOURCE520} target/repository/org/jsoup/jsoup/1.23.1/jsoup-1.23.1.pom
install -Dm644 %{SOURCE521} target/repository/org/jspecify/jspecify/1.0.1/jspecify-1.0.1.jar
install -Dm644 %{SOURCE522} target/repository/org/jspecify/jspecify/1.0.1/jspecify-1.0.1.pom
install -Dm644 %{SOURCE523} target/repository/org/junit/junit-bom/5.11.0-M1/junit-bom-5.11.0-M1.pom
install -Dm644 %{SOURCE524} target/repository/org/junit/junit-bom/6.1.0-M1/junit-bom-6.1.0-M1.pom
install -Dm644 %{SOURCE525} target/repository/org/junit/jupiter/junit-jupiter-params/5.14.4/junit-jupiter-params-5.14.4.jar
install -Dm644 %{SOURCE526} target/repository/org/junit/jupiter/junit-jupiter-params/5.14.4/junit-jupiter-params-5.14.4.pom
install -Dm644 %{SOURCE527} target/repository/org/codehaus/mojo/signature/java18/1.0/java18-1.0.signature
install -Dm644 %{SOURCE528} target/repository/org/codehaus/plexus/plexus/1.0.10/plexus-1.0.10.pom
install -Dm644 %{SOURCE529} target/repository/org/codehaus/plexus/plexus/1.0.11/plexus-1.0.11.pom
install -Dm644 %{SOURCE530} target/repository/org/codehaus/plexus/plexus/10/plexus-10.pom
install -Dm644 %{SOURCE531} target/repository/org/codehaus/plexus/plexus/13/plexus-13.pom
install -Dm644 %{SOURCE532} target/repository/org/codehaus/plexus/plexus/16/plexus-16.pom
install -Dm644 %{SOURCE533} target/repository/org/codehaus/plexus/plexus/17/plexus-17.pom
install -Dm644 %{SOURCE534} target/repository/org/codehaus/plexus/plexus/18/plexus-18.pom
install -Dm644 %{SOURCE535} target/repository/org/codehaus/plexus/plexus/19/plexus-19.pom
install -Dm644 %{SOURCE536} target/repository/org/mockito/mockito-bom/4.11.0/mockito-bom-4.11.0.pom
install -Dm644 %{SOURCE537} target/repository/org/mockito/mockito-bom/5.22.0/mockito-bom-5.22.0.pom
install -Dm644 %{SOURCE538} target/repository/org/mockito/mockito-junit-jupiter/4.11.0/mockito-junit-jupiter-4.11.0.jar
install -Dm644 %{SOURCE539} target/repository/org/codehaus/plexus/plexus/20/plexus-20.pom
install -Dm644 %{SOURCE540} target/repository/org/codehaus/plexus/plexus/23/plexus-23.pom
install -Dm644 %{SOURCE541} target/repository/org/codehaus/plexus/plexus/24/plexus-24.pom
install -Dm644 %{SOURCE542} target/repository/org/codehaus/plexus/plexus/25/plexus-25.pom
install -Dm644 %{SOURCE543} target/repository/org/mockito/mockito-junit-jupiter/4.11.0/mockito-junit-jupiter-4.11.0.pom
install -Dm644 %{SOURCE544} target/repository/org/codehaus/plexus/plexus/5.1/plexus-5.1.pom
install -Dm644 %{SOURCE545} target/repository/org/codehaus/plexus/plexus/8/plexus-8.pom
install -Dm644 %{SOURCE546} target/repository/org/codehaus/plexus/plexus-archiver/4.10.0/plexus-archiver-4.10.0.jar
install -Dm644 %{SOURCE547} target/repository/org/codehaus/plexus/plexus-archiver/4.10.0/plexus-archiver-4.10.0.pom
install -Dm644 %{SOURCE548} target/repository/org/codehaus/plexus/plexus-archiver/4.10.2/plexus-archiver-4.10.2.pom
install -Dm644 %{SOURCE549} target/repository/org/codehaus/plexus/plexus-archiver/4.10.4/plexus-archiver-4.10.4.jar
install -Dm644 %{SOURCE550} target/repository/org/codehaus/plexus/plexus-archiver/4.10.4/plexus-archiver-4.10.4.pom
install -Dm644 %{SOURCE551} target/repository/org/codehaus/plexus/plexus-archiver/4.11.0/plexus-archiver-4.11.0.jar
install -Dm644 %{SOURCE552} target/repository/org/codehaus/plexus/plexus-archiver/4.11.0/plexus-archiver-4.11.0.pom
install -Dm644 %{SOURCE553} target/repository/org/codehaus/plexus/plexus-archiver/4.9.2/plexus-archiver-4.9.2.pom
install -Dm644 %{SOURCE554} target/repository/org/codehaus/plexus/plexus-build-api/1.2.0/plexus-build-api-1.2.0.jar
install -Dm644 %{SOURCE555} target/repository/org/codehaus/plexus/plexus-build-api/1.2.0/plexus-build-api-1.2.0.pom
install -Dm644 %{SOURCE556} target/repository/org/codehaus/plexus/plexus-cipher/2.0/plexus-cipher-2.0.jar
install -Dm644 %{SOURCE557} target/repository/org/codehaus/plexus/plexus-cipher/2.0/plexus-cipher-2.0.pom
install -Dm644 %{SOURCE558} target/repository/org/ow2/asm/asm-commons/9.10.1/asm-commons-9.10.1.jar
install -Dm644 %{SOURCE559} target/repository/org/ow2/asm/asm-commons/9.10.1/asm-commons-9.10.1.pom
install -Dm644 %{SOURCE560} target/repository/org/ow2/asm/asm-tree/9.10.1/asm-tree-9.10.1.jar
install -Dm644 %{SOURCE561} target/repository/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.jar
install -Dm644 %{SOURCE562} target/repository/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.pom
install -Dm644 %{SOURCE563} target/repository/org/ow2/asm/asm-tree/9.10.1/asm-tree-9.10.1.pom
install -Dm644 %{SOURCE564} target/repository/org/ow2/asm/asm/9.10.1/asm-9.10.1.jar
install -Dm644 %{SOURCE565} target/repository/org/ow2/asm/asm/9.10.1/asm-9.10.1.pom
install -Dm644 %{SOURCE566} target/repository/org/ow2/asm/asm/9.10/asm-9.10.jar
install -Dm644 %{SOURCE567} target/repository/org/ow2/asm/asm/9.10/asm-9.10.pom
install -Dm644 %{SOURCE568} target/repository/org/ow2/asm/asm/9.11.1/asm-9.11.1.jar
install -Dm644 %{SOURCE569} target/repository/org/ow2/asm/asm/9.11.1/asm-9.11.1.pom
install -Dm644 %{SOURCE570} target/repository/org/slf4j/jcl-over-slf4j/2.0.20/jcl-over-slf4j-2.0.20.jar
install -Dm644 %{SOURCE571} target/repository/org/slf4j/jcl-over-slf4j/2.0.20/jcl-over-slf4j-2.0.20.pom
install -Dm644 %{SOURCE572} target/repository/org/codehaus/plexus/plexus-component-annotations/2.0.0/plexus-component-annotations-2.0.0.jar
install -Dm644 %{SOURCE573} target/repository/org/codehaus/plexus/plexus-component-annotations/2.0.0/plexus-component-annotations-2.0.0.pom
install -Dm644 %{SOURCE574} target/repository/org/codehaus/plexus/plexus-component-annotations/2.1.0/plexus-component-annotations-2.1.0.jar
install -Dm644 %{SOURCE575} target/repository/org/codehaus/plexus/plexus-component-annotations/2.1.0/plexus-component-annotations-2.1.0.pom
install -Dm644 %{SOURCE576} target/repository/org/codehaus/plexus/plexus-component-annotations/2.2.0/plexus-component-annotations-2.2.0.jar
install -Dm644 %{SOURCE577} target/repository/org/codehaus/plexus/plexus-component-annotations/2.2.0/plexus-component-annotations-2.2.0.pom
install -Dm644 %{SOURCE578} target/repository/org/codehaus/plexus/plexus-component-metadata/2.2.0/plexus-component-metadata-2.2.0.jar
install -Dm644 %{SOURCE579} target/repository/org/codehaus/plexus/plexus-component-metadata/2.2.0/plexus-component-metadata-2.2.0.pom
install -Dm644 %{SOURCE580} target/repository/org/codehaus/plexus/plexus-components/1.1.12/plexus-components-1.1.12.pom
install -Dm644 %{SOURCE581} target/repository/org/slf4j/slf4j-api/2.0.17/slf4j-api-2.0.17.pom
install -Dm644 %{SOURCE582} target/repository/org/slf4j/slf4j-api/2.0.20/slf4j-api-2.0.20.jar
install -Dm644 %{SOURCE583} target/repository/org/slf4j/slf4j-api/2.0.20/slf4j-api-2.0.20.pom
install -Dm644 %{SOURCE584} target/repository/org/codehaus/plexus/plexus-containers/2.0.0/plexus-containers-2.0.0.pom
install -Dm644 %{SOURCE585} target/repository/org/codehaus/plexus/plexus-containers/2.1.0/plexus-containers-2.1.0.pom
install -Dm644 %{SOURCE586} target/repository/org/codehaus/plexus/plexus-containers/2.2.0/plexus-containers-2.2.0.pom
install -Dm644 %{SOURCE587} target/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.jar
install -Dm644 %{SOURCE588} target/repository/org/codehaus/plexus/plexus-i18n/1.0-beta-10/plexus-i18n-1.0-beta-10.pom
install -Dm644 %{SOURCE589} target/repository/org/codehaus/plexus/plexus-i18n/1.1.0/plexus-i18n-1.1.0.jar
install -Dm644 %{SOURCE590} target/repository/org/codehaus/plexus/plexus-i18n/1.1.0/plexus-i18n-1.1.0.pom
install -Dm644 %{SOURCE591} target/repository/org/slf4j/slf4j-bom/2.0.17/slf4j-bom-2.0.17.pom
install -Dm644 %{SOURCE592} target/repository/org/slf4j/slf4j-bom/2.0.20/slf4j-bom-2.0.20.pom
install -Dm644 %{SOURCE593} target/repository/org/codehaus/plexus/plexus-interpolation/1.27/plexus-interpolation-1.27.jar
install -Dm644 %{SOURCE594} target/repository/org/codehaus/plexus/plexus-interpolation/1.27/plexus-interpolation-1.27.pom
install -Dm644 %{SOURCE595} target/repository/org/slf4j/slf4j-parent/2.0.17/slf4j-parent-2.0.17.pom
install -Dm644 %{SOURCE596} target/repository/org/codehaus/plexus/plexus-interpolation/1.28/plexus-interpolation-1.28.pom
install -Dm644 %{SOURCE597} target/repository/org/codehaus/plexus/plexus-interpolation/1.29/plexus-interpolation-1.29.jar
install -Dm644 %{SOURCE598} target/repository/org/codehaus/plexus/plexus-interpolation/1.29/plexus-interpolation-1.29.pom
install -Dm644 %{SOURCE599} target/repository/org/slf4j/slf4j-parent/2.0.20/slf4j-parent-2.0.20.pom
install -Dm644 %{SOURCE600} target/repository/org/codehaus/plexus/plexus-io/3.5.0/plexus-io-3.5.0.jar
install -Dm644 %{SOURCE601} target/repository/org/codehaus/plexus/plexus-io/3.5.0/plexus-io-3.5.0.pom
install -Dm644 %{SOURCE602} target/repository/org/slf4j/slf4j-simple/2.0.20/slf4j-simple-2.0.20-sources.jar
install -Dm644 %{SOURCE603} target/repository/org/codehaus/plexus/plexus-io/3.6.0/plexus-io-3.6.0.jar
install -Dm644 %{SOURCE604} target/repository/org/codehaus/plexus/plexus-io/3.6.0/plexus-io-3.6.0.pom
install -Dm644 %{SOURCE605} target/repository/org/slf4j/slf4j-simple/2.0.20/slf4j-simple-2.0.20.jar
install -Dm644 %{SOURCE606} target/repository/org/slf4j/slf4j-simple/2.0.20/slf4j-simple-2.0.20.pom
install -Dm644 %{SOURCE607} target/repository/org/testcontainers/testcontainers-bom/1.21.3/testcontainers-bom-1.21.3.pom
install -Dm644 %{SOURCE608} target/repository/org/codehaus/plexus/plexus-resources/1.3.0/plexus-resources-1.3.0.jar
install -Dm644 %{SOURCE609} target/repository/org/codehaus/plexus/plexus-resources/1.3.0/plexus-resources-1.3.0.pom
install -Dm644 %{SOURCE610} target/repository/org/codehaus/plexus/plexus-sec-dispatcher/2.0/plexus-sec-dispatcher-2.0.jar
install -Dm644 %{SOURCE611} target/repository/org/codehaus/plexus/plexus-sec-dispatcher/2.0/plexus-sec-dispatcher-2.0.pom
install -Dm644 %{SOURCE612} target/repository/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.jar
install -Dm644 %{SOURCE613} target/repository/org/codehaus/plexus/plexus-testing/2.1.0/plexus-testing-2.1.0.pom
install -Dm644 %{SOURCE614} target/repository/org/codehaus/plexus/plexus-utils/1.4.5/plexus-utils-1.4.5.pom
install -Dm644 %{SOURCE615} target/repository/org/tukaani/xz/1.12/xz-1.12.jar
install -Dm644 %{SOURCE616} target/repository/org/tukaani/xz/1.12/xz-1.12.pom
install -Dm644 %{SOURCE617} target/repository/org/xmlunit/xmlunit-core/2.14.0/xmlunit-core-2.14.0.jar
install -Dm644 %{SOURCE618} target/repository/org/xmlunit/xmlunit-core/2.14.0/xmlunit-core-2.14.0.pom
install -Dm644 %{SOURCE619} target/repository/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.jar
install -Dm644 %{SOURCE620} target/repository/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.pom
install -Dm644 %{SOURCE621} target/repository/org/codehaus/plexus/plexus-utils/3.6.0/plexus-utils-3.6.0.jar
install -Dm644 %{SOURCE622} target/repository/org/codehaus/plexus/plexus-utils/3.6.0/plexus-utils-3.6.0.pom
install -Dm644 %{SOURCE623} target/repository/org/xmlunit/xmlunit-matchers/2.14.0/xmlunit-matchers-2.14.0.jar
install -Dm644 %{SOURCE624} target/repository/org/xmlunit/xmlunit-matchers/2.14.0/xmlunit-matchers-2.14.0.pom
install -Dm644 %{SOURCE625} target/repository/org/codehaus/plexus/plexus-utils/4.0.1/plexus-utils-4.0.1.jar
install -Dm644 %{SOURCE626} target/repository/org/codehaus/plexus/plexus-utils/4.0.1/plexus-utils-4.0.1.pom
install -Dm644 %{SOURCE627} target/repository/org/codehaus/plexus/plexus-utils/4.0.2/plexus-utils-4.0.2.jar
install -Dm644 %{SOURCE628} target/repository/org/codehaus/plexus/plexus-utils/4.0.2/plexus-utils-4.0.2.pom
install -Dm644 %{SOURCE629} target/repository/org/xmlunit/xmlunit-parent/2.14.0/xmlunit-parent-2.14.0.pom
install -Dm644 %{SOURCE630} target/repository/org/yaml/snakeyaml/2.6/snakeyaml-2.6.jar
install -Dm644 %{SOURCE631} target/repository/org/codehaus/plexus/plexus-velocity/2.2.0/plexus-velocity-2.2.0.jar
install -Dm644 %{SOURCE632} target/repository/org/codehaus/plexus/plexus-velocity/2.2.0/plexus-velocity-2.2.0.pom
install -Dm644 %{SOURCE633} target/repository/org/codehaus/plexus/plexus-xml/3.0.1/plexus-xml-3.0.1.jar
install -Dm644 %{SOURCE634} target/repository/org/codehaus/plexus/plexus-xml/3.0.1/plexus-xml-3.0.1.pom
install -Dm644 %{SOURCE635} target/repository/org/yaml/snakeyaml/2.6/snakeyaml-2.6.pom
install -Dm644 %{SOURCE636} target/repository/software/amazon/awssdk/aws-sdk-java-pom/2.33.4/aws-sdk-java-pom-2.33.4.pom
install -Dm644 %{SOURCE637} target/repository/software/amazon/awssdk/bom/2.33.4/bom-2.33.4.pom
install -Dm644 %{SOURCE638} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/1.0.0/org.eclipse.sisu.inject-1.0.0.jar
install -Dm644 %{SOURCE639} target/repository/org/eclipse/sisu/org.eclipse.sisu.inject/1.0.0/org.eclipse.sisu.inject-1.0.0.pom
install -Dm644 %{SOURCE640} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M4/org.eclipse.sisu.plexus-0.9.0.M4.jar
install -Dm644 %{SOURCE641} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/0.9.0.M4/org.eclipse.sisu.plexus-0.9.0.M4.pom
install -Dm644 %{SOURCE642} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/1.0.0/org.eclipse.sisu.plexus-1.0.0.jar
install -Dm644 %{SOURCE643} target/repository/org/eclipse/sisu/org.eclipse.sisu.plexus/1.0.0/org.eclipse.sisu.plexus-1.0.0.pom
install -Dm644 %{SOURCE644} target/repository/org/eclipse/sisu/sisu-inject/0.9.0.M4/sisu-inject-0.9.0.M4.pom
install -Dm644 %{SOURCE645} target/repository/org/eclipse/sisu/sisu-inject/1.0.0/sisu-inject-1.0.0.pom
install -Dm644 %{SOURCE646} target/repository/org/hamcrest/hamcrest/3.0/hamcrest-3.0.jar
install -Dm644 %{SOURCE647} target/repository/org/hamcrest/hamcrest/3.0/hamcrest-3.0.pom
install -Dm644 %{SOURCE648} target/repository/org/jdom/jdom2/2.0.6.1/jdom2-2.0.6.1.jar
install -Dm644 %{SOURCE649} target/repository/org/jdom/jdom2/2.0.6.1/jdom2-2.0.6.1.pom
install -Dm644 %{SOURCE650} target/repository/org/jspecify/jspecify/1.0.0/jspecify-1.0.0.jar
install -Dm644 %{SOURCE651} target/repository/org/jspecify/jspecify/1.0.0/jspecify-1.0.0.pom
install -Dm644 %{SOURCE652} target/repository/org/junit/junit-bom/5.10.0/junit-bom-5.10.0.pom
install -Dm644 %{SOURCE653} target/repository/org/junit/junit-bom/5.10.1/junit-bom-5.10.1.pom
install -Dm644 %{SOURCE654} target/repository/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
install -Dm644 %{SOURCE655} target/repository/org/junit/junit-bom/5.10.3/junit-bom-5.10.3.pom
install -Dm644 %{SOURCE656} target/repository/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom
install -Dm644 %{SOURCE657} target/repository/org/junit/junit-bom/5.11.1/junit-bom-5.11.1.pom
install -Dm644 %{SOURCE658} target/repository/org/junit/junit-bom/5.11.2/junit-bom-5.11.2.pom
install -Dm644 %{SOURCE659} target/repository/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom
install -Dm644 %{SOURCE660} target/repository/org/junit/junit-bom/5.12.1/junit-bom-5.12.1.pom
install -Dm644 %{SOURCE661} target/repository/org/junit/junit-bom/5.12.2/junit-bom-5.12.2.pom
install -Dm644 %{SOURCE662} target/repository/org/junit/junit-bom/5.13.1/junit-bom-5.13.1.pom
install -Dm644 %{SOURCE663} target/repository/org/junit/junit-bom/5.13.4/junit-bom-5.13.4.pom
install -Dm644 %{SOURCE664} target/repository/org/junit/junit-bom/5.14.1/junit-bom-5.14.1.pom
install -Dm644 %{SOURCE665} target/repository/org/junit/junit-bom/5.14.2/junit-bom-5.14.2.pom
install -Dm644 %{SOURCE666} target/repository/org/junit/junit-bom/5.14.3/junit-bom-5.14.3.pom
install -Dm644 %{SOURCE667} target/repository/org/junit/junit-bom/5.14.4/junit-bom-5.14.4.pom
install -Dm644 %{SOURCE668} target/repository/org/junit/junit-bom/5.7.2/junit-bom-5.7.2.pom
install -Dm644 %{SOURCE669} target/repository/org/junit/junit-bom/5.8.0-M1/junit-bom-5.8.0-M1.pom
install -Dm644 %{SOURCE670} target/repository/org/junit/junit-bom/5.9.3/junit-bom-5.9.3.pom
install -Dm644 %{SOURCE671} target/repository/org/junit/jupiter/junit-jupiter-api/5.14.4/junit-jupiter-api-5.14.4.jar
install -Dm644 %{SOURCE672} target/repository/org/junit/jupiter/junit-jupiter-api/5.14.4/junit-jupiter-api-5.14.4.pom
install -Dm644 %{SOURCE673} target/repository/org/junit/jupiter/junit-jupiter-engine/5.14.4/junit-jupiter-engine-5.14.4.jar
install -Dm644 %{SOURCE674} target/repository/org/junit/jupiter/junit-jupiter-engine/5.14.4/junit-jupiter-engine-5.14.4.pom
install -Dm644 %{SOURCE675} target/repository/org/junit/platform/junit-platform-commons/1.14.4/junit-platform-commons-1.14.4.jar
install -Dm644 %{SOURCE676} target/repository/org/junit/platform/junit-platform-commons/1.14.4/junit-platform-commons-1.14.4.pom
install -Dm644 %{SOURCE677} target/repository/org/junit/platform/junit-platform-engine/1.14.4/junit-platform-engine-1.14.4.jar
install -Dm644 %{SOURCE678} target/repository/org/junit/platform/junit-platform-engine/1.14.4/junit-platform-engine-1.14.4.pom
install -Dm644 %{SOURCE679} target/repository/org/junit/platform/junit-platform-launcher/1.14.4/junit-platform-launcher-1.14.4.jar
install -Dm644 %{SOURCE680} target/repository/org/junit/platform/junit-platform-launcher/1.14.4/junit-platform-launcher-1.14.4.pom
install -Dm644 %{SOURCE681} target/repository/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.jar
install -Dm644 %{SOURCE682} target/repository/org/mockito/mockito-core/4.11.0/mockito-core-4.11.0.pom
install -Dm644 %{SOURCE683} target/repository/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.jar
install -Dm644 %{SOURCE684} target/repository/org/objenesis/objenesis/3.0.1/objenesis-3.0.1.pom
install -Dm644 %{SOURCE685} target/repository/org/objenesis/objenesis/3.3/objenesis-3.3.jar
install -Dm644 %{SOURCE686} target/repository/org/objenesis/objenesis/3.3/objenesis-3.3.pom
install -Dm644 %{SOURCE687} target/repository/org/objenesis/objenesis-parent/3.0.1/objenesis-parent-3.0.1.pom
install -Dm644 %{SOURCE688} target/repository/org/objenesis/objenesis-parent/3.3/objenesis-parent-3.3.pom
install -Dm644 %{SOURCE689} target/repository/org/opentest4j/opentest4j/1.3.0/opentest4j-1.3.0.jar
install -Dm644 %{SOURCE690} target/repository/org/opentest4j/opentest4j/1.3.0/opentest4j-1.3.0.pom
install -Dm644 %{SOURCE691} target/repository/org/ow2/asm/asm/9.6/asm-9.6.jar
install -Dm644 %{SOURCE692} target/repository/org/ow2/asm/asm/9.6/asm-9.6.pom
install -Dm644 %{SOURCE693} target/repository/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
install -Dm644 %{SOURCE694} target/repository/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.jar
install -Dm644 %{SOURCE695} target/repository/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.pom
install -Dm644 %{SOURCE696} target/repository/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.pom
install -Dm644 %{SOURCE697} target/repository/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar
install -Dm644 %{SOURCE698} target/repository/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.pom
install -Dm644 %{SOURCE699} target/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.pom
install -Dm644 %{SOURCE700} target/repository/org/slf4j/slf4j-nop/1.7.36/slf4j-nop-1.7.36.jar
install -Dm644 %{SOURCE701} target/repository/org/slf4j/slf4j-nop/1.7.36/slf4j-nop-1.7.36.pom
install -Dm644 %{SOURCE702} target/repository/org/slf4j/slf4j-parent/1.7.30/slf4j-parent-1.7.30.pom
install -Dm644 %{SOURCE703} target/repository/org/slf4j/slf4j-parent/1.7.36/slf4j-parent-1.7.36.pom
install -Dm644 %{SOURCE704} target/repository/org/slf4j/slf4j-parent/1.7.5/slf4j-parent-1.7.5.pom
install -Dm644 %{SOURCE705} target/repository/org/sonatype/forge/forge-parent/5/forge-parent-5.pom
install -Dm644 %{SOURCE706} target/repository/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
install -Dm644 %{SOURCE707} target/repository/org/sonatype/oss/oss-parent/9/oss-parent-9.pom
install -Dm644 %{SOURCE708} target/repository/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.jar
install -Dm644 %{SOURCE709} target/repository/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.pom
install -Dm644 %{SOURCE710} target/repository/org/sonatype/spice/spice-parent/15/spice-parent-15.pom
install -Dm644 %{SOURCE711} target/repository/org/tukaani/xz/1.10/xz-1.10.jar
install -Dm644 %{SOURCE712} target/repository/org/tukaani/xz/1.10/xz-1.10.pom
install -Dm644 %{SOURCE713} target/repository/org/tukaani/xz/1.11/xz-1.11.jar
install -Dm644 %{SOURCE714} target/repository/org/tukaani/xz/1.11/xz-1.11.pom
install -Dm644 %{SOURCE715} target/repository/org/tukaani/xz/1.9/xz-1.9.jar
install -Dm644 %{SOURCE716} target/repository/org/tukaani/xz/1.9/xz-1.9.pom
%if %{with bootstrap}
mkdir -p target/bootstrap
tar -xf %{SOURCE1} -C target/bootstrap --strip-components=1
%endif

%build
# Resolve the selected JDK independently of this noarch package's libdir.
export JAVA_HOME="$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")"
export MAVEN_SKIP_RC=1
unset MAVEN_ARGS MAVEN_OPTS MAVEN_DEBUG_OPTS MAVEN_BASEDIR MAVEN_CONFIG
%if %{with bootstrap}
MAVEN="$PWD/target/bootstrap/bin/mvn"
%else
MAVEN=mvn
%endif
# Use upstream defaults instead of the builder's user or system configuration.
"$MAVEN" --batch-mode --offline --no-transfer-progress \
    --settings apache-maven/src/conf/settings.xml \
    --global-settings apache-maven/src/conf/settings.xml \
    --toolchains apache-maven/src/conf/toolchains.xml \
    --global-toolchains apache-maven/src/conf/toolchains.xml \
    -Dmaven.repo.local="$PWD/target/repository" \
    -DbuildNumber=openRuyi -DskipTests package
mkdir -p target/maven-dist
tar -xf apache-maven/target/apache-maven-%{version}-bin.tar.gz \
    -C target/maven-dist --strip-components=1
rm -f target/maven-dist/bin/*.cmd

%install
install -d %{buildroot}%{maven_home} %{buildroot}%{_bindir}
cp -a target/maven-dist/bin target/maven-dist/boot target/maven-dist/lib %{buildroot}%{maven_home}/
install -d %{buildroot}%{_sysconfdir}/maven
cp -a target/maven-dist/conf/. %{buildroot}%{_sysconfdir}/maven/
mv %{buildroot}%{maven_home}/bin/m2.conf %{buildroot}%{_sysconfdir}/maven/
ln -s ../../..%{_sysconfdir}/maven %{buildroot}%{maven_home}/conf
ln -s ../../../..%{_sysconfdir}/maven/m2.conf %{buildroot}%{maven_home}/bin/m2.conf
for command in mvn mvnDebug mvnyjp; do
    ln -sr "%{buildroot}%{maven_home}/bin/$command" "%{buildroot}%{_bindir}/$command"
done
%fdupes %{buildroot}%{maven_home}

%check
export JAVA_HOME="$(dirname "$(dirname "$(readlink -f %{_bindir}/javac)")")"
export MAVEN_SKIP_RC=1
unset MAVEN_ARGS MAVEN_OPTS MAVEN_DEBUG_OPTS MAVEN_BASEDIR MAVEN_CONFIG
# Run the upstream unit tests with Maven built above, still fully offline.
./target/maven-dist/bin/mvn --batch-mode --offline --no-transfer-progress \
    --settings apache-maven/src/conf/settings.xml \
    --global-settings apache-maven/src/conf/settings.xml \
    --toolchains apache-maven/src/conf/toolchains.xml \
    --global-toolchains apache-maven/src/conf/toolchains.xml \
    -Dmaven.repo.local="$PWD/target/repository" \
    -DbuildNumber=openRuyi test
# Exercise the packaged launcher through a directory symlink such as /bin.
ln -sfn "%{buildroot}%{_bindir}" target/merged-bin
for launcher in "%{buildroot}%{_bindir}/mvn" ./target/merged-bin/mvn; do
    "$launcher" --version > maven-version.txt
    grep -F 'Apache Maven %{version}' maven-version.txt
done

# Keep the noarch claim valid when updating the upstream distribution.
for jar in %{buildroot}%{maven_home}/boot/*.jar %{buildroot}%{maven_home}/lib/*.jar; do
    unzip -t "$jar" > /dev/null
    unzip -Z1 "$jar" > jar-contents.txt
    if grep -E '\.(so([.][0-9]+)*|dll|dylib|jnilib|exe)$' jar-contents.txt; then
        echo "Unexpected native binary in $jar" >&2
        exit 1
    fi
done

%files
%license target/maven-dist/LICENSE target/maven-dist/NOTICE
%doc target/maven-dist/README.txt
%{_bindir}/mvn
%{_bindir}/mvnDebug
%{_bindir}/mvnyjp
%dir %{_sysconfdir}/maven
%dir %{_sysconfdir}/maven/logging
%config(noreplace) %{_sysconfdir}/maven/m2.conf
%config(noreplace) %{_sysconfdir}/maven/settings.xml
%config(noreplace) %{_sysconfdir}/maven/toolchains.xml
%config(noreplace) %{_sysconfdir}/maven/logging/simplelogger.properties
%dir %{maven_home}
%{maven_home}/bin
%dir %{maven_home}/boot
%{maven_home}/boot/*.jar
%license %{maven_home}/boot/*.license
%{maven_home}/conf
%dir %{maven_home}/lib
%{maven_home}/lib/*.jar
%license %{maven_home}/lib/*.license
%dir %{maven_home}/lib/ext
%dir %{maven_home}/lib/ext/hazelcast
%dir %{maven_home}/lib/ext/redisson
%doc %{maven_home}/lib/ext/README.txt
%doc %{maven_home}/lib/ext/hazelcast/README.txt
%doc %{maven_home}/lib/ext/redisson/README.txt

%changelog
%autochangelog
