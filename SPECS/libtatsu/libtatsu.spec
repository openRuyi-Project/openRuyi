# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtatsu
Version:        1.0.5
Release:        %autorelease
Summary:        Library handling the communication with Apple's TSS
License:        LGPL-2.1-only
URL:            https://github.com/libimobiledevice/libtatsu
#!RemoteAsset:  sha256:d98e973747b3a03c1befb1875fa43b1a109b1b332ae2252d8d471b4cfb91df6d
Source0:        https://github.com/libimobiledevice/libtatsu/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libcurl)

%description
The libtatsu library allows creating TSS request payloads, sending them to
Apple's TSS server, and retrieving and processing the response.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep -a
echo "%{version}" > .tarball-version

%conf -p
./autogen.sh

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libtatsu.so.*

%files devel
%{_includedir}/libtatsu/
%{_libdir}/libtatsu.so
%{_libdir}/pkgconfig/libtatsu-1.0.pc

%changelog
%autochangelog
