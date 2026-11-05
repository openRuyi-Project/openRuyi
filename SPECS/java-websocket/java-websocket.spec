# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           java-websocket
Version:        1.6.0
Release:        %autorelease
Summary:        Java WebSocket client and server library
License:        MIT AND LicenseRef-openRuyi-Public-Domain
URL:            https://github.com/TooTallNate/Java-WebSocket
#!RemoteAsset:  sha256:f3ce29efde338707241d47ab4784b19a1e3658bfa0564b5bc5f80c27e5118728
Source0:        https://github.com/TooTallNate/Java-WebSocket/archive/refs/tags/v%{version}.tar.gz#/Java-WebSocket-%{version}.tar.gz
# LibreOffice uses Ant and java.util.logging for its Java UNO WebSocket client.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/external/java_websocket/UnpackedTarball_java_websocket.mk
#!RemoteAsset:  sha256:fb20f0a2e9bf29208a55d457d3aa4c2cca70927991713c204c5192966e4b8c8a
Source1:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/ant-build.patch#/2000-ant-build.patch
#!RemoteAsset:  sha256:5d8c9cddbeb68882955e830abfedff302943646be703b3460215ebdd95d7417b
Source2:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/no-slf4j.patch#/2001-no-slf4j.patch
#!RemoteAsset:  sha256:97ea673c4ff21831893336cd20a3a40a82c2641aa834286bbd6e6ab524e4cdbe
Source3:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0001-cid-1546192-SIC-Inner-class-could-be-made-static.patch#/2002-cid-1546192-SIC-Inner-class-could-be-made-static.patch
#!RemoteAsset:  sha256:882f0875e243e5bb8fef2d0a23f4944646d56e7b49f576bbd5354279f13ac03c
Source4:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0001-cid-1545614-UR-Uninitialized-read-of-field-in-constr.patch#/2003-cid-1545614-UR-Uninitialized-read-of-field-in-constr.patch
#!RemoteAsset:  sha256:f0192480b1b5c860f85e2def7fdaa849ce0839ce57ca9511ab02dc311ed27ef5
Source5:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0002-cid-1545284-UR-Uninitialized-read-of-field-in-constr.patch#/2004-cid-1545284-UR-Uninitialized-read-of-field-in-constr.patch
#!RemoteAsset:  sha256:eae4430bfca0415a0440a9b4fab742217e758a630563909b06d09f11c0b95cb8
Source6:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0001-cid-1546292-DLS-Dead-local-store.patch#/2005-cid-1546292-DLS-Dead-local-store.patch
#!RemoteAsset:  sha256:46369ada17bc220ee8ac2ab20757799fa658bb9ac5abe8bf1ca139a967ab9d1a
Source7:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0001-cid-1545227-Dm-Dubious-method-used.patch#/2006-cid-1545227-Dm-Dubious-method-used.patch
#!RemoteAsset:  sha256:3a40c4a55805e95367ad36843bebfdbe53aec54c6a72aeff1b8345a00a6fbda1
Source8:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0001-cid-1545515-Dm-Dubious-method-used.patch#/2007-cid-1545515-Dm-Dubious-method-used.patch
#!RemoteAsset:  sha256:1ed7fe04500b213a6ed8050a71f9106f723aa517fd970b3d4cc8bfefd5b602a6
Source9:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0001-cid-1546264-Dm-Dubious-method-used.patch#/2008-cid-1546264-Dm-Dubious-method-used.patch
#!RemoteAsset:  sha256:1433f8047b9e4955906fc8ee766f1e89939c156d60cf2368e2aa11a3001d9ebe
Source10:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0001-cid-1546341-Resource-leak-on-an-exceptional-path.patch#/2009-cid-1546341-Resource-leak-on-an-exceptional-path.patch
#!RemoteAsset:  sha256:648a26cb35a8e9705f1b81601f40d82f4ac3b0a057847969cfa597f29eb12fdb
Source11:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0001-cid-1545249-Bad-bit-shift-operation.patch#/2010-cid-1545249-Bad-bit-shift-operation.patch
#!RemoteAsset:  sha256:446d60b3d2963a6592a3a63fd87b5436284d842394b2c3bdbb9b0274cb71646d
Source12:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/java_websocket/patches/0001-cid-1546344-Dm-Dubious-method-used.patch#/2011-cid-1546344-Dm-Dubious-method-used.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  slf4j-jdk14
BuildRequires:  slf4j
BuildRequires:  junit4
BuildRequires:  java-25-openjdk-devel
Requires:       java-25-openjdk-headless

%patchlist
%{SOURCE1}
%{SOURCE2}
%{SOURCE3}
%{SOURCE4}
%{SOURCE5}
%{SOURCE6}
%{SOURCE7}
%{SOURCE8}
%{SOURCE9}
%{SOURCE10}
%{SOURCE11}
%{SOURCE12}

%description
Java-WebSocket implements WebSocket clients and servers with support for
binary frames. LibreOffice uses it for remote UNO connections.

%prep
%autosetup -p1 -n Java-WebSocket-%{version}

%build
ant -nouserlib -f build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 jar

%install
install -Dpm644 dist/java_websocket.jar %{buildroot}%{_datadir}/java/Java-WebSocket/Java-WebSocket.jar

%check
# Run the upstream aggregate suite, including local WebSocket client/server exchanges.
mkdir classes-test
find src/test/java -name '*.java' | sort > test.sources
cp=dist/java_websocket.jar:%{_datadir}/java/junit4.jar:%{_datadir}/java/slf4j-api.jar:%{_datadir}/java/slf4j-jdk14.jar
javac --release 8 -encoding UTF-8 -cp "$cp" -d classes-test @test.sources
java -cp "classes-test:src/test/resources:$cp" org.junit.runner.JUnitCore org.java_websocket.AllTests

%files
%doc README.markdown
%license LICENSE
%{_datadir}/java/Java-WebSocket/

%changelog
%autochangelog
