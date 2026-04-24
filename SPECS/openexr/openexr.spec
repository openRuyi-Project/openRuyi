# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openexr
Version:        3.4.10
Release:        %autorelease
Summary:        Provides the specification and reference implementation of the EXR file format
License:        BSD-3-Clause
URL:            https://www.openexr.com/
VCS:            git:https://github.com/AcademySoftwareFoundation/openexr
#!RemoteAsset:  sha256:b61ae2d0fa4872c5f5fc45618f107945df37c0eba4853263091b949c513d3319
Source0:        https://github.com/AcademySoftwareFoundation/openexr/archive/v%{version}/openexr-%{version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Imath)
BuildRequires:  pkgconfig(zlib)

%description
OpenEXR is an open-source high-dynamic-range floating-point image file format
for high-quality image processing and storage. This package contains the binaries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for OpenEXR.

%files
%doc CHANGES.md CONTRIBUTING.md GOVERNANCE.md SECURITY.md CODE_OF_CONDUCT.md CONTRIBUTORS.md README.md
%license LICENSE.md
%{_bindir}/exr2aces
%{_bindir}/exrenvmap
%{_bindir}/exrheader
%{_bindir}/exrinfo
%{_bindir}/exrmakepreview
%{_bindir}/exrmaketiled
%{_bindir}/exrmanifest
%{_bindir}/exrmultipart
%{_bindir}/exrmultiview
%{_bindir}/exrstdattr
%{_bindir}/exrmetrics
%{_libdir}/libIex*.so.*
%{_libdir}/libIlmThread*.so.*
%{_libdir}/libOpenEXR*.so.*

%files devel
%{_docdir}/OpenEXR/
%{_includedir}/OpenEXR/
%{_libdir}/libIex*.so
%{_libdir}/libIlmThread*.so
%{_libdir}/libOpenEXR*.so
%{_libdir}/cmake/OpenEXR/
%{_libdir}/pkgconfig/OpenEXR.pc

%changelog
%autochangelog
