# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-snaps
%define go_import_path  github.com/gkampitakis/go-snaps

Name:           go-github-gkampitakis-go-snaps
Version:        0.5.21
Release:        %autorelease
Summary:        Snapshot testing library for Go
License:        MIT
URL:            https://github.com/gkampitakis/go-snaps
#!RemoteAsset:  sha256:0247c0c438d88a86a5ef0baa2ab768c1644f5163d5696589586d60bc38a008f6
Source0:        https://github.com/gkampitakis/go-snaps/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Patch0:         2000-force-color-for-color-snapshot-tests.patch
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n go-snaps-0.5.21

BuildRequires:  go
BuildRequires:  go(github.com/gkampitakis/ciinfo)
BuildRequires:  go(github.com/goccy/go-yaml)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/maruel/natural)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(github.com/tidwall/sjson)
BuildRequires:  go-rpm-macros

Provides:       go(github.com/gkampitakis/go-snaps) = %{version}
Provides:       go(github.com/gkampitakis/go-snaps/examples) = %{version}
Provides:       go(github.com/gkampitakis/go-snaps/internal/colors) = %{version}
Provides:       go(github.com/gkampitakis/go-snaps/internal/difflib) = %{version}
Provides:       go(github.com/gkampitakis/go-snaps/internal/test) = %{version}
Provides:       go(github.com/gkampitakis/go-snaps/match) = %{version}
Provides:       go(github.com/gkampitakis/go-snaps/match/internal/yaml) = %{version}
Provides:       go(github.com/gkampitakis/go-snaps/snaps) = %{version}

Requires:       go(github.com/gkampitakis/ciinfo)
Requires:       go(github.com/goccy/go-yaml)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/kr/text)
Requires:       go(github.com/maruel/natural)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/sergi/go-diff)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/tidwall/match)
Requires:       go(github.com/tidwall/pretty)
Requires:       go(github.com/tidwall/sjson)

%description
This package provides Snapshot testing library for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
