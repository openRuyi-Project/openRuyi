# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xevd
Version:        0.5.0
Release:        %autorelease
Summary:        Reference MPEG-5 Part 1 (EVC) decoder
License:        BSD-3-Clause
URL:            https://github.com/mpeg5/xevd
#!RemoteAsset
Source:         https://github.com/mpeg5/xevd/archive/refs/tags/v%{version}.tar.gz
Patch0:         0001-xevd-fix-build-on-non-x86.patch
Patch1:         0002-xevd-fix-neon-header.patch
Patch2:         0003-xevd-link-libm.patch

BuildSystem:    cmake

BuildOption(conf): -DSET_PROF=BASE

BuildRequires:  cmake >= 3.12
BuildRequires:  gcc

%description
The eXtra-fast Essential Video Decoder (XEVD) is an opensource and fast
MPEG-5 EVC decoder. This package contains the command-line tool.

%package        devel
Summary:        Development files for xevd
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The xevd-devel package contains libraries and header files for
developing applications that use xevd.

%prep -a
echo "v%{version}" > version.txt

%install -a
rm -rfv %{buildroot}%{_libdir}/xevd*

%files
%license COPYING
%doc README.md
%{_bindir}/xevd*
%{_libdir}/libxevd*.so.0*

%files devel
%{_libdir}/libxevd*.so
%{_includedir}/xevd*/
%{_libdir}/pkgconfig/xevd*.pc

%changelog
%{?autochangelog}
