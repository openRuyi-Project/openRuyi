# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global majorver        21
%global minorver        0
%global securityver     11
%global buildver        10
%global newjavaver      %{majorver}.%{minorver}.%{securityver}
%global _jvmdir         %_libdir/jvm

%bcond bootstrap        1

Name:           java-21-openjdk
Version:        %{newjavaver}.%{buildver}
Release:        %autorelease
Summary:        OpenJDK 21 Runtime Environment
License:        GPL-2.0-with-classpath-exception
URL:            https://openjdk.org
VCS:            git:https://github.com/openjdk/jdk21u
#!RemoteAsset:  sha256:18edf62aa95c99325725475c0ad5621d8de61f4c84fdb8d2b7efd015a6de8e42
Source0:        https://github.com/openjdk/jdk%{majorver}u/archive/refs/tags/jdk-%{newjavaver}+%{buildver}.tar.gz
%if %{with bootstrap}
#!RemoteAsset:  sha256:8171d95189e675e297b5cb96c7ac6247ab4e9f48da82b13f491fc46ef5d97836
Source1:        https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.8%2B9/OpenJDK21U-jdk_riscv64_linux_hotspot_21.0.8_9.tar.gz
#!RemoteAsset:  sha256:f2dc5418092c43003db8f9005c4a286e1c0104fea96ccdd49e8ebd037cac9219
Source2:        https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.8%2B9/OpenJDK21U-jdk_x64_linux_hotspot_21.0.8_9.tar.gz
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  zip
BuildRequires:  pkgconfig
%if %{without bootstrap}
BuildRequires:  java-21-openjdk
%endif
Requires(post): update-alternatives
Requires(preun): update-alternatives

Provides:       java-%{majorver}-openjdk-devel = %{version}-%{release}
Provides:       java-%{majorver}-openjdk-headless = %{version}-%{release}

%description
The OpenJDK 21 runtime environment.

%prep
%autosetup -p1 -n jdk21u-jdk-%{newjavaver}-%{buildver}

%build
%if %{with bootstrap}
%ifarch riscv64
tar -xf %{SOURCE1} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-21.0.8+9
%endif
%ifarch x86_64
tar -xf %{SOURCE2} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-21.0.8+9
%endif
%else
BOOTJDKPATH=%{_jvmdir}/java-21-openjdk
%endif

ARCH=$(uname -m)
echo $BOOTJDKPATH

mkdir -p build-release
pushd build-release
bash ../configure \
    --with-version-build=%{buildver} \
    --with-version-pre= \
    --with-version-opt= \
    --with-boot-jdk=$BOOTJDKPATH \
    --with-debug-level=release \
    --with-native-debug-symbols=internal \
    --with-vendor-version-string=openRuyi \
    --with-vendor-name="%{_vendor_name}" \
    --with-vendor-url="%{_vendor_url}" \
    --with-vendor-bug-url="%{_vendor_bug_url}" \
    --enable-unlimited-crypto \
    --disable-warnings-as-errors
make images
popd

%install -p
mkdir -p %{buildroot}%{_jvmdir}
cp -a build-release/images/jdk %{buildroot}%{_jvmdir}/java-21-openjdk

%post
alternatives \
  --install %{_bindir}/java java %{_jvmdir}/java-21-openjdk/bin/java 21 \
  --slave %{_bindir}/javac javac %{_jvmdir}/java-21-openjdk/bin/javac \
  --slave %{_bindir}/jlink jlink %{_jvmdir}/java-21-openjdk/bin/jlink \
  --slave %{_bindir}/jmod jmod %{_jvmdir}/java-21-openjdk/bin/jmod \
  --slave %{_bindir}/jar jar %{_jvmdir}/java-21-openjdk/bin/jar \
  --slave %{_bindir}/jarsigner jarsigner %{_jvmdir}/java-21-openjdk/bin/jarsigner \
  --slave %{_bindir}/javadoc javadoc %{_jvmdir}/java-21-openjdk/bin/javadoc \
  --slave %{_bindir}/javap javap %{_jvmdir}/java-21-openjdk/bin/javap \
  --slave %{_bindir}/jcmd jcmd %{_jvmdir}/java-21-openjdk/bin/jcmd \
  --slave %{_bindir}/jconsole jconsole %{_jvmdir}/java-21-openjdk/bin/jconsole \
  --slave %{_bindir}/jdb jdb %{_jvmdir}/java-21-openjdk/bin/jdb \
  --slave %{_bindir}/jdeps jdeps %{_jvmdir}/java-21-openjdk/bin/jdeps \
  --slave %{_bindir}/jdeprscan jdeprscan %{_jvmdir}/java-21-openjdk/bin/jdeprscan \
  --slave %{_bindir}/jfr jfr %{_jvmdir}/java-21-openjdk/bin/jfr \
  --slave %{_bindir}/jimage jimage %{_jvmdir}/java-21-openjdk/bin/jimage \
  --slave %{_bindir}/jinfo jinfo %{_jvmdir}/java-21-openjdk/bin/jinfo \
  --slave %{_bindir}/jmap jmap %{_jvmdir}/java-21-openjdk/bin/jmap \
  --slave %{_bindir}/jps jps %{_jvmdir}/java-21-openjdk/bin/jps \
  --slave %{_bindir}/jpackage jpackage %{_jvmdir}/java-21-openjdk/bin/jpackage \
  --slave %{_bindir}/jrunscript jrunscript %{_jvmdir}/java-21-openjdk/bin/jrunscript \
  --slave %{_bindir}/jshell jshell %{_jvmdir}/java-21-openjdk/bin/jshell \
  --slave %{_bindir}/jstack jstack %{_jvmdir}/java-21-openjdk/bin/jstack \
  --slave %{_bindir}/jstat jstat %{_jvmdir}/java-21-openjdk/bin/jstat \
  --slave %{_bindir}/jstatd jstatd %{_jvmdir}/java-21-openjdk/bin/jstatd \
  --slave %{_bindir}/jwebserver jwebserver %{_jvmdir}/java-21-openjdk/bin/jwebserver \
  --slave %{_bindir}/serialver serialver %{_jvmdir}/java-21-openjdk/bin/serialver

%postun
alternatives --remove java %{_jvmdir}/java-21-openjdk/bin/java

%files
%license LICENSE
%doc README.md
%{_jvmdir}/java-21-openjdk

%changelog
%autochangelog
