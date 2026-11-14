# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libexttextcat
Version:        3.4.9
Release:        %autorelease
Summary:        Language identification using text fingerprints
License:        BSD-3-Clause
URL:            https://wiki.documentfoundation.org/Libexttextcat
VCS:            git:https://git.libreoffice.org/libexttextcat
#!RemoteAsset:  sha256:71e9a3cc6c4a270efd61d76281664341e1fb0412b591f1939516413a992d1e87
Source0:        https://dev-www.libreoffice.org/src/libexttextcat/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
libexttextcat identifies the language of a text by comparing its
character n-grams with reference fingerprints. The package includes
the fingerprint database and the createfp utility.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, linker files and pkg-config metadata for developing with %{name}.

%files
%doc README
%license LICENSE
%{_bindir}/createfp
%{_datadir}/libexttextcat/
%{_libdir}/libexttextcat-2.0.so.*

%files devel
%{_includedir}/libexttextcat/
%{_libdir}/libexttextcat-2.0.so
%{_libdir}/pkgconfig/libexttextcat.pc
%{_datadir}/vala/vapi/libexttextcat.vapi

%changelog
%autochangelog
