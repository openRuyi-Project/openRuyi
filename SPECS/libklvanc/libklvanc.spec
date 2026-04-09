# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libklvanc
Version:        1.6.0
Release:        %autorelease
Summary:        VANC Processing Framework
License:        LGPL-2.1
URL:            https://github.com/stoth68000/libklvanc
#!RemoteAsset
Source:         https://github.com/stoth68000/libklvanc/archive/refs/tags/vid.obe.%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libtool

%description
Libklvanc is a library used for parsing/generation of Vertical Ancillary Data
(VANC) commonly found in the Serial Digital Interface (SDI) wire protocol.
It supports various SMPTE standards for closed captions, AFD, SCTE-104,
timecodes, and more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%build -a
doxygen doxygen/%{name}.doxyconf

%install -a
# Drop sample application
rm -fr %{buildroot}%{_bindir}

%files
%license lgpl-2.1.txt
%doc README.md
%{_libdir}/libklvanc.so.0*

%files devel
%doc html
%{_includedir}/libklvanc/
%{_libdir}/libklvanc.so

%changelog
%autochangelog
