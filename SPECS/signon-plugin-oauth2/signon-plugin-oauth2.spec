# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global gitdate 20210102
%global commit0 fab698862466994a8fdc9aa335c87b4f05430ce6
%global shortcommit %(c=%{commit0}; echo ${c:0:7})

Name:           signon-plugin-oauth2
Version:        0.25+git%{gitdate}.%{shortcommit}
Release:        %autorelease
Summary:        OAuth2 plugin for the Accounts framework
License:        LGPL-2.1-or-later
URL:            https://gitlab.com/accounts-sso/signon-plugin-oauth2
#!RemoteAsset:  sha256:5a1298cc49f504503f54f20f0f5f685e43f541244a654dd3da58951f43782625
Source0:        https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/archive/%{commit0}/signon-plugin-oauth2-%{commit0}.tar.gz
BuildSystem:    autotools

BuildOption(install):  INSTALL_ROOT=%{buildroot}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(signon-plugins)
BuildRequires:  pkgconfig(libproxy-1.0)

%description
OAuth2 plugin for the Accounts framework.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%conf
# No configure.

%build
%{qmake6} \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    LIBDIR=%{_libdir} \
    QMAKE_CXXFLAGS+="-Wno-error=deprecated-declarations" \
    signon-oauth2.pro

%install -a
# Delete tests
rm -fv %{buildroot}/%{_bindir}/signon-oauth2plugin-tests
rm -rfv %{buildroot}/%{_datadir}/signon-oauth2plugin-tests

%files
%{_libdir}/signon/liboauth2plugin.so

%files devel
%{_includedir}/signon-plugins/*.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc

%changelog
%autochangelog
