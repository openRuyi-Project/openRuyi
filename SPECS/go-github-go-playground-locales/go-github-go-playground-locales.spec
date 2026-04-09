# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           locales
%define go_import_path  github.com/go-playground/locales

Name:           go-github-go-playground-locales
Version:        0.14.1
Release:        %autorelease
Summary:        a set of locales generated from the CLDR Project which can be used independently or within an i18n package
License:        MIT
URL:            https://github.com/go-playground/locales
#!RemoteAsset
Source0:        https://github.com/go-playground/locales/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/go-playground/locales) = %{version}

Requires:       go(golang.org/x/text)

%description
Locales is a set of locales generated from the Unicode CLDR Project
(http://cldr.unicode.org/) which can be used independently or within an
i18n package; these were built for use with, but not exclusive to,
Universal Translator (https://github.com/go-playground/universal-
translator).

Features

 [x] Rules generated from the latest CLDR (http://cldr.unicode.
 org/index/downloads) data, v36.0.1
 [x] Contains Cardinal, Ordinal and Range Plural Rules
 [x] Contains Month, Weekday and Timezone translations built in
 [x] Contains Date & Time formatting functions
 [x] Contains Number, Currency, Accounting and Percent formatting
 functions
 [x] Supports the "Gregorian" calendar only ( my time isn't unlimited,
 had to draw the line somewhere )

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
