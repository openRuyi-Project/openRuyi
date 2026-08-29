# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-snaps
%define go_import_path  github.com/gkampitakis/go-snaps

Name:           go-github-gkampitakis-go-snaps
Version:        0.5.22
Release:        %autorelease
Summary:        Snapshot testing library for Go
License:        MIT
URL:            https://github.com/gkampitakis/go-snaps
#!RemoteAsset:  sha256:9d933869757da87b2e1897275c594945b746ce356abb25c58800af4c7a52e893
Source0:        https://github.com/gkampitakis/go-snaps/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Force color in snapshot tests because OBS is neither a terminal nor detected
# as CI, while upstream color golden files include ANSI escapes. - HNO3Miracle
Patch2000:      2000-force-color-for-color-snapshot-tests.patch
# Current Go vet rejects Skipf test calls with arguments but no formatting
# directives. Keep the forwarding test and use a real format string. - HNO3Miracle
Patch2001:      2001-fix-skipf-test-format-for-go-vet.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
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

Provides:       go(github.com/gkampitakis/go-snaps) = %{version}

Requires:       go(github.com/gkampitakis/ciinfo)
Requires:       go(github.com/goccy/go-yaml)
Requires:       go(github.com/kr/pretty)
Requires:       go(github.com/maruel/natural)
Requires:       go(github.com/sergi/go-diff)
Requires:       go(github.com/tidwall/gjson)
Requires:       go(github.com/tidwall/pretty)
Requires:       go(github.com/tidwall/sjson)

%description
go-snaps provides snapshot testing helpers for Go.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
