# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: ayostl <yao_xp@yeah.net>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           iso-codes
Version:        4.18.0
Release:        %autorelease
Summary:        ISO Code Lists and Translations
License:        LGPL-2.1-or-later
URL:            https://salsa.debian.org/iso-codes-team/iso-codes
#!RemoteAsset:  sha256:511f67bf4b51aa77f17c45adbff533242b50f1e370fe49a5706b6341902fac87
Source0:        https://salsa.debian.org/iso-codes-team/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    autotools

BuildOption(install):  INSTALL="%{__install} -p"

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-lxml

Provides:       iso-codes-lang = %{version}

%description
This package provides the ISO-639 language code list, the ISO-3166
territory code list, ISO-3166-2 subterritory lists, and all their
translations in gettext .po form.

%package        devel
Summary:        ISO code lists and translations
Requires:       %{name} = %{version}-%{release}

%description    devel
This package provides the ISO-639 Language code list, the ISO-3166
Territory code list, and ISO-3166-2 sub-territory lists, and all their

%install -a
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc CHANGELOG.md README.md
%license COPYING
%dir %{_datadir}/xml
%dir %{_datadir}/xml/iso-codes
%{_datadir}/xml/iso-codes/*.xml
%{_datadir}/iso-codes

%files devel
%{_datadir}/pkgconfig/iso-codes.pc

%changelog
%autochangelog
