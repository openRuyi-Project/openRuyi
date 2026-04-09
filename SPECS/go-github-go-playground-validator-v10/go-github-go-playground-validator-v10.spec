# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           validator
%define go_import_path  github.com/go-playground/validator/v10

Name:           go-github-go-playground-validator-v10
Version:        10.30.1
Release:        %autorelease
Summary:        Go Struct and Field validation, including Cross Field, Cross Struct, Map, Slice and Array diving
License:        MIT
URL:            https://github.com/go-playground/validator
#!RemoteAsset
Source0:        https://github.com/go-playground/validator/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gabriel-vasile/mimetype)
BuildRequires:  go(github.com/go-playground/assert/v2)
BuildRequires:  go(github.com/go-playground/locales)
BuildRequires:  go(github.com/go-playground/universal-translator)
BuildRequires:  go(github.com/leodido/go-urn)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/go-playground/validator/v10) = %{version}

Requires:       go(github.com/gabriel-vasile/mimetype)
Requires:       go(github.com/go-playground/assert/v2)
Requires:       go(github.com/go-playground/locales)
Requires:       go(github.com/go-playground/universal-translator)
Requires:       go(github.com/leodido/go-urn)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/text)

%description
Package validator implements value validations for structs and
individual fields based on tags.

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
