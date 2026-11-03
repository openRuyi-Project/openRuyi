# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libpagemaker
Version:        0.0.4
Release:        %autorelease
Summary:        Adobe PageMaker document import library
License:        MPL-2.0
URL:            https://wiki.documentfoundation.org/DLP/Libraries/libpagemaker
VCS:            git:https://git.libreoffice.org/libpagemaker
#!RemoteAsset:  sha256:66adacd705a7d19895e08eac46d1e851332adf2e736c566bef1164e7a442519d
Source0:        https://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-werror
BuildOption(conf):  --without-docs
BuildOption(conf):  --enable-tools

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(librevenge-0.0)
BuildRequires:  pkgconfig(librevenge-stream-0.0)
BuildRequires:  pkgconfig(librevenge-generators-0.0)

%description
libpagemaker decodes Adobe PageMaker publications and exposes their
text and page layout to document conversion programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/pmd2raw
%{_bindir}/pmd2svg
%{_bindir}/pmd2text
%{_libdir}/libpagemaker-0.0.so.*

%files devel
%{_includedir}/libpagemaker-0.0/
%{_libdir}/libpagemaker-0.0.so
%{_libdir}/pkgconfig/libpagemaker-0.0.pc

%changelog
%autochangelog
