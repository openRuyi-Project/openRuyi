# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global majorver        27
%global minorver        0
%global securityver     1
%global extraver        2
%global buildver        1
%global newjavaver      %{majorver}.%{minorver}.%{securityver}.0.%{extraver}
%global _jvmdir         %_libdir/jvm

%bcond bootstrap        1

Name:           java-latest-openjdk
Version:        %{newjavaver}.%{buildver}
Release:        %autorelease
Summary:        OpenJDK latest Runtime Environment
License:        GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.org
VCS:            git:https://github.com/openjdk/jdk27u
#!RemoteAsset:  sha256:2f39e68293e3fd3aad04fb0c5aebc0ee8737e82b348f520bd95ebae00f2142e9
Source0:        https://github.com/openjdk/jdk%{majorver}u/archive/refs/tags/jdk-%{newjavaver}+%{buildver}.tar.gz
%if %{with bootstrap}
#!RemoteAsset:  sha256:270d74d7732adbaa7af4e153154126c144e6000bb736fd0985421f75075555aa
Source1:        https://github.com/adoptium/temurin27-binaries/releases/download/jdk-27%2B35/OpenJDK27U-jdk_riscv64_linux_hotspot_27_35.tar.gz
#!RemoteAsset:  sha256:1cf69a4848ffb728b3b260dfd45206a51566ab571a02a30092271d4c580bccbc
Source2:        https://github.com/adoptium/temurin27-binaries/releases/download/jdk-27%2B35/OpenJDK27U-jdk_x64_linux_hotspot_27_35.tar.gz
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

%patchlist
# Add missing Zbs bset/bclr/binv instructions for RVA23
2000-RISC-V-implement-zbs.patch
# Add missing Zfa fround.d instruction for RVA23
2001-RISC-V-implement-Zfa-whith-fround_d.patch
# Eliminate redundant RVV vset instructions in C2
2002-RISC-V-Make-RVV-vset-explicit-in-C2.patch
2003-RISC-V-Track-RVV-vset-policy-plus-fix-vsetvli-tail-and-mask-agnostic.patch
2004-RISC-V-Remove-redundant-RVV-vset-nodes-in-blocks.patch
2005-RISC-V-Remove-redundant-RVV-vset-nodes-across-blocks.patch
2006-RISC-V-C2-Return-inserted-block-from-PhaseCFG-insert_goto_a.patch
2007-RISC-V-Hoist-loop-invariant-RVV-vset-nodes.patch
2008-RISC-V-Add-tracing-for-RVV-vset-optimization.patch
2009-RISC-V-record-vset-state-for-simple-vector-helper-patterns.patch
# Fix repeated rematerialization of AddPNode in the RISC-V backend
2010-C2-optimized-addp-rematerialize.patch
# Optimize CRC32/CRC32C intrinsics
2011-RISC-V-implement-crc32c-intrinsic.patch
2012-RISC-V-implement-slicing-by-8-crc32.patch
2013-RISC-V-resolve-tail-bug-in-vector-update-crc32.patch
# Optimize DES S-box table layout
2014-SECURITY-change_descrypt.patch

%description
The OpenJDK latest runtime environment.

%prep
%autosetup -p1 -n jdk%{majorver}u-jdk-%{newjavaver}-%{buildver}

%build
%if %{with bootstrap}
%ifarch riscv64
tar -xf %{SOURCE1} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-27+35
%endif
%ifarch x86_64
tar -xf %{SOURCE2} -C %{_tmppath}
BOOTJDKPATH=%{_tmppath}/jdk-27+35
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
    --with-version-extra1=%{extraver} \
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
%ifarch riscv64
  %if "%{openruyi_riscv_arch}" == "-march=rva23u64"
    --with-extra-cxxflags="-march=rva23u64_zifencei" \
  %endif
%endif
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
