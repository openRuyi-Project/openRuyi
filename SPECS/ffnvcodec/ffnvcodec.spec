# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ffnvcodec
Version:        13.0.19.0
Release:        %autorelease
Summary:        FFmpeg version of NVIDIA codec API headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
#!RemoteAsset
Source:         https://github.com/FFmpeg/nv-codec-headers/archive/refs/tags/n%{version}.tar.gz
BuildSystem:    autotools

BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  LIBDIR=%{_lib}

BuildRequires:  make
BuildRequires:  pkgconfig

%description
This metapackage requires the development files for the FFmpeg NVIDIA
codec API headers.

%package        devel
Summary:        FFmpeg version of NVIDIA codec API headers

%description    devel
This package contains the header files and pkg-config file required for
FFmpeg to interface with NVIDIA codec APIs.

# No configure.
%conf

%check
# No tests here.

%files devel
%{_includedir}/ffnvcodec
%{_libdir}/pkgconfig/ffnvcodec.pc

%changelog
%autochangelog
