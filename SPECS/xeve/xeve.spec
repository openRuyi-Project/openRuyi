# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xeve
Version:        0.5.1
Release:        %autorelease
Summary:        Reference MPEG-5 Part 1 (EVC) encoder
License:        BSD-3-Clause
URL:            https://github.com/mpeg5/xeve
#!RemoteAsset:  sha256:238c95ddd1a63105913d9354045eb329ad9002903a407b5cf1ab16bad324c245
Source:         https://github.com/mpeg5/xeve/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

Patch0:         0001-xeve-fix-build-on-non-x86.patch
Patch1:         0002-xeve-link-libm.patch

BuildOption(conf):  -DSET_PROF=BASE

BuildRequires:  cmake >= 3.12
BuildRequires:  gcc

%description
The eXtra-fast Essential Video Encoder (XEVE) is an opensource and fast
MPEG-5 EVC encoder. This package contains the command-line tool.

%package        devel
Summary:        Development files for xeve
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The xeve-devel package contains libraries and header files for
developing applications that use xeve.

%prep -a
echo "v%{version}" > version.txt

%install -a
# We're not shipping static libraries shipped under private library subdir
rm -rfv %{buildroot}%{_libdir}/xeve*

%files
%license COPYING
%doc README.md doc
%{_bindir}/xeve*
%{_libdir}/libxeve*.so.0*

%files devel
%{_libdir}/libxeve*.so
%{_includedir}/xeve*/
%{_libdir}/pkgconfig/xeveb.pc

%changelog
%autochangelog
