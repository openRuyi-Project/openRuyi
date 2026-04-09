# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mobile-broadband-provider-info
Version:        20240407
Release:        %autorelease
Summary:        Mobile broadband provider database
License:        CC-PDDC
URL:            https://gitlab.gnome.org/GNOME/mobile-broadband-provider-info
#!RemoteAsset:  sha256:89bfeff215f4bff8e9c3ff2ec25250fdb080d11e9bfa59c6fc71982ac01c814a
Source:         https://download.gnome.org/sources/mobile-broadband-provider-info/20240407/mobile-broadband-provider-info-%{version}.tar.xz
BuildArch:      noarch
BuildSystem:    meson

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  libxslt

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains files necessary for
developing developing applications that use %{name}.

%files
%doc README
%license COPYING
%{_datadir}/mobile-broadband-provider-info

%files devel
%{_datadir}/pkgconfig/mobile-broadband-provider-info.pc

%changelog
%autochangelog
