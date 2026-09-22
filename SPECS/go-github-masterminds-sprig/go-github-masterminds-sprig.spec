# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sprig
%define go_import_path  github.com/Masterminds/sprig

Name:           go-github-masterminds-sprig
Version:        2.22.0
Release:        %autorelease
Summary:        Template function library for Go
License:        MIT
URL:            https://github.com/Masterminds/sprig
VCS:            git:https://github.com/Masterminds/sprig.git
#!RemoteAsset:  sha256:c6d0f6e2a3b2aecc888b62c15defcccf16a44e7435c47c7f158b98946c5ee970
Source0:        https://github.com/Masterminds/sprig/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n sprig-2.22.0
# The network lookup is unavailable in OBS; two string tests pin old goutils
# output, and TestRound assumes x86_64 floating-point rounding.
BuildOption(check):  -skip '^(TestCamelCase|TestGetHostByName|TestRound|TestShuffle)$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Masterminds/goutils)
BuildRequires:  go(github.com/Masterminds/semver)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/huandu/xstrings)
BuildRequires:  go(github.com/imdario/mergo)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/Masterminds/sprig) = %{version}

Requires:       go(github.com/Masterminds/goutils)
Requires:       go(github.com/Masterminds/semver)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/huandu/xstrings)
Requires:       go(github.com/imdario/mergo)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(golang.org/x/crypto)

%description
This package provides the github.com/Masterminds/sprig Go module source.

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
