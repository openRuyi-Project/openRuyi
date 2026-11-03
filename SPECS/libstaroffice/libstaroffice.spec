# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libstaroffice
Version:        0.0.8
Release:        %autorelease
Summary:        Legacy StarOffice document import library
License:        (MPL-2.0 OR LGPL-2.0-or-later) AND LGPL-2.1-or-later
URL:            https://sourceforge.net/projects/libstaroffice/
VCS:            git:https://github.com/fosnola/libstaroffice.git
#!RemoteAsset:  sha256:bbca92882e96c55bd1527670866d6bc7529ccb12786da55a2398b60a063378da
Source0:        https://github.com/fosnola/libstaroffice/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tools

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)

%description
libstaroffice reads binary StarOffice text, spreadsheet and drawing
documents. The included utilities convert these files to open formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc README
%license COPYING.LGPL COPYING.MPL
%{_bindir}/sd2raw
%{_bindir}/sd2svg
%{_bindir}/sd2text
%{_bindir}/sdc2csv
%{_bindir}/sdw2html
%{_libdir}/libstaroffice-0.0.so.*

%files devel
%{_includedir}/libstaroffice-0.0/
%{_libdir}/libstaroffice-0.0.so
%{_libdir}/pkgconfig/libstaroffice-0.0.pc

%changelog
%autochangelog
