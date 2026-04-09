# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           universal-translator
%define go_import_path  github.com/go-playground/universal-translator

Name:           go-github-go-playground-universal-translator
Version:        0.18.1
Release:        %autorelease
Summary:        i18n Translator for Go/Golang using CLDR data + pluralization rules
License:        MIT
URL:            https://github.com/go-playground/universal-translator
#!RemoteAsset
Source0:        https://github.com/go-playground/universal-translator/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/go-playground/locales)

Provides:       go(github.com/go-playground/universal-translator) = %{version}

Requires:       go(github.com/go-playground/locales)

%description
Universal Translator is an i18n Translator for Go/Golang using CLDR data
+ pluralization rules

This package is a thin wrapper around locales
(https://github.com/go-playground/locales) in order to store and
translate text for use in your applications.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
