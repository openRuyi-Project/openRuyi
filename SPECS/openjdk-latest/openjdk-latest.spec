# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global majorver        25
%global minorver        0
%global securityver     0
%global buildver        36
%global newjavaver      %{majorver}.%{minorver}.%{securityver}
%global _jvmdir         %_libdir/jvm

%bcond bootstrap        1

Name:           java-latest-openjdk
Version:        %{newjavaver}.%{buildver}
Release:        %autorelease
Summary:        OpenJDK latest Runtime Environment
License:        GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.org
VCS:            git:https://github.com/openjdk/jdk25u
#!RemoteAsset
Source0:        https://github.com/openjdk/jdk%{majorver}u/archive/refs/tags/jdk-%{majorver}+%{buildver}.tar.gz
%if %{with bootstrap}
#!RemoteAsset
Source1:        https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25%2B36/OpenJDK25U-jdk_riscv64_linux_hotspot_25_36.tar.gz
#!RemoteAsset
Source2:        https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25%2B36/OpenJDK25U-jdk_x64_linux_hotspot_25_36.tar.gz
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
BuildRequires:  java-latest-openjdk
%endif
Requires(post): update-alternatives
Requires(preun): update-alternatives

Provides:       java-openjdk-headless = %{version}-%{release}
Provides:       java-openjdk-devel = %{version}-%{release}
Provides:       java-latest-openjdk-devel = %{version}-%{release}
Provides:       java-latest-openjdk-headless = %{version}-%{release}

%description
The OpenJDK latest runtime environment.

%prep
%autosetup -p1 -n jdk%{majorver}u-jdk-%{majorver}-%{buildver}

%build
%if %{with bootstrap}
%ifarch riscv64
tar -xf %{SOURCE1} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-25+36
%endif
%ifarch x86_64
tar -xf %{SOURCE2} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-25+36
%endif
%else
BOOTJDKPATH=%{_jvmdir}/java-latest-openjdk
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
cp -a build-release/images/jdk %{buildroot}%{_jvmdir}/java-latest-openjdk

%post
alternatives \
  --install %{_bindir}/java java %{_jvmdir}/java-latest-openjdk/bin/java 9999 \
  --slave %{_bindir}/javac javac %{_jvmdir}/java-latest-openjdk/bin/javac \
  --slave %{_bindir}/jlink jlink %{_jvmdir}/java-latest-openjdk/bin/jlink \
  --slave %{_bindir}/jmod jmod %{_jvmdir}/java-latest-openjdk/bin/jmod \
  --slave %{_bindir}/jar jar %{_jvmdir}/java-latest-openjdk/bin/jar \
  --slave %{_bindir}/jarsigner jarsigner %{_jvmdir}/java-latest-openjdk/bin/jarsigner \
  --slave %{_bindir}/javadoc javadoc %{_jvmdir}/java-latest-openjdk/bin/javadoc \
  --slave %{_bindir}/javap javap %{_jvmdir}/java-latest-openjdk/bin/javap \
  --slave %{_bindir}/jcmd jcmd %{_jvmdir}/java-latest-openjdk/bin/jcmd \
  --slave %{_bindir}/jconsole jconsole %{_jvmdir}/java-latest-openjdk/bin/jconsole \
  --slave %{_bindir}/jdb jdb %{_jvmdir}/java-latest-openjdk/bin/jdb \
  --slave %{_bindir}/jdeps jdeps %{_jvmdir}/java-latest-openjdk/bin/jdeps \
  --slave %{_bindir}/jdeprscan jdeprscan %{_jvmdir}/java-latest-openjdk/bin/jdeprscan \
  --slave %{_bindir}/jfr jfr %{_jvmdir}/java-latest-openjdk/bin/jfr \
  --slave %{_bindir}/jimage jimage %{_jvmdir}/java-latest-openjdk/bin/jimage \
  --slave %{_bindir}/jinfo jinfo %{_jvmdir}/java-latest-openjdk/bin/jinfo \
  --slave %{_bindir}/jmap jmap %{_jvmdir}/java-latest-openjdk/bin/jmap \
  --slave %{_bindir}/jps jps %{_jvmdir}/java-latest-openjdk/bin/jps \
  --slave %{_bindir}/jpackage jpackage %{_jvmdir}/java-latest-openjdk/bin/jpackage \
  --slave %{_bindir}/jrunscript jrunscript %{_jvmdir}/java-latest-openjdk/bin/jrunscript \
  --slave %{_bindir}/jshell jshell %{_jvmdir}/java-latest-openjdk/bin/jshell \
  --slave %{_bindir}/jstack jstack %{_jvmdir}/java-latest-openjdk/bin/jstack \
  --slave %{_bindir}/jstat jstat %{_jvmdir}/java-latest-openjdk/bin/jstat \
  --slave %{_bindir}/jstatd jstatd %{_jvmdir}/java-latest-openjdk/bin/jstatd \
  --slave %{_bindir}/jwebserver jwebserver %{_jvmdir}/java-latest-openjdk/bin/jwebserver \
  --slave %{_bindir}/serialver serialver %{_jvmdir}/java-latest-openjdk/bin/serialver

%postun
alternatives --remove java %{_jvmdir}/java-latest-openjdk/bin/java

%files
%license LICENSE
%doc README.md
%{_jvmdir}/java-latest-openjdk

%changelog
%autochangelog
