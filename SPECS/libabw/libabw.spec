# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libabw
Version:        0.1.4
Release:        %autorelease
Summary:        AbiWord document import library
License:        MPL-2.0
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libabw
VCS:            git:https://git.libreoffice.org/libabw
#!RemoteAsset:  sha256:fa2685a3440da6e03a66a778480d93cb95f6064e4541e58e37397680760fd6a0
Source0:        https://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tools

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)

%description
libabw reads AbiWord documents and converts their text and layout through
librevenge. The command-line tools export text, HTML and raw events.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc README
%license COPYING.MPL
%{_bindir}/abw2html
%{_bindir}/abw2raw
%{_bindir}/abw2text
%{_libdir}/libabw-0.1.so.*

%files devel
%{_includedir}/libabw-0.1/
%{_libdir}/libabw-0.1.so
%{_libdir}/pkgconfig/libabw-0.1.pc

%changelog
%autochangelog
