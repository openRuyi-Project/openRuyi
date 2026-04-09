# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           vid.stab
Version:        1.1.1
Release:        %autorelease
Summary:        Video stabilization library
License:        GPL-2.0-or-later
URL:            https://github.com/georgmartius/vid.stab
#!RemoteAsset
Source:         https://github.com/georgmartius/vid.stab/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Vidstab is a video stabilization library which can be plugged-in with Ffmpeg
and Transcode. This package contains the shared library.

%package        devel
Summary:        Development files for vid.stab
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the development files (library and header files) for
developing applications that use vid.stab.

%prep -a
sed -i 's|-DUSE_SSE2 -msse2||' tests/CMakeLists.txt
sed -i 's|-Wall -O0|-Wall -O|' tests/CMakeLists.txt
sed -i 's|return units_failed==0;|return units_failed>0;|' tests/testframework.c

%files
%doc README.md
%license LICENSE
%{_libdir}/libvidstab.so.*

%files devel
%{_includedir}/vid.stab/
%{_libdir}/libvidstab.so
%{_libdir}/pkgconfig/vidstab.pc

%changelog
%autochangelog
