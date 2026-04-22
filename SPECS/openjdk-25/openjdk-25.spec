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
%global securityver     3
%global buildver        9
%global newjavaver      %{majorver}.%{minorver}.%{securityver}
%global _jvmdir         %_libdir/jvm

%bcond bootstrap        1

Name:           java-25-openjdk
Version:        %{newjavaver}.%{buildver}
Release:        %autorelease
Summary:        OpenJDK 25 Runtime Environment
License:        GPL-2.0-with-classpath-exception
URL:            https://openjdk.org
VCS:            git:https://github.com/openjdk/jdk25u
#!RemoteAsset:  sha256:33991482d2e08eaa865212239db7815ad627f2449a836e4a4362301fc1893e12
Source0:        https://github.com/openjdk/jdk%{majorver}u/archive/refs/tags/jdk-%{newjavaver}+%{buildver}.tar.gz
%if %{with bootstrap}
#!RemoteAsset:  sha256:3fc35759502b620f010a9cd2b3da8454f8a49a156ceaebb00de1fd8335682d40
Source1:        https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25%2B36/OpenJDK25U-jdk_riscv64_linux_hotspot_25_36.tar.gz
#!RemoteAsset:  sha256:ee04de95ab9da7287d40bd2173076ecc2a6dd662f007bedfc6eb0380c0ef90e8
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
BuildRequires:  java-25-openjdk
%endif
Requires(post): update-alternatives
Requires(preun): update-alternatives

Provides:       java-%{majorver}-openjdk-devel = %{version}-%{release}
Provides:       java-%{majorver}-openjdk-headless = %{version}-%{release}

%description
The OpenJDK 25 runtime environment.

%prep
%autosetup -p1 -n jdk25u-jdk-%{newjavaver}-%{buildver}

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
BOOTJDKPATH=%{_jvmdir}/java-25-openjdk
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
    --with-vendor-name="openRuyi" \
    --with-vendor-url="%{_vendor_url}" \
    --with-vendor-bug-url="%{_vendor_bug_url}" \
    --enable-unlimited-crypto \
    --disable-warnings-as-errors
make images
popd

%install -p
mkdir -p %{buildroot}%{_jvmdir}
cp -a build-release/images/jdk %{buildroot}%{_jvmdir}/java-25-openjdk

%post
alternatives \
  --install %{_bindir}/java java %{_jvmdir}/java-25-openjdk/bin/java 25 \
  --slave %{_bindir}/javac javac %{_jvmdir}/java-25-openjdk/bin/javac \
  --slave %{_bindir}/jlink jlink %{_jvmdir}/java-25-openjdk/bin/jlink \
  --slave %{_bindir}/jmod jmod %{_jvmdir}/java-25-openjdk/bin/jmod \
  --slave %{_bindir}/jar jar %{_jvmdir}/java-25-openjdk/bin/jar \
  --slave %{_bindir}/jarsigner jarsigner %{_jvmdir}/java-25-openjdk/bin/jarsigner \
  --slave %{_bindir}/javadoc javadoc %{_jvmdir}/java-25-openjdk/bin/javadoc \
  --slave %{_bindir}/javap javap %{_jvmdir}/java-25-openjdk/bin/javap \
  --slave %{_bindir}/jcmd jcmd %{_jvmdir}/java-25-openjdk/bin/jcmd \
  --slave %{_bindir}/jconsole jconsole %{_jvmdir}/java-25-openjdk/bin/jconsole \
  --slave %{_bindir}/jdb jdb %{_jvmdir}/java-25-openjdk/bin/jdb \
  --slave %{_bindir}/jdeps jdeps %{_jvmdir}/java-25-openjdk/bin/jdeps \
  --slave %{_bindir}/jdeprscan jdeprscan %{_jvmdir}/java-25-openjdk/bin/jdeprscan \
  --slave %{_bindir}/jfr jfr %{_jvmdir}/java-25-openjdk/bin/jfr \
  --slave %{_bindir}/jimage jimage %{_jvmdir}/java-25-openjdk/bin/jimage \
  --slave %{_bindir}/jinfo jinfo %{_jvmdir}/java-25-openjdk/bin/jinfo \
  --slave %{_bindir}/jmap jmap %{_jvmdir}/java-25-openjdk/bin/jmap \
  --slave %{_bindir}/jps jps %{_jvmdir}/java-25-openjdk/bin/jps \
  --slave %{_bindir}/jpackage jpackage %{_jvmdir}/java-25-openjdk/bin/jpackage \
  --slave %{_bindir}/jrunscript jrunscript %{_jvmdir}/java-25-openjdk/bin/jrunscript \
  --slave %{_bindir}/jshell jshell %{_jvmdir}/java-25-openjdk/bin/jshell \
  --slave %{_bindir}/jstack jstack %{_jvmdir}/java-25-openjdk/bin/jstack \
  --slave %{_bindir}/jstat jstat %{_jvmdir}/java-25-openjdk/bin/jstat \
  --slave %{_bindir}/jstatd jstatd %{_jvmdir}/java-25-openjdk/bin/jstatd \
  --slave %{_bindir}/jwebserver jwebserver %{_jvmdir}/java-25-openjdk/bin/jwebserver \
  --slave %{_bindir}/serialver serialver %{_jvmdir}/java-25-openjdk/bin/serialver

%postun
alternatives --remove java %{_jvmdir}/java-25-openjdk/bin/java

%files
%license LICENSE
%doc README.md
%{_jvmdir}/java-25-openjdk

%changelog
%autochangelog
