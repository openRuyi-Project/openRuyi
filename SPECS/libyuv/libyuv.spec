# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global git_commit 94417b9d213364905ce849c25719b819b8dbbaaa

Name:           libyuv
Summary:        YUV conversion and scaling functionality library
Version:        0+git20260126.94417b9
Release:        %autorelease
License:        BSD-3-Clause
URL:            https://chromium.googlesource.com/libyuv/libyuv
VCS:            git:https://chromium.googlesource.com/libyuv/libyuv
#!RemoteAsset:  git+https://chromium.googlesource.com/libyuv/libyuv#%{git_commit}
#!CreateArchive
Source:         %{name}-%{version}.tar.gz
BuildSystem:    cmake

Patch:          0001-fix-install-dir.patch

BuildOption(conf):  -DTEST=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtest)

%description
This is an open source project that includes YUV conversion and scaling
functionality. Converts all webcam formats to YUV (I420). Convert YUV to
formats for rendering/effects. Rotate by 90 degrees to adjust for mobile
devices in portrait mode.

%package        devel
Summary:        The development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and development libraries for libyuv.

%prep -a

cat > %{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: %{name}
Description: %{summary}
Version: %{version}
Libs: -lyuv
EOF

%install -a
find %{buildroot} -type f -name "*.a" -delete

install -p -D -m 0644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%files
%license LICENSE
%doc README.md

%files devel
%{_includedir}/libyuv
%{_includedir}/libyuv.h
%{_libdir}/libyuv.so
%{_libdir}/pkgconfig/libyuv.pc

%changelog
%autochangelog
