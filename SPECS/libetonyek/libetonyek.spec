# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libetonyek
Version:        0.1.13
Release:        %autorelease
Summary:        Import library for Apple iWork documents
License:        MPL-2.0
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libetonyek
VCS:            git:https://git.libreoffice.org/libetonyek
#!RemoteAsset:  sha256:032b71cb597edd92a0b270b916188281bc35be55296b263f6817b29adbcb1709
Source0:        https://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  CXXFLAGS="%{optflags} -std=gnu++17"
BuildOption(conf):  --with-liblangtag
BuildOption(conf):  --with-tools
BuildOption(conf):  --enable-tests
BuildOption(conf):  --without-docs
BuildOption(conf):  --with-mdds=3.0

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  make
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(liblangtag)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mdds-3.0)
BuildRequires:  pkgconfig(zlib)

%description
libetonyek parses Apple Keynote, Pages and Numbers documents. Its tools
extract text, render presentations and export spreadsheet data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc README.md
%license COPYING
%{_bindir}/key2raw
%{_bindir}/key2text
%{_bindir}/key2xhtml
%{_bindir}/numbers2csv
%{_bindir}/numbers2raw
%{_bindir}/numbers2text
%{_bindir}/pages2html
%{_bindir}/pages2raw
%{_bindir}/pages2text
%{_libdir}/libetonyek-0.1.so.*

%files devel
%{_includedir}/libetonyek-0.1/
%{_libdir}/libetonyek-0.1.so
%{_libdir}/pkgconfig/libetonyek-0.1.pc

%changelog
%autochangelog
